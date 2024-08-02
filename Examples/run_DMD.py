#!/usr/bin/env python
#
# POD of ERA5.
#
# Last revision: 15/07/2024
from __future__ import print_function, division

import mpi4py
mpi4py.rc.recv_mprobe = False

import os, numpy as np
import pyLOM


## Parameters
VARLIST  = ['temperature']
fname    = 'daily'
DATAFILE = 'dataset_%s.h5' % fname
## Data loadingx
pyLOM.pprint(0, 'Loading data...', flush=True)
d = pyLOM.Dataset.load(DATAFILE)
X = d.X(*VARLIST)
pyLOM.pprint(0, 'Data loaded!', flush=True)

## Run DMD
time = (d.time-d.time[0])*1e-3
print(time)
pyLOM.pprint(0, 'Running DMD...', flush=True)
muReal, muImag, Phi, b = pyLOM.DMD.run_optimized(X, time, r=4, constraints=None, remove_mean=True)
pyLOM.pprint(0, 'DMD done!', flush=True)

## Save POD
pyLOM.pprint(0, 'Saving .h5 ...', flush=True)
pyLOM.DMD.save('DMD_%s.h5' % (fname),muReal,muImag,Phi,b,d.partition_table,nvars=1,pointData=True)
pyLOM.pprint(0, 'h5 saved!', flush=True)

pyLOM.cr_info()
