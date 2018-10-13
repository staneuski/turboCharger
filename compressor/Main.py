# -*- coding: utf-8 -*-
# Calculates safety factors for crankshaft and displays the minimum of them

## Loading input data from project dictionary & some fuctions
from __future__ import division
import math

from piK import piK

from compressorDict import(
      p_a, T_a, k, R, c_p,
      engineType, strokeNumber, engineType, pistonNumber, S, D,
      N_e, n, g_e,
      alpha, eta_v, phi,
      T_aStagn, p_aStagn, c_0,
      sigma_0, sigma_c, sigma_v,
      eta_KsStagn, H_KsStagn,
      E, T_ca,
      proectType
);


## Converting data to SI from dictionary | Перевод в СИ
N_e = N_e*1e03; # -> V
g_e = g_e*1e-03; # -> kg/(V*h) or g/(kV*h)
p_aStagn = p_aStagn*1e06; # -> Pa
D = D*1e-02;      S = S*1e-02; # -> m


## Precalculations

# Lower heat of combustion for fuel | Низшая теплота сгорания в зависимости от типа ДВС
if 'SI' in engineType:
      l_0 = 14.28; # kg \\\\\\ проверить!
elif 'DIESEL' in engineType:
      l_0 = 14.31; # kg
else:
      print 'Set type of the engine correctly ("DIESEL" or "SI")\
 in compressorDict.py file!\n';
      exit();

## Precalculations
# Effective pressure | Среднее эффективное давление
p_e = 0.12*1e03*N_e*strokeNumber/(math.pi*pow(D, 2)*S*n*pistonNumber); # Pa

# Flow volume | Расход
G_K = N_e*g_e*l_0*alpha*phi/3600; # kg/s

# Wheel diameter | Диаметр РК
if (eta_KsStagn == 0) or (H_KsStagn == 0):
      D_2 = 160*G_K + 40; # mm      
      print 'Aproximately the wheel diameter is {D_2_mm:.1f} mm\n' .format(D_2_mm = D_2)
      print 'Now you can set "eta_KsStagn" &/or "H_KsStagn" using experimental\
 data for different wheels diameter.'
      exit();
else:
      D_2 = (160*G_K + 40)*1e-03; # m

# Calculation pressure degree increase with successive approximation method 
# Определение степени повышения давления методом последовательных приближений
# Pi_K = 1;
# validity = 1e-04;
# for i in range(200):
#       if abs(piK(l_0, p_e, Pi_K) - Pi_K) < validity:
#             Pi_K = Pi_K + validity;
#       else:
#             Pi_K = piK(l_0, p_e, Pi_K)

Pi_K = 2.7563;

# Stagnation parameters of inlet | Параметры торможения на входе (1)
T_0Stagn = T_aStagn;
p_0Stagn = sigma_0*p_aStagn;

# Static pressure & temperature of intake in compressor | Статические температура
# и давление на входе в компрессор (3)
T_0 = T_0Stagn - pow(c_0, 2)/2/c_p;
p_0 = p_0Stagn * pow(T_0/T_0Stagn, k/(k - 1)); # Pa

# Isentropy compression work in compressor | Изоэнтропная работа сжатия в компрессоре (4)
L_KsStagn = c_p*T_0Stagn*(pow(Pi_K, (k - 1)/k) - 1); print L_KsStagn

# Wheel outer diameter circular velocity | Окружная скорость на наружном диаметре колеса (5)
u2 = math.sqrt(L_KsStagn / H_KsStagn); print u2;

if u2 >= 550:    
      print 'Wheel outer diameter circular velocity is too high!'
      print 'Try to increase wheel diameter &/or set other ECE parameters'
      exit();

# | Абсолютная скорость потока на входе в РК
      
# Проверка работы Sourcetree

























