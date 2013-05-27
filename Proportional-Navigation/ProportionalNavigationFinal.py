#This code solves a 2 dimensional target interception problem using the
#proportional navigation guidance law

import numpy as np; import matplotlib.pyplot as plt
print('Modules Imported \n\n\n')

#Initial Conditions
xT,yT=4000,10000     #initial target position
xM,yM=1,1000         #initial missile position
velT=200              #target velocity
velM=300             #missile velocity
nT=-1                 #target normal acceleration
he=0                 #heading error
Np=4                 #navigation constant
beta=0               #target angle

#Initialization
beta=np.deg2rad(beta)
he=np.deg2rad(he)
rMT=np.hypot((xT-xM),(yT-yM))                       #Relative radial
uT,vT=velT*np.cos(beta),velT*np.sin(beta)          #Target Vel Components


lamda=np.arctan((yT-yM)/(xT-xM))                    #Relative Bearing
lead=np.arcsin((velT*np.sin(beta+lamda))/velM)      #Lead angle
tetha=lamda+lead
tehe=tetha+he
uM,vM=velM*np.cos(tehe),velM*np.sin(tehe)           #Missile vel components
uMT=uT-uM
vMT=vT-vM
xMT=xT-xM
yMT=yT-yM
velC=-((xMT*uMT + yMT*vMT)/rMT)                     #closing velocity


lamdaD=(xMT*vMT - uMT*uMT)/(rMT**2)
nC=Np*velC*lamdaD                                   #acceleration command to missile
uMD=nC*np.sin(lamda)
vMD=nC*np.cos(lamda)


velCdata=[velC]
xTdata=[xT]
yTdata=[yT]
lamdadata=[lamda]
leaddata=[lead]
tethadata=[tetha]
tehedata=[tehe]

xMdata=[xM]
yMdata=[yM]
betadata=[beta]

rMTdata=[rMT]

#Time initiated to Zero
t=0
tdata=[0]
#s=0.0001             #time step

print('starting calculation\n\n')

#Main Calculator
while(1):
 if rMT<(rMTdata[0]/10):
     s=0.01
 else:
     s=0.1
 t=t+s
 tdata.append(t)

 xT,yT=xT + uT*s,yT + vT*s
 
 betaD=nT/velT
 beta=beta + betaD*s
 uT,vT=velT*np.cos(beta),velT*np.sin(beta)


 xM,yM=xM + uM*s,yM + vM*s
 
 
 rMT=np.hypot((xT-xM),(yT-yM))
 lamda=np.arctan((yT-yM)/(xT-xM))
 lead=np.arcsin((velT*np.sin(beta+lamda))/velM)
 tetha=lamda+lead
 tehe=tetha+he
 
 uM,vM=np.cos(tehe)*(velM + uMD*s),np.sin(tehe)*(velM + vMD*s)

 

 uMT=uT-uM
 vMT=vT-vM
 xMT=xT-xM
 yMT=yT-yM
 velC=-((xMT*uMT + yMT*vMT)/rMT)
 lamdaD=(xMT*vMT - uMT*uMT)/(rMT**2)
 nC=Np*velC*lamdaD
 uMD=nC*np.sin(lamda)
 vMD=nC*np.cos(lamda)
 

 xTdata.append(xT)
 yTdata.append(yT)
 lamdadata.append(lamda)
 leaddata.append(lead)
 tethadata.append(tetha)
 tehedata.append(tehe)
 velCdata.append(velC)

 xMdata.append(xM)
 yMdata.append(yM)
 betadata.append(beta)

 rMTdata.append(rMT)
 print('calculation done for time t = ',t ,' seconds')

 if rMTdata[-1]>rMTdata[-2]:
     break


print('\n\n\n Closest possible distance is ',rMTdata[-2],'metres')
print('Target at position ',xTdata[-2],yTdata[-2])
print('Missile at position ',xMdata[-2],yMdata[-2])
print('Closest approach occurs at ',(tdata[-2]),' seconds')

plt.plot(xMdata[:-1],yMdata[:-1],'--o',xTdata[:-1],yTdata[:-1],'--o',[xMdata[-2],xTdata[-2]],[yMdata[-2],yTdata[-2]],'--')
plt.xlabel('X coordinate -->  metres')
plt.ylabel('Y coordinate -->  metres')
plt.title('Trajectories, Proportional Navigation')
plt.legend(['missile','target','final \nradial'],bbox_to_anchor=(0,0),loc=4)
plt.show()


 
 

 

 
 
 



