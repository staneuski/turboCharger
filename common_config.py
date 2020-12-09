'''
    Python:         3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           common_config
    Description:    Run and ambient paramaters
'''

project = dict(
    # Project type | Тип расчёта
    type = "TYPE1" # "TYPE1" - по параметрам двигателя
                   # "TYPE2" - по расходу и степени повышения давления
)

ambient = dict(
    # Atmospheric pressure | Атмосферное давление
    p = 0.1013, # [MPa]

    # Temperature | температура
    T = 293.0, # [К]
)


# ''' (C) 2018-2020 Stanislau Stasheuski '''