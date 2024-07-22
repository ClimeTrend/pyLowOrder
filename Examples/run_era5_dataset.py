import netCDF4
import pyLOM
import numpy as np

file_path = "/bask/projects/v/vjgo8416-climate/shared/data/era5/2020-01-01_2020-01-30_era5_slice_hourly.nc"

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


minlon, maxlon, nlon = np.min(lon), np.max(lon), lon.shape[0]
minlat, maxlat, nlat = np.min(lat), np.max(lat), lat.shape[0]
## Create pyLOM Dataset
m = pyLOM.Mesh.new_struct2D(nlon, nlat, None, None, np.array([minlon, maxlon]), np.array([minlat, maxlat]))
p = pyLOM.PartitionTable.new(1, m.ncells, m.npoints)
d = pyLOM.Dataset(ptable=p, mesh=m, time=t)

temp  = temp.reshape(nt, nlat*nlon)


d.time = t
d.add_variable('temperature',True,1,temp.T)

d.save('dataset.h5', nopartition=True)

