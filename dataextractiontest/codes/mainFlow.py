
import oauthtoken
import json
import twitterElement

dataloc='/root/sunil/pythontest/data/'
resultsloc='/root/sunil/pythontest/results/'

inpFileName='sample_tweets_data.json'
outFileName='sorted_youtubevideos.csv'
tempFileName='non'+outFileName

print 'here1'

fin = open(dataloc+inpFileName)
fout = open(resultsloc+outFileName)
ftemp = open(resultsloc+tempFileName)

try:
    myjson=json.loads(fin.read())
except:
    print'loading failed!'

print 'reading done!'

nodeKeys={}

def getKeys(inpDict):
    '''returns the set of keys'''
    keysare=inpDict.keys()
    keysare.sort()
    return ','.join(keysare)

def printNode(inp):
    print json.dumps(inp,indent=4)

def printCsvLine(fptr,inpDict):
    '''prints the csv line for the output of the twitterElement.returnYoutubeVideos'''
    for ylink in inpDict:
        fptr.write(ylink+',')
        fptr.write(ylink['id']+',')
        fptr.write(ylink['commentCount']+',')
        fptr.write(ylink['viewCount']+',')
        fptr.write(ylink['favoriteCount']+',')
        fptr.write(ylink['dislikeCount']+',')
        fptr.write(ylink['likeCount']+'\n')

for num,node in enumerate(myjson):
    if num>1000:
        pass
        #break
    print
    printNode(node)
    print
    tElement=twitterElement(node)
    if tElement.validFeedOrNot:
        outputDict=tElement.returnYoutubeVideos
        if outputDict != {}:
            printCsvLine(ftemp, outputDict)

ftemp.close()
fout.close()
fout = open(dataloc+'samplekeys.csv','w')
print 'final list is written to file' 
for elem,nums in nodeKeys.iteritems():
    fout.write(str(nums)+',')
    fout.write(elem+'\n')
fout.close()
