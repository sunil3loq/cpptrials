
import json
import bitlyurl
import urlparse
import youtubeLikes

class twitterElement(object):
    '''manages the functionality for each twitter element in the json'''
    
    def __init__(self,inpDict):
        self.jsonElem=inpDict
        self.links=[]
        self.youtubelinks=[]
        self.youtubeIds=[]
        self.youTubeVideos={}
        self.debugFlag=True
        
    def validFeedOrNot(self):
        '''checks if the jsonElem is valid for searching a video or not'''
        returnBool=True
        if 'entities' not in self.jsonElem:
            returnBool=False
        if self.debugFlag:
            print 'validFeedOrNot returns',returnBool
        return returnBool
    
    def _getTwitterId(self):
        '''returns the twitter post id if present'''
        try:
            return self.jsonElem['id']
        except KeyError:
            raise "Trying to access feed without an id!!"

    def _getLinks(self):
        '''assigns links variable to the list of links in the post. Assumes it is valid'''
        self.links=[]
        for urlElem in self.jsonElem['entities']['urls']:
            self.links.append(urlElem['expanded_url'])
        try:
            for urlElem in self.jsonElem['extended_entities']['urls']:
                self.links.append(urlElem['expanded_url'])
        except KeyError:
            pass
            #print 'urls in extended_entities not found!!'
        if self.debugFlag:
            print 'links got are',self.links
    
    def _getYoutubeId(self,inpParsedUrl,longFormOrNot=True):
        '''takes in the parsed url to get the youtube ID of the video link'''
        if longFormOrNot:
            queries = urlparse.parse_qs(inpParsedUrl.query)
            try:
                return queries["v"][0]
            except:
                return None
        else:
            return inpParsedUrl.path[1:]
    
    def _youtubeOrNot(self,linkInput):
        '''returns True if the link is of a youtube'''
        bitlyObject=bitlyurl.bitlyurl(linkInput)
        if bitlyObject.isBitly():
            linkInput=bitlyObject.expand()
        parsedTuple=urlparse.urlparse(linkInput)
        if self.debugFlag:
            print parsedTuple.hostname
        if parsedTuple.hostname in ['www.youtube.com','youtube.com']:
            return True,parsedTuple,True
        elif parsedTuple.hostname in ['www.youtu.be','youtu.be']:
            return True,parsedTuple,False
        else:
            return False,parsedTuple,True
    
    def _updateYoutubeIds(self):
        '''updates the youtube Ids for the youtube links'''
        self._getLinks()
        self.youtubeIds=[]
        self.youtubelinks=[]
        for ytlink in self.links:
            youOrNot,parsedObj,longUrlOrNot = self._youtubeOrNot(ytlink)
            if youOrNot:
                self.youtubelinks.append(ytlink)
                self.youtubeIds.append(self._getYoutubeId(parsedObj, longUrlOrNot))
        if self.debugFlag:
            print 'youtube links are',self.youtubelinks
            print 'youtube ids are',self.youtubeIds
        
    def returnYoutubeVideos(self):
        '''updates the youtubeIds and also removes non video links to youtube'''
        self._updateYoutubeIds()
        self.youTubeVideos={}
        for xnum in xrange(len(self.youtubelinks)):
            yid=self.youtubeIds[xnum]
            if yid != None:
                ylink=self.youtubelinks[xnum]
                self.youTubeVideos[ylink]={}
                self.youTubeVideos[ylink]['id']=yid
                self.youTubeVideos[ylink].update(youtubeLikes.youtubeLikes(yid).getStats())
        if self.debugFlag:
            print self.youTubeVideos
        return self.youTubeVideos

