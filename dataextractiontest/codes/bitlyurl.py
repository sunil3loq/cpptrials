
import oauthtoken
import urllib2
import urllib
import bitly
import urlparse

class bitlyurl(object):
    '''manages the url shortening and expanding'''
    
    userName,authKey=oauthtoken.getbitlyToken()
    bitlyApi=bitly.Api(login=userName,apikey=authKey)
    
    def __init__(self,inpUrl):
        '''intialisation'''
        self.inpUrl=inpUrl
        
    def shorten(self):
        return bitlyurl.bitlyApi.shorten(self.inpUrl)
    
    def expand(self):
        return bitlyurl.bitlyApi.expand(self.inpUrl)
    
    def isBitly(self):
        '''returns True when the url is a bitly shortened form'''
        parsed=urlparse.urlparse(self.inpUrl)
        if parsed.hostname in ['bit.ly','www.bit.ly']:
            return True
        else:
            return False

if __name__=="__main__":
    myUrl=bitlyurl('https://www.youtube.com/watch?v=ntss2nfKnEc')
    print myUrl.isBitly()
    stemp=myUrl.shorten()
    print stemp
    #http://bit.ly/MegaTest
    #http://bit.ly/1HUF9XL
    sUrl=bitlyurl('http://bit.ly/1HUF9XL')
    print sUrl.isBitly()
    print sUrl.expand()
