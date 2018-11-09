#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Calculates safety factors for crankshaft and displays the minimum of them

## Loading data & calling some fuctions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Funcion for math solvers (pi, sin, cos, etc.) & other
from __future__         import division
from PIL                import ImageFont, Image, ImageDraw
import math, os, shutil, sys

# Some self-made fuctions
from os             import path;    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from defaultValue   import defaultValue
      
# Loading input data from project dictionary
from commonDict import(
    projectType,
    p_a,
    engineType, N_e, n, g_e,
    alpha, phi,
    G_K,
    T_0Stagn
)

from solvedParameters import(
    u_2K, D_2K, n_TCh, eta_KsStagnRated, L_KsStagn, N_K, p_vStagn
)

from turbineDict import(
    R_Exh, c_pExh, k_Exh, dragInletRatio,
    eta_Te, sigma_esc, ro, phiLosses, psiLosses, dzeta, eta_m,
    diameterRatio, outerDiamRatio, innerDiamRatio, alpha_1,
     beta_1Blade, delta, beta
)


## Converting data to SI from dictionary | Перевод в СИ
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N_e = N_e*1e+03; # -> V
g_e = g_e*1e-03; # -> kg/(V*h) or g/(kV*h)
if issubclass(type(delta), float):    delta = delta*1e-03; # -> m

## Default values
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dragInletRatio = defaultValue(dragInletRatio, 1.017); # default dragInletRatio
sigma_esc = defaultValue(sigma_esc, 0.99); # default sigma_esc
diameterRatio = defaultValue(diameterRatio, 1); # default sigma_esc
outerDiamRatio = defaultValue(outerDiamRatio, 0.8);
innerDiamRatio = defaultValue(innerDiamRatio, 0.31);
ro = defaultValue(ro, 0.52);
phiLosses = defaultValue(phiLosses, 0.97); # (16)
alpha_1 = defaultValue(alpha_1, 16); # (18)
beta_1Blade = defaultValue(beta_1Blade, 90);
psiLosses = defaultValue(psiLosses, 0.87) # (29)
delta = defaultValue(delta, 3*1e-04); # 0.3 mm
dzeta = defaultValue(dzeta, 1.3);
beta = defaultValue(beta, 4.6);
eta_m = defaultValue(eta_m, 0.94);


## Precalculations
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Lower heat of combustion for fuel | Низшая теплота сгорания в зависимости от типа ДВС
if 'SI' in engineType:
    l_0 = 14.28; # kg \\\\\\ проверить!
elif 'DIESEL' in engineType:
    l_0 = 14.31; # kg
else:
    exit('Set type of the engine correctly ("DIESEL" or "SI")\
 in commonDict.py file!\n');

# Flow volume | Расход
if 'termPaper' in projectType:
    G_K = N_e*g_e*l_0*alpha*phi/3600; # kg/s

# Inlet turbine temperature (for HW) | Температура перед турбиной
if 'HW' in projectType:
    if D_2K < 0.3:
        T_0Stagn = 923;
    elif (D_2K > 0.3) & (D_2K < 0.64):
        T_0Stagn = 823;
    else:   exit("Error 0: The diameter of the wheel is too big!")

# Outlet turbine pressure | Давление за турбиной
p_2 = dragInletRatio*p_a*1e+06; # Pa

## Turbine parameters calculation
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

G_T = G_K*sigma_esc*(1 + 1/alpha/phi/l_0); # 1. Расход газа через турбину с учетом утечки

# 2. Диаметр колеса турбины и окружная скорость на входе в колесо турбины
D_1 = diameterRatio*D_2K;
u_1 = diameterRatio*u_2K;

L_TsStagn = L_KsStagn*G_K/eta_KsStagnRated/eta_Te/G_T; # 4. Изоэнтропная работа турбины

c_2s = math.sqrt( 2*L_TsStagn ); # 5. Условная изоэнтропная скорость истечения из турбины

# 6. Расчёт параметра ksi
ksi = u_1/c_2s;
if (ksi < 0.64) | (ksi > 0.7):    exit("Error 6:\
 Parameter 'ksi' is not in the allowable diapason! (It equals %0.2f)" %ksi);

# 7. Давление газа на входе в турбину
p_0Stagn = p_2/pow(1 - L_TsStagn/c_pExh/T_0Stagn, k_Exh/(k_Exh - 1) );

# 8. Проверка соотношения полного давления перед впускными клапанами поршневой части и давлением газа на входе в турбину
pressureRelation = p_vStagn/p_0Stagn;
if (pressureRelation < 1.1) | (pressureRelation > 1.3):
    exit("Error 8: Pressure ratio is not in the allowable diapason!\
 Scavenging cannot be happen. (It equals %0.2f)" %pressureRelation);

