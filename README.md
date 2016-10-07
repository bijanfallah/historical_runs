# Optimal Interpolation
Optimal Interpolation of Psdeudo observations in CCLM model
This is the suplemantary material for my submitted paper about the usage of Optimal Interpolation in long-term climate simulations
Version 0.0

## How to run the code:

* First the monthly temperature values shall be calculated for CCLM outputs. 
* Then after editing the io_scrpt.sh and running the code the results are created in pdf format.

## sub codes of io_scrpt.sh:

* PLOT_Stations.py      :  creates the plot with observations for model domain
* make_pseudo_obs.py    :  makes the pseudo-observations
* Create_Input_FIles.py :  creates input files for the OI code
* run_octave.py         :  conducts the Data Assimilation
