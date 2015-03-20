
from headindex import getdatasample
import argparse
parser=argparse.ArgumentParser(description='Parsing Arguments for getting sample columns')

parser.add_argument('--inputdlm','-d',default=',',help='default delimiter of the input file to use')
parser.add_argument('--headstartrow','-hr',default=1,type=int,help='row number of the header')
parser.add_argument('--outputdlm','-od',default='|',help='default delimiter of the output')
parser.add_argument('--outputstartrowfromhead','-sh',default=1,type=int,help='row number of the start from header')
parser.add_argument('--outputendrowfromhead','-eh',default=3,type=int,help='row number of the end from header')
parser.add_argument('inputfile',help='input file')
args=parser.parse_args()

getdatasample(args.inputfile,dlm=args.inputdlm,rowsprintstartfromhead=args.outputstartrowfromhead,rowsprintendfromhead=args.outputendrowfromhead,outdlm=args.outputdlm)
    
