
import argparse

parser=argparse.ArgumentParser(description='Parsing Arguments for getting distinct combinations of columns')

parser.add_argument('--whichcolumns','-c',help=', separated column indexes, starts with 1')

parser.add_argument('inputfile',help='file to read from which is in csv format')
parser.add_argument('outputfile',help='file to write to which will be in vw format')
parser.add_argument('dlm',default=',',help='delimiter')

args=parser.parse_args()

fin = open(args.inputfile)
fout = open(args.outputfile,'w')
collist = args.whichcolumns.split(',')
collist = [s+1 for s in collist]
countdict = {}

for ind,line in enumerate(fin):
    linelist=line.strip().split(args.dlm)
    print ind
    
