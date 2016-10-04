#!/bin/bash

set -ex

NN=500
COR_LEN=1
DIR_python='/home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/CCLM/Python_Codes/historical_runs/src'
DIR_OI='/home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/Optimal_Interpolation/'
DIR_WORK='/scratch/users/fallah/'
while [ $NN -lt 1001 ]; do
 while [ $COR_LEN -lt 61 ]; do
  
     NAME='Second_RUN'
     NAME=${NAME}_${COR_LEN}_${NN}
     mkdir ${DIR_WORK}${NAME}
     cp ${DIR_python}/TEMP/*.py ${DIR_WORK}${NAME}/
     cp ${DIR_python}/*py ${DIR_WORK}${NAME}/
     cp -r ${DIR_OI}optiminterp ${DIR_WORK}${NAME}/

     
     M=50 #Number of influential points

     XX="$DIR_WORK$NAME/Stations$NAME"
     cd $DIR_WORK$NAME
     sed -i "s/NN=600/NN=$NN/g" ${DIR_WORK}${NAME}/make_pseudo_obs.py
     #sed -i "s/NN=500);/NN=$NN);/g" ${DIR_WORK}/${NAME}/CCLM_OUTS.py
     sed -i "s/'RMSE_Patterns_'/'RMSE_Patterns_$NAME'/g" ${DIR_WORK}${NAME}/RMSE_MAPS_INGO.py
     sed -i "s/Stations/Stations$NAME/g" ${DIR_WORK}${NAME}/PLOT_Stations.py
     sed -i "s/NN=1000/NN=$NN/g" ${DIR_WORK}${NAME}/PLOT_Stations.py
     sed -i "s/NN=1000#number/NN=$NN#number/g" ${DIR_WORK}${NAME}/Create_Input_FIles.py
     sed -i "s/NN=1000#number/NN=$NN#number/g" ${DIR_WORK}${NAME}/run_octave.py
     var1=$(echo ${DIR_OI}optiminterp/inst/)
     var2=$(echo ${DIR_WORK}${NAME}/optiminterp/inst/)
     sed -i "s%$var1%$var2%g" ${DIR_WORK}${NAME}/run_octave.py
     
     sed -i "s/'last_m100_l20/'last_m$M$COR_LEN/g" ${DIR_WORK}${NAME}/run_octave.py
     sed -i "s/lenx = 20;/lenx = $COR_LEN/g" ${DIR_WORK}${NAME}/optiminterp/inst/run_IO.m
     sed -i "s/leny = 20;/leny = $COR_LEN/g" ${DIR_WORK}${NAME}/optiminterp/inst/run_IO.m
     sed -i "s/m= 50;/m= $M/g" ${DIR_WORK}${NAME}/optiminterp/inst/run_IO.m
     var1=$(echo ${DIR_python})
     var2=$(echo ${DIR_WORK}${NAME})
     sed -i "s%$var1%$var2%g" ${DIR_WORK}${NAME}/optiminterp/inst/run_IO.m


     # Python calls:

     python ${DIR_WORK}${NAME}/PLOT_Stations.py

     python ${DIR_WORK}${NAME}/make_pseudo_obs.py

     python ${DIR_WORK}${NAME}/Create_Input_FIles.py

     python ${DIR_WORK}${NAME}/run_octave.py

     #let COR_LEN=COR_LEN+1
     COR_LEN=`expr $COR_LEN + 1`
     echo $COR_LEN
 done
 #let NN=NN+100
 NN=`expr $NN + 100`
 echo $NN
done





