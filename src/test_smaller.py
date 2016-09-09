from CCLM_OUTS import Plot_CCLM
import matplotlib.pyplot as plt
import gc

Plot_CCLM(bcolor='black', grids='TRUE')

for i in xrange(4,5):
    Plot_CCLM(dir_mistral='/work/bb0962/work2/member0'+str(i)+'_relax_0_small/post/', name='member0'+str(i)+'_relax_0_T_2M_ts_monmean_1995.nc',
          bcolor='cyan', var='T_2M', flag='FALSE', color_map='FALSE', alph=.6+(.4/i), grids='FALSE', grids_color='yellow')

Plot_CCLM(dir_mistral='/work/bb0962/work2/member_relax_0_small/post/', name='member_relax_0_T_2M_ts_monmean_1995.nc',
          bcolor='red', var='T_2M', flag='FALSE', color_map='FALSE', alph=1, grids='FALSE',grids_color='red')

pdf='test_smaller_'
plt.savefig("Figure_" +pdf+ ".pdf")
plt.close()
gc.collect()
