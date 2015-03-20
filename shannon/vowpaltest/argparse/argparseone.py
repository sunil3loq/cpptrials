
import argparse

parser=argparse.ArgumentParser(description='First')
'''
#for checking if the verbose flag is present -- using action='store_flase' stores False when present
parser.add_argument('--verbose','-v',action='store_true',help='verbose flag')
parser.add_argument('--countit','-c',action='count',help='count these argument parameters')
'''
parser.add_argument('--appendthese','-a',action='append',help='append the arguments with this action')
'''
parser.add_argument('choicearg',choices=['amar','akbar','anthony'])
#required argument
parser.add_argument('--limit','-l',type=int,required=True,help='limit number which is required')
parser.add_argument('--default','-d',default=5,type=int,help='default parameter to 5')
'''
parser.add_argument('fileread',type=argparse.FileType('r'),help='file to read from')
parser.add_argument('filewrite',type=argparse.FileType('w'),help='file to write to')
parser.add_argument('numargs',nargs=5)
'''
#could use * for all of the parameters in argurment
parser.add_argument('starargs',nargs='*')
#could use + to make require one or more parameters and return them all in numargs
parser.add_argument('plusargs',nargs='+')
#could use ? to make a positional argument optional
parser.add_argument('optionalarg',nargs='?')
parser.add_argument('remargs',nargs=argparse.REMAINDER)
'''

args=parser.parse_args()

'''
if args.verbose:
    print 'Verbose!'
else:
    print 'not Verbose'
'''

print args
print args.appendthese
