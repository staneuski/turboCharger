# -*- coding: utf-8 -*-
# Calculates safety factors for crankshaft and displays the minimum of them

## Loading input data from project dictionary & some fuctions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
      eta_KsStagn, H_KsStagn, phi_flow,
      dzeta_inlet, dzeta_BA, relW_2rToC_1a, dzeta_TF, alpha_wh, tau_2,
      relD_1H, relD_1B,
      i, tau_1, z_K, beta_2Blade,
      E, T_ca,
      proectType
);


## Converting data to SI from dictionary | Перевод в СИ
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

N_e = N_e*1e03; # -> V
g_e = g_e*1e-03; # -> kg/(V*h) or g/(kV*h)
p_aStagn = p_aStagn*1e06; # -> Pa
D = D*1e-02;      S = S*1e-02; # -> m


## Precalculations
## ~~~~~~~~~~~~~~~

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

# Wheel diameter | Диаметр рабочего колеса
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
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ Inlet part | Входное устройство ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# Stagnation parameters of inlet | Параметры торможения на входе (1)
T_0Stagn = T_aStagn;
p_0Stagn = sigma_0*p_aStagn;

# Static pressure & temperature of intake in compressor | Статические температура
# и давление на входе в компрессор (3)
T_0 = T_0Stagn - pow(c_0, 2)/2/c_p;
p_0 = p_0Stagn * pow(T_0/T_0Stagn, k/(k - 1)); # Pa

L_KsStagn = c_p*T_0Stagn*(pow(Pi_K, (k - 1)/k) - 1); # Isentropy compression work in compressor | Изоэнтропная работа сжатия в компрессоре (4)

# Wheel outer diameter circular velocity | Окружная скорость на наружном диаметре колеса (5)
u_2 = math.sqrt(L_KsStagn / H_KsStagn);
if u_2 >= 550:    
      print 'Wheel outer diameter circular velocity is too high!'
      print 'Try to increase wheel diameter &/or set other ECE parameters'
      exit();

c_1 = phi_flow*u_2; # | Абсолютная скорость потока на входе в рабочее колесо (6)

T_1 = T_0 + (pow(c_0, 2) - pow(c_1, 2))/2/c_p; # | Температура воздуха на входе в рабочее колесо (7)

# | Расчёт потерь энергии во впускном коллекторе (8)
if issubclass(type(dzeta_inlet), str):    dzeta_inlet = 0.45;    # default dzeta_inlet
L_inlet = dzeta_inlet*pow(c_1, 2)/2;




# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ Compressor wheel | Рабочее колесо ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

n_1 = ( k/(k - 1) - L_inlet/R/(T_1 - T_0) )/ \
( k/(k - 1) - L_inlet/R/(T_1 - T_0) - 1); # | Показатель политропы сжатия в компрессоре (33)

p_1 = p_0*pow(T_1/T_0, n_1/(n_1 - 1)); # | Давление на входе в колесо (10)

ro_1 = p_1/R/T_1; # | Плотность на входе в колесо (11)

F_1 = G_K/c_1/ro_1; # | Площадь поперечного сечения в колесе (12)

D_1H = math.sqrt( 4*F_1/math.pi/(1 - pow(relD_1B/relD_1H, 2)) ); # | Наружный диаметр колеса на входе D_1H (13)

D_1B = relD_1B/relD_1H*D_1H; # | Внутренний диаметер на входе (втулочный диаметр) (14)

# | Наружный диаметр колеса на комперссора на выходе (15)
D_2 = round( D_1H/relD_1H, 3 );
print 'The diameter of the wheel is {D_2_mm} mm\n' .format(D_2_mm = D_2*1e+03);

n_tCh = 60*u_2/math.pi/D_2; # 1/min, | Частота вращения турбокомпрессора (16)

D_1 = math.sqrt(( pow(D_1B, 2) + pow(D_1H, 2) )/2); # | Средний диаметр на входе в колесо

u_1 = math.pi*D_1*n_tCh/60; # | Окружная скорость на среднем диаметре входа (18)

# | Угол входа потока в рабочее колесо на среднем диамметре в относительном движении (19)
beta_1 = math.degrees(math.atan( c_1/u_1 ));
if issubclass(type(i), str):    
      print 'Degree of the wheel inlet flow is {0:.3f}' .format(beta_1);
      print 'Now you can set "i", using recomendations'
      exit();

