import requests
GAME_API = {
    'EU': {
        'locale': [
            'en_GB', 'de_DE', 'es_ES', 'fr_FR',
            'it_IT', 'pl_PL', 'pt_PT', 'ru_RU',
        ],
        'base_url': 'https://eu.api.battle.net/wow/',
    },
    'KR': {
        'locale': ['ko_KR', ],
        'base_url': 'https://kr.api.battle.net/wow/',
    },

    'TW': {
        'locale': ['zh_TW', ],
        'base_url': 'https://tw.api.battle.net/wow/',
    },

    'US': {
        'locale': ['en_US', 'pt_BR', 'es_MX'],
        'base_url': 'https://us.api.battle.net/wow/',
    },
}

BASE_URL = "https://{region}.battle.net/"


class Api(object):
    def __init__(self, region='EU', locale='en_GB', token=None):
        self.region = region
        self.locale = locale
        if token is not None:
            self.token = token

    def get(self, method):
        url = f"{GAME_API[self.region]['base_url']}/{method}?locale = {self.locale} & apikey = {self.toekn}"
        r = requests.get(url)
        return r.json()
