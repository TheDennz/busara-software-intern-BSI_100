from os import environ

SESSION_CONFIGS = [
    dict(
        name='mini_ultimatum_game',
        app_sequence=['mini_ultimatum_game', 'exit_survey'],  # Replace with the name of your app
        num_demo_participants=3,
        num_rounds=1,  # Set the number of rounds as needed
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)


PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'KES'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1921889376756'

INSTALLED_APPS = ['otree', 'mini_ultimatum_game', 'exit_survey']
