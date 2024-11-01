import csv
import os

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # Reading teams from a CSV file
    'TEAMS': {},
    'FLAG_FORMAT': str(rf"{os.getenv('FLAG_FORMAT', r'A&D\{[A-z0-9]{32}\}')}"),

    # System protocol configuration
    'SYSTEM_PROTOCOL': os.getenv('SYSTEM_PROTOCOL','cardinal'),
    'SYSTEM_URL': os.getenv('SYSTEM_URL','127.0.0.1:80/api'),
    'SYSTEM_TOKEN': os.getenv('SYSTEM_TOKEN', 'abcdefghijklmnopqrstuvwxyz'),

    # 'SYSTEM_PORT': os.getenv('SYSTEM_PORT', 31337),

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'your_secret_token',

    # Flag submission settings
    'SUBMIT_FLAG_LIMIT': int(os.getenv('SUBMIT_FLAG_LIMIT', 50)),
    'SUBMIT_PERIOD': int(os.getenv('SUBMIT_PERIOD', 5)),
    'FLAG_LIFETIME': int(os.getenv('FLAG_LIFETIME', 5 * 60)),

    # Reading server password from environment variable
    'SERVER_PASSWORD': os.getenv('SERVER_PASSWORD', 'default_password'),

    # API authorization settings
    'ENABLE_API_AUTH': bool(os.getenv('ENABLE_API_AUTH', False)),
    'API_TOKEN': os.getenv('API_TOKEN', ''),
}

# Load teams from CSV
def load_teams_from_csv(csv_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            team_name, team_ip = row
            CONFIG['TEAMS'][team_name] = team_ip

# Call this function to load teams
load_teams_from_csv('/etc/exploitfarm/config/teams.csv')

print(CONFIG)
