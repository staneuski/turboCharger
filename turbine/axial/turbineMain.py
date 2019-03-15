#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# License
#     This program is free software: you can redistribute it and/or
#     modify it under the terms of the GNU General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#     General Public License for more details.
#
# Script
#     Main
#
# Description
#     Calculates parameters of axial turbine using 0D method
# 
#-----------------------------------------------------------------------

## Loading data & calling some fuctions

# Funcion for math solvers (pi, sin, cos, etc.) & other
from __future__         import division
from PIL                import ImageFont, Image, ImageDraw
import math, os, shutil, sys

# Some self-made fuctions
from os             import path;\
    sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from defaultValue   import defaultValue

# Loading input data from project dictionaries
from commonDict       import *
from turbineDict      import *
from solvedParameters import *

# Converting data to SI from dictionary | Перевод в СИ
N_e = N_e*1e+03 # -> V
g_e = g_e*1e-03 # -> kg/(V*h) or g/(kV*h)
if issubclass(type(delta), float):    delta = delta*1e-03; # -> m

execfile('include/defaultValuesCoefficients.py') # default values
execfile('../../programFiles/logo.py') # printing the logo

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

## Precalculations
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Lower heat of combustion for fuel | Низшая теплота сгорания в зависимости от типа ДВС
if 'SI' in engineType:
    l_0 = 14.25; # kg
elif 'DIESEL' in engineType:
    l_0 = 14.31; # kg
else:
    exit('Set type of the engine correctly ("DIESEL" or "SI")\
 in commonDict.py file!\n')

# Outlet turbine pressure | Давление за турбиной
p_2 = dragInletRatio*p_a*1e+06 # Pa

## Turbine parameters calculation
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

G_T = G_K*sigma_esc*(1 + 1/alpha/phi/l_0) # 1. Расход газа через турбину с учетом утечки

L_TsStagn = L_KsStagn*G_K/eta_KsStagnRated/eta_Te/G_T # 3. Изоэнтропная работа турбины

c_2s = math.sqrt( 2*L_TsStagn ) # 4. Условная изоэнтропная скорость истечения из турбины

u_1 = ksi*c_2s # 5. Расчёт скорости на входе

p_0Stagn = p_2/pow(1 - L_TsStagn/c_pExh/T_0Stagn, k_Exh/(k_Exh - 1) ) # 7. Давление газа на входе в турбину

# 8. Проверка соотношения полного давления перед впускными клапанами поршневой части и давлением газа на входе в турбину
pressureRelation = p_vStagn/p_0Stagn
if (pressureRelation <= 1.1):
    exit("\nError 8: Scavenging cannot be happen because the pressure ratio is too small!\n\
It equals %0.2f, but must be more than 1.1\n" %pressureRelation)

L_cS = L_TsStagn*(1 - rho) # 9. Изоэнтропная работа расширения (располагаемый теплоперепад) в сопловом аппарате

c_1 = phiLosses*math.sqrt( 2*L_cS ) # 11. Абсолютная скорость с1 на выходе из соплового аппарата

c_1a = c_1*math.sin(math.radians( alpha_1 )) # 13. Радиальная составляющая абсолютной скорости (c_1a == w_1a)

c_1u = c_1*math.cos(math.radians( alpha_1 )) # 14. Окружная составляющая абсолютной скорости на выходе из соплового аппарата

w_1u = c_1u - u_1; # 15. Окружная составляющая относительной скорости на выходе из соплового аппарата

beta_1 = beta_1Blade - math.degrees(math.atan( w_1u/c_1a )) # 16. Значение угла β_1 наклона вектора относительной скорости w_1

T_1 = T_0Stagn - pow(c_1, 2)/2/c_pExh # 17. Температура газа на входе в колесо

# 18. Давление на входе в колесо
p_1 = p_0Stagn*pow(1 - L_cS/c_pExh/T_0Stagn, k_Exh/(k_Exh - 1) )
pressureRelationSetOfNozzles = p_1/p_0Stagn

ro_1 = p_1/R_Exh/T_1 # 19. Плотность ρ_1 на входе в колесо

D_1 = 60*u_1/math.pi/n_TCh # 20. Средний диаметр решеток соплового аппарата на выходе и рабочего колеса на входе

# 21. Высота лопаток соплового аппарата
l_1 = G_T/math.pi/D_1/ro_1/c_1/math.sin(math.radians( alpha_1 ))
if (l_1/D_1 < 0.16) | (l_1/D_1 > 0.25):
    exit("\nError 21: Blade height 'l_1' is not in the allowable diapason!\n\
It equals %0.2f but must be from 0.16 to 0.25" %(l_1/D_1));

