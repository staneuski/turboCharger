# -*- coding: utf-8 -*-
# Common paramaters for all subprojects

## Type of project
## ~~~~~~~~~~~~~~~
projectType = "termPaper"; # "HW" - для Д/З, "termPaper" - для курсового проекта 


## Standart paramaters
## ~~~~~~~~~~~~~~~~~~~
p_a = 0.1013; # MPa, atmospheric pressure | атмосферное давление
T_a = 293; # К, temperature | температура
k = 1.4; # isentropy coefficient | коэффициент изоэнтропы
R = 287.2; # gas constant | газовая постоянная
c_p = 1005; # J/(kg*K), isobar heat capacity | изобарная теплоёмкость 


## Engine data | Данные ДВС
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
engineType = "DIESEL"; # type of the engine: "DIESEL" or "SI" | вид ДВС: для ВоС - "DIESEL", для ВЭИ - "SI"
strokeNumber = 4; # number of strokes | тактность ДВС
pistonNumber = 4; # piston number | число цилиндров
S = 8.8; # cm, piston stroke | ход поршня
D = 8.5; # cm, cylinder bore | диаметр цилиндра

N_e = 100; # kV, effective power | эффективная мощность
n = 4000; # 1/min, rated speed | номинальная частота вращения
g_e = 0.24; # kg/(kV*h), brake-specific fuel consumption | удельный эффективный расход топлива

# Combustion parameters | Параметры сгорания
alpha = 1.8; # excess of air coefficient | коэффициент избытка воздуха
eta_v = 0.963; # admission coefficient | коэффициент наполнения
phi = 1.025; # expulsion coefficient | коэффициент продувки


## Для Д/З
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pi_K = 1.9; # степень повышения давления в компрессоре
G_K = 0.25; # кг/с, расход через компрессор
