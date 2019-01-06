# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# Dictionary
#     commonDict
#
# Description
#     Common paramaters for all subprojects for 0D calculation
# 
#-----------------------------------------------------------------------

## Type of project
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
projectType = "termPaper"; # "HW" - для Д/З, "termPaper" - для курсового проекта 


## Standart paramaters
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
p_a         = 0.1013; # MPa, atmospheric pressure | атмосферное давление
T_a         = 293; # К, temperature | температура
k           = 1.4; # isentropy coefficient | коэффициент изоэнтропы
R           = 287.2; #  J/(kg*K), gas constant | газовая постоянная
c_p         = 1005; # J/(kg*K), isobar heat capacity | изобарная теплоёмкость 


## Engine data | Данные ДВС
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
engineType  = "DIESEL"; # type of the engine: "DIESEL" or "SI" | вид ДВС: для ВоС - "DIESEL", для ВЭИ - "SI"
strokeNumber= 4; # number of strokes | тактность ДВС
pistonNumber= 4; # piston number | число цилиндров
S           = 8.8; # cm, piston stroke | ход поршня
D           = 8.5; # cm, cylinder bore | диаметр цилиндра

N_e         = 100; # kV, effective power | эффективная мощность
n           = 4000; # 1/min, rated speed | номинальная частота вращения
g_e         = 0.24; # kg/(kV*h), brake-specific fuel consumption | удельный эффективный расход топлива

# Combustion parameters | Параметры сгорания
alpha       = 1.8; # excess of air coefficient | коэффициент избытка воздуха
eta_v       = 0.963; # admission coefficient | коэффициент наполнения
phi         = 1.025; # expulsion coefficient | коэффициент продувки


## Other paramaters
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
E           = 0.7; # 0.6…0.75 - heat efficiency coefficient | коэффициент тепловой эффективности
T_ca        = 309; # K, coolant temperature | температура охлаждающего агента (воды)
T_0Stagn    = 874; # K temperature of inlet turbine gases | температура газов перед турбиной


## Для Д/З или расчёта осевой турбины!
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
G_K         = 3.4837; # кг/с, расход через компрессор (для расчёта осевой турбины должен быть задан!)
Pi_K        = 1.9; # степень повышения давления в компрессоре

