from CCLM_OUTS import Plot_CCLM
import matplotlib.pyplot as plt
Plot_CCLM(bcolor='black')

Plot_CCLM(dir_mistral='/work/bb0962/work1/work/member/post/', name='lffd1979010100c.nc',
          bcolor='red', var='HSURF', flag='FALSE', color_map='FALSE')

Plot_CCLM(dir_mistral='/work/bb0962/work1/work/member02/post/', name='lffd1979010100c.nc',
          bcolor='red', var='HSURF', flag='FALSE', color_map='FALSE')

pdf='test'
plt.savefig("Figure_" +pdf+ ".pdf")
plt.close()
