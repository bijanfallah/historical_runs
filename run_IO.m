% Program to read INOUT files and run the IO scheme
%DIR='/var/autofs/net/home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/CCLM/Python_Codes/historical_runs/src/TEMP';
system('cp /home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/CCLM/Python_Codes/historical_runs/src/TEMP/INPUT.csv ./')
%system('cp /var/autofs/net/home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/CCLM/Python_Codes/historical_runs/src/TEMP/INPUT.csv ./')
system('cp /home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/CCLM/Python_Codes/historical_runs/src/TEMP/LON.out ./')
system('cp /home/fallah/Documents/DATA_ASSIMILATION/Bijan/CODES/CCLM/Python_Codes/historical_runs/src/TEMP/LAT.out ./')

DIR='./'
INPUT=load(strcat(DIR,'/INPUT.csv'));
LON=load(strcat(DIR,'/LON.out'));
LAT=load(strcat(DIR,'/LAT.out'));
lenx = 20; % Correlation length in x direction
leny = 20; % Correlation length in y direction
m    = 50; % Number of influential points
  for i=0:11
    iter=find(INPUT(:,4)==i);
   % iter
    i
    [fi,vari] = optiminterp2(INPUT(iter,1),INPUT(iter,2),INPUT(iter,3),INPUT(iter,5),lenx,leny,m,LON,LAT);
    csvwrite(strcat('fi',num2str(i),'.csv'),reshape(fi',size(fi)(2),size(fi)(1)))
    csvwrite(strcat('vari',num2str(i),'.csv'),reshape(vari',size(fi)(2),size(fi)(1)))

  endfor

