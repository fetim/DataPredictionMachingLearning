import numpy as np
import pandas as pd
import matplotlib.pylab as pl
import lasio


las = lasio.read("data/1FL1PI.las")

lasdata = las.df()

print(las.keys())
print(las.version)

lasdata.fillna(value=-999.25)

lasdata["FACIES"] = lasdata['GR'] - lasdata['NEUT']

cols = lasdata.columns.tolist()

cols = cols[-1:] + cols[:-1]

lasdata =lasdata[cols]

print(lasdata.describe())

# ztop=lasdata.DEPTH.min(); zbot=lasdata.DEPTH.max()

# pl.plot(lasdata.GR,lasdata.DEPTH,'-')

# pl.axis([lasdata.GR.min(), lasdata.GR.max(), lasdata.DEPTH.max(), lasdata.DEPTH.min()])
# pl.show()