beta_1Blade = beta_1 + i; # | Угол установки лопаток на среднем диаметре (20)

# | Абсолютная скорость при учёте толщины лопаток (21)
if issubclass(type(tau_1), str):    tau_1 = 0.85;    # default tau_1
c_1Tau = c_1 / tau_1;

u_1H = math.pi*D_1H*n_tCh/60; # | Угол установки лопаток на среднем диаметре (20)

w_1H = math.sqrt(pow(c_1Tau, 2) + pow(u_1H, 2)); # | Относительная скорость на наружном диаметре входа в колесо (23)

# | Число маха на наружном диаметре входа в колесо (24)
M_w1 = w_1H/math.sqrt(k*R*T_1);
if M_w1 > 0.9:
      print 'Warning!\nMach number (M = {0:.2f}) is too high!' .format(M_w1);
      print 'Try to change "tau_1" &/or other parameters.'
      # exit();
      
w_1 = math.sqrt(pow(c_1Tau, 2) + pow(u_1, 2)); # | Относительная скорость на среднем диаметре входа в колесо (25)

# | Удельная работа потерь во входном вращающемся направляющем аппарате колеса (26)
if issubclass(type(dzeta_BA), str):    dzeta_BA = 0.3;   # default dzeta_BA
L_BA = dzeta_BA*pow(w_1, 2)/2;

# | Радиальная составляющая абсолютной скорости / радиальная составляющая относительной скорости на выходе из колеса (27)
if issubclass(type(relW_2rToC_1a), str):    relW_2rToC_1a = 1.05;   # default relW_2rToC_1a
c_2r = relW_2rToC_1a * c_1;

# | Потери на поворот и трение в межлопаточных каналах рабочего колеса (28)
if issubclass(type(dzeta_TF), str):    dzeta_TF = 0.15;   # default dzeta_TF
L_TF = dzeta_TF*pow(c_2r, 2)/2;

# | Потери на трение диска колеса о воздух в сумме с вентиляционными потерями (29)
if issubclass(type(alpha_wh), str):    alpha_wh = 0.06;   # default alpha_wh
L_TB = alpha_wh*pow(u_2, 2);

mu = 1/(1+2/3*math.pi/z_K \
    *math.sin(math.radians(beta_2Blade))/(1 - pow(D_1/D_2, 2)) ); # | Коэффициент мощности учитывабщий число лопаток и проч. (31)

T_2 = T_1 + (mu + alpha_wh - 0.5*pow(mu, 2))*pow(u_2, 2)/c_p; # | Температура воздуха за колесом (32)

n_2 = ( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) )/ \
( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) - 1); # | Показатель политропы сжатия в колесе (33)

p_2 = p_1*pow(T_2/T_1, n_2/(n_2 - 1)); # | Давление на выходе из колеса (34)

ro_2 = p_2/R/T_2; # | Плотность на выходе из колеса (35)

c_2u = mu*(u_2 - c_2r/math.tan(math.radians(beta_2Blade))); # | Окружная составляющая абсолютной скорости на выходе (36)

c_2 = math.sqrt(pow(c_2u, 2) + pow(c_2r, 2)); # | Абсолютная скорость на выходе из колеса

w_2u = u_2 - c_2u; # | Окружная составляющая относительной скорости на выходе из колеса (38)

w_2 = math.sqrt(pow(w_2u, 2) + pow(c_2r, 2)); # | Относительная скорость на выходе из колеса (c_2r = w_2r) (39)

beta_1 = math.degrees(math.acos( w_2u/w_2 )); # | Угол между веторами относительной и окружной скорости на выходе из колеса (40)

alpha_2 = math.degrees(math.acos( c_2u/c_2 )); # | Угол между веторами абсолютной и окружной скорости на выходе из колеса (40)

# | Ширина колеса на выходе из турбины (41)
if issubclass(type(tau_2), str):    tau_2 = 0.94;   # default tau_2
b_2 = G_K/math.pi/D_2/c_2r/ro_2/tau_2;

T_2Stagn = T_2 + pow(c_2, 2)/2/c_p; # | Температура заторможенного потока на выходе из колеса (43)




# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[ Diffuser | Диффузор ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]




print T_2Stagn;


















