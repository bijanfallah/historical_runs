# run octave from python (IO code )
from oct2py import octave
import numpy as np
from RMSE_MAPS_INGO import read_data_from_mistral as rdfm
DIR='/home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/Optimal_Interpolation/optiminterp/inst/'
octave.run(DIR+"run_IO.m")

## read forecast :
#NN=1000#number of observations should be read from previous funcions!!!!
NN=600
month_length=12
t_f, lat_f, lon_f, rlat_f, rlon_f =rdfm(dir='/work/bb0962/work3/member04_relax_3_big/post/',
                                        name='member04_relax_3_T_2M_ts_monmean_1995.nc',
                                        var='T_2M')
print(t_f.shape)
## add correction to forecast :
result_IO = t_f - t_f
import os.path
import csv
import numpy
from sklearn.metrics import mean_squared_error
if os.path.isfile(DIR+'fi'+str(month_length-1)+'.csv')==True:
    for i in range(0,month_length):
        print(i)
        fil=DIR + 'fi' + str(i) + '.csv'
        result=numpy.array(list(csv.reader(open(fil,"rb"),delimiter=','))).astype('float')
        result_IO[i,:,:] = np.squeeze(t_f[i,:,:]) + result
        #print(max(result_IO[i,:,:]))
        #print(max(result))
# have to polish from now on:
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

from RMSE_MAPS_INGO import read_data_from_mistral as rdfm
from CCLM_OUTS import Plot_CCLM

#plt.contourf(rlon_f, rlat_f, np.squeeze(result_IO[5,:,:]),50, cmap='jet', vmin=270, vmax=320)
#plt.colorbar()
#plt.show()
#plt.close()

# plot difference
buffer = 20
pdf_name= 'last_m100_l20.pdf'
t_o, lat_o, lon_o, rlat_o, rlon_o = rdfm(dir='/work/bb0962/work3/member_relax_3_big/post/',
                                         name='member_relax_3_T_2M_ts_monmean_1995.nc', var='T_2M')
start_lon=(buffer+4)
start_lat=(buffer-4)
dext_lon = t_o.shape[2] - (2 * buffer)
dext_lat = t_o.shape[1] - (2 * buffer)
forecast = result_IO[:, start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]
obs = t_o[:, buffer:buffer + dext_lat, buffer:buffer + dext_lon]
RMSE=np.zeros((forecast.shape[1],forecast.shape[2]))
lats_f1=lat_f[start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]
lons_f1=lon_f[start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]
#print(forecast.shape[:])
#print(obs.shape[:])
for i in range(0,forecast.shape[1]):
    for j in range(0,forecast.shape[2]):
        forecast_resh=np.squeeze(forecast[:,i,j])
        obs_resh=np.squeeze(obs[:,i,j])
        RMSE[i,j] = mean_squared_error(obs_resh, forecast_resh) ** 0.5
fig = plt.figure('1')
fig.set_size_inches(14, 10)
rp = ccrs.RotatedPole(pole_longitude=-165.0,
                          pole_latitude=46.0,
                          globe=ccrs.Globe(semimajor_axis=6370000,
                                           semiminor_axis=6370000))


pc = ccrs.PlateCarree()
ax = plt.axes(projection=rp)
ax.coastlines('50m', linewidth=0.8)
v = np.linspace(0, 1, 11, endpoint=True)
# Write the RMSE mean in a file
import csv
from itertools import izip
names='RMSE_'+pdf_name+'.csv'
with open(names, 'wb') as f:
     writer = csv.writer(f)
     writer.writerow([NN,np.mean(RMSE)])


cs=plt.contourf(lons_f1, lats_f1, RMSE,v, transform=ccrs.PlateCarree(), cmap=plt.cm.terrain)

cb = plt.colorbar(cs)
cb.set_label('RMSE [K]', fontsize=20)
cb.ax.tick_params(labelsize=20)
ax.gridlines()
ax.text(-45.14, 15.24, r'$45\degree N$',
        fontsize=15)
ax.text(-45.14, 35.73, r'$60\degree N$',
        fontsize=15)
ax.text(-45.14, -3.73, r'$30\degree N$',
        fontsize=15)
ax.text(-45.14, -20.73, r'$15\degree N$',
        fontsize=15)
ax.text(-19.83, -35.69, r'$0\degree $',
        fontsize=15)
ax.text(15.106, -35.69, r'$20\degree E$',
        fontsize=15)
plt.hlines(y=min(rlat_f), xmin=min(rlon_f), xmax=max(rlon_f), color='red',linestyles= 'dashed', linewidth=2)
plt.hlines(y=max(rlat_f), xmin=min(rlon_f), xmax=max(rlon_f), color='red',linestyles= 'dashed', linewidth=2)
plt.vlines(x=min(rlon_f), ymin=min(rlat_f), ymax=max(rlat_f), color='red',linestyles= 'dashed', linewidth=2)
plt.vlines(x=max(rlon_f), ymin=min(rlat_f), ymax=max(rlat_f), color='red',linestyles= 'dashed', linewidth=2)

plt.hlines(y=min(rlat_o), xmin=min(rlon_o), xmax=max(rlon_o), color='black',linestyles= 'dashed', linewidth=2)
plt.hlines(y=max(rlat_o), xmin=min(rlon_o), xmax=max(rlon_o), color='black',linestyles= 'dashed', linewidth=2)
plt.vlines(x=min(rlon_o), ymin=min(rlat_o), ymax=max(rlat_o), color='black',linestyles= 'dashed', linewidth=2)
plt.vlines(x=max(rlon_o), ymin=min(rlat_o), ymax=max(rlat_o), color='black',linestyles= 'dashed', linewidth=2)
plt.hlines(y=min(rlat_o[buffer:-buffer]), xmin=min(rlon_o[buffer:-buffer]), xmax=max(rlon_o[buffer:-buffer]), color='black', linewidth=4)
plt.hlines(y=max(rlat_o[buffer:-buffer]), xmin=min(rlon_o[buffer:-buffer]), xmax=max(rlon_o[buffer:-buffer]), color='black', linewidth=4)
plt.vlines(x=min(rlon_o[buffer:-buffer]), ymin=min(rlat_o[buffer:-buffer]), ymax=max(rlat_o[buffer:-buffer]), color='black', linewidth=4)
plt.vlines(x=max(rlon_o[buffer:-buffer]), ymin=min(rlat_o[buffer:-buffer]), ymax=max(rlat_o[buffer:-buffer]), color='black', linewidth=4)
Plot_CCLM(dir_mistral='/work/bb0962/work3/member_relax_3_big/post/',name='member_relax_3_T_2M_ts_monmean_1995.nc',bcolor='black',var='T_2M',flag='FALSE',color_map='TRUE', alph=1, grids='FALSE', grids_color='red', rand_obs='TRUE', NN=NN)
plt.title("Shift "+ str(4)+pdf_name)

xs, ys, zs = rp.transform_points(pc,
                                 np.array([-17, 105.0]),
                                 np.array([3, 60])).T
# rp = ccrs.RotatedPole(pole_longitude=-162.0,
#                      pole_latitude=39.25,
#                      globe=ccrs.Globe(semimajor_axis=6370000,
#                                          semiminor_axis=6370000))
ax.set_xlim(xs)
ax.set_ylim(ys)
# Plot_CCLM(bcolor='black', grids='FALSE', flag='FALSE')
plt.savefig(pdf_name)

plt.close()