D_2H = outerDiamRatio*D_1;# 9. Наружный диаметр рабочего колеса турбины на выходе

D_2B = innerDiamRatio*D_1; # 10. Внутренний (втулочный) диаметр колеса

# 11. Средний диаметр колеса турбины на выходе
D_2 = math.sqrt(( pow(D_2B, 2) + pow(D_2H, 2) )/2);

# 12. Вычисление параметра µ
mu = D_2/D_1;
if (mu < 0.5) | (mu > 0.8): exit("Error 12:\
 Geometeric parameter 'mu' is not in the allowable diapason! (It equals %0.2f)" %mu);

L_cS = L_TsStagn*(1 - ro); # 15. Изоэнтропная работа расширения (располагаемый теплоперепад) в сопловом аппарате

c_1 = phiLosses*math.sqrt( 2*L_cS ); # 17. Абсолютная скорость с1 на выходе из соплового аппарата

c_1r = c_1*math.sin(math.radians( alpha_1 )); # 19. Радиальная составляющая абсолютной скорости (c_1r == w_1r)

c_1u = c_1*math.cos(math.radians( alpha_1 )); # 20. Окружная составляющая абсолютной скорости на выходе из соплового аппарата

w_1u = c_1u - u_1; # 21. Окружная составляющая относительной скорости на выходе из соплового аппарата

w_1 = math.sqrt(pow(c_1r, 2) - pow(w_1u, 2)); # 22. Относительная скорость на входе в рабочее колесо

# 23. Значение угла β_1 наклона вектора относительной скорости w_1
beta_1 = beta_1Blade - math.degrees(math.atan( w_1u/c_1r ));
if (beta_1 < 80) | (beta_1 > 100):
    exit("Error 23: Angle 'beta_1' is not in the allowable diapason!\n\
Try to change 'beta_1Blade' parameter. (It equals %0.1f)" %beta_1);

T_1 = T_0Stagn - pow(c_1, 2)/2/c_pExh; # 24. Температура газа на входе в колесо

p_1 = p_0Stagn*pow(1 - L_cS/c_pExh/T_0Stagn, k_Exh/(k_Exh - 1) ); # 25. Давление на входе в колесо

ro_1 = p_1/R_Exh/T_1; # 26. Плотность ρ_1 на входе в колесо

b_1 = G_T/math.pi/D_1/ro_1/c_1r; # 27. Ширина лопаток b1 на входе в колесо

L_pS = ro*L_TsStagn; # 28. Изоэнтропная работа расширения в рабочем колесе (располагаемый теплоперепад) на входе в колесо

u_2 = mu*u_1; # 30. Окружная скорость на среднем диаметре D_2 выхода из рабочего колеса

# 31. Относительная скорость на среднем диаметре D_2
w_2 = psiLosses*math.sqrt( 2*L_pS + pow(w_1, 2) - pow(u_1, 2) + pow(u_2, 2) );

T_2 = T_1 - (pow(w_2, 2) - pow(u_2, 2) - pow(w_1, 2) + pow(u_1, 2))/2/c_pExh# 32. Температура Т_2 на выходе из колеса

ro_2 = p_2/R_Exh/T_2; # 33. Плотность на выходе из колеса

F_2 = math.pi/4*(pow(D_2H, 2) - pow(D_2B, 2)); # 34. Площадь сечения на выходе из колеса

G_losses = 0.45*2*delta*G_T/(D_2H - D_2B)*(1 + (D_2H - D_2B)/2/D_2); # 35. Утечки через этот радиальный зазор Δ между корпусом и колесом турбины составят

G_F2 = G_T - G_losses; # 36. Расход через сечение F_2 на выходе из колеса

w_2a = G_F2/F_2/ro_2; # 37. Аксиальные составляющие относительной w_2а и абсолютной с_2а скоростей на выходе из колеса (w_2a == c_2a)

# 38. Окружная составляющая относительной скорости на выходе из колеса
if (pow(w_2, 2) - pow(w_2a, 2)) > 0:
    w_2u = math.sqrt(pow(w_2, 2) - pow(w_2a, 2));
else:   exit("Error 38: Radicand is less then 0!")

beta_2 = math.degrees(math.asin( w_2a/w_2 )); # 39. Угол β_2 наклона вектора относительной скорости w2 на выходе из рабочего колеса

c_2u = w_2u - u_2; # 40. Окружная составляющая с2u абсолютной скорости на выходе из колеса

c_2 = math.sqrt(pow(w_2a, 2) + pow(c_2u, 2)); # 41. Абсолютная скорость на выходе из колеса

