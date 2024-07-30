"""
Script to create a pyLOM dataset (as a .h5 file) from a .nc file containing ERA5 data.
Currently only works for surface temperature (i.e. 2D data on a lat-lon grid and 1D time).
Update the file_path and freq variables to match the .nc file you want to convert.
"""

import netCDF4
import pyLOM
import numpy as np

## User inputs
file_path = "/bask/projects/v/vjgo8416-climate/shared/data/era5/1990-01-01_2020-01-10_era5_slice_monthly.nc"
freq = "monthly"


print("Loadding dataset...")
## Load variables from .nc file
with netCDF4.Dataset(file_path, 'r') as nc_file:
    #Latitude and longitude
    lat = nc_file['latitude'][:]
    lon = nc_file['longitude'][:]
    #Time
    t  = nc_file['time'][:]
    nt = t.shape[0]
    #Variables
    temp  = nc_file['2m_temperature'][:]

print("Creating pyLOM dataset...")

minlon, maxlon, nlon = np.min(lon), np.max(lon), lon.shape[0]
minlat, maxlat, nlat = np.min(lat), np.max(lat), lat.shape[0]
## Create pyLOM Dataset
m = pyLOM.Mesh.new_struct2D(nlon, nlat, None, None, np.array([minlon, maxlon]), np.array([minlat, maxlat]))
p = pyLOM.PartitionTable.new(1, m.ncells, m.npoints)
d = pyLOM.Dataset(ptable=p, mesh=m, time=t)

temp  = temp.reshape(nt, nlat*nlon)

d.time = t
d.add_variable('temperature',True,1,temp.T)

print("Saving dataset...")

d.save(f'dataset_{freq}.h5', nopartition=True)

print("Done!")