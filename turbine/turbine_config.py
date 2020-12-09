'''
    Python:         3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           turbine_config
    Description:    Radial turbine parameters
                    РК, рабочее колесо
                    СА, сопловой аппарат
'''
turbine = dict(

    type = "radial", # 'radial' or 'axial'

    # Energy conversion efficiency (ECE) & other coefficints
    # КПД и другие коэффициенты
    efficiency  = dict(
        #1 Коэффициент утечки
        # sigma_esc = 0.99, #0.9…0.99 {0.99}

        #3 Turbine energy conversion efficiency | КПД турбины
        # eta_Te = 0.73, #wght {0.73}, radial turbine
                         #0.7…0.85 {0.795}, axial turbine

        #5 Коэффициент утечки
        # ksi = 0.56, #0.5…0.65 (0.56}, axial turbine only

        #6|13 Cтепень реактивности
        # rho = 0.52, #0.45…0.55 {0.52}, radial turbine
                      #0.30…0.50 {0.38}, axial turbine

        #27 Коэффициент нагрузки соплового аппарата
        # c_u1 = 0.95, #0.85…1.05 {0.95}, axial turbine only

        #50 Коэффициент нагрузки рабочего колеса
        # c_u2 = 0.85, #0.8…0.9 {0.85}, axial turbine only

        #51 Коэффициент учитывающий неравномерность потока на выходе из РК
        # dzeta = 1.24, #1.1…1.5 {1.24}, radial turbine only

        #61|66 Механический КПД
        # eta_m = 0.94, #0.92…0.96 {0.94}
    ),

    # Geometric parameters | Параметры геометрии
    geometry = dict(
        #18|11 Угол α_1 наклона вектора абсолютной скорости с_1
        # alpha_1 = 0.0, #0…1 {0.0} [deg], radial turbine
                         #14…30 {16} [deg], axial turbine

        #23|16 Угол установки лопаток
        # beta_1Blade = 90.0, # {90} [deg]

        #35|38 Радиальный зазор Δ между корпусом и РК турбины
        # delta = 0.3, #0.3…1.5 {0.3} [mm], radial turbine
                       #0.7…1.5 {0.8} [mm], axial turbine

        # Geometric сoefficients | Коэффициенты геометрии
        coefficients = dict(
            #2 Отношение диаметров колеса турбины и компрессора
            # D_ratio = 1.0, #1.0…1.1 {1.0}, radial turbine only

            #9 Отношение диаметров РК турбины к её наружному диаметру
            # d_outer_ratio = 0.8, #wght {0.8}, radial turbine only

            #10 Отношение диаметров РК турбины к её внутреннему диаметру
            # d_inner_ratio = 0.95, #wght {0.95}, radial turbine only

            #22 Отношение шага решётки соплового аппарата к её высоте
            # t1Tol1 = 0.88, #0.8…0.9 {0.88}, axial turbine only

            #26 Коэффициент ширины решётки
            # m  = 1.08, # {1.08}, axial turbine only (for Ma=0.4…0.6)

            #45 Отношение шага решётки соплового аппарата к её высоте
            # t2Tol2 = 0.81, #0.8…0.9 {0.81}, axial turbine only

            #55|61 Опытный коэффициент, зависящий от типа РК
            # beta = 4.6, #3.5…5.0 {4.6}, radial turbine
                          # {2}, axial turbine
        )
    ),

    # Losses coeficients | Коэффициенты потерь
    losses = dict(
        # Коэффициент отношения давления на выходе из турбины к атмосферному
        # drag_inlet_ratio = 1.017, #1.01…1.1 {1.017}

        #16|10 Скоростной Коэффициент ϕ учитывающий потери скорости в СА
        # phi = 1.0, #wght {1}, radial turbine
                     #0.96…0.98 {0.97}, axial turbine

        #29 Cкоростной Коэффициент ψ учитывающий потери скорости в РК
        # psi = 0.96, #wght {0.96}, radial turbine
                      #0.92…0.98 {0.95}, axial turbine
    )
)


# ''' (C) 2018-2019 Stanislau Stasheuski '''