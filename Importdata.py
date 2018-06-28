# import lasio

# las = lasio.read("WLC_PETRO_COMPUTED_INPUT_1.las")

# print(las.params)


import numpy as np
import matplotlib.pylab as pl

filename="WLC_PETRO_COMPUTED_INPUT_1_SEMHEADER.las"

Matrix = np.loadtxt(filename, unpack = True)

np.shape(Matrix)

Matrix[ Matrix==-999.25] = np.nan
depth = Matrix[0,:]
log1 = Matrix[7,:]
# log2 =Matrix[8,:]
# log3 =Matrix[14,:]


print(np.shape(log1))
print(np.shape(depth))

pl.plot(depth,log1)
pl.draw()
pl.show()
