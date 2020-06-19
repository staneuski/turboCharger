# -*- coding: utf-8 -*-
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           compressorConfig

    Description:    Parameters of the compressor
        РК  - рабочее колесо
        ЛД  - лопаточный диффузор
        БЛД - безлопаточный диффузор
        НА  - направляющий аппарат
'''
from commonConfig import ambient
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

compressor = dict(

    type     = "radial",

    # Тип диффузора: БЛД ('VANELESS') или ЛД ('VANED')
    diffuser = 'VANELESS', # 'VANELESS' or ='VANED'

    # Расход через компрессор ['TYPE2']
    G_K      = 4.5, # [kg/s] (для осевой турбины должен быть задан)

    # Cтепень повышения давления в компрессоре ['TYPE2']
    pi_K     = 3.0,

    # Initial parameters | Начальные параметры
    initial = dict(
        #- Inlet gas parameters | Параматры газа на входе
        #0 Stagnation pressure | давление торможения
        p_aStagn    = ambient['p'], # [MPa]

        #0 Stagnation pressure | температура торможения
        T_aStagn    = ambient['T'], # [К]

        #0 Intake speed | скорость на входе
        c_0         = 'DEFAULT', # [m/s] {40}
    ),

    # Efficiency parameters | Параметры эффективности
    efficiency = dict(
        #5 Напорный изоэнтропный КПД
        H_KsStagn   = 'DEFAULT', #wght {0.4}

        #6 Коэффициент напора
        phi_flow    = 'DEFAULT', #wght {0.4}

        #15 КПД компрессора (для 'TYPE2')
        eta_KsStagn = 'DEFAULT', #wght {0.6}

        #46 Политропный КПД диффузора
        eta_diff    = 'DEFAULT', #0.55…0.78 {0.75}
    ),

    # Geometric parameters
    geometry = dict(
        # 'EQV' предварительная оценка диаметра по формуле
        # (для компрессоров с небольшим расходом и D_2 <= 24см)
        # <00> - задание предварительной оценки диаметра явно (в см)
        estimD_2       = 'EQV', # 'EQV' / <int> [cm] (2.25)

        #0 Угол лопаток на выходе из рабочего колеса
        beta_2Blade = 'DEFAULT', #55…75 {75}

        #20 Угол атаки на входе в РК
        iDeg                = 3.913, #2…6 [deg]

        #30 Количество лопаток РК
        z_K                 = 12, #9…40

        #F50 Уоличество лопаток ЛД - 'VANELESS'
        z_diffuser          = 13, #7…35

        #F49 Разница в наклоне лопоток на выходе из ЛД и РК 'VANELESS' 
        deltaDiffuser       = 'DEFAULT', # 10…15 [deg] {14}

        # Geometric coefficients | Коэффициенты геометрии
        coefficients = dict(
            #- Параметр округления диаметра РК
            DToSTD = 'OFF', # 'OFF' округление диаметра до целых [см]
                            # или до величины кратной 5 [мм] при D<85 [мм]
                            # 'ON' округление диаметра до ряда стандартных значений

            #13 Diameter coefficients | Коэффициенты диаметра
            relD_1H             = 'DEFAULT', #wght {0.6}
            relD_1B             = 'DEFAULT', #wght {0.55}

            #27 Отношение w_2r к с_1a (27)
            relW_2rToC_1a       = 'DEFAULT', #wght {0.6}

            #44 Отношение ширины (безлопаточной части) диффузора на входе и выходе
            vanelessWideCoef    = 'DEFAULT', #0.7…1.0 {0.9} 'VANED' / 0.95…1 {1} 'VANELESS'

            #45 Отношение диаметра (безлопаточной части) диффузора на входе и выходе
            vanelessDiamCoef    = 'DEFAULT', #1.6…1.9 {1.8}'VANED' / 1.05…1.2 {1.14}'VANELESS'

            #51 Отношение скорости на выходе из компрессора
            #   к скорости на выходе из диффузора
            relDiffOutToCompOut = 'DEFAULT', #1.3…1.4 {1.4}

            #F47 Отношение диаметра лопаточной части ЛД на входе и выходе ('VANED')
            vanedDiamCoef       = 'DEFAULT', #1.35…1.7 {1.6}

            #F48 Отношение ширины лопаточной части ЛД на входе и выходе ('VANED')
            vanedWideCoef       = 'DEFAULT', #1…1.3 {1}
        )
    ),

    # Losses coeficients | Коэффициенты потерь
    losses = dict(
        #0 Коэффициент потерь полного давления
        sigma_0     = 0.980, #0 0.96…0.985 {0.98}

        #0 Коэффициент потерь в охладителе
        sigma_c     = 0.985, #0 {0.985}

        #0 Коэффициент потерь в коллекторе
        sigma_v     = 0.992, #0 {0.992}

        #8 Коэффициент сопротивления
        dzeta_inlet = 'DEFAULT', #0.03…0.06 {0.04}

        #26 Коэффициент потерь в НА
        dzeta_BA    = 'DEFAULT', #0.1…0.3 {0.26}

        #28 Коэффициент потерь на трение в межлопаточных каналах
        dzeta_TF    = 'DEFAULT', #0.1…0.2 {0.18}

        #29 Коэффициент дисковых потерь
        alpha_wh    = 'DEFAULT', #0.04…0.08 {0.05}

        #F51 Показатель политропы сжатия в ЛД ('VANED')
        n_diffuser  = 'DEFAULT', #1.5…1.8 {1.55}

        #53 Показатель политропы сжатия в воздухосборнике/улитке
        n_housing   = 'DEFAULT', #1.85…2.2 {1.9}
    ),

    # Load factors | Коэффициенты загромождения
    load = dict(
        #21 Коэффициент загромождения на входе в РК
        tau_1 = 'DEFAULT', #0.8…0.9 {0.9}

        #42 Коэффициент загромождения на выходе из РК
        tau_2 = 'DEFAULT', #0.92…0.96 {0.94}

        #21 Коэффициент загромождения на входе в ЛД
        tau_3 = 'DEFAULT', #0.95…0.97 {0.96}

        #42 Коэффициент загромождения на выходе из ЛД
        tau_4 = 'DEFAULT', #0.96…0.98 {0.965}
    ),
)


# ''' (C) 2018-2020 Stanislau Stasheuski '''