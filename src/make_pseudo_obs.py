def extract_pseudo(NN=600):
    '''
    :param NN: number of observations
    :return: PO, lon, lat, rlon, rlat pseudo obs and their locations in rotated and regular grid
    '''

    import numpy as np
    np.random.seed(777)
    import random
    random.seed(777)
    from RMSE_MAPS_INGO import read_data_from_mistral as rdfm
    from CCLM_OUTS import rand_station_locations as rsl
    s, t = rsl(N=1000, sed=777)
    TT=t.values()
    SS=s.values()
    from rotgrid import Rotgrid

    mapping = Rotgrid(-165.0, 46.0, 0, 0)
    for i in range(0, NN):
        print(t.values()[i])
        (TT[i], SS[i]) = mapping.transform(TT[i], SS[i])

    points=np.zeros((NN,3))
    points[:, 1] = SS[0:NN]
    points[:, 2] = TT[0:NN]

    t_o, lat_o, lon_o, rlat_o, rlon_o = rdfm(dir='/work/bb0962/work3/member_relax_3_big/post/',
                                             name='member_relax_3_T_2M_ts_monmean_1995.nc',
                                             var='T_2M')


    print(t_o.shape)
    Interp_Vals=np.zeros((NN,12))
    Interp_Vals_dirty=np.zeros((NN,12))
    noise=np.zeros((NN,12))
    from scipy.interpolate import RegularGridInterpolator as RegInt
    z=range(0,12)
    my_interpolating_function = RegInt((z,rlat_o, rlon_o), t_o, method='nearest')
    for i in range(0,12):
        points[:, 0] = np.zeros(NN)+i
        Interp_Vals[:,i] = my_interpolating_function(points)
    for k in range(0,NN):
        #noise[k,:] = np.random.normal(0, np.sqrt(np.var(Interp_Vals[k,:])/200), 12)
        noise[k,:] = np.random.normal(0, .5, 12)
        Interp_Vals_dirty[k,:] = Interp_Vals[k,:] + noise[k,:]


    return(Interp_Vals_dirty, Interp_Vals, TT[0:NN], SS[0:NN], t_o, rlon_o, rlat_o)

# Programs body
import numpy as np
NN=200
Temp_Station_dirty, Temp_Station, rlon_s, rlat_s, t_o , rlon_o, rlat_o=extract_pseudo(NN)

#for checking put flag='TRUE'
flag=False

if flag==True:
    import matplotlib.pyplot as plt
    plt.contourf(rlon_o, rlat_o, t_o[1, :, :]-273,100,cmap='jet', vmin=-10, vmax=20)
    plt.colorbar()
    plt.scatter(rlon_s, rlat_s, c=np.squeeze(Temp_Station_dirty[:,1])-273, cmap='jet', s=50, vmin=-10, vmax=20)
    plt.show()


if flag==True:
    import matplotlib.pyplot as plt
    #plt.contourf(rlon_o, rlat_o, t_o[1, :, :]-273,100,cmap='jet', vmin=-10, vmax=20)
    #plt.colorbar()
    s=np.power(Temp_Station_dirty[:, 1] - Temp_Station[:, 1], 2)
    s=np.sqrt(s)
    plt.scatter(rlon_s, rlat_s, c=np.squeeze(s), cmap='jet', s=50, vmin=0, vmax=2)
    plt.colorbar()
    plt.show()

# Now test it with the grid
# test perfect!!!
import csv
from itertools import izip
from itertools import repeat
with open('Stations_DATA.csv', 'wb') as f:
    writer = csv.writer(f)
    for i in range(0,12):
        writer.writerows(izip(rlon_s,rlat_s,Temp_Station[:,i],Temp_Station_dirty[:,i],list(repeat(i,NN))))



import pandas as pd
df = pd.read_csv('Stations_DATA.csv')
df.columns=['lon','lats','Vals','Vals_dirty','Time']

