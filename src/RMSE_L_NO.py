'''
Program to plot the changes of RMSE with respect to the changes in correlation length and number of observations
'''
DIR='/scratch/users/fallah/IO'
import numpy as np
import csv
#res= np.zeros((16,50))
res= np.zeros((5,50))
k=0
#for i in range(500,2100,100):
for i in range(500,1000,100):
    kk=0
    for j in range(1,51):
        if (j<10):
            names=DIR+'/Second_RUN_'+str(j)+'_'+str(i)+'/TEMP/RMSE_last_m'+str(500+j)+'.pdf.csv'
        else:
            names=DIR+'/Second_RUN_'+str(j)+'_'+str(i)+'/TEMP/RMSE_last_m'+str(5000+j)+'.pdf.csv'
        result = np.array(list(csv.reader(open(names, "rb"), delimiter=','))).astype('float')
        print(result)
        res[k,kk]=result[0,1]
        print(res[k,kk])
        print(k,kk)
        kk=kk+1
    k=k+1



import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.set_size_inches(14, 10)
#for i in range(16):
x=range(1,51)

for i in range(5):
    ax.plot(x,res[i,:],'o-', label=str(i*100+500), lw=3, alpha=.7, ms=10)
    ax.legend(loc='upper center', shadow=True)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_title("", y=1.05)
ax.set_ylabel(r"$RMSE$", labelpad=5,size=32)
ax.set_xlabel(r"$L$", labelpad=5,size=32)
plt.legend(loc=4, shadow=True,fontsize=32)
plt.xlim(0,51)
plt.tick_params(axis='both', which='major', labelsize=22)
plt.savefig('Correlation_vs_RMSE.pdf')