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

# -------------------------------- "TYPE2" ------------------------------------

# Расход через компрессор
G_K  = 4.5 # [kg/s] (для осевой турбины должен быть задан и при "TYPE2")

# Cтепень повышения давления в компрессоре
pi_K = 3.0


# ''' (C) 2018-2020 Stanislau Stasheuski '''