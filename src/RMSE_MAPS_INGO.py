# Program to show the maps of RMSE averaged over time
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import os
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from CCLM_OUTS import Plot_CCLM
# option == 1 ->  shift 4 with default cclm domain and nboundlines = 3
# option == 2 ->  shift 4 with smaller cclm domain and nboundlines = 3
# option == 3 ->  shift 4 with smaller cclm domain and nboundlines = 6
# option == 4 ->  shift 4 with corrected smaller cclm domain and nboundlines = 3
# option == 5 ->  shift 4 with corrected smaller cclm domain and nboundlines = 4
# option == 6 ->  shift 4 with corrected smaller cclm domain and nboundlines = 6
# option == 7 ->  shift 4 with corrected smaller cclm domain and nboundlines = 9
# option == 8 ->  shift 4 with corrected bigger cclm domain and nboundlines = 3
from CCLM_OUTS import Plot_CCLM
def read_data_from_mistral(dir='/work/bb0962/work1/work/member/post/',name='member_T_2M_ts_seasmean.nc',var='T_2M'):
    # type: (object, object, object) -> object
    #a function to read the data from mistral work

    """

    :rtype: object
    """
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

def calculate_MAPS_RMSE_of_the_member(member='1', buffer=4, option=0):
    # function to cut the area and calculate RMSE
    # buffer is the number of grid points to be skipeed
    #
    pdf = 'RMSE_Patterns_'
    if option == 1:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work1/work/member/post/',
                                                                   name='member_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work1/work/member0' + str(member) + '/post/',
            name='member0' + str(member) + '_T_2M_ts_monmean_1995.nc',
            var='T_2M')
        #pdf_name="Figure_" +pdf+ str(member)+ "_"+str(buf)+"_Default.pdf"
        pdf_name="RMSE_"+"_Default.pdf"

    if option == 2:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work2/member/post/',
                                                                   name='member_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) + '/post/',
            name='member0' + str(member) + '_T_2M_ts_monmean_1995.nc',
            var='T_2M')
        pdf_name="Figure_" +pdf+ str(member)+ "_"+str(buf)+"_Small.pdf"
    if option == 3:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work2/member/post/',
                                                                   name='member_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) + '_relax/post/',
            name='member0' + str(member) + '_relax_T_2M_ts_monmean_1995.nc',
            var='T_2M')
        pdf_name="Figure_" +pdf+ str(member)+ "_"+str(buf)+"_Small_relax6.pdf"



    if option == 4:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work2/member_relax_0_small/post/',
                                                                   name='member_relax_0_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) + '_relax_0_small/post/',
            name='member0' + str(member) + '_relax_0_T_2M_ts_monmean_1995.nc',
            var='T_2M')
        #pdf_name = "Figure_" + pdf + str(member) + "_" + str(buf) + "relax_0_small.pdf"
        pdf_name = "Figure03_RMSE.pdf"
    if option == 5:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work2/member_relax_4_small/post/',
                                                                   name='member_relax_4_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) + '_relax_4_small/post/',
            name='member0' + str(member) + '_relax_4_T_2M_ts_monmean_1995.nc',
            var='T_2M')
       # pdf_name = "Figure_" + pdf + str(member) + "_" + str(buf) + "relax_9_small.pdf"
        pdf_name="Figure04_RMSE.pdf"
    if option == 6:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work2/member_relax_6_small/post/',
                                                                   name='member_relax_6_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) + '_relax_6_small/post/',
            name='member0' + str(member) + '_relax_6_T_2M_ts_monmean_1995.nc',
            var='T_2M')
       # pdf_name = "Figure_" + pdf + str(member) + "_" + str(buf) + "relax_6_small.pdf"
        pdf_name="Figure05_RMSE.pdf"
    if option == 7:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work2/member_relax_9_small/post/',
                                                                   name='member_relax_9_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) + '_relax_9_small/post/',
            name='member0' + str(member) + '_relax_9_T_2M_ts_monmean_1995.nc',
            var='T_2M')
       # pdf_name = "Figure_" + pdf + str(member) + "_" + str(buf) + "relax_9_small.pdf"
        pdf_name="Figure06_RMSE.pdf"
    if option == 8:
        t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work3/member_relax_3_big/post/',
                                                                   name='member_relax_3_T_2M_ts_monmean_1995.nc', var='T_2M')
        t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work3/member0' + str(member) + '_relax_3_big/post/',
            name='member0' + str(member) + '_relax_3_T_2M_ts_monmean_1995.nc',
            var='T_2M')
       # pdf_name = "Figure_" + pdf + str(member) + "_" + str(buf) + "relax_9_small.pdf"
        pdf_name="Figure07_RMSE.pdf"
    #rel='6'
    #t_o, lat_o, lon_o, rlat_o, rlon_o = read_data_from_mistral(dir='/work/bb0962/work2/member/post/',name='member_T_2M_ts_monmean_1995.nc',var='T_2M')
    #t_f, lat_f, lon_f, rlat_f, rlon_f  = read_data_from_mistral(dir='/work/bb0962/work2/member/post/',name='member_T_2M_ts_monmean_1995.nc',var='T_2M')
    #t_f, lat_f, lon_f, rlat_f, rlon_f  = read_data_from_mistral(dir='/work/bb0962/work2/member0'+str(member)+'/post/', name='member0'+str(member)+'_T_2M_ts_monmean_1995.nc',
    #                                       var='T_2M')
    #t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) +'_relax_'+str(rel)+'/post/',
    #    name='member0' + str(member) +'_relax_'+str(rel)+ '_T_2M_ts_monmean_1995.nc',
    #                                           var='T_2M')
    # t_f, lat_f, lon_f, rlat_f, rlon_f = read_data_from_mistral(dir='/work/bb0962/work2/member0' + str(member) +'_relax'+'/post/',
    #     name='member0' + str(member) +'_relax_T_2M_ts_monmean_1995.nc',
    #                                            var='T_2M')


    os.system('rm -f *.nc')
    row_lat = lat_o[buffer, buffer].squeeze()
    row_lon = lon_o[buffer, buffer].squeeze()
    #print(row_lat)
    #print(row_lon)
    #print(lat_o)[0,0]
    #print(lat_o)[0,-1]
    #print(lon_f)
    #start_lon = np.where(lon_f == row_lon)[-1][0]
    #start_lat = np.where(lat_f == row_lat)[0][-1]

    #start_lon = np.where((lon_f-row_lon)<0.001)[-1][0]
    #start_lat = np.where((lat_f-row_lat)<0.001)[0][-1]
    start_lon=(buffer+4)
    start_lat=(buffer-4)
    #print('nowwwwwwwww')
    #print(start_lat)
    #print(start_lon)
    dext_lon = t_o.shape[2] - (2 * buffer)
    dext_lat = t_o.shape[1] - (2 * buffer)
    #print('thennnnnnnn')
    #print(dext_lon)
    #print(dext_lat)
    forecast = t_f[:, start_lat:start_lat + dext_lat, start_lon:start_lon + dext_lon]
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

    return(RMSE, lats_f1, lons_f1, rlat_f, rlon_f, rlat_o, rlon_o, pdf_name)

