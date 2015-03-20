
import argparse

def addimpinfile(inpfile,outfile,zeroimp=1,oneimp=1):
    '''adds the importance col to the vw file as given'''
    vwfilein = open(inpfile)
    vw=open(outfile,'w')
    for line in vwfilein:
        linelist=line.strip().split(" ",1)
        if linelist[0] in ['0','-1']:
            imp=zeroimp
        else:
            imp=oneimp
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

    parser.add_argument('--zeroimp',type=int,default=1,help='default value of 0 importance')
    parser.add_argument('--oneimp',type=int,default=1,help='default value of 1 importance')
    parser.add_argument('--zeroone',type=bool,default=True,help='True if the prediction on 0 and 1')
    parser.add_argument('inputfile',type=str,help='file in vw format')
    parser.add_argument('outputfile',type=str,help='file out in vw format with importance')
    

    args=parser.parse_args()
    addimpinfile(args.inputfile,args.outputfile,args.zeroimp,args.oneimp)

