import sys
sys.modules[__name__].__dict__.clear()
from CCLM_OUTS import Plot_CCLM
import matplotlib.pyplot as plt
fig = plt.figure('1')
fig.set_size_inches(14, 10)
Plot_CCLM(dir_mistral='/work/bb0962/work3/member_relax_3_big/post/',name='member_relax_3_T_2M_ts_monmean_1995.nc',bcolor='red',var='T_2M',flag='FALSE',color_map='TRUE', alph=1, grids='TRUE', grids_color='red', rand_obs='TRUE')
plt.savefig('Stations.pdf')
plt.close()

### http://eca.knmi.nl/download/ensembles/Haylock_et_al_2008.pdf
# TODO: 1- Find the nearest obs grid to the station ---Done
# TODO: 2- Assign the value of this point to the station (or using the interpolation method !!!????) --Done
# TODO: 3- Add random white noise to the Station (import numpy as np, pure = np.linspace(-1, 1, 100),
# TODO:    noise = np.random.normal(0, 1, 100),signal = pure + noise)
# TODO: Polish the code (reproduceable)
# TODO: add the YUSCF-- files of the two domain runs to the pdf!!!
# TODO: and the netcdf file?!!!!!

