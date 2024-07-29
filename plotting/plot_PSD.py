"""
Script to plot the Power Spectral Density (PSD) of the POD modes temporal evolution.
The PSD is estimated using the Welch method.
The plots are saved in the `figs/` folder.

The script requires the following files:
    - The POD file `POD_{variable}.h5`
"""

from scipy.signal import welch
import numpy as np
import matplotlib.pyplot as plt
import pyLOM

## User Inputs
variable = 'daily'  # "hourly", "daily", "monthly"
modes = np.arange(10) # Modes to plot
fs = 1/24  # Sampling frequency (e.g. for daily, fs=1/24 - 1 sample every 24 hours)
x_label = 'Frequency [1/hour]'

## Load POD
_, _, V = pyLOM.POD.load('POD_%s.h5' % variable)

for mode in modes:
    # compute PSD
    f, Pxx = welch(V[mode, :], fs)

    # plot in log-log scale
    fig, ax = plt.subplots()
    ax.loglog(f, Pxx)
    ax.set_xlabel('Frequency [1/hour]')
    ax.set_ylabel('PSD')
    ax.set_title(f'PSD of mode {mode}')

    # save figure
    plt.savefig(f'figs/PSD_{mode}_{variable}.png')
    plt.close()

