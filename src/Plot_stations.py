from __future__ import division
# program to plot the Breitenmosser Stations
__author__ = 'Bijan'
'''
This is a function to plot CCLM outputs.

'''
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature
#Plot_CCLM(bcolor='black', grids='FALSE')
#Plot_CCLM(dir_mistral='/work/bb0962/work1/work/member/post/', name='member_T_2M_ts_seasmean.nc',
#          bcolor='red', var='T_2M', flag='FALSE', color_map='FALSE', alph=1, grids='FALSE',grids_color='red')
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
file= open('/var/autofs/net/home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/Optimal_Interpolation/optiminterp/src/Breitenmosser_OBS_coord.txt','r')
for line in file:
    line = line.strip()
    columns = line.split()
    lat = columns[0]
    lon = columns[1]
file.close()
plt.scatter(lon, lat, marker='o', c=grids_color, s=5, zorder=10)
#rlonss, rlatss = np.meshgrid(rlons,rlats)
#plt.scatter(rlonss, rlatss, marker='o', c=grids_color, s=5, zorder=10)
xs, ys, zs = rp.transform_points(pc,
                                     np.array([-10, 90.0]),
                                     np.array([15, 65])).T
ax.set_xlim(xs)
ax.set_ylim(ys)
pdf='Stations'
plt.savefig(pdf+ ".pdf")
plt.close()
