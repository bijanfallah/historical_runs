from __future__ import division
__author__ = 'Bijan'
'''
This is a function to plot CCLM outputs.

'''
from netCDF4 import Dataset as NetCDFFile
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages
import os
import cartopy.crs as ccrs
import cartopy.feature

if not os.path.exists('TEMP'):
    os.makedirs('TEMP')
os.chdir('TEMP')

def Plot_CCLM(dir_mistral='/scratch/b/b324045/cclm-sp_2.1/data/ext/',name='europe_0440.nc',bcolor='red',var='HSURF',flag='TRUE'
              ,color_map='TRUE', alph=1):
    # type: (object, object, object, object, object, object) -> object
    CMD = 'scp $mistral:'+ dir_mistral+ name+' ./'
    os.system(CMD)
    nc = NetCDFFile(name)
    os.remove(name)
    lats = nc.variables['lat'][:]
    lons = nc.variables['lon'][:]
    rlats = nc.variables['rlat'][:]  # extract/copy the data
    rlons = nc.variables['rlon'][:]
    t = nc.variables[var][:].squeeze()
    nc.close()
    fig = plt.figure('1')
    fig.set_size_inches(14, 10)
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
    t[t < 0] = 0
    if flag=='TRUE':
        v = np.linspace(0, 3000, 11, endpoint=True)
        cs = plt.contourf(lons, lats, t, v, transform=ccrs.PlateCarree(), cmap=plt.cm.terrain)
        if color_map=='TRUE':
            cb = plt.colorbar(cs)
            cb.set_label('topography [m]', fontsize=20)
            cb.ax.tick_params(labelsize=20)
    ax.add_feature(cartopy.feature.OCEAN,
                   edgecolor='black', facecolor='white',
                   linewidth=0.8)
    ax.gridlines()
    ax.text(-31.14, 4.24, r'$45\degree N$',
            fontsize=15)
    ax.text(-31.14, 24.73, r'$60\degree N$',
            fontsize=15)
    ax.text(-19.83, -29.69, r'$0\degree $',
            fontsize=15)
    ax.text(2.106, -29.69, r'$20\degree E$',
            fontsize=15)
    ax.text(24, -29.69, r'$20\degree E$',
            fontsize=15)
    plt.hlines(y=min(rlats), xmin=min(rlons), xmax=max(rlons), color=bcolor, linewidth=4, alpha=alph)
    plt.hlines(y=max(rlats), xmin=min(rlons), xmax=max(rlons), color=bcolor, linewidth=4, alpha=alph)
    plt.vlines(x=min(rlons), ymin=min(rlats), ymax=max(rlats), color=bcolor, linewidth=4, alpha=alph)
    plt.vlines(x=max(rlons), ymin=min(rlats), ymax=max(rlats), color=bcolor, linewidth=4, alpha=alph)
    xs, ys, zs = rp.transform_points(pc,
                                     np.array([-10, 90.0]),
                                     np.array([15, 65])).T
    ax.set_xlim(xs)
    ax.set_ylim(ys)

#os.chdir('../')