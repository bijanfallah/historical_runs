# Program to show the maps of RMSE averaged ove time
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import os
from netCDF4 import Dataset as NetCDFFile
import numpy as np
season='JJA'

def read_data_from_mistral(dir='/scratch/b/b324045/cclm-sp_2.1/chain/work/member/post/',name='lffd1979010100c.nc',var='HSURF'):
    #a function to read the data from mistral work

    CMD = 'scp $mistral:' + dir + name + ' ./'
    os.system(CMD)
    nc = NetCDFFile(name)
    os.remove(name)
    lats = nc.variables['lat'][:]
    lons = nc.variables['lon'][:]
    t = nc.variables[var][:].squeeze()
    rlats = nc.variables['rlat'][:]  # extract/copy the data
    rlons = nc.variables['rlon'][:]
    nc.close()

    return(t, lats, lons, rlats, rlons)

def calculate_MAPS_RMSE_of_the_member(member='1', buffer=4):
    # function to cut the area and calculate RMSE
    # buffer is the number of grid points to be skipeed
    #
    t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/scratch/b/b324045/cclm-sp_2.1/chain/work/member/post/')
    t_f, lat_f, lon_f, rlat_f, rlon_f  = read_data_from_mistral(dir='/scratch/b/b324045/cclm-sp_2.1/chain/work/member0'+str(member)+'/post/', name='lffd1979010100c.nc',
                                           var='HSURF')
    os.system('rm -f *.nc')
    row_lat = lat_o[buffer, buffer].squeeze()
    row_lon = lon_o[buffer, buffer].squeeze()
    start_lon = np.where(lon_f == row_lon)[-1][0]
    start_lat = np.where(lat_f == row_lat)[0][-1]

    dext_lon = t_o.shape[1] - (2 * buffer)
    dext_lat = t_o.shape[0] - (2 * buffer)

    forecast = t_f[start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]
    obs = t_o[buffer:buffer + dext_lat, buffer:buffer + dext_lon]
    RMSE=np.zeros((forecast.shape[0],forecast.shape[1]))
    lats_f1=lat_f[start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]
    lons_f1=lon_f[start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]

    RMSE=abs(obs-forecast)
    return(RMSE, lats_f1, lons_f1, rlat_f, rlon_f, rlat_o, rlon_o)

import cartopy.crs as ccrs
import cartopy.feature

pdf='RMSE_Patterns'
buf=5
for i in range(1,9):
    nam , lats_f1, lons_f1, rlat_f, rlon_f, rlat_o, rlon_o   = calculate_MAPS_RMSE_of_the_member(i, buffer=buf)
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
    v = np.linspace(0, 1, 11, endpoint=True)
    cs = plt.contourf(lons_f1,lats_f1,nam, v, transform=ccrs.PlateCarree(), cmap=plt.cm.terrain)
    cb = plt.colorbar(cs)
    cb.set_label('RMSE [K]', fontsize=20)
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
    plt.hlines(y=min(rlat_f), xmin=min(rlon_f), xmax=max(rlon_f), color='red',linestyles= 'dashed', linewidth=2)
    plt.hlines(y=max(rlat_f), xmin=min(rlon_f), xmax=max(rlon_f), color='red',linestyles= 'dashed', linewidth=2)
    plt.vlines(x=min(rlon_f), ymin=min(rlat_f), ymax=max(rlat_f), color='red',linestyles= 'dashed', linewidth=2)
    plt.vlines(x=max(rlon_f), ymin=min(rlat_f), ymax=max(rlat_f), color='red',linestyles= 'dashed', linewidth=2)

    plt.hlines(y=min(rlat_o), xmin=min(rlon_o), xmax=max(rlon_o), color='black',linestyles= 'dashed', linewidth=2)
    plt.hlines(y=max(rlat_o), xmin=min(rlon_o), xmax=max(rlon_o), color='black',linestyles= 'dashed', linewidth=2)
    plt.vlines(x=min(rlon_o), ymin=min(rlat_o), ymax=max(rlat_o), color='black',linestyles= 'dashed', linewidth=2)
    plt.vlines(x=max(rlon_o), ymin=min(rlat_o), ymax=max(rlat_o), color='black',linestyles= 'dashed', linewidth=2)

    plt.hlines(y=min(rlat_o[buf:-buf]), xmin=min(rlon_o[buf:-buf]), xmax=max(rlon_o[buf:-buf]), color='black', linewidth=4)
    plt.hlines(y=max(rlat_o[buf:-buf]), xmin=min(rlon_o[buf:-buf]), xmax=max(rlon_o[buf:-buf]), color='black', linewidth=4)
    plt.vlines(x=min(rlon_o[buf:-buf]), ymin=min(rlat_o[buf:-buf]), ymax=max(rlat_o[buf:-buf]), color='black', linewidth=4)
    plt.vlines(x=max(rlon_o[buf:-buf]), ymin=min(rlat_o[buf:-buf]), ymax=max(rlat_o[buf:-buf]), color='black', linewidth=4)

    plt.title("Shift "+ str(i))



    xs, ys, zs = rp.transform_points(pc,
                                     np.array([-10, 90.0]),
                                     np.array([15, 65])).T
    ax.set_xlim(xs)
    ax.set_ylim(ys)

    plt.savefig("Figure_topo" +pdf+ str(i)+ "_"+str(buf)+".pdf")
    plt.close()


#
#
