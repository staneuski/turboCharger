# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# Dictionary
#     turbineDict
#
# Description
#     Parameters of the radial turbine
#     РК - рабочее колесо
#     СА - сопловой аппарат
# 
#-----------------------------------------------------------------------

## Exhaust gas parameters
R_Exh          = 286.4 #J/(kg*K), gas constant|газовая постоянная (c39)
c_pExh         = 1128.7 #J/(kg*K), isobar heat capacity|изобарная теплоёмкость (c39)
k_Exh          = 1.34 #isentropy coefficient|коэф. изоэнтропы (c39)
dragInletRatio = 'DEFAULT' #1.01…1.1 (1.017 dflt)|коэф. отношения давления на выходе из турбины к атмосферному (c40)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Energy conversion efficiency (ECE) & other coefficints|КПД и др. коэффициенты
sigma_esc   = 'DEFAULT' #0.9…0.99 (0.99 dflt)|коэф. утечки (1)
eta_Te      = 'DEFAULT' #wght(0.8 dflt) turbine energy conversion efficiency|КПД турбины (3)
ro          = 'DEFAULT' #0.45…0.55 (0.52 dflt)|степень реактивности (13)
phiLosses   = 'DEFAULT' #wght(1 dflt)|скоростной коэф. ϕ, учитывающий потери скорости в СА (16)
psiLosses   = 'DEFAULT' #wght(0.96 dflt)|скоростной коэф. ψ, учитывающий потери скорости в РК (29)
dzeta       = 'DEFAULT' #1.1…1.5 (1.3 dflt)|коэф., учитывающий неравномерность потока на выходе из РК (51)
eta_m       = 'DEFAULT' #0.92…0.96 (0.94 dflt)|механический КПД (60)

# Geometric parameters|Параметры геометрии
alpha_1     = 'DEFAULT' #deg,0…1 (0 dflt)|угол α_1 наклона вектора абсолютной скорости с_1 (18)
beta_1Blade = 'DEFAULT' #deg,(90 dflt)|угол установки лопаток (23)
delta       = 'DEFAULT' #mm,0.3…1.5 (0.3 dflt)|радиальный зазор Δ между корпусом и РК (35)

# Geometric сoefficients|Коэффициенты геометрии 
diameterRatio  = 'DEFAULT' #1.0…1.1 (1.0 dflt)|отношение диаметров колеса турбины и компрессора (2)
outerDiamRatio = 'DEFAULT' #wght(0.8 dflt)|отношение диаметров РК турбины к её наружному диаметру (9)
innerDiamRatio = 'DEFAULT' #wght(0.95 dflt)|отношение диаметров РК турбины к её внутреннему диаметру (10)
beta           = 'DEFAULT' #3.5…5.0 (4.6 dflt)|опытный коэф., зависящий от типа РК (55)

