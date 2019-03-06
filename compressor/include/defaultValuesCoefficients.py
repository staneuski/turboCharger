# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# Included script
#     defaultValuesCoefficients
#
# Description
#     Default values for coefficients
# 
#-----------------------------------------------------------------------

beta_2Blade         = defaultValue(beta_2Blade, 75)

c_0                 = defaultValue(c_0,         40)

eta_KsStagn         = defaultValue(eta_KsStagn, 0.55)
H_KsStagn           = defaultValue(H_KsStagn,   0.4)
phi_flow            = defaultValue(phi_flow,    0.4)
eta_diff            = defaultValue(eta_diff,    0.75)

deltaDegDiff        = defaultValue(deltaDegDiff, 14)

relD_1H             = defaultValue(relD_1H,             0.6)
relD_1B             = defaultValue(relD_1B,             0.55)
relW_2rToC_1a       = defaultValue(relW_2rToC_1a,       0.6)
if 'VANELESS' in diffuserType:
    vanelessWideCoef    = defaultValue(vanelessWideCoef,    0.9)
    vanelessDiamCoef    = defaultValue(vanelessDiamCoef,    1.8)
elif 'VANED' in diffuserType:
    vanelessWideCoef    = defaultValue(vanelessWideCoef,    1)
    vanelessDiamCoef    = defaultValue(vanelessDiamCoef,    1.14)    
else:   exit('Set type of the diffuser correctly ("VANED"\
 or "VANELESS") in commonDict.py dictionary!\n')
vanedWideCoef       = defaultValue(vanedWideCoef,       1)
vanedDiamCoef       = defaultValue(vanedDiamCoef,       1.6)
relDiffOutToCompOut = defaultValue(relDiffOutToCompOut, 1.4)

dzeta_inlet         = defaultValue(dzeta_inlet, 0.04)
dzeta_BA            = defaultValue(dzeta_BA,    0.26)
dzeta_TF            = defaultValue(dzeta_TF,    0.18)
alpha_wh            = defaultValue(alpha_wh,    0.05)
n_housing           = defaultValue(n_housing,   1.9)
n_diffuser          = defaultValue(n_diffuser,  1.55)

tau_1               = defaultValue(tau_1,   0.9)
tau_2               = defaultValue(tau_2,   0.94)
tau_3               = defaultValue(tau_3,   0.93)
tau_4               = defaultValue(tau_4,   0.965)







