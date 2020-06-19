# -*- coding: utf-8 -*-
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           engineConfig
    Description:    Turbocharger's engine paramaters

'''

engine = dict(

    geometry = dict(
        # Piston number | Число цилиндров
        pistonNo = 4.0,

        # Piston stroke | Ход поршня
        stroke   = 8.8, # [cm]

        # Сylinder bore | Диаметр цилиндра
        bore     = 8.5, # [cm]
    ),

    # Effective parameters | Эффективные параметры
    efficiency = dict(
        # Engine speed | Номинальная частота вращения
        RPM = 4000.0, # [1/min]

        # Effective power | Эффективная мощность
        N_e = 100.0, # [kW]

        # Effective fuel consumption | Удельный эффективный расход топлива
        b_e = 0.24, # [kg/kW/h]
    ),

    # Combustion parameters | Параметры сгорания
    combustion = dict(
        # Engine type | Тип двигателя
        ignition  = 'CI', # 'CI' or 'SI' - compression or spark

        # Strokes number | Тактность
        strokeNo = 4.0,

        # Air excess coefficient | Коэффициент избытка воздуха
        alpha = 1.8,

        # Admission coefficient | Коэффициент наполнения
        eta_v = 0.963,

        # Expulsion coefficient | Коэффициент продувки
        phi   = 1.025,
    ),

    # Heat (transfer) paramaters
    heat = dict(
        # Heat efficiency coefficient | Коэффициент тепловой эффективности
        E        = 0.7, # 0.6…0.75

        # Coolant temperature | Температура охлаждающего агента (воды)
        T_ca     = 309.0, # [K]

        # Temperature of inlet turbine gases | Температура газов перед турбиной
        T_0Stagn = 874.0, # [K]
    ),

    # Exhaust gas parameters | Параметры выпускных газов
    exhaust = dict(
        # Isobar heat capacity | Изобарная теплоёмкость
        c_p         = 1128.7, # [J/kg/K]

        #p39 Gas constant | Газовая постоянная
        R          = 286.4, # [J/kg/K]

        #p39 Isentropy coefficient | Коэффициент изоэнтропы
        k          = 1.34,
    )
)


# ''' (C) 2018-2020 Stanislau Stasheuski '''