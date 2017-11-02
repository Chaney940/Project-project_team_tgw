# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:25:28 2017

@author: trz22
"""
import numpy as np

class Model:
    straddle,strike, spot, texp,intr,divr= None, None, None, None, None, None
    def __init__(self,straddle,strike, spot, texp, intr=0, divr=0):
        self.texp = texp
        self.straddle = straddle
        self.intr = intr
        self.divr = divr
        self.spot = spot
        self.strike = strike
        
    def h_a(self,ita=0):
        a=[  3.994961687345134*10**1	,
                    2.100960795068497*10**1	,
                    4.980340217855084*10**1	,
                    5.988761102690991*10**2	,
                    1.848489695437094*10**3	,
                    6.106322407867059*10**3	,
                    2.493415285349361*10**4	,
                    1.266458051348246*10**4	]
        b=[1.000000000000000*10**0		,
                    4.990534153589422*10**1		,
                    3.093573936743112*10**1		,
                    1.495105008310999*10**3		,
                    1.323614537899738*10**3		,
                    1.598919697679745*10**4		,
                    2.392008891720782*10**4		,
                    3.608817108375034*10**3		,
                    2.067719486400926*10**2		,
                    1.174240599306013*10**1		]
        for i in range(0,7):
            up=0
            up=up+a[i]*ita**i;
        for i in range(0,9):
            down=0
            down=down+b[i]*ita**i;
        return np.sqrt(ita)*up/down
    
    def ita(self, straddle,strike, spot):
             v=(spot-strike)/straddle
             ita_1=2*v/np.arctanh(v)  
             return ita_1
         
    def impvol(self):
            straddle=self.straddle
            strike=self.strike
            spot=self.spot
            texp=self.texp
            ita_2=self.ita(straddle,strike, spot)
            h_a1=self.h_a(ita_2)
            vol = np.sqrt(np.pi/(2*texp))*straddle*h_a1
            return vol
        
        
#test        
sabr_bsm_mc = Model(17,5, 20, 50, intr=0, divr=0)
print(sabr_bsm_mc.impvol())