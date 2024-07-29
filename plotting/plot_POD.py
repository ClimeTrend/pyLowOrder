"""
This script plots:
    1. The POD spatial modes on a world map
    2. The temporal evolution of the POD modes
    3. The cumulative energy of the POD modes
The plots are saved in the `figs/` folder.
The script requires the following files:
    - The dataset file `dataset_{variable}.h5`
    - The POD file `POD_{variable}.h5`
"""

import pyLOM
import matplotlib.pyplot as plt
import numpy as np
import MapPlotter as mp

font = {'weight': 'bold', 'size': 12}
plt.rc('font', **font)

## User Inputs
variable = 'daily'  # "hourly", "daily", "monthly"
modes    = np.arange(20)  # Modes to plot
prlevel  = 0
x_label_temporal = 'Time [days]'

## Dataset load
d = pyLOM.Dataset.load('dataset_%s.h5'%variable)

## Get the latitude and longitude values
lat  = np.flip(np.unique(d.mesh.xyz[:,1]))
lon  = np.unique(d.mesh.xyz[:,0])
nlat = lat.shape[0]
nlon = lon.shape[0]

## Load POD
U, S, V = pyLOM.POD.load('POD_%s.h5' % variable,ptable=d.partition_table)

for mode in modes:
    ## Plot data
    varplot = U[:,mode].reshape((nlat, nlon))
    plotter = mp.MapPlotter(projection='PlateCarree')
    # Create basic parameters dictionary
    params  = plotter.defaultParams()

    # DPI
    params['dpi']      = 100
    # Which features need to be plotted?
    params['features'] = ['coastline','continents','rivers','image']
    params['img']      = 'world.png'
    # A bit of formatting on the title and axis
    params['title']    = [variable,{'weight':'bold','style':'italic'}]
    params['xlabel']   = ['Longitude (deg)']
    params['ylabel']   = ['Latitude (deg)']
    # A bit of formatting on the colorbar
    params['cmap']     = 'seismic'
    params['tick_format'] = '%.2e'
    params['bounds']     = [-np.max(np.abs(varplot)), np.max(np.abs(varplot))]
    plotter.plot(lon, lat, varplot, params=params)
    plotter.save('figs/mode_%i_%s.png' % (mode, variable))
    plotter.close()


    plt.figure(figsize=(8,6))
    plt.plot(V[mode,:],'g', linewidth=2, label='Mode %i'% (mode))
    plt.xlabel(x_label_temporal)
    plt.ylabel(r'$V_i$')
    plt.title('Mode %i' %(mode))
    plt.tight_layout
    plt.savefig('figs/temporal_%i_%s.pdf' % (mode,variable), dpi=300)
    plt.close()

energy = np.cumsum(S**2)/np.sum(S**2)
print(np.argwhere(energy>0.99)[0,0])
plt.figure()
plt.plot(np.cumsum(S**2)/np.sum(S**2),'bo')
plt.xlabel('Mode')
plt.ylabel('Cumulative energy')
plt.savefig('figs/energy_%s.png'%variable, dpi=300)
plt.close()

#plt.show()