# 42. Угол α_2 выхода потока из колеса в абсолютном движении
alpha_2 = 90 - math.degrees(math.atan( c_2u/w_2a ));
if (alpha_2 < 75) | (alpha_2 > 105):
    exit("Error 42: Angle 'alpha_2' is not in the allowable diapason! (It equals %0.1f)" %alpha_2);

Z_c = (1/pow(phiLosses, 2) - 1)*pow(c_1, 2)/2; # 43. Потери в сопловом аппарате турбины

Z_p = (1/pow(psiLosses, 2) - 1)*pow(w_2, 2)/2; # 44. Потери в рабочем колесе

Z_Blades = Z_c + Z_p; # 45. Суммарные потери в лопаточных каналах

L_TBlades = L_TsStagn - Z_Blades; # 46. Лопаточная работа турбины

eta_TBlades = L_TBlades/L_TsStagn; # 47. Лопаточный КПД η_(т.л) турбины

Z_SteadyOutlet = pow(c_2, 2)/2; # 48. Потери в Z′_в с выходной скоростью при условии равномерного потока на выходе из рабочего колеса

L_TuSteadyFromLosses = L_TBlades - Z_SteadyOutlet; # 49. Работа L′_тu на окружности колеса c учётом потерь определёная через потери

L_TuSteady = u_1*c_1u + u_2*c_2u; # 50. Работа L′_тu на окружности колеса c учётом потерь определёная с помощью формулы Эйлера

Z_UnsteadyOutlet = dzeta*Z_SteadyOutlet; # 51. Действительные потери Z_в с выходной скоростью (для потока с неравномерностью на выходе)

L_Tu = L_TBlades - Z_UnsteadyOutlet; # 52. Действительная работа на окружности колеса

# 53. Окружной КПД η_тu турбины
eta_Tu = L_Tu/L_TsStagn;
if (eta_Tu < 0.75) | (eta_Tu > 0.9):
    exit("Error 53: Angle 'eta_Tu' is not in the allowable diapason! (It equals %0.3f)" %eta_Tu);

Z_y = L_Tu*G_losses/G_T; # 54. Потери Zу, обусловленные утечкой газа через радиальные зазоры между колесом и корпусом

N_TB = 735.5*beta*(ro_1 + ro_2)/2*pow(D_1, 2)*pow(u_1/100, 3); # 55. Мощность N_тв, затрачиваемая на трение колеса в корпусе и вентиляцию

Z_TB = N_TB/G_T; # 56. Потери Z_тв на трение и вентиляцию

Z_extra = Z_y + Z_TB; # 57. Суммарные дополнительные потери Z_д , включающие потери на утечки, трение и вентиляцию

L_Ti = L_Tu - Z_extra; # 58. Внутренняя работа L_тi турбины

eta_Ti = L_Ti/L_TsStagn; # 59. Внутренний КПД η_тi турбины

eta_TeRated = eta_m*eta_Ti; # 60. Эффективный КПД η`_тe  турбины

differenceEta = abs(eta_TeRated - eta_Te)/eta_Te*100; # % | 61. Расхождение с заданным КПД турбины

L_Te = eta_TeRated*L_TsStagn; # 62. Эффективная работа L_т е турбины

N_T = L_Te*G_T; # 63. Мощность N_т на валу турбины

differenceN = abs(N_K - N_T)/N_K*100; # % | 64. Расхождение с мощностью N_к, потребляемой компрессором


## Displaying the results
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Display some results right in the Terminal window
print "Energy conversion efficiency coeficients are:\n\
    eta_Te  = {0}   - setted\n\
    eta_Te' = {1:.4f} - rated"\
    .format(eta_Te, eta_TeRated); # (dict) & (60)
print 'Error of calculation between them is {0:.3f}%\n' .format(differenceEta); # (61)

print "Power consumption:\n\
    N_c = {N_K_kW:.3f} kW - for compressor\n\
    N_t = {N_T_kW:.3f} kW - for turbine"\
    .format(N_K_kW = N_K*1e-03, N_T_kW = N_T*1e-03); # (compressor) & (63)
print 'Error of calculation between them is {0:.3f}%\n' .format(differenceN); # (62)

print "If something doesn't work correctly make the new issue or check the others:\n\
https://github.com/StasF1/turboCharger/issues"#u'\n\N{COPYRIGHT SIGN} 2018 Stanislau Stasheuski'


## Report generation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
execfile('include/reportGenerator.py') # saving the report
execfile('include/picturesEditor.py') # editing pictures
execfile('include/createResultsFolder.py') # saving the results to the resultsFolder



