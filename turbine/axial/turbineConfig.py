# -*- coding: utf-8 -*-
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           turbineConfig
    Description:    Parameters of the axial turbine
                    РК - рабочее колесо
                    СА - сопловой аппарат
'''
turbine = dict(

    type = "axial",

    # Energy conversion efficiency (ECE) & other coefficints
    # КПД и другие коэффициенты
    efficiency  = dict(
        #1 Коэффициент утечки
        sigma_esc = 'DEFAULT', #0.9…0.99 {0.99}

        #3 КПД турбины
        eta_Te    = 'DEFAULT', #0.7…0.85 {0.795}

        #5 Коэффициент утечки
        ksi       = 'DEFAULT', #0.5…0.65 (0.56}

        #6 Степень реактивности
        rho       = 'DEFAULT', #0.3…0.5 {0.38}

        #27 Коэффициент нагрузки соплового аппарата
        c_u1      = 'DEFAULT', #0.85…1.05 {0.95}

        #50 Коэффициент нагрузки рабочего колеса
        c_u2      = 'DEFAULT', #0.8…0.9 {0.85}

        #66 Механический КПД
        eta_m     = 'DEFAULT', #0.92…0.96 {0.94}
    ),

    # Geometric parameters | Параметры геометрии
    geometry = dict(
        #11 Угол α_1 наклона вектора абсолютной скорости с_1
        alpha_1     = 'DEFAULT', #14…30 {16} [deg]

        #16 Угол установки лопаток
        beta_1Blade = 'DEFAULT', # {90} [deg]

        #27 Угол входа потока (!)
        alpha_0     = 'DEFAULT', # {90} [deg]

        #38 Радиальный зазор Δ между корпусом и РК турбины
        delta       = 'DEFAULT', #0.7…1.5 {0.8} [mm]

        # Geometric сoefficients | Коэффициенты геометрии
        coefficients = dict(
            #22 Отношение шага решётки соплового аппарата к её высоте
            t1Tol1 = 'DEFAULT', #0.8…0.9 {0.88}

            #26 Коэффициент ширины решётки (необходим только при числах Маха 0.4…0.6)
            m      = 'DEFAULT', # {1.08}

            #45 Отношение шага решётки соплового аппарата к её высоте
            t2Tol2 = 'DEFAULT', #0.8…0.9 {0.81}

            #61 Опытный коэффициент зависящий от типа рабочего колеса
            beta   = 'DEFAULT', # {2}
        )
    ),

    # Losses coeficients | Коэффициенты потерь
    losses = dict(
        #p40 Коэффициент отношения давления на выходе из турбины к атмосферному
        dragInletRatio = 'DEFAULT', #1.01…1.1 {1.017}

        #10 Скоростной Коэффициент ϕ, учитывающий потери скорости в СА
        phi = 'DEFAULT', #0.96…0.98 {0.97}

        #30 Скоростной Коэффициент ψ, учитывающий потери скорости в РК
        psi = 'DEFAULT', #0.92…0.98 {0.95}
    ),
)


# ''' (C) 2018-2019 Stanislau Stasheuski '''