# -*- coding: utf-8 -*-

import xmltramp 
import exceptions
import urllib2

armory_url = 'http://%(region)s.wowarmory.com/%(action)s.xml?%(query)s'
user_agent = 'Firefox/3.1'
regions = ('eu', 'us', 'ru', )

class Char:
    """ Retrive character data from Armory server
    
       c = Char(realm='Kul Tiras', region = 'eu', name='Pythonista')
    """
    
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
        url = armory_url % {'region': region, 'action': action, 'query': '&'.join('%s=%s' % (key, value) for key, value in query_string.items())}
        
        request = urllib2.Request(url, headers={'User-Agent': user_agent})
        opener = urllib2.build_opener()
        self.rawdata = opener.open(request).read()
        
        self.data = xmltramp.seed(opener.open(request))
        self.rawdata = ""
    
    def loadFileData(self, source_file):
        """ Load data from local file """
        f = open(source_file, 'r')
        self.data = xmltramp.seed(opener.open(request))
        
        
        
    