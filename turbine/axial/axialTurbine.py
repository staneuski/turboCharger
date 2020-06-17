#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    Script:         axialTurbine
    Description:    Calculate axial turbine parameters using 0D method

'''
from __future__         import division
import math, os, shutil, sys
from PIL                import ImageFont, Image, ImageDraw

from os             import path;\
    sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from defaultValue   import defaultValue

# Loading input data from project dictionaries
from commonConfig     import *
from turbineConfig    import *
from solvedParameters import *

# Converting data to SI dimensions
N_e = N_e*1e+03 # -> [W]
g_e = g_e*1e-03 # -> [kg/W/h] or [g/kW/h]
if issubclass(type(delta), float):    delta = delta*1e-03; # -> [m]

# Set default values
exec(compile(open('include/defaultValuesCoefficients.py', "rb").read(),
                  'include/defaultValuesCoefficients.py', 'exec'))
# Output the logo
exec(compile(open('../../etc/logo.py', "rb").read(),
                  '../../etc/logo.py', 'exec'))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Теоретическое количество воздуха, необходимое для сгорания 1 кг топлива
if 'SI' in engineType:
    l_0 = 14.25; # [kg]
elif 'DIESEL' in engineType:
    l_0 = 14.31; # [kg]
else:
    exit('Set type of the engine correctly ("DIESEL" or "SI")\
 in commonConfig.py file!\n')

# Outlet turbine pressure | Давление за турбиной
p_2 = dragInletRatio*p_a*1e+06 # [Pa]


# Axial turbine parameters
# ~~~~~~~~~~~~~~~~~~~~~~~~
#1 Расход газа через турбину с учетом утечки
G_T = G_K*sigma_esc*(1 + 1/alpha/phi/l_0)

#3 Изоэнтропная работа турбины
L_TsStagn = L_KsStagn*G_K/eta_KsStagnRated/eta_Te/G_T

#4 Условная изоэнтропная скорость истечения из турбины
c_2s = math.sqrt( 2*L_TsStagn )

#5  Расчёт скорости на входе
u_1 = ksi*c_2s

#7 Давление газа на входе в турбину
p_0Stagn = p_2/pow(1 - L_TsStagn/c_pExh/T_0Stagn, k_Exh/(k_Exh - 1) ) 

#8 Проверка соотношения полного давления перед впускными клапанами
#  поршневой части и давлением газа на входе в турбину
pressureRelation = p_vStagn/p_0Stagn
if (pressureRelation <= 1.1):
    exit("\nError 8: Scavenging cannot happen because the pressure ratio is too small!\n\
It equals %0.2f, but must be more than 1.1\n" %pressureRelation)

#9 Изоэнтропная работа расширения
#  (располагаемый теплоперепад) в сопловом аппарате
L_cS = L_TsStagn*(1 - rho)

#11 Абсолютная скорость с1 на выходе из соплового аппарата
c_1 = phiLosses*math.sqrt( 2*L_cS )

#13 Радиальная составляющая абсолютной скорости (c_1a == w_1a)
c_1a = c_1*math.sin(math.radians( alpha_1 ))

#14 Окружная составляющая абсолютной скорости на выходе из соплового аппарата
c_1u = c_1*math.cos(math.radians( alpha_1 ))

#15 Окружная составляющая относительной скорости
#   на выходе из соплового аппарата
w_1u = c_1u - u_1

#16 Значение угла β_1 наклона вектора относительной скорости w_1
beta_1 = beta_1Blade - math.degrees(math.atan( w_1u/c_1a ))

#17 Температура газа на входе в колесо
T_1 = T_0Stagn - pow(c_1, 2)/2/c_pExh 

#18 Давление на входе в колесо
p_1 = p_0Stagn*pow(1 - L_cS/c_pExh/T_0Stagn, k_Exh/(k_Exh - 1) )
pressureRelationSetOfNozzles = p_1/p_0Stagn

#19 Плотность ρ_1 на входе в колесо
ro_1 = p_1/R_Exh/T_1

#20 Средний диаметр решеток соплового аппарата на выходе
#   и рабочего колеса на входе
D_1 = 60*u_1/math.pi/n_TCh

#21 Высота лопаток соплового аппарата
l_1 = G_T/math.pi/D_1/ro_1/c_1/math.sin(math.radians( alpha_1 ))
if (l_1/D_1 < 0.16) | (l_1/D_1 > 0.25):
    exit("\nError 21: Blade height 'l_1' is not in the allowable diapason!\n\
It equals %0.2f but must be from 0.16 to 0.25" %(l_1/D_1))

#22 Шаг решётки соплового аппарата
t_1_0 = RELt1_l1*l_1

#23 Число лопаток соплового аппарата
z_1 = round( math.pi*D_1/t_1_0 )

#23 Шаг решётки соплового аппарата с учётом округления числа лопаток
t_1 = math.pi*D_1/z_1

#25 Число Маха на выходе из сопловой решетки
M_c1 = c_1/math.sqrt( k_Exh*R_Exh*T_1 )

#26 Ширина решетки в наиболее узкой ее части
if (M_c1 > 0.4) & (M_c1 < 0.6):
    a_1 = t_1*math.sin(math.radians( alpha_1 ))/m
elif M_c1 >= 0.6:
    a_1 = t_1*math.sin(math.radians( alpha_1 ))
else:
    exit("\nError 26: Mach number is not in the allowable diapason!\n\
It equals %0.1f but must be at least more then 0.4" %(M_c1))

#27 Ширина b_1 соплового аппарата по направлению оси вращения
b_1 = t_1*2*math.sin(math.radians( alpha_1 ))\
    *math.sin(math.radians(alpha_0 + alpha_1))\
    /math.sin(math.radians( alpha_0 ))/c_u1

#28 Относительная скорость w1 на входе в рабочее колесо
w_1 = math.sqrt(
          pow(c_1, 2) + pow(u_1, 2) - 2*c_1*u_1*math.cos(math.radians( alpha_1 ))
      )

#29 Изоэнтропная работа расширения в рабочем колесе
#   (располагаемый теплоперепад) на входе в колесо
L_pS = rho*L_TsStagn

#31 Относительная скорость на среднем диаметре D_2
w_2 = psiLosses*math.sqrt( 2*L_pS + pow(w_1, 2) )

#32 Температура Т_2 на выходе из колеса
T_2 = T_1 - (pow(w_2, 2) - pow(w_1, 2))/2/c_pExh

#33 Плотность на выходе из колеса
ro_2 = p_2/R_Exh/T_2

#35 Площадь проходного сечения F_2 на выходе из колеса
F_2 = math.pi*D_1*l_1

#36 Осевая составляющая относительной скорости на выходе в первом приближении
w_2a = G_T/F_2/ro_2

#37 Угол β_2 наклона вектора относительной скорости w2
#   на выходе из рабочего колеса
beta_2_0 = math.degrees(math.asin( w_2a/w_2 ))

#38 Утечки через этот радиальный зазор Δ между корпусом
#   и колесом турбины составят
G_losses = delta*G_T/l_1/math.sin(math.radians( beta_2_0 ))

#39 Расход через сечение F_2
G_F2 = G_T - G_losses

#40 Осевые составляющие относительной w_2a и абсолютной с_2а скоростей
#   на выходе из колеса (w_2a == с_2а)
c_2a = G_F2/F_2/ro_2

#41 Уточнённый угол β_2 наклона вектора относительной скорости w2
#   на выходе из рабочего колеса
beta_2 = math.degrees(math.asin( c_2a/w_2 ))

#42 Окружная составляющая с_2u абсолютной скорости на выходе из колеса
c_2u = w_2*math.cos(math.radians( beta_2 )) - u_1

#43 Абсолютная скорость на выходе из колеса
c_2 = math.sqrt(pow(c_2a, 2) + pow(c_2u, 2))

#44 Угол α_2 выхода потока из колеса в абсолютном движении
alpha_2 = math.degrees(math.asin( c_2a/c_2 ))
if (alpha_2 < 80) | (alpha_2 > 100):
    exit("\nError 44: Angle 'alpha_2' is not in the allowable diapason!\n\
It equals %0.1f but must be from 80 to 100 degrees." %alpha_2)

#45 Шаг решётки рабочего колеса
t_2_0 = RELt2_l2*l_1

#46 Число лопаток рабочего колеса
z_2 = round( math.pi*D_1/t_2_0 )

#47 Шаг решётки рабочего колеса с учётом округления числа лопаток
t_2 = math.pi*D_1/z_2

#48 Число Маха на выходе из сопловой решетки
M_w2 = w_2/math.sqrt( k_Exh*R_Exh*T_2 ) 

#49 Ширина решетки в наиболее узкой ее части
if (M_c1 > 0.4) & (M_c1 < 0.6):
    a_2 = t_2*math.sin(math.radians( beta_2 ))/m
elif M_c1 >= 0.6:
    a_2 = t_2*math.sin(math.radians( beta_2 ))
else:
    exit("\nError 49: Mach number is not in the allowable diapason!\n\
It equals %0.1f but must be at least more then 0.4" %(M_c1))

#50 Ширина b_2 рабочего колеса по направлению оси вращения
b_2 = 2*t_2*math.sin(math.radians( beta_2 ))\
      /c_u2/math.sin(math.radians( beta_1 ))\
           *math.sin(math.radians(beta_1 + beta_2))\

#51 Потери в сопловом аппарате турбины
Z_c = (1/pow(phiLosses, 2) - 1)*pow(c_1, 2)/2

#52 Потери в рабочем колесе
Z_p = (1/pow(psiLosses, 2) - 1)*pow(w_2, 2)/2

#53 Суммарные потери в лопаточных каналах
Z_Blades = Z_c + Z_p

#54 Лопаточная работа турбины
L_TBlades = L_TsStagn - Z_Blades

#55 Лопаточный КПД η_(т.л) турбины
eta_TBlades = L_TBlades/L_TsStag

#56 Потери в Z′_в с выходной скоростью при условии
#   равномерного потока на выходе из рабочего колеса
Z_SteadyOutlet = pow(c_2, 2)/2

#57 Работа L′_тu на окружности колеса c учётом потерь
#   (определёная через потери)
L_TuFromLosses = L_TBlades - Z_SteadyOutlet

#58 Работа L′_тu на окружности колеса c учётом потерь
#   (определёная с помощью формулы Эйлера)
L_Tu = u_1*(c_1u + c_2u)

#59 Окружной КПД η_тu турбины
eta_Tu = L_Tu/L_TsStagn
if (eta_Tu < 0.8) | (eta_Tu > 0.9):
    print("\nError 59: ECE 'eta_Tu' is not in the allowable diapason!\n\
It equals {0:.3f} but must be from 0.8 to 0.9\n" .format(eta_Tu))

#60 Потери Z_у, обусловленные утечкой газа через радиальные зазоры
#   между колесом и корпусом
Z_y = L_Tu*G_losses/G_T

#61 Мощность N_тв, затрачиваемая на трение колеса в корпусе и вентиляцию
N_TB = 735.5*beta*(ro_1 + ro_2)/2*pow(D_1, 2)*pow(u_1/100, 3)

#62 Потери Z_тв на трение и вентиляцию
Z_TB = N_TB/G_T

#63 Суммарные дополнительные потери Z_д,
#   включающие потери на утечки, трение и вентиляцию
Z_extra = Z_y + Z_TB

#64 Внутренняя работа L_тi турбины
L_Ti = L_Tu - Z_extra

#65 Внутренний КПД η_тi турбины
eta_Ti = L_Ti/L_TsStagn

#66 Эффективный КПД η`_тe турбины
eta_TeRated = eta_m*eta_Ti

#67 Расхождение с заданным КПД турбины
differenceEta = abs(eta_TeRated - eta_Te)/eta_Te*100

#68 Эффективная работа L_т е турбины
L_Te = eta_TeRated*L_TsStagn

#69 Мощность N_т на валу турбины
N_T = L_Te*G_T

#70 Расхождение с мощностью N_к, потребляемой компрессором
differenceN = abs(N_K - N_T)/N_K*100


# Display the results
# ~~~~~~~~~~~~~~~~~~~
# Display some results right in the Terminal window
print("Energy conversion efficiency coeficients are:\n\
    eta_Te  = {0:.4f} - set\n\
    eta_Te' = {1:.4f} - rated"\
    .format(eta_Te, eta_TeRated)) # (dict) & (60)
print('\nError of calculation between them is {0:.3f}%\n'\
    .format(differenceEta)) # (61)

print("Power consumption:\n\
    N_c = {N_K_kW:.3f} kW - of compressor\n\
    N_t = {N_T_kW:.3f} kW - of turbine"\
    .format(N_K_kW = N_K*1e-03, N_T_kW = N_T*1e-03)) # (compressor) & (63)
print('\nError of calculation between them is {0:.3f}%\n'\
    .format(differenceN)) # (62)

print("If something doesn't work correctly make a new issue or check the others:\n\
https://github.com/StasF1/turboCharger/issues")


# Generate report
# ~~~~~~~~~~~~~~~
# Create a report
exec(compile(open('include/reportGenerator.py', "rb").read(),
                 'include/reportGenerator.py', 'exec'))
# Edit pictures
exec(compile(open('include/picturesEditor.py', "rb").read(),
                  'include/picturesEditor.py', 'exec'))
# Save the results to the results/ folder
exec(compile(open('include/createResultsFolder.py', "rb").read(),
                  'include/createResultsFolder.py', 'exec'))


# ''' (C) 2019-2020 Stanislau Stasheuski '''