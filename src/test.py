from CCLM_OUTS import Plot_CCLM
import matplotlib.pyplot as plt
Plot_CCLM(bcolor='black', grids='FALSE')

for i in xrange(1,8):
    Plot_CCLM(dir_mistral='/work/bb0962/work1/work/member0'+str(i)+'/post/', name='lffd1979010100c.nc',
          bcolor='cyan', var='HSURF', flag='FALSE', color_map='FALSE', alph=.6+(.4/i), grids='FALSE', grids_color='yellow')

Plot_CCLM(dir_mistral='/work/bb0962/work1/work/member/post/', name='lffd1979010100c.nc',
          bcolor='red', var='HSURF', flag='FALSE', color_map='FALSE', alph=1, grids='FALSE',grids_color='red')

pdf='test'
plt.savefig("Figure_" +pdf+ ".pdf")
plt.close()
