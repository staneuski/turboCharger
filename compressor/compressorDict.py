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
# 
#-----------------------------------------------------------------------

# Stagnation (*) parameters for inlet
# Loading input data from project dictionary 
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from commonDict import(p_a, T_a)

p_aStagn    = p_a # MPa, stagnation pressure | давление торможения
T_aStagn    = T_a # К, stagnation pressure | температура торможения
c_0         = 40 # m/s (40 - default), intake speed | скорость на входе 

# Losses coefficients | Коэффициенты потерь
sigma_0     = 0.98 # | коэффициент потерь полного давления
sigma_c     = 0.985 # | коэффициент потерь в охладителе
sigma_v     = 0.992 # | коэффициент потерь в коллекторе

# Energy conversion efficiency (ECE) & other coefficints | КПД и др. коэффициенты
eta_KsStagn = "DEFAULT" # 0…1 (0.6 - default) compressor energy conversion efficiency | КПД компрессора (весовой коэффициент)
H_KsStagn   = "DEFAULT" # 0…1 (0.4 - default) | напорный изоэнтропный КПД (весовой коэффициент)
phi_flow    = "DEFAULT" # 0…1 (0.4 - default) | коэффициент напора (весовой коэффициент)
eta_diff    = "DEFAULT" # 0.55…0.78 (0.75 - default) | политропный КПД диффузора (46)

# Loses coeficients | Коэффициенты потерь
dzeta_inlet = "DEFAULT" # 0.03…0.06, (0.04 - default) | коэффициент сопротивления (8)
dzeta_BA    = "DEFAULT" # 0.1…0.3 (0.26 - default) | коэффициент потерь в направляющем аппарате (26)
dzeta_TF    = "DEFAULT" # 0.1…0.2 (0.18 - default) | коэффициент потерь на трение в межлопаточных каналах (28)
alpha_wh    = "DEFAULT" # 0.04…0.08 (0.05 - default) | коэффициент дисковых потерь (29)

# Geometric coefficients etc. | Коэффициенты геометрии и проч.
relD_1H     = "DEFAULT" # 0…1 (0.6 - default) diameter coefficient | коэффициент диаметра (весовой коэффициент) (13)
relD_1B     = "DEFAULT" # 0…1 (0.55 - default) diameter coefficient | коэффициент диаметра (весовой коэффициент) (13)
relW_2rToC_1a       = "DEFAULT" # 0…1 (0.6 - default) | отношение w_2r к с_1a (весовой коэффициент) (27)
diffuserWideCoef    = "DEFAULT" # 0.7…1.0 (0.9 - default) | отношение ширины диффузора на входе и выходе (44)
diffuserDiamCoef    = "DEFAULT" # 1.6…1.9 (1.8 - default) | отношение диаметра диффузора на входе и выходе (45)
relDiffOutToCompOut = "DEFAULT" # 1.3…1.4 (1.4 - default) | Отношение скорости на выходе из компрессора к скорости на выходе из диффузора (51)
n_housing   = "DEFAULT" # 1.85…2.2 (1.9 - default) | Показатель политропы сжатия в воздухосборнике/улитке (53)

# Geometric parameters
roundDiamToSTD = "OFF" # "ON" - округление диаметра до ряда стандартных значений / "OFF" - округление диаметра до целых в см (или до величины кратной 5 мм для диаметров меньших 85 мм)
deltaDiam   = "DEFAULT" # mm, (0 - default) | размер изменяющий на данное значение оценку предварительного диаметра (может быть как меньше, так и больше нуля)
iDeg        = 3.913 # 2…6 deg | угол атаки на входе в колесо (20)
z_K         = 12 # 9…34 | количество лопаток (30)
tau_1       = "DEFAULT" # 0.8…0.9, (0.9 - default) | коэффициент загромождения (стеснения), учитывающий толщину лопаток
tau_2       = "DEFAULT" # 0.92…0.96 (0.94 - default) | коэффициент загромождения (42)
beta_2Blade = "DEFAULT" # deg, 55…75 (75 - default) | угол лопаток на выходе из рабочего колеса (компрессор с лопатками оогнутыми назад)








