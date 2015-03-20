
import argparse

def addimp(impfile,inpfile,outfile,impdlm=',',impcol=1,imphead=True):
    '''adds the importance col in the importance file to the vw file'''
    vwfilein = open(inpfile)
    vw=open(outfile,'w')
    impfin=open(impfile)
    imphead=impfin.readline()
    for line in vwfilein:
        linelist=line.strip().split(" ",1)
        impline=impfin.readline()
        imp=impline.strip().split(impdlm)[impcol-1]
        imp=str(imp)
        newlist=['','','']
        newlist[0]=linelist[0]
        newlist[1]=imp
        newlist[2]=linelist[1]
        newline=" ".join(newlist)
        vw.write(newline+'\n')
    vw.close()
    return 1

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='argparser for addition of importance column to an existing vw file ')

    parser.add_argument('imporfile',type=str,help='file with importance column')
    parser.add_argument('--impdlm',type=str,default=',',help='dlm for the importance file')
    parser.add_argument('--impcol',type=int,default=1,help='column of the importance col')
    parser.add_argument('--imphead',type=bool,default=True,help='header present in the imp file')
    parser.add_argument('inputfile',type=str,help='file in vw format')
    parser.add_argument('outputfile',type=str,help='file out in vw format with importance')
    

    args=parser.parse_args()
    addimp(args.imporfile,args.inputfile,args.outputfile,args.impdlm,args.impcol,args.imphead)

