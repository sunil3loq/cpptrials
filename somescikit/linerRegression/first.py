__author__ = 'sunil'

from sklearn.datasets import load_boston

boston=load_boston()

'''
#exploring the boston data loaded
print boston.data.shape

print dir(boston)

print boston.keys()

print boston.target.shape

print boston.data[:5,]

print boston.target[:5]

print boston.feature_names

'''

import pandas as pd
import matplotlib.pyplot as plt

#plot the scatter plot for lstat and medv
print boston.feature_names

featureindex={}

for x in xrange(len(boston.feature_names)):
    featureindex[boston.feature_names[x]]=x

fig, ax = plt.subplots()

ax.scatter(boston.data[:,featureindex['LSTAT']],boston.target,color='grey')
ax.set(xlabel='lstat',ylabel='medv')

plt.show()

#fitting a simple linear regression model

import statsmodels.formula.api as smf

lm=smf.ols(formula='MEDV~')