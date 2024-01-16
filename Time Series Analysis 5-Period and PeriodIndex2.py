import pandas as pd
import numpy as np

idx1 = pd.period_range('2022','2023',freq='q')
print(idx1)
print(idx1[0].start_time)
print(idx1[0].end_time)

#####################
idx2 = pd.period_range('2022',periods=10,freq='3M')
print(idx2)
print(idx2[0].start_time)
print(idx2[0].end_time)

####### Convert period index to date time index #############
idxt=idx2.to_timestamp()
print(idxt)

######### Convert date time index to period index
print(idxt.to_period())

