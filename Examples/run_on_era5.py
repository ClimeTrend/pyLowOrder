import xarray as xr
import pickle

import pyLOM

path = "/bask/projects/v/vjgo8416-climate/shared/data/era5/2020-01-01_2020-01-30_era5_slice.nc"

data = xr.open_dataset(path)
temperature = data["temperature"]
temperature = temperature.values

a, b, c, d = temperature.shape

temperature = temperature.reshape(a, b * c * d)

Ai = pyLOM.utils.mpi_scatter(temperature, root=0, do_split=True)

Ui, S, V = pyLOM.math.tsqr_svd(Ai)

U = pyLOM.utils.mpi_gather(Ui, root=0)

path_save = "/bask/projects/v/vjgo8416-climate/shared/data/era5/pylom-svd-results"

# save numpy arrays as pickle files

with open(f"{path_save}/U.pkl", "wb") as f:
    pickle.dump(U, f)

with open(f"{path_save}/S.pkl", "wb") as f:
    pickle.dump(S, f)

with open(f"{path_save}/V.pkl", "wb") as f:
    pickle.dump(V, f)


