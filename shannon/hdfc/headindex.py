
from collections import OrderedDict
import os

def getdatasample(filein,dlm=',',headatrow=1,rowsprintstartfromhead=1,rowsprintendfromhead=3,outdlm='|'):
    '''returns the colnames mapped to the column number'''
    fin=open(filein)
    leftrows=headatrow+1
    rownum=0
    mydict = OrderedDict()
    numdict= OrderedDict()
    for line in fin:
        leftrows=leftrows-1
        if leftrows<=0:
            rownum=rownum+1
        if rownum>rowsprintendfromhead:
            break
        if leftrows==1:
            colnum=0
            linelist=line.strip().split(dlm)
            for elem in linelist:
                colnum=colnum+1
                mydict[colnum]=str(colnum)+outdlm+elem
        if rownum>0:
            linelist=line.strip().split(dlm)
            colnum=0
            for elem in linelist:
                colnum=colnum+1
                mydict[colnum]=mydict[colnum]+outdlm+elem
    for elem in mydict:
        print mydict[elem]
    return mydict

def getheaddict(filein,dlm=','):
    '''returns the dict mapping the cols to the names'''
    fin = open(filein)
    lineone=fin.readline()
    linelist=lineone.strip().split(dlm)
    colnamemap=OderedDict()
    colnum=-1
    for elem in linelist:
        colnum=colnum+1
        colnamemap[elem]=colnum
    return colnamemap

def subsetcols(filein,cols,fileout,dlm=',',removeflag=0):
    '''selects a subset of the cols from the input file
    if the removeflag=1 then the list of cols are removed from original file
    else list of cols are selected'''
    cmd='cut -s'
    colsstrelem=[str(x) for x in cols]
    colstr=','.join(colsstrelem)
    cmd=cmd+' -f'+colstr
    cmd=cmd+' -d'+dlm
    if removeflag:
        cmd=cmd+' --complement'
    cmd=cmd+' '+filein+' > '+fileout
    try:
        print cmd
        os.system(cmd)
        return 'success subsetcols'
    except:
        return 'problem with subsetcols'

if __name__=='__main__':
    '''
    headdict=getdatasample('/home/sunil/data/carbadbuydata/training.csv')
    #print subsetcols('/home/sunil/data/carbadbuydata/training.csv',[1,3,5],'/home/sunil/data/carbadbuydata/trainingsmall.csv',removeflag=1)
    print subsetcols('/home/sunil/data/carbadbuydata/training.csv',[1,3,5,4,7,8,9,10,11,12,13,14,15,16,17,18,27,28,29,30,31]
            ,'/home/sunil/data/carbadbuydata/trainingsmallcontonly.csv',removeflag=1)
    
    headdict=getdatasample('/home/sunil/data/carbadbuydata/test.csv')
    print subsetcols('/home/sunil/data/carbadbuydata/test.csv',[2,4,6,5,19,8,9,10,11,12,13,14,15,16,17,18,32,28,29,30,31]
            ,'/home/sunil/data/carbadbuydata/testsmallcontonly.csv',removeflag=1)
    '''
    headdict=getdatasample('/home/loq/sunil/carbadbuydata/trainingsmall.csv')
    
