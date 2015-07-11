
import oauthtoken
import urllib2
import urllib

class bitlyurl(object):
    '''manages the url shortening and expanding'''
    
    def __init__(self,inpUrl):
        '''intialisation'''
        self.inpUrl=inpUrl
        self.authkey=oauthtoken.getbitlyToken()
        self.api=''
        self.version=''
        
    def shorten(self):
        raise NotImplementedError
    
    def expand(self):
        raise NotImplementedError
    
    def isBitly(self):
        '''returns True when the url is a bitly shortened form'''
        raise NotImplementedError