# Based on the Book "Atoms Molecules and Photons - Wolfgang Demtroder" 2nd Edition
# Normalised Radial Equations on page 163 Table 5.1

import numpy as np
import matplotlib.pyplot as plt

#defining range and constants
r = np.linspace(0,25,num=300)
a = 0.529

#defining functions to make the equations compact
def Nf(nn):
    temp = pow(1/(nn*a),(3/2))
    return temp

def Xf(nn):
    ra = np.linspace(0,25,num=300) #just a repitition from line 8
    temp = ra/(nn*a)
    return temp

#evaluating the values
#y<n value>_<l value>

n=1
y1_0 = 2*Nf(n)*np.exp(-Xf(n))

n=2
y2_0 = 2*Nf(n)*np.exp(-Xf(n))*(1-Xf(n)) 
y2_1 = (2/pow(3,1/2))*Nf(n)*np.exp(-Xf(n))*Xf(n)

n=3
y3_0 = 2*Nf(n)*np.exp(-Xf(n))*(1-(2*Xf(n))+((2*pow(Xf(n),2))/3))
y3_1 = (2/3)*pow(2,1/2)*Nf(n)*np.exp(-Xf(n))*Xf(n)*(2-Xf(n))
y3_2 = (4/(3*pow(10,1/2)))*Nf(n)*np.exp(-Xf(n))*pow(Xf(n),2)

n=4
y4_0 = 2*Nf(n)*np.exp(-Xf(n))*(1-(3*Xf(n))+(2*pow(Xf(n),2))-(pow(Xf(n),3)/3))
y4_1 = 2*pow((5/3),1/2)*Nf(n)*np.exp(-Xf(n))*Xf(n)*(1-Xf(n)+(pow(Xf(n),2)/5))
y4_2 = 2*pow(1/5,1/2)*Nf(n)*np.exp(-Xf(n))*Xf(n)*Xf(n)*(1-(Xf(n)/3))
y4_3 = (2/(3*pow(25,1/2)))*Nf(n)*np.exp(-Xf(n))*pow(Xf(n),3)

####
###
## All plots
#

plt.plot(r,y1_0, label = "n=1,l=0")
plt.plot(r,y2_0, label = "n=2,l=0")
plt.plot(r,y2_1, label = "n=2,l=1")
plt.plot(r,y3_0, label = "n=3,l=0")
plt.plot(r,y3_1, label = "n=3,l=1")
plt.plot(r,y3_2, label = "n=3,l=2")
plt.plot(r,y4_0, label = "n=4,l=0")
plt.plot(r,y4_1, label = "n=4,l=1")
plt.plot(r,y4_2, label = "n=4,l=2")
plt.plot(r,y4_3, label = "n=4,l=3")
plt.ylim(-0.3,1)
#plt.xlim(-2,10)
plt.xlabel("Radius r")
plt.ylabel("Normalized Radial Wave function R(r)")
plt.grid(color = 'lightgrey', linestyle = '-')
plt.legend()
plt.show()


####
###
## Only n=1
#
plt.plot(r,y1_0, label = "n=1,l=0")
plt.ylim(-0.3,1.5)
plt.xlabel("Radius r")
plt.ylabel("Normalized Radial Wave function R(r)")
plt.grid(color = 'lightgrey', linestyle = '-')
plt.legend()
plt.show()

####
###
##  for n = 2
#
plt.plot(r,y2_0, label = "n=2,l=0")
plt.plot(r,y2_1, label = "n=2,l=1")
plt.ylim(-0.3,0.8)
plt.xlabel("Radius r")
plt.ylabel("Normalized Radial Wave function R(r)")
plt.grid(color = 'lightgrey', linestyle = '-')
plt.legend()
plt.show()

####
###
## for n=3
#
plt.plot(r,y3_0, label = "n=3,l=0")
plt.plot(r,y3_1, label = "n=3,l=1")
plt.plot(r,y3_2, label = "n=3,l=2")
plt.ylim(-0.3,0.8)
plt.xlabel("Radius r")
plt.ylabel("Normalized Radial Wave function R(r)")
plt.grid(color = 'lightgrey', linestyle = '-')
plt.legend()
plt.show()

####
###
## for n = 4
#
plt.plot(r,y4_0, label = "n=4,l=0")
plt.plot(r,y4_1, label = "n=4,l=1")
plt.plot(r,y4_2, label = "n=4,l=2")
plt.plot(r,y4_3, label = "n=4,l=3")
plt.ylim(-0.3,0.6)
plt.xlabel("Radius r")
plt.ylabel("Normalized Radial Wave function R(r)")
plt.grid(color = 'lightgrey', linestyle = '-')
plt.legend()
plt.show()
