#This code solves a 2 dimensional target interception problem using the
#velocity pursuit guidance law
#Warning:This code was written intutively without any reference material
#and might not be correct.



import numpy as np; import matplotlib.pyplot as plt
print('Modules Imported \n\n')


# Initial Positions and velocities
xT,yT=5000,100     #initial target position
xM,yM=1,1         #initial missile position
velT=20              #target velocity
velM=200             #missile velocity
angT=-2              #target angle of motion
angM=45             #missile launch angle

#Initialization

tetha=np.arctan(yT/xT)    #Target bearing
rT=np.hypot(xT,yT)        #Target radial

alpha=np.arctan(yM/xM)    #Missile bearing
rM=np.hypot(xM,yM)        #Missile radial


rMT=np.hypot((xT-xM),(yT-yM))        #Realtive radial
gamma=np.arctan((yT-yM)/(xT-xM))     #Relative bearing

xTdata=[xT]
yTdata=[yT]
tethadata=[tetha]
rTdata=[rT]

xMdata=[xM]
yMdata=[yM]
alphadata=[alpha]
rMdata=[rM]

rMTdata=[rMT]
gammadata=[gamma]

# Velocity Components
uT,vT=velT*np.cos(np.deg2rad(angT)),velT*np.sin(np.deg2rad(angT))
uM,vM=velM*np.cos(np.deg2rad(angM)),velM*np.sin(np.deg2rad(angM))

#Time initialized to Zero
t=0
tdata=[0]

print('starting calculation')

#Main Calculator
while(1):
 if rMT<(rMTdata[0]/10):
     s=0.01
 else:
     s=0.1
 t=t+s
 tdata.append(t)

 xT=xT + uT*s
 yT=yT + vT*s
 tetha=np.arctan(yT/xT)
 rT=np.hypot(xT,yT)
 xTdata.append(xT)
 yTdata.append(yT)
 tethadata.append(tetha)
 rTdata.append(rT)
 
 
 uM,vM=velM*np.cos(gamma),velM*np.sin(gamma)
 
 xM=xM + uM*s
 yM=yM + vM*s
 
 gamma=np.arctan((yT-yM)/(xT-xM))
 alpha=np.arctan(yM/xM)
 rM=np.hypot(xM,yM)
 rMT=np.hypot((xT-xM),(yT-yM))
 
 xMdata.append(xM)
 yMdata.append(yM)
 alphadata.append(alpha)
 rMdata.append(rM)
 rMTdata.append(rMT)
 
 gammadata.append(gamma)
 print('calculation done for time t = ',t ,' seconds')

 if rMTdata[-1]>rMTdata[-2]:
     break
 
 
  
print('\n\n\n Closest possible distance is ',rMTdata[-2],'metres')
print('Target at position ',xTdata[-2],yTdata[-2])
print('Missile at position ',xMdata[-2],yMdata[-2])
print('Closest approach occurs at ',tdata[-2],' seconds')

plt.plot(xMdata[:-1],yMdata[:-1],'--o',xTdata[:-1],yTdata[:-1],'--o',[xMdata[-2],xTdata[-2]],[yMdata[-2],yTdata[-2]],'--')
plt.xlabel('X coordinate -->  metres')
plt.ylabel('Y coordinate -->  metres')
plt.title('Trajectories, Velocity Pursuit')
plt.legend(['missile','target','final \nradial'],bbox_to_anchor=(0,0),loc=4)
plt.show()


	
