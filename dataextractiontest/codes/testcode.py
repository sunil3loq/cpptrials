#!/usr/bin/python
import json

dataloc='/root/sunil/pythontest/data/'

filename='sample_tweets_data.json'
smallfilename='small_sample_tweets_data.json'

print 'here1'

fin = open(dataloc+filename)
fout=open(dataloc+smallfilename,'w')

try:
    myjson=json.loads(fin.read())
except:
    print'loading failed!'

def printNode(inp):
    print json.dumps(inp,indent=4)

newList=[]

for num,node in enumerate(myjson):
    if num>1000:
        #pass
        break
    newList.append(node)

json.dump(newList,fout)
fout.close()

'''
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBr_SpOWfrd9f8WvGZK7mN24P-j3C1aVYc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(inpId):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the videos.list method to retrieve location details for each video.
  video_response = youtube.videos().list(
    id=inpId,
    part='id, statistics'
  ).execute()

  print video_response['items'][0]['statistics']
  print type(video_response)
  
if __name__ == "__main__":
#https://www.youtube.com/watch?v=ntss2nfKnEc
  try:
    youtube_search('ntss2nfKnEc')
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
'''

'''
import urlparse
link1="http://youtu.be/Fnd6rRmU3vk"
link2="https://youtu.be/ZVVxAWTjqiA"
link3="http://www.yOUtu.be/yRZcW_8e4QM"
link4="https://www.youtube.com/watch?v=4oDMfbVagfo"
link5="http://www.youtube.com/watch?v=CaHXmaoyZp0"
link6="http://BiT.lY/1005Hlk"
link9="https://www.yoUTUBe.com/user/PlayTmz"

def parsePrint(inpLink):
    parsed=urlparse.urlparse(inpLink)
    print 'parsing>>',inpLink
    print 'scheme  :', parsed.scheme
    print 'netloc  :', parsed.netloc
    print 'path    :', parsed.path
    print 'params  :', parsed.params
    print 'query   :', parsed.query
    print 'fragment:', parsed.fragment
    print 'username:', parsed.username
    print 'password:', parsed.password
    print 'hostname:', parsed.hostname, '(in lower case?)'
    print 'port    :', parsed.port
    print 'check   :',parsed.path[1:]
    
parsePrint(link1)
parsePrint(link2)
parsePrint(link3)
parsePrint(link4)
parsePrint(link5)
parsePrint(link6)
parsePrint(link9)
'''
