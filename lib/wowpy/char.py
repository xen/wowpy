# -*- coding: utf-8 -*-
armory_url = 'http://%(region)s.wowarmory.com/%(action)s.xml?%(query)s'
user_agent = 'Firefox/3.1'
regions = ('eu', 'us', 'ru', )

class Char:
    
    def __init__(self, realm, name, region='eu'):
        self.realm = realm
        self.name = name
        self.region = region
        
    def loadData(self):
        pass
    
    