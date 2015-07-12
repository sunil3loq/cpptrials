
import oauthtoken
import json
import twitterElement
import pandas as pd

debugFlag=False
printNodeFlag=False

#dataloc='/root/sunil/pythontest/data/'
#resultsloc='/root/sunil/pythontest/results/'
dataloc='../data/'
resultsloc='../results/'

inpFileName='small_sample_tweets_data.json'
outFileName='sorted_youtubevideos.csv'
tempFileName='non'+outFileName

print 'here1'

fin = open(dataloc+inpFileName)
ftemp = open(resultsloc+tempFileName,'w')

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
    print
    print json.dumps(inp,indent=4)
    print

def csvDefinition():
    headList=['youtubelink','twitterid','youtubeId','commentCount','viewCount',
              'favoriteCount','dislikeCount','likeCount\n']
    return ','.join(headList)

def printCsvLine(fptr,inpDict):
    '''prints the csv line for the output of the twitterElement.returnYoutubeVideos'''
    for ylink,val in inpDict.iteritems():
        fptr.write(ylink+',')
        fptr.write(str(val['twitterId'])+',')
        fptr.write(val['id']+',')
        fptr.write(val['commentCount']+',')
        fptr.write(val['viewCount']+',')
        fptr.write(val['favoriteCount']+',')
        fptr.write(val['dislikeCount']+',')
        fptr.write(val['likeCount']+'\n')

ftemp.write(csvDefinition())
for num,node in enumerate(myjson):
    if num!=110:
        pass
        #continue
    #printNode(node)
    if debugFlag:
        print
        print 'num value is',num
        if printNodeFlag:
            printNode(node)
    try:
        tElement=twitterElement.twitterElement(node)
        if tElement.validFeedOrNot():
            outputDict=tElement.returnYoutubeVideos()
            if outputDict != {}:
                printCsvLine(ftemp, outputDict)
    except:
        #printNode(node)
        raise
ftemp.close()

pdFrame=pd.read_csv(resultsloc+tempFileName)

pdFrame.sort(columns='likeCount',ascending=False,inplace=True)

pdFrame.to_csv(resultsloc+outFileName,index=False)

'''
fout = open(dataloc+'samplekeys.csv','w')
print 'final list is written to file' 
for elem,nums in nodeKeys.iteritems():
    fout.write(str(nums)+',')
    fout.write(elem+'\n')
fout.close()
'''
