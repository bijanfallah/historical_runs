from CCLM_OUTS import Plot_CCLM
import matplotlib.pyplot as plt
import gc

Plot_CCLM(bcolor='black', grids='TRUE')

for i in xrange(1,8):
    Plot_CCLM(dir_mistral='/work/bb0962/work1/work/member0'+str(i)+'/post/', name='member0'+str(i)+'_T_2M_ts_seasmean.nc',
          bcolor='cyan', var='T_2M', flag='FALSE', color_map='FALSE', alph=.6+(.4/i), grids='TRUE', grids_color='yellow')

Plot_CCLM(dir_mistral='/work/bb0962/work1/work/member/post/', name='member_T_2M_ts_seasmean.nc',
          bcolor='red', var='T_2M', flag='FALSE', color_map='FALSE', alph=1, grids='TRUE',grids_color='red')

pdf='test'
plt.savefig("Figure_" +pdf+ ".pdf")
plt.close()
gc.collect()