# -*- coding: utf-8 -*-

## Exhaust gas parameters
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
R_Exh = 286.4; # J/(kg*K), gas constant | газовая постоянная
c_pExh = 1128.7; # J/(kg*K), isobar heat capacity | изобарная теплоёмкость
k_Exh = 1.34; # isentropy coefficient | коэффициент изоэнтропы
dragInletRatio = "DEFAULT"; # 1.01…1.1 (1.017 - default) | коэффициент отношения давления на выходе из турбины к атмосферному давлению


## Turbine parameters
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Energy conversion efficiency (ECE) & other coefficints | КПД и др. коэффициенты
eta_Te = 0.69; # turbine energy conversion efficiency | КПД турбины (3)
sigma_esc = "DEFAULT"; # 0.9…0.99 (0.99 - default) | коэффициент утечки (1)
ro = "DEFAULT"; # 0.45…0.55 (0.52 - default) | степень реактивности (13)
phiLosses = "DEFAULT" # 0.93…0.97 (0.97 - default) | скоростной коэффициент ϕ, учитывающий потери скорости в сопловом аппарате (16)
psiLosses = "DEFAULT" # 0.85…0.94 (0.87 - default) | скоростной коэффициент ψ, учитывающий потери скорости в рабочем колесе (29)
dzeta = "DEFAULT" # 1.3…1.5 (1.3 - default) | коэффициент, учитывающий неравномерность потока на выходе из рабочего колеса (51)
eta_m = "DEFAULT" # 0.92…0.96 (0.94 - default) | механический КПД (60)

# Geometric parameters
diameterRatio = "DEFAULT"; # 1.0…1.1 (1.0 - default) | отношение диаметров колеса турбины и компрессора (2)
outerDiamRatio = "DEFAULT" # 0.7…0.85 (0.85 - default) | отношение диаметров колеса турбины к её наружному диаметру (9)
innerDiamRatio = "DEFAULT" # 0.25…0.32 (0.31 - default) | отношение диаметров колеса турбины к её внутреннему диаметру (10)
alpha_1 = "DEFAULT" # deg, 15…25 (16 - default) | угол α_1 наклона вектора абсолютной скорости с_1 (18)
beta_1Blade = "DEFAULT" # deg, (90 - default) | угол установки лопаток (23)
delta = "DEFAULT" # mm, 0.3…1.5 (0.3 - default) | радиальный зазор Δ между корпусом и колесом турбины (35)
beta = "DEFAULT" # 3.5…5.0 (4.6 - default) | опытный коэффициент, зависящий от типа рабочего колеса



# Stagnation (*) parameters for inlet
T_0Stagn = 874; # K | температура газов перед турбиной





