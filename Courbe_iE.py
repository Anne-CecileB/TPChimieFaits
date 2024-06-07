
# -*- coding: utf-8 -*-
from math import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


#Trace et analyse courbe (i,E)

iE_100 = pd.read_csv('iE_fer_02.txt', delim_whitespace=True)
i100 = iE_100['i']*0.8-2 # conversion voltage sortie - intensite reelle
E100 = iE_100['E']*0.8-2 # conversion voltage sortie - voltage reel

iE_150 = pd.read_csv('iE_fer_150mL.txt', delim_whitespace=True)
i150 = iE_150['i']*0.8-2 # conversion voltage sortie - intensite reelle
E150 = iE_150['E']*0.8-2 # conversion voltage sortie - voltage reel

iE_200 = pd.read_csv('iE_fer_200mL.txt', delim_whitespace=True)
i200 = iE_200['i']*0.8-2 # conversion voltage sortie - intensite reelle
E200 = iE_200['E']*0.8-2 # conversion voltage sortie - voltage reel

#
plt.figure(1)
plt.clf()
plt.title(r'Courbes i-E du FeIII/FeII, melanges equimolaires')
plt.plot(E100,i100,'m', label = 'C = 0.1 mol/L')
plt.plot(E150,i150,'c', label = 'C = 0.0666 mol/L')
plt.plot(E200,i200,'purple', label = 'C = 0.05 mol/L')
plt.xlabel(r'E (V)')
plt.ylabel(r'i (mA)')
plt.legend()
plt.tight_layout()
plt.savefig('plot_iE')

E_calomel = 0.244 #par rapport a ESH

E0_100 = E100[np.min(np.where(i100>=0))] + E_calomel
E0_150 = E150[np.min(np.where(i150>=0))] + E_calomel
E0_200 = E200[np.min(np.where(i200>=0))] + E_calomel

print('Valeurs du potentiel de Nernst du couple :'+str(E0_100)+' V, '+str(E0_150)+' V, '+str(E0_200)+' V.')
print('Valeur théorique du potentiel de Nernst du couple : 0.68 V')
#

C100 = 0.1 #mol/L
C150 = 0.066666 #mol/L
C200 = 0.05 #mol/L

#Lecture graphique
i100_lim = 0.599
i150_lim = 0.402
i200_lim = 0.248

plt.figure(2)
plt.clf()
plt.title(r'Influence de la concentration sur i$_{lim, diff}$')
plt.plot(C100,i100_lim,'mx')
plt.plot(C150,i150_lim,'cx')
plt.plot(C200,i200_lim,'x', color = 'purple')
plt.xlabel(r'C (mol/L)')
plt.ylabel(r'i$_{lim}$ (mA)')
plt.tight_layout()
plt.savefig('plot_i_limite')
#
plt.show()
