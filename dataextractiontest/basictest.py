
import oauthtoken
import json

myauth = oauthtoken.getbitlyToken()

dataloc='../../data/'

filename='sample_tweets_data.json'

fin = open(dataloc+filename)

myjson=json.load(fin)

nodeKeys=set([])

def getKeys(inpDict):
    '''returns the set of keys'''
    return set(inpDict.keys())

for num,node in enumerate(myjson):
    if num>100:
        break
    nodeKeys.union(getKeys(node))
    
print nodeKeys