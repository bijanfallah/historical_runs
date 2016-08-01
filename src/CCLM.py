from __future__ import division
__author__ = 'Bijan'
from mpl_toolkits.basemap import Basemap, cm
from netCDF4 import Dataset as NetCDFFile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.backends.backend_pdf import PdfPages
import os
if not os.path.exists('TEMP'):
    os.makedirs('TEMP')
os.chdir('TEMP')


CMD = "scp $mistral:/scratch/b/b324045/cclm-sp_2.1/data/ext/europe_0440.nc ./"
os.system(CMD)
fname = "europe_0440.nc"
nc = NetCDFFile(fname)
lats = nc.variables['rlat'][:]  # extract/copy the data
lons = nc.variables['rlon'][:]
#x,y =   m(*np.meshgrid(lons,lats))
temp = nc.variables['HSURF'][:]
t=np.squeeze(temp)
