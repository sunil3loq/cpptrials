import argparse
import random

def genrandintcol(fileout,colhead,minval=0,maxval=10,nsamp=1000):
    '''generates the column with random values'''
    fout = open(fileout,'w')
    fout.write(colhead+'\n')
    for linenum in xrange(nsamp):
        rnum=random.randint(minval,maxval)
        fout.write(str(rnum)+'\n')
    return 1

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='arg parser for the code to generate the random number')
    parser.add_argument('--numsamples','-n',type=int,default=1000,help='Number of samples to be present')
    parser.add_argument('--minval',type=int,default=0,help='Min value of range for random')
    parser.add_argument('--maxval',type=int,default=10,help='Max value of range for random')
    parser.add_argument('--colname',type=str,help='Name of the randome column')
    parser.add_argument('fileout',type=str,help='Have a separate namespace for each categorical value')
    args=parser.parse_args()

    genrandintcol(args.fileout,args.colname,args.minval,args.maxval,args.numsamples)
