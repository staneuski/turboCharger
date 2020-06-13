# -*- coding: utf-8 -*-
# '''
#     API:            Python 3.x
#     Project:        https://github.com/StasF1/turboCharger
#     Version:        2.x
#     License:        GNU General Public License 3.0 ( see LICENSE )
#     Author:         Stanislau Stasheuski
#
#     File:           compressorDict
#
#     Description:    Parameters of the compressor
#         РК  - рабочее колесо
#         ЛД  - лопаточный диффузор
#         БЛД - безлопаточный диффузор
#         НА  - направляющий аппарат
#
# '''
# Stagnation (*) parameters for inlet & loading input data from project dictionary 
import sys
from os import path;\
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from commonDict import(p_a, T_a)
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Настройки расчёта
# ~~~~~~~~~~~~~~~~~
#- Параметр округления диаметра РК
roundDiamToSTD = 'OFF' # 'OFF' округление диаметра до целых [см]
                       # или до величины кратной 5 [мм] при D<85 [мм]
                       # 'ON' округление диаметра до ряда стандартных значений

#- Тип диффузора: БЛД ('VANELESS') или ЛД ('VANED')
diffuserType   = 'VANELESS' # 'VANELESS' or ='VANED'

# 'EQV' предварительная оценка диаметра по формуле
# (для компрессоров с небольшим расходом и D_2 <= 24см)
# <00> - задание предварительной оценки диаметра явно (в см)
estimD_2       = 'EQV' # 'EQV' / <int> [cm] (2.25)


# Initial parameters | Начальные параметры
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#0 Угол лопаток на выходе из рабочего колеса (компрессор с лопатками
#  отогнутыми назад)
beta_2Blade = 'DEFAULT' #55…75 {75}

#- Inlet gas parameters | Параматры газа на входе
#0 Stagnation pressure | давление торможения
p_aStagn    = p_a # [MPa]

#0 Stagnation pressure | температура торможения
T_aStagn    = T_a # [К]

#0 Intake speed | скорость на входе 
c_0         = 'DEFAULT' # [m/s] {40}

#- Losses coefficients | Коэффициенты потерь
#0 Коэффициент потерь полного давления
sigma_0     = 0.980 #0 0.96…0.985 {0.98}

#0 Коэффициент потерь в охладителе
sigma_c     = 0.985 #0 {0.985}

#0 Коэффициент потерь в коллекторе
sigma_v     = 0.992 #0 {0.992}


# Efficiency parameters | Параметры эффективности
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#5 Напорный изоэнтропный КПД
H_KsStagn   = 'DEFAULT' #wght {0.4}

#6 Коэффициент напора
phi_flow    = 'DEFAULT' #wght {0.4}

#15 КПД компрессора (для 'TYPE2')
eta_KsStagn = 'DEFAULT' #wght {0.6}

#46 Политропный КПД диффузора
eta_diff    = 'DEFAULT' #0.55…0.78 {0.75}


# Geometric parameters
# ~~~~~~~~~~~~~~~~~~~~
#20 Угол атаки на входе в РК
iDeg                = 3.913 #2…6 [deg]

#30 Количество лопаток РК
z_K                 = 12 #9…40

#F50 Уоличество лопаток ЛД - 'VANELESS'
z_diffuser          = 13 #7…35

#F49 Разница в наклоне лопоток на выходе из ЛД и РК 'VANELESS' 
deltaDegDiff        = 'DEFAULT' # 10…15 [deg] {14}

#- Geometric coefficients | Коэффициенты геометрии
#13 Diameter coefficients | Коэффициенты диаметра
relD_1H             = 'DEFAULT' #wght {0.6}
relD_1B             = 'DEFAULT' #wght {0.55}

#27 Отношение w_2r к с_1a (27)
relW_2rToC_1a       = 'DEFAULT' #wght {0.6}

#44 Отношение ширины (безлопаточной части) диффузора на входе и выходе
vanelessWideCoef    = 'DEFAULT' #0.7…1.0 {0.9} 'VANED'/0.95…1 {1} 'VANELESS'

#45 Отношение диаметра (безлопаточной части) диффузора на входе и выходе
vanelessDiamCoef    = 'DEFAULT' #1.6…1.9 {1.8}'VANED'/ 1.05…1.2 {1.14}'VANELESS'

#51 Отношение скорости на выходе из компрессора
#   к скорости на выходе из диффузора
relDiffOutToCompOut = 'DEFAULT' #1.3…1.4 {1.4}

#F47 Отношение диаметра лопаточной части ЛД на входе и выходе ('VANED')
vanedDiamCoef       = 'DEFAULT' #1.35…1.7 {1.6}

#F48 Отношение ширины лопаточной части ЛД на входе и выходе ('VANED')
vanedWideCoef       = 'DEFAULT' #1…1.3 {1}


# Loses coeficients | Коэффициенты потерь
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#8 Коэффициент сопротивления
dzeta_inlet = 'DEFAULT' #0.03…0.06 {0.04}

#26 Коэффициент потерь в НА
dzeta_BA    = 'DEFAULT' #0.1…0.3 {0.26}

#28 Коэффициент потерь на трение в межлопаточных каналах
dzeta_TF    = 'DEFAULT' #0.1…0.2 {0.18}

#29 Коэффициент дисковых потерь
alpha_wh    = 'DEFAULT' #0.04…0.08 {0.05}

#F51 Показатель политропы сжатия в ЛД ('VANED')
n_diffuser  = 'DEFAULT' #1.5…1.8 {1.55}

#53 Показатель политропы сжатия в воздухосборнике/улитке
n_housing   = 'DEFAULT' #1.85…2.2 {1.9}


# Load factors | Коэффициенты загромождения
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#21 Коэффициент загромождения на входе в РК
tau_1 = 'DEFAULT' #0.8…0.9 {0.9}

#42 Коэффициент загромождения на выходе из РК
tau_2 = 'DEFAULT' #0.92…0.96 {0.94}

#21 Коэффициент загромождения на входе в ЛД
tau_3 = 'DEFAULT' #0.95…0.97 {0.96}

#42 Коэффициент загромождения на выходе из ЛД
tau_4 = 'DEFAULT' #0.96…0.98 {0.965}


# ''' (C) 2018-2020 Stanislau Stasheuski '''