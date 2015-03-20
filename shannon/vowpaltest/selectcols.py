
from headindex import subsetcols
import argparse
parser=argparse.ArgumentParser(description='Parsing Arguments for selecting columns in output')

parser.add_argument('--inputdlm','-d',default=',',help='default delimiter of the input file to use')
parser.add_argument('--removeflag','-r',action='store_true',default=False,help='remove the columns given else keep them')
parser.add_argument('inputfile',help='input file')
parser.add_argument('outputfile',help='output file')
parser.add_argument('cols',help='columns to be kept to removed')

args=parser.parse_args()

print subsetcols(args.inputfile,args.cols.split(','),args.outputfile,dlm=args.inputdlm,removeflag=args.removeflag)
