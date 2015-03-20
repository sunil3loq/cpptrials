import argparse
import re

parser=argparse.ArgumentParser(description='Parsing Arguments for code converting csv to vw')
parser.add_argument('--svmformat',action='store_true',default=False,help='Vowpal format if False, LibSVM else')
parser.add_argument('--categoricalnamespace','-cns',action='store_true',help='Have a separate namespace for each categorical value')
parser.add_argument('--useheaders','-uh',default=1,type=int,help='Use headers as names of the features, give 0 to not use')
parser.add_argument('--startrow',default=2,type=int,help='starting row number of the actual values to use')
parser.add_argument('--label','-l',default=1,type=int,help='column number of the label')
parser.add_argument('--importance','-imp',default=-1,type=int,help='column number of the importance')
parser.add_argument('--tag','-t',default=-1,type=int,help='column number of the tag')
parser.add_argument('--ignorecolumns','-i',default='-1',help='provide list of columns to ignore. , separated string without spaces')
parser.add_argument('--catcolumns','-c',default='-1',help='provide list of columns that are categorical. , separated string w/o spaces')
parser.add_argument('--printcounter','-p',default=10000,type=int,help='prints the progress as row number for every printcounter lines')
parser.add_argument('--zerosofdvremain','-z',action='store_true',default=False,help='Do not convert the label to 1 and -1 for binary classification')
parser.add_argument('--inputdlm','-d',default=',',help='default delimiter of the input file to use')
parser.add_argument('--sample','-s',action='store_true',default=False,help='if you want to run for sample of 20')
parser.add_argument('--cleanspaces','-cls',action='store_true',default=False,help='clean the spaces and other keywords')
#parser.add_argument('--cleannulls','-cln',action='store_true',default=True,help='clean the NA/NULL from the dataset')


parser.add_argument('inputfile',type=argparse.FileType('r'),help='file to read from which is in csv format')
parser.add_argument('jaffa',type=argparse.FileType('w'),help='file to write to which will be in vw format')

args=parser.parse_args()

def createindexdictfromlist(inlist):
    '''creates the identity dict of the list index'''
    dictout = {}
    for num,elem in enumerate(inlist):
        dictout[num]=num
    return dictout

def namespacedcatvalstring(namespace,catval,scale=1):
    '''generates the string for the input with namespace and cat val'''
    return " |"+str(namespace)+" "+str(catval)

def catvalstring(colname,colval):
    '''generates the string for the input for categorical variables without a namespace'''
    return " "+str(colname)+"_"+str(colval)

def numvalstring(colname,colval):
    '''generates the string for the input for numerical variables'''
    return " "+str(colname)+":"+str(colval)

def getpositivelist(inlist):
    '''get the positive numbers list from given'''
    outlist=[]
    for elems in inlist:
        if elems>=0:
            outlist.append(elems)
    return outlist

#vowpalkeyletters
vowpalkeys="[ :|']"

#reading the header
rowstart=args.startrow
headdict={}
if args.useheaders==1:
    headline=args.inputfile.next()
    headlist=headline.strip().split(args.inputdlm)
    rowstart=rowstart-1
    for varnum,val in enumerate(headlist):
        headdict[varnum]=val

#leaving unnecessary rows
while(rowstart>1):
    temp=args.inputfile.next()
    rowstart=rowstart-1

#Actual data parsing
labelcol=args.label-1
importancecol=args.importance-1
tagcol=args.tag-1
ignores=[int(x)-1 for x in args.ignorecolumns.split(',')]
cats=[int(x)-1 for x in args.catcolumns.split(',')]
ignores=ignores+cats
ignores.append(labelcol)
ignores.append(importancecol)
ignores.append(tagcol)
ignorespos=getpositivelist(ignores)
catspos=getpositivelist(cats)
print args
print "ignores\n",ignores,ignorespos
print "cats\n",cats,catspos

for num,line in enumerate(args.inputfile):
    line=re.sub(vowpalkeys,"",line)
    #print "num is",num
    if args.sample and num>20:
        break
    linelist=line.strip().split(args.inputdlm)
    if num==0:
        numcols=list(set(range(len(linelist))).difference(set(ignorespos)))
        numcols.sort()
        if args.useheaders==0:
            headdict=createindexdictfromlist(linelist)
        print "headdict\n",headdict
        print "numcols\n",numcols
    catstring=""
    for numtwo,elem in enumerate(catspos):
        if args.categoricalnamespace:
            catstring=catstring+namespacedcatvalstring(headdict[elem],linelist[elem])
        else:
            if numtwo==0:
                catstring=" |cats"
            catstring=catstring+catvalstring(headdict[elem],linelist[elem])
    if tagcol<0:
        tagappend=" "
    else:
        tagappend=" "+str(linelist[tagcol])
    numstring=tagappend+"|nums"
    for numthree,elem in enumerate(numcols):
        if linelist[elem]==0.0:
            thisnumval=""
        else:
            thisnumval=numvalstring(headdict[elem],linelist[elem])
        numstring=numstring+thisnumval
    dvval=int(linelist[labelcol])
    if dvval==0.0 and not args.zerosofdvremain:
        dvval=-1
    dvpartstring=str(dvval)
    if importancecol>=0:
        dvpartstring=dvpartstring+" "+str(linelist[importancecol])
    args.jaffa.write(dvpartstring+numstring+catstring+"\n")