t_1_0 = RELt1_l1*l_1 # 22. Шаг решётки соплового аппарата

z_1 = round( math.pi*D_1/t_1_0 ) # 23. Число лопаток соплового аппарата

t_1 = math.pi*D_1/z_1 # 23. Шаг решётки соплового аппарата с учётом округления числа лопаток

M_c1  = c_1/math.sqrt( k_Exh*R_Exh*T_1 ) # 25. Число Маха на выходе из сопловой решетки

# 26. Ширина решетки в наиболее узкой ее части
if (M_c1 > 0.4) & (M_c1 < 0.6):
    a_1 = t_1*math.sin(math.radians( alpha_1 ))/m
elif M_c1 >= 0.6:
    a_1 = t_1*math.sin(math.radians( alpha_1 ))
else:
    exit("\nError 26: Mach number is not in the allowable diapason!\n\
It equals %0.1f but must be at least more then 0.4" %(M_c1));

b_1 = t_1*2*math.sin(math.radians( alpha_1 ))*math.sin(math.radians(alpha_0 + alpha_1))\
    /c_u1/math.sin(math.radians( alpha_0 )) # 27. Ширина b_1 соплового аппарата по направлению оси вращения

w_1 = math.sqrt( pow(c_1, 2) + pow(u_1, 2) - 2*c_1*u_1*math.cos(math.radians( alpha_1 )) ) # 28. Относительная скорость w1 на входе в рабочее колесо

L_pS = rho*L_TsStagn # 29. Изоэнтропная работа расширения в рабочем колесе (располагаемый теплоперепад) на входе в колесо

w_2 = psiLosses*math.sqrt( 2*L_pS + pow(w_1, 2) ) # 31. Относительная скорость на среднем диаметре D_2

T_2 = T_1 - (pow(w_2, 2) - pow(w_1, 2))/2/c_pExh # 32. Температура Т_2 на выходе из колеса

ro_2 = p_2/R_Exh/T_2 # 33. Плотность на выходе из колеса

F_2 = math.pi*D_1*l_1 # 35. Площадь проходного сечения F_2 на выходе из колеса

w_2a = G_T/F_2/ro_2 # 36. Осевая составляющая относительной скорости на выходе в первом приближении

beta_2_0 = math.degrees(math.asin( w_2a/w_2 )) # 37. Угол β_2 наклона вектора относительной скорости w2 на выходе из рабочего колеса

G_losses = delta*G_T/l_1/math.sin(math.radians( beta_2_0 )) # 38. Утечки через этот радиальный зазор Δ между корпусом и колесом турбины составят

G_F2 = G_T - G_losses # 39. Расход через сечение F_2

c_2a = G_F2/F_2/ro_2 # 40. Осевые составляющие относительной w_2a и абсолютной с_2а скоростей на выходе из колеса (w_2a == с_2а)

beta_2 = math.degrees(math.asin( c_2a/w_2 )) # 41. Уточнённый угол β_2 наклона вектора относительной скорости w2 на выходе из рабочего колеса

c_2u = w_2*math.cos(math.radians( beta_2 )) - u_1 # 42. Окружная составляющая с_2u абсолютной скорости на выходе из колеса

c_2 = math.sqrt(pow(c_2a, 2) + pow(c_2u, 2)) # 43. Абсолютная скорость на выходе из колеса

# 44. Угол α_2 выхода потока из колеса в абсолютном движении
alpha_2 = math.degrees(math.asin( c_2a/c_2 ));
if (alpha_2 < 80) | (alpha_2 > 100):
    exit("\nError 44: Angle 'alpha_2' is not in the allowable diapason!\n\
It equals %0.1f but must be from 80 to 100 degrees." %alpha_2);

t_2_0 = RELt2_l2*l_1 # 45. Шаг решётки рабочего колеса

z_2 = round( math.pi*D_1/t_2_0 ) # 46. Число лопаток рабочего колеса

t_2 = math.pi*D_1/z_2 # 47. Шаг решётки рабочего колеса с учётом округления числа лопаток

M_w2  = w_2/math.sqrt( k_Exh*R_Exh*T_2 ) # 48. Число Маха на выходе из сопловой решетки

# 49. Ширина решетки в наиболее узкой ее части
if (M_c1 > 0.4) & (M_c1 < 0.6):
    a_2 = t_2*math.sin(math.radians( beta_2 ))/m
