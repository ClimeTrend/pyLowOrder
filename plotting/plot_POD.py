import pyLOM
import matplotlib.pyplot as plt
import numpy as np
import MapPlotter as mp

## Input
variable = 'hourly'
modes    = np.arange(20)
prlevel  = 0

## Dataset load
d = pyLOM.Dataset.load('dataset_%s.h5'%variable)

## Get the latitude and longitude values
lat  = np.flip(np.unique(d.mesh.xyz[:,1]))
lon  = np.unique(d.mesh.xyz[:,0])
nlat = lat.shape[0]
nlon = lon.shape[0]

## Load POD
U, S, V = pyLOM.POD.load('POD_%s.h5' % variable,ptable=d.partition_table)

np.save('V_%s.npy' % variable, V)

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
    plotter.save('mode_%i_%s.png' % (mode, variable))

    plt.figure(figsize=(8,6))
    plt.plot(V[mode,:],'b', linewidth=2, label='Mode %i'% (mode))
    plt.xlabel('Time [hours]')
    plt.ylabel(r'$V_i$')
    plt.title('Mode %i' %(mode))
    plt.savefig('temporal_%i_%s.png'%(mode,variable), dpi=300)

energy = np.cumsum(S**2)/np.sum(S**2)
print(np.argwhere(energy>0.99)[0,0])
plt.figure()
plt.plot(np.cumsum(S**2)/np.sum(S**2),'bo')
plt.xlabel('Mode')
plt.ylabel('Cumulative energy')
plt.savefig('energy_%s.png'%variable, dpi=300)

#plt.show()

