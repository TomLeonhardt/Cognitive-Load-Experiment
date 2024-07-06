from os import environ

SESSION_CONFIGS = [
    {
        'name': 'cognitive_load_experiment',
        'display_name': "Cognitive Load Experiment",
        'num_demo_participants': 1,
        'app_sequence': ['cognitive_load_experiment'],
    },
]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    {
        'name': 'cognitive_room',
        'display_name': 'Cognitive Experiment Room',
    },
]

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'your_default_password')

SECRET_KEY = 'blahblah'

INSTALLED_APPS = ['otree', 'cognitive_load_experiment']
