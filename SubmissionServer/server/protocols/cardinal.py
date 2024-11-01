import requests
from server import app
from server.models import FlagStatus, SubmitResult

RESPONSES = {
    FlagStatus.QUEUED: ['queued'],
    FlagStatus.ACCEPTED: ['success'],
    FlagStatus.REJECTED: ['incorrect flag', 'submission failed', 'please do not submit the flag repeatedly', 'self-submission', 'incorrect flag for this round'],
}

# Timeout in seconds for the requests
TIMEOUT = 5

def submit_flags(flags, config):
    for item in flags:
        # Sending the POST request with flag in the required format
        r = requests.post(
            config['SYSTEM_URL'],
            headers={'Authorization': config['SYSTEM_TOKEN']},
            json={'flag': item.flag},  # flag in the correct form
            timeout=TIMEOUT
        )
        
        app.logger.debug('Sending submission request %s', str(r.request.body))

        # Parse the response
        response = r.json()
        app.logger.warning('Response json: %s', response)

        # Extract the 'msg' from the response
        response_msg = response.get('msg', '').strip().lower()

        unknown_responses = set()
        found_status = FlagStatus.QUEUED  # Default to QUEUED unless matched

        # Match the response 'msg' with known substrings
        for status, substrings in RESPONSES.items():
            if any(s in response_msg for s in substrings):
                found_status = status
                break
        else:
            if response_msg not in unknown_responses:
                unknown_responses.add(response_msg)
                app.logger.warning('Unknown checksystem response (flag will be resent): %s', response_msg)

        # Yield the result with the flag, status, and the response message
        yield SubmitResult(item.flag, found_status, response_msg)
