#!/usr/bin/env python

"""
Run POD on ERA5 data.
The data is loaded from a .h5 file and the POD results are saved in a new .h5 file.

Udpate the user inputs as needed before running the script.
"""

from __future__ import print_function, division

import mpi4py
mpi4py.rc.recv_mprobe = False

import os, numpy as np
import pyLOM

## User inputs
freq = "biweekly"
DATAFILE = f'dataset_{freq}.h5'
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
pyLOM.POD.save(f'POD_{freq}.h5',PSI,S,V,d.partition_table,nvars=1,pointData=True)
pyLOM.pprint(0, 'h5 saved!', flush=True)

pyLOM.cr_info()
