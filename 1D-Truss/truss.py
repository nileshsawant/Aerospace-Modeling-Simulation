#This code solves a simple problem of trusses using two links

import numpy as np
from decimal import *


class Stiffness:
	def __init__(self,angle,youngs,area,length):
		self.ang=angle
		self.you=youngs
		self.ar=area
		self.lnt=length
		self.c=(np.cos(np.deg2rad(self.ang)))
		self.s=(np.sin(np.deg2rad(self.ang)))
		self.matx=(np.array([[self.c**2,self.c*self.s,-self.c**2,-self.c*self.s],[self.c*self.s,self.s**2,-self.s*self.c,-self.s**2],[-self.c**2,-self.c*self.s,self.c**2,self.c*self.s],[-self.c*self.s,-self.s**2,self.c*self.s,self.s**2]]))
		self.ale=(self.ar*self.you)/self.lnt
		self.alematt=self.matx*self.ale

trus2=Stiffness(120,10e6,0.1,10)
trus3=Stiffness(60,10e6,0.1,10)
dispmat=np.array([0,0,0,1,0,0]).T
forcemat=np.array([0,0,0,-1732,0,0]).T

matb=np.zeros((6,6))
matc=np.zeros((6,6))

matb[:4,:4]=trus2.alematt
matc[2:,2:]=trus3.alematt

matk=matb+matc

tempmat=np.dot(matk,dispmat)

tempmat2=(forcemat/tempmat)

tempmat3=np.dot(matk,tempmat2)

print('The displacement matrix is: \n', np.around(tempmat2,decimals=10))
print('\n\n\n\n')
print('The force matrix is: \n', np.around(tempmat3,decimals=10))


input()
exit()


