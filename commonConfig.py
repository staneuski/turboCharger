# -*- coding: utf-8 -*-
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           commonConfig
    Description:    Common paramaters for all subprojects for 0D calculation

'''

# Project type | Тип расчёта
projectType = "TYPE1" # "TYPE1" - по параметрам двигателя
                      # "TYPE2" - по расходу и степени повышения давления

# Atmospheric pressure  | Атмосферное давление
p_a = 0.1013 # [MPa]

# Temperature | температура
T_a = 293 # [К]

# Isentropy coefficient | Коэффициент изоэнтропы
k   = 1.4

# Gas constant | Газовая постоянная
R   = 287.2 # [J/kg/K]

# Isobar heat capacity | Изобарная теплоёмкость
c_p = 1005.0 # [J/kg/K]

# -------------------------------- "TYPE1" ------------------------------------

# Engine data | Данные ДВС
engine = dict(
    # Engine type | Тип двигателя
    type  = 'DIESEL', # 'DIESEL' or 'SI'

    #- Engine gometric parameters
    # Strokes number | Тактность
    strokeNo = 4.0,

    # Piston number | Число цилиндров
    pistonNo = 4.0,

    # Piston stroke | Ход поршня
    stroke   = 8.8, # [cm]

    # Сylinder bore | Диаметр цилиндра
    bore     = 8.5, # [cm]

    # Engine speed | Номинальная частота вращения
    RPM = 4000.0, # [1/min]

    #- Effective parameters | Эффективные параметры
    efficiency = dict(
        # Effective power | Эффективная мощность
        N_e = 100.0, # [kW]

        # Effective fuel consumption | Удельный эффективный расход топлива
        b_e = 0.24, # [kg/kW/h]
    ),

    #- Combustion parameters | Параметры сгорания
    combustion = dict(
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
)


# -------------------------------- "TYPE2" ------------------------------------

# Расход через компрессор
G_K  = 4.5 # [kg/s] (для осевой турбины должен быть задан и при "TYPE2")

# Cтепень повышения давления в компрессоре
pi_K = 3.0


# ''' (C) 2018-2020 Stanislau Stasheuski '''