elif M_c1 >= 0.6:
    a_2 = t_2*math.sin(math.radians( beta_2 ))
else:
    exit("\nError 49: Mach number is not in the allowable diapason!\n\
It equals %0.1f but must be at least more then 0.4" %(M_c1));

b_2 = 2*t_2*math.sin(math.radians( beta_2 ))*math.sin(math.radians(beta_1 + beta_2))\
    /c_u2/math.sin(math.radians( beta_1 )) # 50. Ширина b_2 рабочего колеса по направлению оси вращения

Z_c = (1/pow(phiLosses, 2) - 1)*pow(c_1, 2)/2; # 51. Потери в сопловом аппарате турбины

Z_p = (1/pow(psiLosses, 2) - 1)*pow(w_2, 2)/2; # 52. Потери в рабочем колесе

Z_Blades = Z_c + Z_p; # 53. Суммарные потери в лопаточных каналах

L_TBlades = L_TsStagn - Z_Blades; # 54. Лопаточная работа турбины

eta_TBlades = L_TBlades/L_TsStagn; # 55. Лопаточный КПД η_(т.л) турбины

Z_SteadyOutlet = pow(c_2, 2)/2; # 56. Потери в Z′_в с выходной скоростью при условии равномерного потока на выходе из рабочего колеса

L_TuFromLosses = L_TBlades - Z_SteadyOutlet; # 57. Работа L′_тu на окружности колеса c учётом потерь (определёная через потери)

L_Tu = u_1*(c_1u + c_2u); # 58. Работа L′_тu на окружности колеса c учётом потерь (определёная с помощью формулы Эйлера)

# 59. Окружной КПД η_тu турбины
eta_Tu = L_Tu/L_TsStagn;
if (eta_Tu < 0.8) | (eta_Tu > 0.9):
    print "\nError 59: ECE 'eta_Tu' is not in the allowable diapason!\n\
It equals {0:.3f} but must be from 0.8 to 0.9\n" .format(eta_Tu)

Z_y = L_Tu*G_losses/G_T; # 60. Потери Z_у, обусловленные утечкой газа через радиальные зазоры между колесом и корпусом

N_TB = 735.5*beta*(ro_1 + ro_2)/2*pow(D_1, 2)*pow(u_1/100, 3); # 61. Мощность N_тв, затрачиваемая на трение колеса в корпусе и вентиляцию

Z_TB = N_TB/G_T; # 62. Потери Z_тв на трение и вентиляцию

Z_extra = Z_y + Z_TB; # 63. Суммарные дополнительные потери Z_д , включающие потери на утечки, трение и вентиляцию

L_Ti = L_Tu - Z_extra; # 64. Внутренняя работа L_тi турбины

eta_Ti = L_Ti/L_TsStagn; # 65. Внутренний КПД η_тi турбины

eta_TeRated = eta_m*eta_Ti; # 66. Эффективный КПД η`_тe  турбины

differenceEta = abs(eta_TeRated - eta_Te)/eta_Te*100; # 67. Расхождение с заданным КПД турбины

L_Te = eta_TeRated*L_TsStagn; # 68. Эффективная работа L_т е турбины

N_T = L_Te*G_T; # 69. Мощность N_т на валу турбины

differenceN = abs(N_K - N_T)/N_K*100; # 70. Расхождение с мощностью N_к, потребляемой компрессором


## Displaying the results
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Display some results right in the Terminal window
print "Energy conversion efficiency coeficients are:\n\
    eta_Te  = {0:.4f} - setted\n\
    eta_Te' = {1:.4f} - rated"\
    .format(eta_Te, eta_TeRated) # (dict) & (60)
print '\nError of calculation between them is {0:.3f}%\n' .format(differenceEta) # (61)

print "Power consumption:\n\
    N_c = {N_K_kW:.3f} kW - of compressor\n\
    N_t = {N_T_kW:.3f} kW - of turbine"\
    .format(N_K_kW = N_K*1e-03, N_T_kW = N_T*1e-03) # (compressor) & (63)
print '\nError of calculation between them is {0:.3f}%\n' .format(differenceN) # (62)

print "If something doesn't work correctly make the new issue or check the others:\n\
https://github.com/StasF1/turboCharger/issues"#u'\n\N{COPYRIGHT SIGN}
print '2018 Stanislau Stasheuski'


## Report generation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
execfile('include/reportGenerator.py') # saving the report
execfile('include/picturesEditor.py') # editing pictures
execfile('include/createResultsFolder.py') # saving the results to the resultsFolder



