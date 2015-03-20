# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
from scipy import stats

# <codecell>

train=pd.read_csv('/home/loq/sunil/feb15/vowpaltest/trainpl.csv')

# <codecell>

pldata=train[['pl']]

# <codecell>

col=train.columns

# <codecell>

colsnew=col[:-1]

# <codecell>

train=train[colsnew]

# <codecell>

trainsamp=train

# <codecell>

train=(trainsamp-trainsamp.mean())/(trainsamp.std())

# <codecell>

train['pl']=pldata

# <codecell>

train.to_csv('/home/loq/sunil/feb15/vowpaltest/trainzpl.csv')

# <codecell>


