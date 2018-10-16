# -*- coding: utf-8 -*-
# Data for calculation

# Standart paramaters
p_a = 0.1013; # MPa, atmospheric pressure | атмосферное давление
T_a = 293; # К, temperature | температура
k = 1.4; # isentropy coefficient | коэффициент изоэнтропы
R = 287.2; # gas constant | газовая постоянная
c_p = 1005; # J/(kg*K), isobar heat capacity | изобарная теплоёмкость 

#  Engine data | Данные ДВС
engineType = "DIESEL"; # type of the engine: "DIESEL" or "SI" | вид ДВС: "DIESEL" для ВоС или "SI" для ВЭИ
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

# Stagnation (*) parameters for inlet
p_aStagn = p_a; # MPa, stagnation pressure | давление торможения
T_aStagn = T_a; # К, stagnation pressure | температура торможения
c_0 = 40; # m/s, intake speed | скорость на входе 

# Losses coefficients | Коэффициенты потерь
sigma_0 = 0.98; # | Коэффициент потерь полного давления
sigma_c = 0.985; # | Коэффициент потерь в охладителе
sigma_v = 0.992; # | Коэффициент потерь в коллекторе

# Energy conversion efficiency (ECE) & other coefficints | КПД и др. коэффициенты
# Set "0" when it is unknown | Если какой-либо параметр неизвестен принять его как "0"
eta_KsStagn = 0.74; # compressor energy conversion efficiency | КПД компрессора
H_KsStagn = 0.6; # | напорный изоэнтропный КПД
phi_flow = 0.3; # | коэффициент напора

# Other paramaters
E = 0.7; # heat efficiency coefficient | коэффициент тепловой эффективности
T_ca = 309; # K, coolant temperature | температура охлаждающего агента (воды)



# Тип проекта (для Д/З задать "HW")
proectType = 0; # "HW"


