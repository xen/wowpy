# -*- coding: utf-8 -*-
import requests

REGIONS = ('US', 'EU', 'APAC', 'CN')
LOCALES = (
    'en_GB',
    'de_DE',
    'es_ES',
    'fr_FR',
    'it_IT',
    'pl_PL',
    'pt_PT',
    'ru_RU',
)


BASE_URL = "https://{region}.battle.net/"

# armory_url = 'http://%(region)s.wowarmory.com/%(action)s.xml?%(query)s'
regions = ('eu', 'us', 'ru', )


class Char:
    """ Retrive character data from Armory server

       c = Char(realm='Kul Tiras', region = 'eu', name='Pythonista')
    """
    base_info = {'Name': '',
                 'Level': 0,
                 'Class': 0,
                 'ClassId': 0,
                 'Faction': 0,
                 'Gender': 0,
                 'GenderId': 0,
                 'GuildName': '',
                 'GuildUrl': '',
                 'LastModified': '',
                 'Prefix': '',
                 'Race': '',
                 'RaceId': 0,
                 'Realm': '',
                 'Suffix': '',
                 }
    arena_info = {'BattleGroup': '',
                  'Faction': '',
                  'FactionId': 0,
                  'GamesPkayed': 0,
                  'GamesWon': 0,
                  'LastSeasonsRanking': 0,
                  'Name': '',  # Arena team name
                  'Ranking': 0,
                  'Rating': 0,
                  'SeasonGamesPlayed': 0,
                  'SeasonGamesWon': 0,
                  'Url': '',
                  'MembersTitle': [],
                  }
    talents_info = {'TalentTree': '',  # format 'X/Y/Z'
                    # format profession = [{'skill': '', 'max':'', 'name': '', 'value': ''}, skill2]
                    'Professions': [],

                    }
    stats_info = {'BaseStats': [],
                  'Resistances': [],
                  'Melee': [],
                  'Ranged': [],
                  'Spell': [],
                  'Defenses': [],
                  }
    #items_info = {}

    def __init__(self, realm, name, region='eu', source_file=None):
        self.realm = realm
        self.name = name
        self.region = region
        if source_file:
            self.loadFileData(source_file)
        else:
            self.loadData()

    def loadData(self):
        """ Get data from server """
        url = armory_url % {'region': region, 'action': action, 'query': '&'.join(
            '%s=%s' % (key, value) for key, value in query_string.items())}

        request = urllib2.Request(url, headers={'User-Agent': user_agent})
        opener = urllib2.build_opener()
        self.rawdata = opener.open(request).read()

        self.data = xmltramp.seed(opener.open(request))
        self.rawdata = ""

    def loadFileData(self, source_file):
        """ Load data from local file """
        f = open(source_file, 'r')
        self.data = xmltramp.seed(opener.open(request))
