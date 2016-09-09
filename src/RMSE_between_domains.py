# from CCLM_OUTS import Plot_CCLM
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import os
from netCDF4 import Dataset as NetCDFFile
import numpy as np
season='JJA'

def read_data_from_mistral(dir='/work/bb0962/work1/work/member/post/',name='member_T_2M_ts_seasmean.nc',var='T_2M'):
    #a function to read the data from mistral work

    CMD = 'scp $mistral:' + dir + name + ' ./'
    os.system(CMD)
    nc = NetCDFFile(name)
    os.remove(name)
    lats = nc.variables['lat'][:]
    lons = nc.variables['lon'][:]
    t = nc.variables[var][:].squeeze()
    nc.close()

    return (t,lats,lons)

def calculate_RMSE_of_the_member(member='1', buffer=4):
    # function to cut the area and calculate RMSE
    # buffer is the number of grid points to be skipeed
    #
    t, lats, lons = read_data_from_mistral(dir='/work/bb0962/work1/work/member/post/',name='member_T_2M_ts_seasmean.nc',var='T_2M')
    t1, lats1, lons1 = read_data_from_mistral(dir='/work/bb0962/work1/work/member0'+str(member)+'/post/', name='member0'+str(member)+'_T_2M_ts_seasmean.nc',
                                           var='T_2M')
    os.system('rm -f *.nc')
    row_lat = lats[buffer, buffer].squeeze()
    row_lon = lons[buffer, buffer].squeeze()
    start_lon = np.where(lons1 == row_lon)[-1][0]
    start_lat = np.where(lats1 == row_lat)[0][-1]
    dext_lon = t.shape[2]-(2*buffer)
    dext_lat = t.shape[1]-(2*buffer)
    forecast = t1[:, start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]
    obs = t[:, buffer:buffer + dext_lat, buffer:buffer + dext_lon]
    size_area=obs.shape[1]*obs.shape[2]
    RMSE=np.zeros((obs.shape[0]-1))
    for i in range(0,t.shape[0]-1):
        forecast_resh=forecast[i,:,:].reshape(size_area)
        obs_resh=obs[i,:,:].reshape(size_area)

        RMSE[i] = mean_squared_error(obs_resh, forecast_resh) ** 0.5
    return(RMSE)
pdf='time_series'
buf=5
for i in range(1,9):
    nam    = calculate_RMSE_of_the_member(i, buffer=buf)
    fig = plt.figure('1')
    fig.set_size_inches(14, 10)
    plt.plot(nam, label = str(i))
plt.legend(loc='best')
plt.savefig("Figure_" +pdf+ "_"+str(buf)+".pdf")
plt.close()
# TODO make maps of the RMSE for some random time !!
# TODO Then maybe run CCLM with smaller domain !!!
