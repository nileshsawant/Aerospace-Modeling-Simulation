#!/Library/Frameworks/Python.framework/Versions/2.6/bin/python

# PROGRAM: stdatm.py
# FUNCTION: Provide (T,rho,p) for a given h_G (geometric altitude).
# Input: h_G
# Output: T,rho,p

import sys
import os
import math

T_s     = 288.16  # K
rho_s   = 1.225   # kg/m^3
p_s     = 101325  # N/m^2
g_0     = 9.80665 # m/s^2
R       = 8.3144e3/28.966 # N-m/kg-K
r_Earth = 6356.77e3 # m

hG = float(sys.argv[1]) # m

h = ( r_Earth / (r_Earth + hG) ) * hG

# Define (T,h) pair ranges, whether isotherm or gradient, and a if gradient.
tempDist = {
  0:{'type':'gradient','a':-6.5E-3,'T_low':288.16}, # [key] = geopotential altitude, [a] = K/m, [T_low] = K
  11000.0:{'type':'isotherm','a':None,'T_low':216.66},
  25000.0:{'type':'gradient','a':3E-3,'T_low':216.66},
  47000.0:{'type':'isotherm','a':None,'T_low':282.66},
  53000.0:{'type':'gradient','a':-4.5E-3,'T_low':282.66},
  79000.0:{'type':'isotherm','a':None,'T_low':165.66},
  90000.0:{'type':'gradient','a':4E-3,'T_low':165.66},
  105000.0:{'type':'terminus','a':None,'T_low':225.66},
  }

a = tempDist.keys()
a.sort()
if h < a[0]:
  print "Error 1: The geopotential altitude must be greater than %s." % a[0]
  sys.exit(1)
if h > a[-1]:
  print "Error 2: The geopotential altitude must be less than %s." % a[-1]
  sys.exit(1)

# @Function: all_gradient
# @Description: Determine temperature, pressure, and density for a gradient region in consistent metric units.
# @Input: h - target geopotential altitude
# @       h1 - reference geopotential altitude
# @       a - slope of gradient
# @       T1 - reference temperature
# @       p1 - reference pressure
# @       rho1 - reference density
# @Output: temp - temperature at given h
# @        press - pressure at given h
# @        dens - density at given h
def all_gradient(h,h1,a,T1,p1,rho1):
  temp  = T1 + a * ( h - h1 )
  press = p1 * ( temp / T1 ) ** ( - g_0 / R / a )
  dens  = rho1 * ( temp / T1 ) ** ( - g_0/R/a - 1)
  return(temp,press,dens)

# @Function: all_isotherm
# @Description: Determine temperature, pressure, and density for an isothermal region in consistent metric units.
# @Input: h - target geopotential altitude
# @       h1 - reference geopotential altitude
# @       a - slope of gradient
# @       T1 - reference temperature
# @       p1 - reference pressure
# @       rho1 - reference density
# @Output: temp - temperature at given h
# @        press - pressure at given h
# @        dens - density at given h
def all_isotherm(h,h1,a,T1,p1,rho1):
  temp  = T1
  press = p1 * math.exp(-g_0/R/T1*(h-h1))
  dens  = rho1 * math.exp(-g_0/R/T1*(h-h1))
  return(temp,press,dens)

# Determine the reference conditions.
p_base = p_s
rho_base = rho_s
for i in range(len(a)-1):
  print 'index=',i
  h_base = a[i]
  type = tempDist[a[i]]['type']
  slope = tempDist[a[i]]['a']
  T_low = tempDist[a[i]]['T_low']
  # When we find the right region, we terminate the reference calculations.
  if h >= a[i] and h < a[i+1]: break
  h_next = a[i+1]
  if type == 'isotherm': dummy,p_base,rho_base = all_isotherm(h_next,h_base,slope,T_low,p_base,rho_base)
  if type == 'gradient': dummy,p_base,rho_base = all_gradient(h_next,h_base,slope,T_low,p_base,rho_base)

# Determine the target conditions.
if type == 'isotherm': temp,press,dens = all_isotherm(h,h_base,slope,T_low,p_base,rho_base)
if type == 'gradient': temp,press,dens = all_gradient(h,h_base,slope,T_low,p_base,rho_base)

print " Altitude (hG) = %.0f m (geometric)" % hG
print " Altitude (h)  = %.0f m (geopotential)" % h
print " Temperature   = %.2f K" % temp
print " Pressure      = %.4e N/m^2" % press
print " Density       = %.4e kg/m^3" % dens
