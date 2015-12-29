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

'''
fig, ax = plt.subplots()

ax.scatter(boston.data[:,featureindex['LSTAT']],boston.target,color='grey')
ax.set(xlabel='lstat',ylabel='medv')

#plt.show()
'''

#fitting a simple linear regression model

import statsmodels.api as sm

lm=sm.OLS(boston.target,boston.data)
results=lm.fit()

print results.summary()

#print dir(results)

print results.params

#converting the numpy boston array to a pandas array and further models on it
bostondf= pd.DataFrame(boston.data,columns=boston.feature_names)
bostondfall=bostondf.copy()

bostondfall['MEDV']=pd.Series(boston.target)

print bostondf.head()

print bostondfall.head()

import statsmodels.formula.api as smf
import statsmodels.api as sm

idvs=' + '.join(boston.feature_names)

lm2results = smf.ols(formula='MEDV ~'+idvs,data=bostondfall).fit()

print lm2results.summary()

print lm2results.params

print dir(lm2results)

print lm2results.predict(bostondf.head())

print lm2results.predict(bostondfall.head())

#function to plot the scatter and the line of the predicted

import numpy as np

def scatterlinemodelplot(xvals,yvals,predictor,xlab,ylab='DV',scolor='grey',lcolor='red',numpoints=100):
    newxvals=np.linspace(xvals.min(),xvals.max(),numpoints)
    newyvals=predictor.predict(pd.Series({xlab:newxvals}))
    print 'xs are'
    print newxvals
    print 'ys are'
    print newyvals
    fig, ax= plt.subplots()
    ax.scatter(xvals,yvals,color=scolor)
    ax.plot(newxvals,newyvals,color=lcolor)
    ax.set(xlabel=xlab,ylabel=ylab)
    plt.show()

# testing with one variable as in the R code

lm3 = smf.ols(formula='MEDV~LSTAT',data=bostondfall).fit()

print lm3.summary()

print lm3.predict(pd.Series({'LSTAT':np.linspace(0,1,10)}))
#scatterlinemodelplot(bostondfall.LSTAT,bostondfall.MEDV,lm3,'LSTAT',numpoints=10)

#plotting the residual plots on this model
fighere=plt.figure()
sm.graphics.plot_partregress_grid(lm3,fig=fighere)
#plt.show()

#confidence intervals in the model
print lm3.conf_int()

#on two variables

lm4=smf.ols(formula='MEDV~LSTAT+AGE',data=bostondfall).fit()

print lm4.summary()

#more on model with all variables

lm2=lm2results

#print lm2.summary()

fighere2=plt.figure()
sm.graphics.plot_partregress_grid(lm2,fig=fighere2)

fighere3,ax3 = plt.subplots()

sm.graphics.plot_leverage_resid2(lm2,ax=ax3)

#plt.show()

#nonliner interactions
lm5=smf.ols(formula='MEDV~LSTAT*AGE',data=bostondfall).fit()

#print lm5.summary()

#lm6=smf.ols(formula='MEDV~LSTAT+I(LSTAT^2)',data=bostondfall)

#preparing the linear models in scikit

xcolumns=['LSTAT','AGE']
ycolumns=['MEDV']
xvalues=bostondfall[xcolumns]
yvalues=bostondfall[ycolumns]

from sklearn.linear_model import LinearRegression

sklm1 = LinearRegression()
sklm1.fit(xvalues,yvalues)

print sklm1.coef_
print sklm1.intercept_

print zip(xcolumns,sklm1.coef_[0])

#creating a dataset with 