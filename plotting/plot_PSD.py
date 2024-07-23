from scipy.signal import welch
import numpy as np
import matplotlib.pyplot as plt


# load .npy file
V = np.load('V_daily.npy')

# compute PSD. The sampling frequency is 1 sample per 24 hours
fs = 1/24
mode = 1
f, Pxx = welch(V[mode, :], fs)

# plot in log-log scale
fig, ax = plt.subplots()
ax.loglog(f, Pxx)
ax.set_xlabel('Frequency [1/hour]')
ax.set_ylabel('PSD')
ax.set_title(f'PSD of mode {mode}')

# save figure
plt.savefig(f'PSD_{mode}.png')

# plot time series
fig, ax = plt.subplots()
ax.plot(V[mode, :])
ax.set_xlabel('Time [days]')
ax.set_title(f'Mode {mode} time series')

# save figure
plt.savefig(f'time_series_{mode}.png')

