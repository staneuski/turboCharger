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

ambient = dict(
    # Atmospheric pressure  | Атмосферное давление
    p = 0.1013, # [MPa]

    # Temperature | температура
    T = 293.0, # [К]
)

# Isentropy coefficient | Коэффициент изоэнтропы
k   = 1.4

# Gas constant | Газовая постоянная
R   = 287.2 # [J/kg/K]

# Isobar heat capacity | Изобарная теплоёмкость
c_p = 1005.0 # [J/kg/K]


# ''' (C) 2018-2020 Stanislau Stasheuski '''