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
DATAFILE = 'dataset.h5'
VARLIST  = ['temperature']
## Data loadingx
pyLOM.pprint(0, 'Loading data...', flush=True)
d = pyLOM.Dataset.load(DATAFILE)
X  = d.X(*VARLIST)
pyLOM.pprint(0, 'Data loaded!', flush=True)

## Run POD
pyLOM.pprint(0, 'Running POD...', flush=True)
PSI,S,V = pyLOM.POD.run(X,remove_mean=True) # PSI are POD modes
pyLOM.pprint(0, 'POD done!', flush=True)

## Save POD
pyLOM.pprint(0, 'Saving .h5 ...', flush=True)
pyLOM.POD.save('POD.h5',PSI,S,V,d.partition_table,nvars=1,pointData=True)
pyLOM.pprint(0, 'h5 saved!', flush=True)

pyLOM.cr_info()
