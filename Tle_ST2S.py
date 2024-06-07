
# -*- coding: utf-8 -*-
from math import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


#Mesure et analyse de la fraicheur du lait
plt.figure(1)
plt.clf()

V = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.4,6.6,6.65,7,7.1,7.3,7.5,7.7,8,8.2,8.5,8.7,9,9.5,10,10.5,11.1,11.5,12,12.6,13,13.5,14,14.5,15,15.505,16,16.6,17,17.5,18,18.5,19,20.05]) #en mL
pH = np.array([6.86,6.93,7,7.08,7.16,7.24,7.34,7.45,7.55,7.68,7.79,7.85,8.21,8.24,8.31,8.35,8.40,8.46,8.51,8.56,8.63,8.71,8.74,8.80,8.92,9.01,9.10,9.22,9.28,9.37,9.45,9.51,9.60,9.66,9.73,9.80,9.87,9.92,9.99,10.04,10.09,10.14,10.19,10.24,10.34])

plt.figure(1)
plt.title(r'Saut pH')
plt.plot(V,pH)
plt.xlabel(r'V$_{verse}$')
plt.ylabel(r'pH')
plt.tight_layout()
plt.savefig('plot_ph')

def function(x,a,b):
    return(a*x+b)
    
C1, cov1 = curve_fit(function,V[6:13], 10**(-pH[6:13])*V[6:13])
C2, cov2 = curve_fit(function,V[30:], 10**(-pH[30:])*V[30:])

plt.figure(2)
plt.clf()
plt.plot(V,10**(-pH)*V,'x')
plt.plot(V[6:20],C1[0]*V[6:20]+C1[1],'m')
plt.plot(V[13:],C2[0]*V[13:]+C2[1],'c')
plt.xlabel(r'V$_{verse}$')
#plt.yticks(fontsize=30)
plt.ylabel(r'pH')
plt.tight_layout()
plt.savefig('plot_Gran')

intersection = (C2[1]-C1[1])/(C1[0]-C2[0])
print(r'V_{eq} = ', intersection, 'mL')
    
plt.show()

#Mesure et analyse de la contenance en ions sulfate dans l'eau SO4^2- + Ba2+ (dosage conductiométrique)
Vcond = np.array([0,0.5,1.1,1.5,2.1,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,10,10.5,11,12.1,12.5,13,14,15,16,17,18,19,20,21,22.1,23,24,25]) #en mL
Cond = np.array([1.451,1.502,1.472,1.481,1.490,1.498,1.507,1.517,1.525,1.537,1.547,1.559,1.570,1.584,1.595,1.608,1.619,1.632,1.643,1.674,1.688,1.714,1.783,1.822,1.868,1.977,1.981,2.185,2.284,2.380,2.476,2.572,2.657,2.756,2.834,2.919,3.006]) #(mS/cm)

C1, cov1 = curve_fit(function,Vcond[:20], Cond[:20])
C2, cov2 = curve_fit(function,Vcond[23:], Cond[23:])

plt.figure(3)
plt.clf()
plt.plot(Vcond,Cond,'x')
plt.plot(Vcond,C1[0]*Vcond+C1[1],'m')
plt.plot(Vcond[16:],C2[0]*Vcond[16:]+C2[1],'c')
plt.xlabel(r'V$_{verse}$')
#plt.yticks(fontsize=30)
plt.ylabel(r'Conductance')
plt.tight_layout()
plt.savefig('plot_conductimetrie')

plt.show()

intersection = (C2[1]-C1[1])/(C1[0]-C2[0])
print(r'V_{eq, cond} = ', intersection, 'mL')
