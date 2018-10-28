# -*- coding: utf-8 -*-

## Compressor parameters
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Stagnation (*) parameters for inlet
# Loading input data from project dictionary 
import sys;
from os import path;
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) );
from commonDict import(p_a, T_a);

p_aStagn = p_a; # MPa, stagnation pressure | давление торможения
T_aStagn = T_a; # К, stagnation pressure | температура торможения
c_0 = 40; # m/s, intake speed | скорость на входе 

# Losses coefficients | Коэффициенты потерь
sigma_0 = 0.98; # | коэффициент потерь полного давления
sigma_c = 0.985; # | коэффициент потерь в охладителе
sigma_v = 0.992; # | коэффициент потерь в коллекторе

# Energy conversion efficiency (ECE) & other coefficints | КПД и др. коэффициенты
# Set "UNKNOWN" if it's unknown | Если какой-либо параметр неизвестен принять его как "UNKNOWN"
eta_KsStagn = 0.74; # compressor energy conversion efficiency | КПД компрессора
H_KsStagn = 0.6; # | напорный изоэнтропный КПД
phi_flow = 0.3; # | коэффициент напора
eta_diff = "DEFAULT"; # 0.55...0.78 (0.75 - default) | политропный КПД диффузора (46)

# Loses coeficients | Коэффициенты потерь
# Set "DEFAULT" to set default value | Если какой-либо параметр, чтобы принять его по-умолчанию (как "DEFAULT")
dzeta_inlet = 0.04; # 0.03...0.06, (0.45 - default) | коэффициент сопротивления
dzeta_BA = 0.26; # 0.1...0.3 (0.2 - default) | коэффициент потерь в направляющем аппарате (26)
dzeta_TF = 0.18; # 0.1...0.2 (0.15 - default) | коэффициент потерь на трение в межлопаточных каналах (28)
alpha_wh = 0.05; # 0.04...0.08 (0.06 - default) | коэффициент дисковых потерь (29)
tau_2 = "DEFAULT"; # 0.92...0.96 (0.94 - default) | коэффициент загромождения (42)

# Geometric coefficients etc. | Коэффициенты геометрии и проч.
relD_1H = 0.67; # diameter coefficient | коэффициент диаметра
relD_1B = 0.225; # diameter coefficient | коэффициент диаметра
relW_2rToC_1a = "DEFAULT"; # 0.9...1.2 (1.05 - default) | отношение w_2r к с_1a (27)
diffuserWideCoef = "DEFAULT"; # 0.92...0.96 (0.9 - default) | отношение ширины диффузора на входе и выходе (44)
diffuserDiamCoef = "DEFAULT"; # 1.6...1.9 (1.8 - default) | отношение диаметра диффузора на входе и выходе (45)
relDiffOutToCompOut = "DEFAULT"; # 1.3...1.4 (1.4 - default) | Отношение скорости на выходе из компрессора к скорости на выходе из диффузора (51)
n_housing = "DEFAULT"; # 1.85...2.2 (1.9 - default) | Показатель политропы сжатия в воздухосборнике/улитке (53)

# Geometric parameters
# Set "UNKNOWN" if it's unknown | Если какой-либо параметр неизвестен принять его как "UNKNOWN"
iDeg = 3.913; # 2...6 deg | угол атаки на входе в колесо
tau_1 = 0.9; # 0.8...0.9, (0.85 - default) | коэффициент загромождения (стеснения), учитывающий толщину лопаток
z_K = 12; # 9...34 | количество лопаток
beta_2Blade = 75; # | угол лопаток на выходе из рабочего колеса


## Other paramaters
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
E = 0.7; # heat efficiency coefficient | коэффициент тепловой эффективности
T_ca = 309; # K, coolant temperature | температура охлаждающего агента (воды)


