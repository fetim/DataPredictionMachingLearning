import numpy as np
import pandas as pd
import matplotlib.pylab as pl
import lasio

# read las file
laspath="data/1FL1PI.las"
las = lasio.read(laspath)

#Convert lasio to DataFrame
lasdata = las.df()

#print(las.keys())

# replace unvalid values
lasdata.fillna(value=-999.25)

agppath="data/1FL0001PI_agp_PREPARED.csv"
rawagp = pd.read_csv(agppath)#, na_values=["-999.25"])

# # categorical data type. 
rawagp['FACIES'] = rawagp['FACIES'].astype('category')

# Creating 'FACIES' category in lasdata
lasdata['FACIES'] = ''

for count, depth in enumerate(rawagp.DEPTH,start=1):        
    indx=list(lasdata[(rawagp.DEPTH[count-1] < lasdata['DEPTH'])  & (lasdata['DEPTH'] < rawagp.DEPTH[count])].index)
    print(count)
    facie = rawagp.loc[count,'FACIES']
    lasdata.loc[indx,'FACIES'] = facie


# Merging AGP facie information in las file
# facies_depth = rawagp.DEPTH[:6]
# well_depth = lasdata['DEPTH'].iloc[:1600]

#     print('Last FACIE')#,idx_las,depth[idx_las])     
#     print(idx_las,lasdata.FACIES[idx_las])
# #print(rawagp.iloc[0]['DEPTH'])

# Put Facies first
# cols = lasdata.columns.tolist()
# cols = cols[-1:] + cols[:-1]
# lasdata =lasdata[cols]
# lasdata['FACIES'] = lasdata['FACIES'].astype('category')


lasdata.to_csv("outtest.csv", sep='\t')

# ztop=lasdata.DEPTH.min(); zbot=lasdata.DEPTH.max()

# pl.plot(lasdata.GR,lasdata.DEPTH,'-')

# pl.axis([lasdata.GR.min(), lasdata.GR.max(), lasdata.DEPTH.max(), lasdata.DEPTH.min()])
# pl.show()