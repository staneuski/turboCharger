#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    Script:         radialTurbine
    Description:    Calculate radial turbine parameters using 0D method

'''
from __future__ import division
import math, os, shutil, sys
from PIL        import ImageFont, Image, ImageDraw
sys.path.extend(
    ['../../', '../../etc/', '../../etc/turbine/', '../../compressor/', '../']
)
sys.path.extend(['pre/', 'post/'])

from logo             import logo
from default_value     import default_value
from output           import output

from set_default_values import set_default_values
from plot2func import eta_plot2func, alpha_plot2func, phi_plot2func, psi_plot2func, ksi_plot2func,\
                               relD_1H, relD_2B

# Loading input data from project dictionaries
from commonConfig     import *
from engineConfig     import *
from compressorConfig import *
from turbineConfig    import *
from compressorToTurbineConfig import *

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
logo()

# Converting data to SI dimensions
engine['efficiency']['N_e'] *= 1e+03 # -> [W]
engine['efficiency']['b_e'] *= 1e-03 # -> [kg/W/h] or [g/engine['inlet']['k']W/h]
if issubclass(type(turbine['geometry']['delta']), float):
    turbine['geometry']['delta'] *= 1e-03 # -> [m]

set_default_values(engine['exhaust'], turbine)

# Set values using balance coefficients from dictionary
turbine['efficiency']['eta_Te'] = eta_plot2func(
    turbine['efficiency']['eta_Te'], D_2K
)
turbine['geometry']['alpha_1'] = alpha_plot2func(
    turbine['geometry']['alpha_1'], D_2K
)
turbine['losses']['phi'] = phi_plot2func(
    turbine['losses']['phi'], D_2K
)
turbine['losses']['psi'] = psi_plot2func(
    turbine['losses']['psi'], D_2K
)
turbine['geometry']['coefficients']['outerDiamRatio'] = relD_1H(
    turbine['geometry']['coefficients']['outerDiamRatio'], D_2K
)
turbine['geometry']['coefficients']['innerDiamRatio'] = relD_2B(
    turbine['geometry']['coefficients']['innerDiamRatio'], D_2K
)

# Теоретическое количество воздуха, необходимое для сгорания 1 кг топлива
if 'SI' in engine['combustion']['ignition']:
    engine['combustion']['l_0'] = 14.28 # [kg]
elif 'CI' in engine['combustion']['ignition']:
    engine['combustion']['l_0'] = 14.31 # [kg]
else:
    exit('Set type of the engine correctly ("DIESEL" or "SI")\
 in commonConfig.py file!\n')

# Flow volume | Расход
if 'TYPE1' in run['type']:
    compressor['G_K'] = engine['efficiency']['N_e']\
        *engine['efficiency']['b_e']\
        *engine['combustion']['l_0']\
        *engine['combustion']['alpha']\
        *engine['combustion']['phi']/3600.0
    # [kg/s]

# Inlet turbine temperature (for HW) | Температура перед турбиной
if 'HW' in run['type']:
    if D_2K < 0.3:
        T_0Stagn = 923.0
    elif (D_2K > 0.3) & (D_2K < 0.64):
        T_0Stagn = 823.0
    else:
        exit("\033[91mError 0: The diameter of the wheel is too big!")

# Outlet turbine pressure | Давление за турбиной
p_2 = turbine['losses']['dragInletRatio']*ambient['p']*1e+06 # [Pa]


# Radial turbine parameters
# ~~~~~~~~~~~~~~~~~~~~~~~~~
#1 Расход газа через турбину с учетом утечки
G_T = compressor['G_K']*turbine['efficiency']['sigma_esc']*(
    1 + 1/engine['combustion']['alpha']
         /engine['combustion']['phi']
         /engine['combustion']['l_0']
)

#2 Диаметр колеса турбины и окружная скорость на входе в колесо турбины
D_1 = turbine['geometry']['coefficients']['diameterRatio']*D_2K
u_1 = turbine['geometry']['coefficients']['diameterRatio']*u_2K

#4 Изоэнтропная работа турбины
L_TsStagn = L_KsStagn*compressor['G_K']/eta_KsStagnRated/turbine['efficiency']['eta_Te']/G_T

#5 Условная изоэнтропная скорость истечения из турбины
c_2s = math.sqrt( 2*L_TsStagn )

#6 Расчёт параметра ksi
ksi = u_1/c_2s
ksiLower = ksi_plot2func(0, D_2K)
ksiUpper = ksi_plot2func(1, D_2K)
if (ksi < ksiLower) | (ksi > ksiUpper):
    exit("\033[91mError 6: Parameter 'ksi' is not in the allowable diapason!\
 It equals %2.3f but must be from %0.2f to %1.3f."
        %(ksiLower, ksiUpper, ksi)
    )

#7 Давление газа на входе в турбину
p_0Stagn = p_2\
    /pow(
        1 - L_TsStagn/engine['exhaust']['c_p']/engine['heat']['T_0Stagn'],
        engine['exhaust']['k']/(engine['exhaust']['k'] - 1)
    )

#8 Проверка соотношения полного давления перед впускными клапанами поршневой
#  части и давлением газа на входе в турбину
pressureRelation = p_vStagn/p_0Stagn
if (pressureRelation < 1.1) | (pressureRelation > 1.3):
    exit("\033[91mError 8: Pressure ratio is not in the allowable diapason!\
        \nIt equals %0.2f but must be from 1.1 to 1.3.\
        \nScavenging cannot be happen."
        %pressureRelation
    )

#9 Наружный диаметр рабочего колеса турбины на выходе
D_2H = turbine['geometry']['coefficients']['outerDiamRatio']*D_1

#10 Внутренний (втулочный) диаметр колеса
D_2B = turbine['geometry']['coefficients']['innerDiamRatio']*D_1

#11 Средний диаметр колеса турбины на выходе
D_2 = math.sqrt((D_2B**2 + D_2H**2)/2)

#12 Вычисление параметра µ
mu = D_2/D_1
if (mu < 0.5) | (mu > 0.8): 
    exit("\033[91mError 12:\
 Geometeric parameter 'mu' is not in the allowable diapason! (It equals %0.2f)"
        %mu
    )

#15 Изоэнтропная работа расширения (располагаемый теплоперепад)
#   в сопловом аппарате
L_cS = L_TsStagn*(1 - turbine['efficiency']['rho'])

#17 Абсолютная скорость с1 на выходе из соплового аппарата
c_1 = turbine['losses']['phi']*math.sqrt( 2*L_cS )

#19 Радиальная составляющая абсолютной скорости (c_1r == w_1r)
c_1r = c_1*math.sin(math.radians( turbine['geometry']['alpha_1'] ))

#20 Окружная составляющая абсолютной скорости
#   на выходе из соплового аппарата
c_1u = c_1*math.cos(math.radians( turbine['geometry']['alpha_1'] ))

#21 Окружная составляющая относительной скорости
#   на выходе из соплового аппарата
w_1u = c_1u - u_1

#22 Относительная скорость на входе в рабочее колесо
w_1 = math.sqrt(c_1r**2 - w_1u**2)

#23 Значение угла β_1 наклона вектора относительной скорости w_1
beta_1 = turbine['geometry']['beta_1Blade'] - math.degrees(math.atan(w_1u/c_1r))
if (beta_1 < 80) | (beta_1 > 100):
    exit("\033[91mError 23: Angle 'beta_1' is not in the allowable diapason!\n\
        \nIt equals %0.1f but must be from 80 to 100 degrees."
        %beta_1
    )

#24 Температура газа на входе в колесо
T_1 = engine['heat']['T_0Stagn'] - c_1**2/2/engine['exhaust']['c_p']

#25 Давление на входе в колесо
p_1 = p_0Stagn\
    *pow(
        1 - L_cS/engine['exhaust']['c_p']/engine['heat']['T_0Stagn'],
        engine['exhaust']['k']/(engine['exhaust']['k'] - 1)
    )

#26 Плотность ρ_1 на входе в колесо
rho_1 = p_1/engine['exhaust']['R']/T_1

#27 Ширина лопаток b1 на входе в колесо
b_1 = G_T/math.pi/D_1/rho_1/c_1r

#28 Изоэнтропная работа расширения в рабочем колесе
#   (располагаемый теплоперепад) на входе в колесо
L_pS = turbine['efficiency']['rho']*L_TsStagn

#30 Окружная скорость на среднем диаметре D_2 выхода из рабочего колеса
u_2 = mu*u_1

#31 Относительная скорость на среднем диаметре D_2
w_2 = turbine['losses']['psi']\
    *math.sqrt(2*L_pS + w_1**2 - u_1**2 + u_2**2)

#32 Температура Т_2 на выходе из колеса
T_2 = T_1 - (
        (w_2**2 - u_2**2 - w_1**2 + u_1**2)\
        /2/engine['exhaust']['c_p']
    )

#33 Плотность на выходе из колеса
rho_2 = p_2/engine['exhaust']['R']/T_2

#34 Площадь сечения на выходе из колеса
F_2 = math.pi/4*(D_2H**2 - D_2B**2)

#35 Утечки через радиальный зазор Δ между корпусом и колесом турбины
G_losses = 0.45*2*turbine['geometry']['delta']*G_T/(D_2H - D_2B)\
    *(1 + (D_2H - D_2B)/2/D_2)

#36 Расход через сечение F_2 на выходе из колеса
G_F2 = G_T - G_losses

#37 Аксиальные составляющие относительной w_2а и
#   абсолютной с_2а скоростей на выходе из колеса (w_2a == c_2a)
w_2a = G_F2/F_2/rho_2

#38 Окружная составляющая относительной скорости на выходе из колеса
if (w_2**2 - w_2a**2) > 0:
    w_2u = math.sqrt(w_2**2 - w_2a**2)
else:
    exit("\033[91mError 38: Radicand is less then 0!\
        \nDifference between speeds is %0.3f m/s."
        %(w_2a - w_2)
    )

#39 Угол β_2 наклона вектора относительной скорости w2
#   на выходе из рабочего колеса
beta_2 = math.degrees(math.asin(w_2a/w_2))

#40 Окружная составляющая с2u абсолютной скорости на выходе из колеса
c_2u = w_2u - u_2

#41 Абсолютная скорость на выходе из колеса
c_2 = math.sqrt(w_2a**2 + c_2u**2) 

#42 Угол α_2 выхода потока из колеса в абсолютном движении
alpha_2 = 90 - math.degrees(math.atan( c_2u/w_2a ))
if (alpha_2 < 75) | (alpha_2 > 105):
    exit("\033[91mError 42: Angle 'alpha_2' is not in the allowable diapason!\
        \nIt equals %0.1f but must be from 75 to 105 degrees."
        %alpha_2
    )

#43 Потери в сопловом аппарате турбины
Z_c = (1/turbine['losses']['phi']**2 - 1)*c_1**2/2

#44 Потери в рабочем колесе
Z_p = (1/turbine['losses']['psi']**2 - 1)*w_2**2/2

#45 Суммарные потери в лопаточных каналах
Z_Blades = Z_c + Z_p

#46 Лопаточная работа турбины
L_TBlades = L_TsStagn - Z_Blades

#47 Лопаточный КПД η_(т.л) турбины
eta_TBlades = L_TBlades/L_TsStagn

#48 Потери в Z′_в с выходной скоростью при условии равномерного потока на
#   выходе из рабочего колеса
Z_SteadyOutlet = c_2**2/2

#49 Работа L′_тu на окружности колеса c учётом потерь
#   определёная через потери
L_TuSteadyFromLosses = L_TBlades - Z_SteadyOutlet

#50 Работа L′_тu на окружности колеса c учётом потерь
#   определёная с помощью формулы Эйлера
L_TuSteady = u_1*c_1u + u_2*c_2u

#51 Действительные потери Z_в с выходной скоростью
#   (для потока с неравномерностью на выходе)
Z_UnsteadyOutlet = turbine['efficiency']['dzeta']*Z_SteadyOutlet

#52 Действительная работа на окружности колеса
L_Tu = L_TBlades - Z_UnsteadyOutlet

#53 Окружной КПД η_тu турбины
eta_Tu = L_Tu/L_TsStagn
if (eta_Tu < 0.75) | (eta_Tu > 0.9):
    exit("\033[91mError 53: Angle 'eta_Tu' is not in the allowable diapason!\
        \nIt equals %0.3f but must be from 0.75 to 0.9."
        %eta_Tu
    )

#54 Потери Zу, обусловленные утечкой газа через радиальные зазоры
#   между колесом и корпусом
Z_y = L_Tu*G_losses/G_T

#55 Мощность N_тв, затрачиваемая на трение колеса в корпусе и вентиляцию
N_TB = 735.5*turbine['geometry']['coefficients']['beta']\
    *(rho_1 + rho_2)/2*D_1**2*pow(u_1/100, 3)

#56 Потери Z_тв на трение и вентиляцию
Z_TB = N_TB/G_T

#57 Суммарные дополнительные потери Z_д , включающие потери
#   на утечки,трение и вентиляцию
Z_extra = Z_y + Z_TB

#58 Внутренняя работа L_тi турбины
L_Ti = L_Tu - Z_extra

#59 Внутренний КПД η_тi турбины
eta_Ti = L_Ti/L_TsStagn

#60 Эффективный КПД η`_тe турбины
eta_TeRated = turbine['efficiency']['eta_m']*eta_Ti

#61 Расхождение с заданным КПД турбины
errorEta = (turbine['efficiency']['eta_Te'] - eta_TeRated)\
    /turbine['efficiency']['eta_Te']*100 # [%]

#62 Эффективная работа L_т е турбины
L_Te = eta_TeRated*L_TsStagn

#63 Мощность N_т на валу турбины
N_T = L_Te*G_T

#64 Расхождение с мощностью N_к, потребляемой компрессором
errorN = (N_K - N_T)/N_K*100 # [%]


# Display results
output(turbine, eta_TeRated, errorEta, N_K, N_T, errorN)


# Generate report
# ~~~~~~~~~~~~~~~
# Create a report
exec(compile(open('post/post_report.py', "rb").read(),
                  'post/post_report.py', 'exec'))
# Edit pictures
exec(compile(open('post/post_pictures.py', "rb").read(),
                  'post/post_pictures.py', 'exec'))
# Save the results to the results/ folder
exec(compile(open('post/post_results.py', "rb").read(),
                  'post/post_results.py', 'exec'))


# ''' (C) 2018-2020 Stanislau Stasheuski '''