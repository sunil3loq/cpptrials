# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
from scipy import stats

# <codecell>

test=pd.read_csv('/home/loq/sunil/feb15/vowpaltest/testpl.csv')

# <codecell>

pldata=test[['pl']]

# <codecell>

col=test.columns

# <codecell>

colsnew=col[:-1]

# <codecell>

test=test[colsnew]

# <codecell>

testsamp=test

# <codecell>

test=(testsamp-testsamp.mean())/(testsamp.std())

# <codecell>

test['pl']=pldata

# <codecell>

test.to_csv('/home/loq/sunil/feb15/vowpaltest/testzpl.csv',index=False)

# <codecell>


