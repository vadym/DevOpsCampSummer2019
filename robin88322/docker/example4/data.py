import xarray as xr
import pandas as pd
import numpy as np

file = xr.open_dataset(f's_radiation_2018.nc')
df = file.to_dataframe()
rec = df.to_records().tolist()
df1 = pd.DataFrame(rec, columns = ['latitude', 'longitude', 'time', 'ssr'])
print(df1[0:50])
