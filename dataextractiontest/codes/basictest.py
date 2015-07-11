
import oauthtoken
import json

myauth = oauthtoken.getbitlyToken()

dataloc='/root/sunil/pythontest/data/'
resultsloc='/root/sunil/pythontest/results/'

filename='sample_tweets_data.json'

print 'here1'

fin = open(dataloc+filename)


try:
    myjson=json.loads(fin.read())
except:
    print'loading failed!'


nodeKeys={}

def getKeys(inpDict):
    '''returns the set of keys'''
    keysare=inpDict.keys()
    keysare.sort()
    return ','.join(keysare)

print 'reading done!'

def printNode(inp):
    print json.dumps(inp,indent=4)

foutdicts=open(dataloc+'actualsdicts.csv','w')

for num,node in enumerate(myjson):
    if num>10:
        pass
        #break
    printNode(node)
    print
    keyString=getKeys(node)
    if keyString not in nodeKeys:
        nodeKeys[keyString]=1
    else:
        nodeKeys[keyString]+=1
    #print 'nodeKeys are',nodeKeys
foutdicts.close()
 
fout = open(dataloc+'samplekeys.csv','w')
print 'final list is written to file' 
for elem,nums in nodeKeys.iteritems():
    fout.write(str(nums)+',')
    fout.write(elem+'\n')
fout.close()
