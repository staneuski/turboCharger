# -*- coding: utf-8 -*-
# '''
#     API:            Python 3.x
#     Project:        https://github.com/StasF1/turboCharger
#     Version:        2.x
#     License:        GNU General Public License 3.0 ( see LICENSE )
#     Author:         Stanislau Stasheuski
#
#     File:           commonConfig
#     Description:    Common paramaters for all subprojects for 0D calculation
#
# '''

# Тип расчёта
projectType = "TYPE1" # "TYPE1" - по параметрам двигателя
                      # "TYPE2" - по расходу и степени повышения давления

# -------------------------------- "TYPE2" ------------------------------------

# Расход через компрессор
G_K  = 3.4837 # [kg/s] (для осевой турбины должен быть задан и при "TYPE2")

# Cтепень повышения давления в компрессоре
Pi_K = 1.9

# -------------------------------- "TYPE1" ------------------------------------

# Standart (ambient) paramaters
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Atmospheric pressure  | Атмосферное давление
p_a = 0.1013 # [MPa]

# Temperature | температура
T_a = 293 # [К]

# Isentropy coefficient | Коэффициент изоэнтропы
k   = 1.4

# Gas constant | Газовая постоянная
R   = 287.2 # [J/kg/K]

# Isobar heat capacity | Изобарная теплоёмкость
c_p = 1005 # [J/kg/K]


# Engine data | Данные ДВС
# ~~~~~~~~~~~~~~~~~~~~~~~~
# Engine type | Тип двигателя
engineType  = "DIESEL" # "DIESEL" or "SI"

#- Engine gometric parameters
# Strokes number | Тактность
strokeNumber= 4

# Piston number | Число цилиндров
pistonNumber= 4

# Piston stroke | Ход поршня
S           = 8.8 # [cm]

# Сylinder bore | Даметр цилиндра
D           = 8.5 # [cm]

#- Effective parameters | Эффективные параметры
# Effective power | Эффективная мощность
N_e         = 100 # [kW]

# Effective speed | Номинальная частота вращения
n           = 4000 # [1/min]

# brake-specific fuel consumption | Удельный эффективный расход топлива
g_e         = 0.24 # [kg/kW/h]

#- Combustion parameters | Параметры сгорания
# Air excess coefficient | Коэффициент избытка воздуха
alpha       = 1.8

# Admission coefficient | Коэффициент наполнения
eta_v       = 0.963

# Expulsion coefficient | Коэффициент продувки
phi         = 1.025


# Other paramaters
# ~~~~~~~~~~~~~~~~
# Heat efficiency coefficient | Коэффициент тепловой эффективности
E        = 0.7 # 0.6…0.75

# Coolant temperature | Температура охлаждающего агента (воды)
T_ca     = 309 # [K]

# Temperature of inlet turbine gases | Температура газов перед турбиной
T_0Stagn = 874 # [K]


# ''' (C) 2018-2020 Stanislau Stasheuski '''