#This program calculates normal shockwave properties for known upstream conditions

print('Enter 1 for earth, 2 for mars  ')
planet=int(input())

import math

if planet==1:
	gama=1.4
	gama=float(gama)
	print('You selcted Earth')
else:
	gama=1.29
	gama=float(gama)
	print('You selected Mars')

print('Gamma set to ',gama)

print(' ')
print('Enter the upstream mach number')
m0=float(input())
m1=math.sqrt(  ((gama - 1) * pow(m0,2) + 2) / (2 * gama * pow(m0,2) - (gama - 1))  )
print('The downstream mach number is ',m1)

print(' ')
def calc():
    print(' ')
    print('Enter 1 for pressure, 2 for temperature, 3 for density, 4 to quit')
    choice=int(input())


    if choice==1:
        print(' ')
        print('Enter the upstream static pressure in pascals  ')
        p0=float(input())
        p1=p0 * (2* gama * math.pow(m0,2) - (gama - 1)) / (gama + 1)
        print('The downstream pressure is', p1 ,'pascals')
        calc()
    elif choice==2:
        print(' ')
        print('Enter the upstream static temperature in kelvin')
        t0=float(input())
        t1= t0 * ((2 * gama * pow(m0,2) - (gama - 1)) * ((gama - 1) * pow(m0,2) + 2) / ((gama + 1)**2 * pow(m0,2))) 
        print('The downstream static temperature is',t1 ,'kelvin')
        calc()
    elif choice==3:
        print(' ')
        print('Enter the upstream density in kg/m3 ')
        d0=float(input())
        d1=d0*( ((gama + 1) * pow(m0,2) ) / ((gama -1 ) * pow(m0,2) + 2) )
        print('The downstream density is ',d1 ,'kg/m3')
        calc()
    else:
        print(' ')
        print('Press enter or click OK to exit, Thank You!')
        exit()

calc()



