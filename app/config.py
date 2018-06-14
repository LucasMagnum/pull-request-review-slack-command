import os

# Server
PORT = os.getenv('PORT', 8000)


# Application
ALLOWED_CHANNELS = os.getenv('ALLOWED_CHANNELS', '').split(',')
ALLOWED_DOMAINS = os.getenv('ALLOWED_DOMAINS', '').split(',')

BLACKLIST_REVIEWERS = os.getenv('BLACKLIST_REVIEWERS', '').split(',')
NUMBER_OF_REVIEWERS = os.getenv('NUMBER_OF_REVIEWERS', 2)
