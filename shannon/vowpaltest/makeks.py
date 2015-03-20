
import argparse
import pandas as pd
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages 

def getks(csvin,pdfout,nbins=10,actualcolnum=1,predcolnum=2,headerwith=True):
    '''makes the KS'''
    pddata=pd.
if __name__=="__main__":
    parser=argparse.ArgumentParser(description='argparser for making ks')

    parser.add_argument('--numbins','-n',type=int,default=10,help='Number of KS bins')
    parser.add_argument('--actualcol',type=int,default=1,help='Column number of the Actual Values')
    parser.add_argument('--predcol',type=int,default=2,help='Column number of the Predicted Values')
    parser.add_argument('filein','-f',type=str,help='Input File')
    parser.add_argument('pdfout',type=str,help='Output File')
    parser.add_argument('--header',type=bool,default=True,help='Header is present in True')

    args=parser.parse_args()
