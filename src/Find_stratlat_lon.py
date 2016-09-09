import os
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from RMSE_MAPS_INGO import read_data_from_mistral
t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/scratch/b/b324045/cclm-sp_2.1/data/ext/',
                                                                   name='domain2016090909104.nc', var='Z0')
print 'first 10 rlats : ',  rlat_o[0:10]
print
print 'first 10 rlons : ',  rlon_o[0:10]