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
      eta_KsStagn, H_KsStagn, phi_flow, dzeta_inlet, relD_1H, relD_1B,
      i, tau_1,
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

# Effective pressure | Среднее эффективное давление
p_e = 0.12*1e03*N_e*strokeNumber/(math.pi*pow(D, 2)*S*n*pistonNumber); # Pa

# Flow volume | Расход
G_K = N_e*g_e*l_0*alpha*phi/3600; # kg/s

# Wheel diameter | Диаметр рабочее колесо
if ( issubclass(type(eta_KsStagn), str) ) or \
      ( issubclass(type(H_KsStagn), str) ) or ( issubclass(type(phi_flow), str) ):
      D_2 = 160*G_K + 40; # mm      
      print 'Aproximately the wheel diameter is {D_2_mm:.1f} mm\n' .format(D_2_mm = D_2);
      print 'Now you can set "eta_KsStagn", "H_KsStagn" & "phi_flow" using experimental\
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

## Compressor parameters calculation

# Stagnation parameters of inlet | Параметры торможения на входе (1)
T_0Stagn = T_aStagn;
p_0Stagn = sigma_0*p_aStagn;

# Static pressure & temperature of intake in compressor | Статические температура
# и давление на входе в компрессор (3)
T_0 = T_0Stagn - pow(c_0, 2)/2/c_p;
p_0 = p_0Stagn * pow(T_0/T_0Stagn, k/(k - 1)); # Pa

# Isentropy compression work in compressor | Изоэнтропная работа сжатия в компрессоре (4)
L_KsStagn = c_p*T_0Stagn*(pow(Pi_K, (k - 1)/k) - 1);

# Wheel outer diameter circular velocity | Окружная скорость на наружном диаметре колеса (5)
u_2 = math.sqrt(L_KsStagn / H_KsStagn);

if u_2 >= 550:    
      print 'Wheel outer diameter circular velocity is too high!'
      print 'Try to increase wheel diameter &/or set other ECE parameters'
      exit();

# | Абсолютная скорость потока на входе в рабочее колесо (6)
c_1 = phi_flow*u_2;

# | Температура воздуха на входе в рабочее колесо (7)
T_1 = T_0 + (pow(c_0, 2) - pow(c_1, 2))/2/c_p;

# | Расчёт потерь энергии во впускном коллекторе (8)
deltaL_inlet = dzeta_inlet*pow(c_1, 2)/2;

# | Показатель политропы при течении во входном устройстве (9)
n_1 = ( k/(k - 1) - deltaL_inlet/R/(T_1 - T_0) )/ \
( k/(k - 1) - deltaL_inlet/R/(T_1 - T_0) - 1);

# | Давление на входе в колесо (10)
p_1 = p_0*pow(T_1/T_0, n_1/(n_1 - 1));

# | Плотность на входе в колесо (11)
ro_1 = p_1/R/T_1;

# | Площадь поперечного сечения в колесе (12)
F_1 = G_K/c_1/ro_1;

# | Наружный диаметр колеса на входе D_1H (13)
D_1H = math.sqrt( 4*F_1/math.pi/(1 - pow(relD_1B/relD_1H, 2)) );

# \ Внутренний диаметер на входе (втулочный диаметр) (14)
D_1B = relD_1B/relD_1H*D_1H;

# | Наружный диаметр колеса на комперссора на выходе (15)
D_2 = round( D_1H/relD_1H, 3 );
print 'The diameter of the wheel is {D_2_mm} mm\n' .format(D_2_mm = D_2*1e+03);

# | Частота вращения турбокомпрессора (16)
n_tCh = 60*u_2/math.pi/D_2; # 1/min

# | Средний диаметр на входе в колесо
D_1 = math.sqrt(( pow(D_1B, 2) + pow(D_1H, 2) )/2);

# | Окружная скорость на среднем диаметре входа (18)
u_1 = math.pi*D_1*n_tCh/60;

# | Угол входа потока в рабочее колесо на среднем диамметре в относительном движении (19)
beta_1 = math.degrees(math.atan( c_1/u_1 ));

if issubclass(type(i), str):    
      print 'Degree of the wheel inlet flow is {0:.3f}' .format(beta_1);
      print 'Now you can set "i", using recomendations'
      exit();

# | Угол установки лопаток на среднем диаметре (20)
beta_1Blade = beta_1 + i;

# | Абсолютная скорость при учёте толщины лопаток (21)
if issubclass(type(tau_1), str):    tau_1 = 0.85; # default tau_1

c_1Tau = c_1 / tau_1;

# | Окружная скорость на наружном диаметре входа в колесо (22)
u_1H = math.pi*D_1H*n_tCh/60;

# | Относительная скорость на наружном диаметре входа в колесо (21)
w_1H = math.sqrt(pow(c_1Tau, 2) + pow(u_1H, 2));

# | Число маха на наружном диаметре входа в колесо (22)
M_w1 = w_1H/math.sqrt(k*R*T_1);

if M_w1 > 0.9:
      print 'Warning!\nMach number (M = {0:.2f}) is too high!' .format(M_w1);
      print 'Try to change "tau_1" &/or other parameters.'
      # exit();
      
# | Относительная скорость на среднем диаметре входа в колесо (23)
w_1 = math.sqrt(pow(c_1Tau, 2) + pow(u_1, 2));














