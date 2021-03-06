import sys
sys.modules[__name__].__dict__.clear()
from CCLM_OUTS import Plot_CCLM
import matplotlib.pyplot as plt
fig = plt.figure('1')
fig.set_size_inches(14, 10)
NN=1000
Plot_CCLM(dir_mistral='/work/bb0962/work3/member_relax_3_big/post/',name='member_relax_3_T_2M_ts_monmean_1995.nc',bcolor='red',var='T_2M',flag='FALSE',color_map='TRUE', alph=1, grids='TRUE', grids_color='red', rand_obs='TRUE', NN=NN)
plt.savefig('Stations.pdf')
plt.close()

### http://eca.knmi.nl/download/ensembles/Haylock_et_al_2008.pdf


