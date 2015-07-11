
import json
import bitlyurl
import random

class twitterElement(object):
    '''manages the functionality for each twitter element in the json'''
    
    def __init__(self,inpDict):
        self.jsonElem=inpDict
        self.links=[]
        self.youtubelinks=[]
        
    def _validFeedOrNot(self):
        '''checks if the jsonElem is valid for searching a video or not'''
        return random.choice(['True','False'])
        raise NotImplementedError
    
    def _getLinks(self):
        '''assigns links variable to the list of links in the post'''
        #self.links=[]
        raise NotImplementedError
    
    def _youtubeOrNot(self,linkInput):
        '''returns True if the link is of a youtube'''
        bitlyObject=bitlyurl(linkInput)
        if bitlyObject.isBitly():
            linkInput=bitlyObject.expand()
        raise NotImplementedError
    
    def _getYoutubeLinks(self):
        '''assigns the youtubelinks to the total youtube links'''
        self._getLinks()
        self.youtubelinks=filter(self._youtubeOrNot(),self.links)
    
    