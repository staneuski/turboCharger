# -*- coding: utf-8 -*-
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           turbineConfig
    Description:    Radial turbine parameters
                    РК - рабочее колесо
                    СА - сопловой аппарат
'''
turbine = dict(

    type = "radial",

    # Energy conversion efficiency (ECE) & other coefficints
    # КПД и другие коэффициенты
    efficiency  = dict(
        #1 Коэффициент утечки
        sigma_esc = 'DEFAULT', #0.9…0.99 {0.99}

        #3 Turbine energy conversion efficiency | КПД турбины
        eta_Te    = 'DEFAULT', #wght {0.73}

        #13 Cтепень реактивности
        rho       = 'DEFAULT', #0.45…0.55 {0.52}

        #51 Коэффициент учитывающий неравномерность потока на выходе из РК
        dzeta     = 'DEFAULT', #1.1…1.5 {1.24}

        #61 Механический КПД (60)
        eta_m     = 'DEFAULT', #0.92…0.96 {0.94}
    ),

    # Geometric parameters | Параметры геометрии
    geometry = dict(
        #18 Угол α_1 наклона вектора абсолютной скорости с_1
        alpha_1     = 'DEFAULT', #0…1 {0} [deg]

        #23 угол установки лопаток
        beta_1Blade = 'DEFAULT', # {90} [deg]

        #35 Радиальный зазор Δ между корпусом и РК
        delta       = 'DEFAULT', #0.3…1.5 {0.3} [mm]

        # Geometric сoefficients | Коэффициенты геометрии
        coefficients = dict(
            #2 Отношение диаметров колеса турбины и компрессора
            diameterRatio  = 'DEFAULT', #1.0…1.1 {1.0}

            #9 Отношение диаметров РК турбины к её наружному диаметру
            outerDiamRatio = 'DEFAULT', #wght {0.8}

            #10 Отношение диаметров РК турбины к её внутреннему диаметру
            innerDiamRatio = 'DEFAULT', #wght {0.95}

            #55 Опытный коэффициент, зависящий от типа РК
            beta           = 'DEFAULT', #3.5…5.0 {4.6}
        )
    ),

    # Losses coeficients | Коэффициенты потерь
    losses = dict(
        #p40 Коэффициент отношения давления на выходе из турбины к атмосферному
        dragInletRatio = 'DEFAULT', #1.01…1.1 {1.017}

        #16 Скоростной Коэффициент ϕ учитывающий потери скорости в СА
        phi = 'DEFAULT', #wght {1}

        #29 Cкоростной Коэффициент ψ учитывающий потери скорости в РК
        psi = 'DEFAULT', #wght {0.96}
    )
)


# ''' (C) 2018-2019 Stanislau Stasheuski '''