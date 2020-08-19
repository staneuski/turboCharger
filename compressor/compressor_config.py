'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           compressor_config

    Description:    Parameters of the compressor
        РК  - рабочее колесо
        ЛД  - лопаточный диффузор
        БЛД - безлопаточный диффузор
        НА  - направляющий аппарат
'''
# from common_config import ambient
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

compressor = dict(

    type = "radial",

    # Diffuser type
    # Тип диффузора (лопаточный или безлопаточный)
    # diffuser = 'VANED', #'VANELESS' or 'VANED' {'VANELESS'}

    # Расход через компрессор ['TYPE2']
    G = 4.5, # [kg/s], for project['type'] == 'TYPE2' only or for axial turbine

    # Cтепень повышения давления в компрессоре
    pi = 3.0, # for project['type'] == 'TYPE2' only

    # Initial parameters | Начальные параметры
    initial = dict(
        #- Inlet gas parameters | Параматры газа на входе
        #0 Stagnation pressure | давление торможения
        # p_aStagn = ambient['p'], # [Pa]

        #0 Stagnation pressure | температура торможения
        # T_aStagn = ambient['T'], # [К]

        #0 Intake speed | скорость на входе
        # c_0 = 40.0, # [m/s] {40.0}
    ),

    # Efficiency parameters | Параметры эффективности
    efficiency = dict(
        #5 Напорный изоэнтропный КПД
        # H_KsStagn = 0.4, #wght {0.4}

        #6 Коэффициент напора
        # phi_flow = 0.6, #wght {0.4}

        #15 КПД компрессора
        # eta_KsStagn = 0.1, #wght {0.6} for project['type'] == 'TYPE2' only

        #46 Политропный КПД диффузора
        # eta_diffuser = 0.75, #0.55…0.78 {0.75}
    ),

    # Geometric parameters
    geometry = dict(
        # 'EQV' предварительная оценка диаметра по формуле
        # (для компрессоров с небольшим расходом и D_2 <= 24см)
        # <00> - задание предварительной оценки диаметра явно (в см)
        estimD_2 = 'EQV', # 'EQV' / <int> [cm] (2.25)

        #0 Угол лопаток на выходе из рабочего колеса
        # beta_2Blade = 75, #55…75 {75}

        #20 Угол атаки на входе в РК
        iDeg = 3.913, #2…6 [deg]

        #30 Количество лопаток РК
        blades = 12, #9…40

        #F50 Уоличество лопаток ЛД
        blades_diffuser = 13, #7…35, for vaneless diffuser

        #F49 Разница в наклоне лопоток на выходе из ЛД и РК
        # deltaDiffuser = 14.0, # 10…15 [deg] {14}, for vaneless diffuser only

        # Geometric coefficients | Коэффициенты геометрии
        coefficients = dict(
            #- Параметр округления диаметра РК
            DToSTD = 'OFF', # 'OFF' округление диаметра до целых [см]
                            #  или до величины кратной 5 [мм] при D<85 [мм]
                            # 'ON' округление диаметра до ряда
                            #  стандартных значений

            #13 Diameter coefficients | Коэффициенты диаметра
            # D_1Down_relative = 0.6, #wght {0.6}
            # D_1Up_relative = 0.55, #wght {0.55}

            #27 Отношение w_2r к с_1a (27)
            # w2r_c1a_ratio = 0.6, #wght {0.6}

            diffuser = dict(
                #44 Отношение ширины (безлопаточной части)
                #   диффузора на входе и выходе
                # vaneless_wide = 1.0, #0.95…1.0 {1.0}, for vaneless diffuser
                                       #0.70…1.0 {0.9}, for vaned diffuser

                #45 Отношение диаметра (безлопаточной части)
                #   диффузора на входе и выходе
                # vaneless_diam = 1.12, #1.05…1.2 {1.14}, for vaneless diffuser
                                        #1.6…1.9  {1.8}, for vaned diffuser

                #51 Отношение скорости на выходе из компрессора
                #   к скорости на выходе из диффузора
                # c_out_ratio = 1.4, #1.3…1.4 {1.4}

                #F47 Отношение диаметра лопаточной части ЛД
                #    на входе и выходе
                # vaned_diam = 1.6, #1.35…1.7 {1.6}, for vaned diffuser only

                #F48 Отношение ширины лопаточной части ЛД
                #    на входе и выходе
                # vaned_wide = 1.0, #1.0…1.3 {1.0}, for vaned diffuser only
            ),
        ),
    ),

    # Losses coeficients | Коэффициенты потерь
    losses = dict(
        # Коэффициент потерь полного давления
        # sigma_0 = 0.980, #0 0.96…0.985 {0.98}

        # Коэффициент потерь в охладителе
        # sigma_c = 0.985, #0 {0.985}

        # Коэффициент потерь в коллекторе
        # sigma_v = 0.992, #0 {0.992}

        #8 Коэффициент сопротивления
        # dzeta_inlet = 0.04, #0.03…0.06 {0.04}

        #26 Коэффициент потерь в НА
        # dzeta_BA = 0.26, #0.1…0.3 {0.26}

        #28 Коэффициент потерь на трение в межлопаточных каналах
        # dzeta_TF = 0.18, #0.1…0.2 {0.18}

        #29 Коэффициент дисковых потерь
        # alpha_wh = 0.05, #0.04…0.08 {0.05}

        #F51 Показатель политропы сжатия в ЛД
        # n_diffuser = 1.55, #1.5…1.8 {1.55}, for vaned diffuser only

        #53 Показатель политропы сжатия в воздухосборнике/улитке
        # n_housing = 1.9, #1.85…2.2 {1.9}
    ),

    # Load factors | Коэффициенты загромождения
    load = dict(
        #21 Коэффициент загромождения на входе в РК
        # tau_1 = 0.9, #0.8…0.9 {0.9}

        #42 Коэффициент загромождения на выходе из РК
        # tau_2 = 0.94, #0.92…0.96 {0.94}

        #21 Коэффициент загромождения на входе в ЛД
        # tau_3 = 0.96, #0.95…0.97

        #42 Коэффициент загромождения на выходе из ЛД
        # tau_4 = 0.965, #0.96…0.98 {0.965}
    ),
)


# ''' (C) 2018-2020 Stanislau Stasheuski '''