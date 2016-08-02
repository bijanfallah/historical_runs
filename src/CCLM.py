from __future__ import division
__author__ = 'Bijan'
from netCDF4 import Dataset as NetCDFFile
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import cartopy.crs as ccrs
import cartopy.feature

if not os.path.exists('TEMP'):
    os.makedirs('TEMP')
os.chdir('TEMP')


CMD = "scp $mistral:/scratch/b/b324045/cclm-sp_2.1/data/ext/europe_0440.nc ./"
os.system(CMD)
fname = "europe_0440.nc"
nc = NetCDFFile(fname)
lats = nc.variables['lat'][:]
lons = nc.variables['lon'][:]
rlats = nc.variables['rlat'][:]  # extract/copy the data
rlons = nc.variables['rlon'][:]
t = nc.variables['HSURF'][:].squeeze()

rotpole = nc.variables['rotated_pole']
nc.close()


fig = plt.figure()
fig.set_size_inches(18,10)


rp = ccrs.RotatedPole(pole_longitude=-162.0,
                      pole_latitude=39.25,
                      globe=ccrs.Globe(semimajor_axis=6370000,
                                       semiminor_axis=6370000))
pc = ccrs.PlateCarree()

ax = plt.axes(projection=rp)
ax.coastlines('50m', linewidth=0.8)
ax.add_feature(cartopy.feature.LAKES,
               edgecolor='black', facecolor='none',
               linewidth=0.8)
##ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=2, color='gray', alpha=0.5, linestyle='--')
##x,y = rp(lons,lats)
#ax.drawcoastlines()
t[t < 0] = 0
cs = plt.contourf(lons,lats,t,10, transform=ccrs.PlateCarree(),cmap=plt.cm.terrain)
ax.add_feature(cartopy.feature.OCEAN,
               edgecolor='black', facecolor='white',
               linewidth=0.8)
ss=ax.gridlines()
ax.text(-31.14,4.24,r'$45\degree N$',
        fontsize=15)
ax.text(-31.14,24.73,r'$60\degree N$',
        fontsize=15)
ax.text(-19.83,-29.69,r'$0\degree $',
        fontsize=15)
ax.text(2.106,-29.69,r'$20\degree E$',
        fontsize=15)
ax.text(24,-29.69,r'$20\degree E$',
        fontsize=15)
plt.hlines(y=min(rlats), xmin=min(rlons), xmax=max(rlons), color='red',linewidth=4)
plt.hlines(y=max(rlats), xmin=min(rlons), xmax=max(rlons), color='red',linewidth=4)
plt.vlines(x=min(rlons), ymin=min(rlats), ymax=max(rlats), color='red',linewidth=4)
plt.vlines(x=max(rlons), ymin=min(rlats), ymax=max(rlats), color='red',linewidth=4)
cb=plt.colorbar(cs)
cb.set_label(' ', fontsize=20)
cb.ax.tick_params(labelsize=20)
# In order to reproduce the extent, we can't use cartopy's smarter
# "set_extent" method, as the bounding box is computed based on a transformed
# rectangle of given size. Instead, we want to emulate the "lower left corner"
# and "upper right corner" behaviour of basemap.
xs, ys, zs = rp.transform_points(pc,
                                 np.array([-10, 90.0]),
                                 np.array([15, 65])).T
ax.set_xlim(xs)
ax.set_ylim(ys)
name='test'
plt.savefig("Figure_"+name+".pdf")######Figure04.a
plt.close()







