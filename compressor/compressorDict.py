# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# Dictionary
#     compressorDict
#
# Description
#     Parameters of the compressor
#     РК  - рабочее колесо
#     ЛД  - лопаточный диффузор
#     БЛД - безлопаточный диффузор
#     НА  - направляющий аппарат
# 
#-----------------------------------------------------------------------

# Stagnation (*) parameters for inlet & loading input data from project dictionary 
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from commonDict import(p_a, T_a)

# 'ON' - округление диаметра до ряда стандартных значений
# 'OFF' - округление диаметра до целых в см (или до величины кратной 5 мм
# для диаметров меньших 85 мм)
roundDiamToSTD = 'OFF'

diffuserType   = 'VANELESS' #'VANELESS' для БЛД / 'VANED' для ЛД

# 'EQV' - предварительная оценка диаметра по формуле
# (для компрессоров с небольшим расходом и D_2 <= 24см)
# <00> - задание предварительной оценки диаметра явно (в см)
estimD_2    = 'EQV' #BOOL / cm (2.25)

# Угол лопаток на выходе из рабочего колеса (компрессор с лопатками
# отогнутыми назад) (0)
beta_2Blade = 'DEFAULT' #deg,55…75 (75 dflt)

# Inlet gas parameters|Параматры газа на входе
p_aStagn    = p_a #MPa, stagnation pressure|давление торможения
T_aStagn    = T_a #К, stagnation pressure|температура торможения
c_0         = 'DEFAULT' #m/s,(40 dflt) intake speed|скорость на входе 

# Losses coefficients|Коэффициенты потерь
sigma_0     = 0.98 #0.96…0.985(0.98 dflt)|коэф. потерь полного давления (0)
sigma_c     = 0.985 #(0.985 dflt)|коэф. потерь в охладителе(0)
sigma_v     = 0.992 #(0.992 dflt)|коэф. потерь в коллекторе (0)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

## Energy conversion efficiency (ECE) & other coefficints|КПД и др. коэф-ты
eta_KsStagn = 'DEFAULT' #wght (0.6 dflt)|КПД компрессора (для 'TYPE2' - (15))
H_KsStagn   = 'DEFAULT' #wght (0.4 dflt)|напорный изоэнтропный КПД (5)
phi_flow    = 'DEFAULT' #wght (0.4 dflt)|коэф. напора (6)
eta_diff    = 'DEFAULT' #0.55…0.78 (0.75 dflt)|политропный КПД диффузора (46)

## Geometric parameters
iDeg        = 3.913 #2…6 deg|угол атаки на входе в РК (20)
z_K         = 12 #9…40|количество лопаток РК (30)
z_diffuser  = 13 #7…35 'VANELESS'|количество лопаток ЛД (F50)
deltaDegDiff= 'DEFAULT' #deg,10…15 (14 dflt) 'VANELESS'|разница в наклоне лопоток на выходе из ЛД и РК (F49)

## Geometric coefficients etc.|Коэффициенты геометрии и проч.
relD_1H             = 'DEFAULT' #wght (0.6 dflt) diameter coefficient|коэф. диаметра (13)
relD_1B             = 'DEFAULT' #wght (0.55 dflt) diameter coefficient|коэф. диаметра (13)
relW_2rToC_1a       = 'DEFAULT' #wght (0.6 dflt)|отношение w_2r к с_1a (27)
vanelessWideCoef    = 'DEFAULT' #0.7…1.0 (0.9 dflt)'VANED'/0.95…1 (1 dflt)'VANELESS'|отношение ширины (безлопаточной части) диффузора на входе и выходе (44)
vanelessDiamCoef    = 'DEFAULT' #1.6…1.9 (1.8 dflt)'VANED'/ 1.05…1.2 (1.14 dflt)'VANELESS'|отношение диаметра (безлопаточной части) диффузора на входе и выходе (45)
vanedWideCoef       = 'DEFAULT' #1…1.3 (1 dflt)'VANELESS'|отношение ширины лопаточной части ЛД на входе и выходе (F48)
vanedDiamCoef       = 'DEFAULT' #1.35…1.7 (1.6 dflt)'VANELESS'|отношение диаметра лопаточной части ЛД на входе и выходе (F47)
relDiffOutToCompOut = 'DEFAULT' #1.3…1.4 (1.4 dflt)|отношение скорости на выходе из компрессора к скорости на выходе из диффузора (51)

## Loses coeficients|Коэффициенты потерь
dzeta_inlet = 'DEFAULT' #0.03…0.06, (0.04 dflt)|коэф. сопротивления (8)
dzeta_BA    = 'DEFAULT' #0.1…0.3 (0.26 dflt)|коэф. потерь в НА (26)
dzeta_TF    = 'DEFAULT' #0.1…0.2 (0.18 dflt)|коэф. потерь на трение в межлопаточных каналах (28)
alpha_wh    = 'DEFAULT' #0.04…0.08 (0.05 dflt)|коэф. дисковых потерь (29)
n_diffuser  = 'DEFAULT' #1.5…1.8 (1.55 dflt)|показатель политропы сжатия в ЛД (F51)
n_housing   = 'DEFAULT' #1.85…2.2 (1.9 dflt)|показатель политропы сжатия в воздухосборнике/улитке (53)

## Load factors|Коэффициенты загромождения
tau_1       = 'DEFAULT' #0.8…0.9 (0.9 dflt)|коэф. загромождения на входе в РК (21)
tau_2       = 'DEFAULT' #0.92…0.96 (0.94 dflt)|коэф. загромождения на выходе из РК (42)
tau_3       = 'DEFAULT' #0.95…0.97 (0.96 dflt)'VANELESS'|коэф. загромождения на входе в ЛД (21)
tau_4       = 'DEFAULT' #0.96…0.98 (0.965 dflt)'VANELESS'|коэф. загромождения на выходе из ЛД (42)



