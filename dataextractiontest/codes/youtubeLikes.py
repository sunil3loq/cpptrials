
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import oauthtoken

class youtubeLikes(object):
    '''manages the statistics parameters for the video in youtube'''
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    DEVELOPER_KEY = oauthtoken.getYoutubeToken()
    
    def __init__(self,inpId):
        self.videoId=inpId
        self.debugFlag=False
    def getStats(self):
        '''returns the dictionary of stats for the input video'''
        youtube = build(youtubeLikes.YOUTUBE_API_SERVICE_NAME, 
                        youtubeLikes.YOUTUBE_API_VERSION,
                        developerKey=youtubeLikes.DEVELOPER_KEY)
        video_response = youtube.videos().list(id=self.videoId,
                                               part='id, statistics'
                                               ).execute()
        if self.debugFlag:
            print video_response
        try:
            return video_response['items'][0]['statistics']
        except IndexError:
            print 'stats not available for',self.videoId
            return {'commentCount':'NA','viewCount':'NA','favoriteCount':'NA','dislikeCount':'NA','likeCount':'0'}
  
if __name__ == "__main__":
#https://www.youtube.com/watch?v=ntss2nfKnEc
  try:
    idObj=youtubeLikes('ntss2nfKnEc')
    print idObj.getStats()
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