import cartopy.crs as ccrs
import cartopy.feature

option=8
buf=20
for i in range(4,5):
    nam , lats_f1, lons_f1, rlat_f, rlon_f, rlat_o, rlon_o , pdf_name   = calculate_MAPS_RMSE_of_the_member(i, buffer=buf, option=option)
    fig = plt.figure('1')
    fig.set_size_inches(14, 10)
    #Plot_CCLM(bcolor='black', grids='FALSE')
    #rp = ccrs.RotatedPole(pole_longitude=-162.0,
    #                      pole_latitude=39.25,
    #                      globe=ccrs.Globe(semimajor_axis=6370000,
    #                                       semiminor_axis=6370000))

    rp = ccrs.RotatedPole(pole_longitude=-165.0,
                          pole_latitude=46.0,
                          globe=ccrs.Globe(semimajor_axis=6370000,
                                           semiminor_axis=6370000))


    pc = ccrs.PlateCarree()
    ax = plt.axes(projection=rp)
    ax.coastlines('50m', linewidth=0.8)
    #ax.add_feature(cartopy.feature.LAKES,
    #               edgecolor='black', facecolor='none',
    #               linewidth=0.8)
    v = np.linspace(0, 1, 11, endpoint=True)
    cs = plt.contourf(lons_f1,lats_f1,nam, v, transform=ccrs.PlateCarree(), cmap=plt.cm.terrain)
    cb = plt.colorbar(cs)
    cb.set_label('RMSE [K]', fontsize=20)
    cb.ax.tick_params(labelsize=20)
    ax.add_feature(cartopy.feature.OCEAN,
                   edgecolor='black', facecolor='white',
                   linewidth=0.8)
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
    #ax.text(26, -29.69, r'$40\degree E$',
    #        fontsize=15)
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

    plt.title("Shift "+ str(i)+pdf_name)

    xs, ys, zs = rp.transform_points(pc,
                                     np.array([-17, 105.0]),
                                     np.array([3, 60])).T
    # rp = ccrs.RotatedPole(pole_longitude=-162.0,
    #                      pole_latitude=39.25,
    #                      globe=ccrs.Globe(semimajor_axis=6370000,
    #                                          semiminor_axis=6370000))
    ax.set_xlim(xs)
    ax.set_ylim(ys)

    plt.savefig(pdf_name)

    plt.close()

