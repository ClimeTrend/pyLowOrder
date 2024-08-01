"""
Script to plot the Power Spectral Density (PSD) of the POD modes temporal evolution.
The PSD is estimated using the Welch method.
The plots are saved in the `figs/` folder.

The script requires the following files:
    - The POD file `POD_{variable}.h5`

Make sure to update the user inputs as needed.
"""

from scipy.signal import welch, periodogram
import numpy as np
import matplotlib.pyplot as plt
import pyLOM

## User Inputs
variable = 'biweekly'  # "hourly", "daily", "monthly", "biweekly"
modes = np.arange(5) # Modes to plot
fs = 1/336  # Sampling frequency: how many samples per hour (e.g. for daily, fs=1/24 - 1 sample every 24 hours)
x_label = 'Frequency [1/hour]'

## Plotting settings
font = {'weight': 'bold', 'size': 12}
plt.rc('font', **font)

## Load POD
_, _, V = pyLOM.POD.load('POD_%s.h5' % variable)

for mode in modes:
    # compute PSD
    f, Pxx = periodogram(V[mode, :], fs)
    f_welch, Pxx_welch = welch(V[mode, :], fs)

    # plot in log-log scale
    fig, ax = plt.subplots()
    ax.loglog(f, Pxx, color='blue', label='Periodogram')
    ax.loglog(f_welch, Pxx_welch, color='red', label='Welch')
    plt.ylim(1e-6, 1e2)
    plt.grid(which='both', axis='x')
    ax.set_xlabel('Frequency [1/hour]')
    ax.set_ylabel('PSD')
    ax.set_title(f'PSD of mode {mode}')
    ax.legend()

    # save figure
    plt.savefig(f'figs/PSD_{mode}_{variable}.pdf', dpi=300)
    plt.close()

