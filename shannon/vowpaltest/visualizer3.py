
import matplotlib
matplotlib.use('Agg')
import numpy as np
import pylab as pl
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages('sal_atm_wdl_graph.pdf')

filename = '/var/lib/HPCCSystems/mydropzone/eda/intermediate/atm_wdl_by_sal.csv'
#filename = '/var/lib/HPCCSystems/mydropzone/eda/intermediate/pin_atm_txn.csv'

#columns =['value']

columns = ['ratio','avg_sal']

dataset = pd.read_csv(filename)

print dataset.columns.values


for each in columns:
        row_values = dataset[each]*10000
        #bins = [0, 1000, 3000, 5000, 7000, 10000, 20000, 30000, 100000]
        std = row_values.std(axis=0)
        bins = range(0, 100, 1)
        n, bins, patches = pl.hist(row_values, bins, histtype='bar', rwidth=0.8)
        pl.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
        #pl.clf()
        #pl.cla()
        pl.title(each)
pl.savefig(pp, format='pdf')
pp.close()

