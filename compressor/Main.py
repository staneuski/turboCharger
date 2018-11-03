#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calculates safety factors for crankshaft and displays the minimum of them

## Loading data & calling some fuctions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Funcion for math solvers (pi, sin, cos, etc.)
from __future__ import division;    import math
import PIL;             from PIL    import ImageFont, Image, ImageDraw

# Some self-made fuctions
from piK import piK
from diffOutTemp import diffOutTemp
from standardisedSize import standardisedSize
import sys; from os import path;
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from defaultValue import defaultValue

# Loading input data from project dictionary
import sys;    from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from commonDict import(
    projectType,
    p_a, T_a, k, R, c_p,
    engineType, strokeNumber, pistonNumber, S, D,
    N_e, n, g_e,
    alpha, eta_v, phi,
    Pi_K, G_K
)

from compressorDict import(
    T_aStagn, p_aStagn, c_0,
    sigma_0, sigma_c, sigma_v,
    eta_KsStagn, H_KsStagn, phi_flow, eta_diff,
    dzeta_inlet, dzeta_BA, dzeta_TF, alpha_wh,
    relD_1H, relD_1B, relW_2rToC_1a, diffuserWideCoef, diffuserDiamCoef,
      relDiffOutToCompOut, n_housing,
    iDeg, z_K, tau_1, tau_2, beta_2Blade,
)


## Converting data to SI from dictionary | Перевод в СИ
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N_e = N_e*1e03; # -> V
g_e = g_e*1e-03; # -> kg/(V*h) or g/(kV*h)
p_aStagn = p_aStagn*1e06; # -> Pa
D = D*1e-02;      S = S*1e-02; # -> m


## Default values
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dzeta_inlet = defaultValue(dzeta_inlet, 0.04); # default dzeta_inlet
tau_1 = defaultValue(tau_1, 0.9);    # default tau_1
dzeta_BA = defaultValue(dzeta_BA, 0.26);   # default dzeta_BA
relW_2rToC_1a = defaultValue(relW_2rToC_1a, 1.05);   # default relW_2rToC_1a
dzeta_TF = defaultValue(dzeta_TF, 0.18);   # default dzeta_TF
alpha_wh = defaultValue(alpha_wh, 0.05);   # default alpha_wh
beta_2Blade = defaultValue(beta_2Blade, 75);   # default beta_2Blade
tau_2 = defaultValue(tau_2, 0.94);   # default tau_2
diffuserWideCoef = defaultValue(diffuserWideCoef, 0.9);   # default diffuserWideCoef
diffuserDiamCoef = defaultValue(diffuserDiamCoef, 1.8);   # default diffuserDiamCoef
eta_diff = defaultValue(eta_diff, 0.75);   # default eta_diff
relDiffOutToCompOut = defaultValue(relDiffOutToCompOut, 1.4);   # default relDiffOutToCompOut
n_housing = defaultValue(n_housing, 1.9);   # default n_housing


## Precalculations
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Lower heat of combustion for fuel | Низшая теплота сгорания в зависимости от типа ДВС
if 'SI' in engineType:
    l_0 = 14.28; # kg \\\\\\ проверить!
elif 'DIESEL' in engineType:
    l_0 = 14.31; # kg
else:
    exit('Set type of the engine correctly ("DIESEL" or "SI")\
 in commonDict.py file!\n');
      
# Effective pressure | Среднее эффективное давление
p_e = 0.12*1e03*N_e*strokeNumber/(math.pi*pow(D, 2)*S*n*pistonNumber); # Pa

# Flow volume | Расход
if 'termPaper' in projectType:
    G_K = N_e*g_e*l_0*alpha*phi/3600; # kg/s

# Wheel diameter | Диаметр рабочего колеса
if ( issubclass(type(eta_KsStagn), str) ) or \
    ( issubclass(type(H_KsStagn), str) ) or ( issubclass(type(phi_flow), str) ):
    D_2 = 160*G_K + 40; # mm      
    print 'Aproximately the wheel diameter is {D_2_mm:.1f} mm\n' .format(D_2_mm = D_2);
    print 'Now you can set "eta_KsStagn", "H_KsStagn" & "phi_flow" using experimental\
    data for different wheels diameter.'
    exit();
else:
    D_2 = (160*G_K + 40)*1e-03; # m
    D_2_mm0 = D_2*1e03; # mm

# Calculation pressure degree increase with successive approximation method 
# Определение степени повышения давления методом последовательных приближений
if 'termPaper' in projectType:
    Pi_K = 1;
    validity = 1e-04;
    for i in range(5000):
        if abs(piK(l_0, p_e, Pi_K) - Pi_K) < validity:
            Pi_K = Pi_K + validity;
        else:
            Pi_K = piK(l_0, p_e, Pi_K)
            

## Compressor parameters calculation
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# [[[[[[[[[[[[[[[[[[[[ Inlet part | Входное устройство ]]]]]]]]]]]]]]]]]]]]

# Stagnation parameters of inlet | Параметры торможения на входе (1)
T_0Stagn = T_aStagn;
p_0Stagn = sigma_0*p_aStagn;

# Static pressure & temperature of intake in compressor | Статические температура и давление на входе в компрессор (3)
T_0 = T_0Stagn - pow(c_0, 2)/2/c_p;
p_0 = p_0Stagn * pow(T_0/T_0Stagn, k/(k - 1)); # Pa
L_KsStagn = c_p*T_0Stagn*(pow(Pi_K, (k - 1)/k) - 1); # Isentropy compression work in compressor | Изоэнтропная работа сжатия в компрессоре (4)

# Wheel outer diameter circular velocity | Окружная скорость на наружном диаметре колеса (5)
u_2 = math.sqrt(L_KsStagn / H_KsStagn);
if u_2 >= 550:    exit('Error 5:\n\
 Wheel outer diameter circular velocity is too high!\n\
Try to increase wheel diameter &/or set other ECE parameters');

c_1 = phi_flow*u_2; # | Абсолютная скорость потока на входе в рабочее колесо (6)

T_1 = T_0 + (pow(c_0, 2) - pow(c_1, 2))/2/c_p; # | Температура воздуха на входе в рабочее колесо (7)

L_inlet = dzeta_inlet*pow(c_1, 2)/2; # | Расчёт потерь энергии во впускном коллекторе (8)  


# [[[[[[[[[[[[[[[[[[[ Compressor wheel | Рабочее колесо ]]]]]]]]]]]]]]]]]]]

n_1 = ( k/(k - 1) - L_inlet/R/(T_1 - T_0) )/ \
( k/(k - 1) - L_inlet/R/(T_1 - T_0) - 1); # | Показатель политропы сжатия в компрессоре (9)

p_1 = p_0*pow(T_1/T_0, n_1/(n_1 - 1)); # | Давление на входе в колесо (10)

rho_1 = p_1/R/T_1; # | Плотность на входе в колесо (11)

F_1 = G_K/c_1/rho_1; # | Площадь поперечного сечения в колесе (12)

D_1H = math.sqrt( 4*F_1/math.pi/(1 - pow(relD_1B/relD_1H, 2)) ); # | Наружный диаметр колеса на входе D_1H (13)

D_1B = relD_1B/relD_1H*D_1H; # | Внутренний диаметер на входе (втулочный диаметр) (14)

# | Наружный диаметр колеса на комперссора на выходе (15)
D_2estimated = D_1H/relD_1H*1e+03; # mm
D_2 = standardisedSize( D_2estimated ) * 1e-03; # m

n_tCh = 60*u_2/math.pi/D_2; # 1/min, | Частота вращения турбокомпрессора (16)

D_1 = math.sqrt(( pow(D_1B, 2) + pow(D_1H, 2) )/2); # | Средний диаметр на входе в колесо

u_1 = math.pi*D_1*n_tCh/60; # | Окружная скорость на среднем диаметре входа (18)

# | Угол входа потока в рабочее колесо на среднем диамметре в относительном движении (19)
beta_1 = math.degrees(math.atan( c_1/u_1 ));
if issubclass(type(iDeg), str):    
    print 'Degree of the wheel inlet flow is {0:.3f}' .format(beta_1);
    print 'Now you can set "i", using recomendations'
    exit();

beta_1Blade = beta_1 + iDeg; # | Угол установки лопаток на среднем диаметре (20)

c_1Tau = c_1 / tau_1; # | Абсолютная скорость при учёте толщины лопаток (21)

u_1H = math.pi*D_1H*n_tCh/60; # | Угол установки лопаток на среднем диаметре (20)

w_1H = math.sqrt(pow(c_1Tau, 2) + pow(u_1H, 2)); # | Относительная скорость на наружном диаметре входа в колесо (23)

# | Число маха на наружном диаметре входа в колесо (24)
M_w1 = w_1H/math.sqrt(k*R*T_1);
if M_w1 > 0.9:
    print 'Warning!\nMach number (M = {0:.2f}) is too high!' .format(M_w1);
    print 'Try to change "tau_1" &/or other parameters.'
    # exit();
      
w_1 = math.sqrt(pow(c_1Tau, 2) + pow(u_1, 2)); # | Относительная скорость на среднем диаметре входа в колесо (25)

L_BA = dzeta_BA*pow(w_1, 2)/2; # | Удельная работа потерь во входном вращающемся направляющем аппарате колеса (26)

c_2r = relW_2rToC_1a * c_1; # | Радиальная составляющая абсолютной скорости / радиальная составляющая относительной скорости на выходе из колеса (27)

L_TF = dzeta_TF*pow(c_2r, 2)/2; # | Потери на поворот и трение в межлопаточных каналах рабочего колеса (28)

L_TB = alpha_wh*pow(u_2, 2); # | Потери на трение диска колеса о воздух в сумме с вентиляционными потерями (29)

# | Коэффициент мощности учитывабщий число лопаток и проч. (31)
mu = 1/(1+2/3*math.pi/z_K \
    *math.sin(math.radians(beta_2Blade))/(1 - pow(D_1/D_2, 2)) );

T_2 = T_1 + (mu + alpha_wh - 0.5*pow(mu, 2))*pow(u_2, 2)/c_p; # | Температура воздуха за колесом (32)

n_2 = ( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) )/ \
( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) - 1); # | Показатель политропы сжатия в колесе (33)

p_2 = p_1*pow(T_2/T_1, n_2/(n_2 - 1)); # | Давление на выходе из колеса (34)

rho_2 = p_2/R/T_2; # | Плотность на выходе из колеса (35)

c_2u = mu*(u_2 - c_2r/math.tan(math.radians(beta_2Blade))); # | Окружная составляющая абсолютной скорости на выходе (36)

c_2 = math.sqrt(pow(c_2u, 2) + pow(c_2r, 2)); # | Абсолютная скорость на выходе из колеса

w_2u = u_2 - c_2u; # | Окружная составляющая относительной скорости на выходе из колеса (38)

w_2 = math.sqrt(pow(w_2u, 2) + pow(c_2r, 2)); # | Относительная скорость на выходе из колеса (c_2r = w_2r) (39)

beta_2 = math.degrees(math.acos( w_2u/w_2 )); # | Угол между векторами относительной и окружной скорости на выходе из колеса (40)

alpha_2 = math.degrees(math.acos( c_2u/c_2 )); # | Угол между векторами абсолютной и окружной скорости на выходе из колеса (40)

b_2 = G_K/math.pi/D_2/c_2r/rho_2/tau_2; # | Ширина колеса на выходе из турбины (41)

T_2Stagn = T_2 + pow(c_2, 2)/2/c_p; # | Температура заторможенного потока на выходе из колеса (43)


# [[[[[[[[[[[[[[[[[[[[[[[[[[ Diffuser | Диффузор ]]]]]]]]]]]]]]]]]]]]]]]]]]

b_4 = diffuserWideCoef * b_2; # | Ширина безлопаточного диффузора на выходе (44)

D_4 = diffuserDiamCoef * D_2; # | Диаметр безлопаточного диффузора на выходе (45)

n_4 = (eta_diff * k/(k - 1))/(eta_diff * k/(k - 1) - 1); # | Показатель политропы сжатия в диффузоре (46)

# | Температура на выходе из диффузора (методом последовательных приближений) (47)
T_4 = T_2;
validity = 1e-02;
for i in range(5000):
    if abs(diffOutTemp(b_2, D_2, T_2, c_2, b_4, D_4, T_4, n_4) - T_4) > validity:
        T_4 = T_4 + validity;
    else:
        T_4 = diffOutTemp(b_2, D_2, T_2, c_2, b_4, D_4, T_4, n_4);

print T_4;    T_4 = 412.26;    print T_4;

p_4 = p_2*pow(T_4/T_2, n_4/(n_4 - 1)); # | Давление на выходе из колеса (48)

rho_4 = p_4/R/T_4; # | Плотность на выходе из колеса (49)

c_4 = c_2*D_2*b_2*rho_2/D_4/b_4/rho_4; # | Скорость на выходе из диффузора (50)


# [[[[[[[[[[[[[[[[[[[[[[[[[[[ Housing | Улитка ]]]]]]]]]]]]]]]]]]]]]]]]]]]

c_K = c_4/relDiffOutToCompOut; # | Скорость на выходе из компрессора (51)

T_K = T_4 + (pow(c_4, 2) - pow(c_K, 2))/2/c_p; # | Температура на выходе из компрессора (52)

p_K = p_4*pow(T_K/T_4, n_housing/(n_housing - 1)); # | Давление на выходе из компрессора (54)

T_KStagn = T_K + pow(c_K, 2)/2/c_p; # | Температура заторможенного потока на выходе (55)


# [[[[[[[[[[[[[[ Data processing | Оценка полученных данных ]]]]]]]]]]]]]]
p_KStagn = p_K*pow(T_KStagn/T_K, k/(k - 1)); # | давление заторможенного потока на выходе (56)

Pi_KStagn = p_KStagn/p_0Stagn; # | Действительная степень повышения давления в компрессоре (57)

L_KsStagnRated = c_p*T_0Stagn*(pow(Pi_KStagn, (k - 1)/k) - 1); # | Изоэнтропная работа по расчётной степени повышения давления (58)

eta_KsStagnRated = (pow(Pi_KStagn, (k - 1)/k) - 1) / (T_KStagn/T_0Stagn - 1); # | Расчётный изоэнтропный КПД по заторможенным параметрам (59)

differenceEta = abs(eta_KsStagnRated - eta_KsStagn)/eta_KsStagn * 100; # | Расхождение с заданным КПД компрессора (60)

H_KsStagnRated = L_KsStagnRated/pow(u_2, 2); # | Расчётный коэффициент напора по заторможенным параметрам (61)

differenceH = abs(H_KsStagnRated - H_KsStagn)/H_KsStagn*100; # | Расхождение с заданным КПД компрессора (62)

N_K = G_K*L_KsStagn/eta_KsStagnRated; # | Мощность затрачиваемая на привод компрессора (63)

p_vStagn = p_KStagn*sigma_c*sigma_v; # | Полное давление перед впускными клапанами поршневой части (64)

differencePi_K = abs(Pi_KStagn - Pi_K)/Pi_K * 100; # | Расхождение с предварительно оценнёной/заданной степенью повышения давления компрессора (+)


## Save data to calculate turbine
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
toTurbine = open("solvedParameters.py", "w")
toTurbine.write("# -*- coding: utf-8 -*-\n")
toTurbine.write("# This dictionary compiltes automaticaly!\n\n")
toTurbine.write("# Solved parameters from compressor\n\n")
toTurbine.write("u_2K = %.7f; # m/s\n\n" %u_2);
toTurbine.write("D_2K = %.3f; # m\n\n" %D_2);
toTurbine.write("n_TCh = %.2f; # RPM\n\n" %n_tCh);
toTurbine.write("eta_KsStagnRated = %.7f;\n\n" %eta_KsStagnRated);
toTurbine.write("L_KsStagn = %.7f; # J/kg\n\n" %L_KsStagn);
toTurbine.write("N_K = %.7f; # V\n\n" %N_K);
toTurbine.write("p_vStagn = %.7f; # Pa\n\n\n\n" %p_vStagn)


## Displaying the results
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Display some results right in the Terminal window
D_2_mm = D_2*1e+03
print 'Diameter of the wheel is {0} mm\n' .format(D_2_mm); # (15)
print 'Actual pressure degree increase is {0:.2f}' .format(Pi_KStagn); # (57)
print 'When precalculated (or setted, if it is a homework) pressure degree\
 increase is {0:.1f}' .format(Pi_K)
print 'Error of calculation between them is {0:.3f}%\n' .format(differencePi_K); # (60)
    
print "Energy conversion efficiency coeficients are:\n\
    eta_Ks*  = {0}   - setted\n\
    eta_Ks*' = {1:.4f} - rated" .format(eta_KsStagn, eta_KsStagnRated); # (dict) & (59)
print 'Error of calculation between them is {0:.3f}%\n' .format(differenceEta); # (60)

print "Isentropy head coeficients are:\n\
    H_Ks*  = {0}   - setted\n\
    H_Ks*' = {1:.4f} - rated" .format(H_KsStagn, H_KsStagnRated); # (dict) & (61)
print 'Error of calculation between them is {0:.3f}%\n' .format(differenceH); # (62)


## Saving the report
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
report = open("compressorReport.md", "w")

# Предварительные расчёты
if 'termPaper' in projectType:
    p_e_MPa = p_e*1e-06;
    report.write(
"#Предварительные расчёты\n\
- Среднее эффективное давление:\n\
$$\n p_{e} = {0,12*10^{3}N_{e}\\tau \over \pi D^{2}Sni} = %0.4f \quad МПа,\n$$\n\n\
- Расход: \n\
$$\n G_{к} = {N_{e}g_{e}l_{0}\\alpha\\phi \over 3600} = %1.4f \quad кг/с, \n$$\n\n\
- Предварительная оценка диаметра колеса:\n\
$$\n D_{2} = 160G_{K} + 40 = %2.0f \quad мм, \n$$\n\n\
- Cтепень повышения давления полученная методом последовательных приближений:\n\
$$\n \pi_{к} = %3.4f, \n$$\n\n" %(p_e_MPa, G_K, D_2_mm0, Pi_K)  );

else:   report.write(
"#Условие домашнего задания\n\
- Расход:\
\n$$\n G_{к} = %0.2f \quad кг/с, \n$$\n\n\
- Cтепень повышения давления:\
\n$$\n \pi_{к} = %1.2f, \n$$\n\n" %(G_K, Pi_K)    );

## Расчёт
report.write("#Расчёт\n\
Расчет был выполнен в следующем порядке.\n\n")
report.write("1. Температура $$ T_{0}^{*} $$ и давление $$ p_{0}^{*} $$\
 торможения на входе в компрессор ($$ \sigma_{0} = %0.2f$$):\
\n$$\n T_{0}^{*} = T_{0}^{*} = %1.f\quad К;\quad\
 p_{0}^{*} = \sigma_{0}p_{a}^{*} = %2.f\quad  Па \n$$\n\n"
%(sigma_0, T_aStagn, p_aStagn) ); 
report.write("2. Скорость воздуха на входе в компрессор выбирают в пределах 30…80 м/c.\
 Принимаем $$ с_{0} = %0.f $$ м/с.\n\n"
 %c_0 );
report.write("3. Статические температура и давление на входе в компрессор:\
 \n$$\n T_{0} = T_{0}^{*} - {c_{0}^{*} \over 2c_{p}} = %0.3f\quad К;\quad\
 p_{0}^{*} = p_{0}^{*} \left( {T_{0} \over T_{0}^{*}} \\right)^{k \over k-1}\
 = %1.0f \quad Па \n$$\n\n"
 %(T_0, p_0) );
report.write("4. Изоэнтропная работа сжатия в компрессоре:\
 \n$$\n L_{КS}^{*} = c_{p}T_{0}^{*} \left( (\pi_К^{*})^{k \over k-1} - 1\\right)\
 = %0.1f \quad Дж/кг \n$$\n\n"
 %L_KsStagn);
report.write("5. С помощью зависимостей, приведенных на рисунке 2.2[1],\
 для ожидаемого значения $$ D_{2} = %0.f $$ мм выберем коэффициент напора\
 по заторможенным параметрам (напорный изоэнтропный КПД).\
 Пусть в первом приближении $$ H_{KS}^{*} = %1.2f. $$\
 Окружную скорость на наружном диаметре колеса компрессора вычисляем по формуле:\
 \n$$\n u_{2} = \sqrt{L_{КS}^{*} \over H_{KS}^{*}} = %3.2f  \quad м/с\n$$\n\
По соображениям прочности рабочего колеса значение окружной скорости должно составлять\
 u2 ≤ 450…550 м/с.\n\n"
 %(D_2_mm0, H_KsStagn, u_2)); 
report.write("6. С помощью зависимостей, показанных на рис. 2.2[1],\
 выберем значение отношения осевой составляющей абсолютной скорости\
 потока на входе в рабочее колесо к окружной скорости на выходе — коэффициент расхода\
 $$ \\varphi = c_{1a}/u_{2} = %0.2f$$. В компрессорах, применяемых для наддува поршневых двигателей,\
 закрутка на входе в рабочее колесо практически не применяется, т. е.\
 $$ c_{1u} = 0 $$ и $$ c_{1} = c_{1a} $$. Тогда\
 \n$$\n c_{1} = \\varphi u_{2} = %1.2f \quad м/с. \n$$\n\n" %(phi_flow, c_1));
report.write("7. Температура воздуха на входе в рабочее колесо\
 \n$$\n T_{1} = T_{0} + {c_{0}^{2}-c_{1}^{2} \over 2c_{p}} = %0.2f \quad K \n$$\n\n"
 %T_1); 
report.write("8. Для расчета потерь энергии во впускном патрубке из\
 диапазона 0.03…0.06 выбираем значение $$ \zeta_{вп} = %0.3f $$. Тогда\
 \n$$\n \Delta L_{вп} = \zeta_{вп}{c_{1}^{2} \over 2} = %1.3f \quad Дж/кг \n$$\n\n"
 %(dzeta_inlet, L_inlet));
report.write("9. Показатель политропы при течении во входном устройстве\
 определяем из выражения:\
 \n$$\n {n_{1} \over n_{1} - 1} = {k_{1} \over k_{1} - 1} -\
 {\Delta L_{вп} \over R(T_{1} - T_{0})} \n$$\n Тогда, решив уравнение методом\
 последовательных приближений, получим $$n_{1} = %0.5f$$\n\n"
 %n_1);
report.write("10. Теперь можно определить давление p1 на входе в колесо:\
 \n$$\n p_{1}^{*} = p_{0} \left( {T_{1} \over T_{1}^{*}} \\right)^{k \over k-1}\
 = %1.0f \quad Па \n$$\n\n"
 %p_1);
report.write("11. Плотность на входе в колесо:\
 \n$$\n \\rho = {p_{1} \over RT_{1}} = %0.4f \quad Па \n$$\n\n"
 %rho_1);
report.write("12. Площадь поперечного сечения входа в колесо колесо:\
 \n$$\n F_{1} = {G_{K} \over c_{1}\\rho_{1}} = %0.6f \quad кг/м^{3} \n$$\n\n"
 %F_1);
report.write("13. Наружный диаметр колеса на входе определяется из соотношения\
 \n$$\n D_{1н} = \sqrt{{F_{1} \over (\pi/4)(1 - \overline{D}^2)}},\n$$\n где\
 $$ \overline{D} =  {\overline{D}_{1в} \over \overline{D}_{1н}} $$\n\
 Выбирая с помощью рис. 2.2[1] для ожидаемого значения диаметра\
 $$ D_{2} = %0.f $$ мм значения $$ \overline{D}_{1в} = %1.3f $$ и\
 $$ \overline{D}_{1н} = %2.3f $$. Тогда $$ D_{1н} = %4.5f $$\n\n"
 %(D_2_mm0, relD_1B, relD_1H, D_1H) );
report.write("14. Внутренний диаметр на входе (втулочный диаметр):\
 \n$$\n D_{1в} = \overline{D}D_{1н} = %0.5f \n$$\n\n" %D_1B);
report.write("15. Наружный диаметр колеса компрессора на выходе,\
 оценивается по формуле:\
 \n$$\n D_{2} = {D_{1н} \over \overline{D}_{1н}} = %0.4f\quad мм\n$$\n\
 После оценки диаметра, принимается ближайшее значение\
 из ряда нормальных значений: $$ D_2 = %1.f$$ мм\n\n"
 %(D_2estimated, D_2_mm) );
report.write("16. Частота вращения ротора турбокомпрессора:\
 \n$$\n n_{тк} = {60u_{2} \over \pi D_{2}} = %0.1f\quad мин^{-1} \n$$\n\n"
 %n_tCh);
report.write("17. Средний диаметр на входе в колесо:\
 \n$$\n D_{1} = \sqrt{{ D_{1в}^2+D_{1н}^2 \over 2}} = %0.6f\quad м\n$$\n\n"
 %D_1);
report.write("18. Окружная скорость на среднем диаметре входа:\
 \n$$\n u_{1} = \pi D_{1} {n_{тк} \over 60} = %0.3f\quad м/c \n$$\n\n"
 %u_1);
report.write("19. Угол входа потока в рабочее колесо на среднем диаметре\
 в относительном движении:\
 \n$$\n \\beta_{1} = arctg \left({ c_{1} \over u_{1} }\\right) = %0.3f° \n$$\n\n"
 %beta_1);
report.write("20. Угол атаки _i_ на входе в колесо рекомендуется принимать в диапазоне 2…6°.\
 Выберем $$ i = %0.2f° $$, тогда можно назначить угол установки лопаток\
 на среднем диаметре $$ D_{1} $$:\
 \n$$\n \\beta_{1л} = \\beta_{1} + i = %1.3f° \n$$\n\
Соответствующий план скоростей на входе в колесо показан на развертке\
 цилиндрического сечения, проведенного на диаметре $$D_{1}$$:\n"
 %(iDeg, beta_1Blade) );
report.write(
"![alt text](dimensionedBlades.png)\n\
<center>\
<b> Рисунок 1 </b> - <i>Векторный план скоростей на входе в рабочее колесо компрессора</i>\
</center>\n\n"
);
report.write("21. После входа в колесо значения абсолютной скорости $$с_{1}$$\
 возрастают в результате уменьшения проходного сечения вследствие загромождения\
 лопатками. Соответствующий коэффициент загромождения (стеснения)\
 $$\\tau_{1}$$, учитывающий толщину лопаток, составляет обычно 0.8…0.9.\
 Выберем значение $$\\tau_{1} = %0.2f$$. Тогда, с учетом загромождения:\
 \n$$\n c_{1\\tau} = {c_{1} \over \\tau_{1}} = %1.3f\quad м/с \n$$\n\n"
 %(tau_1, c_1Tau) );
report.write("22. Окружная скорость на наружном диаметре входа в колесо\
 \n$$\n u_{1н} = \pi D_{1н} {n_{тк} \over 60} = %0.3f\quad м/c \n$$\n\n"
 %u_1H);
report.write("23. Относительная скорость w1н на наружном диаметре входа в колесо\
 \n$$\n w_{1н} = \sqrt{c_{1\\tau}^2 + u_{1н}^2} = %0.3f\quad м/c \n$$\n\n"
 %w_1H);
report.write("24. Соответствующее число Маха:\
 \n$$\n M_{w1} = {w_{1н} \over \sqrt{kRT_{1}}} = %0.5f \n$$\n\
Полученное число Маха удовлетворяет необходимым требованиям\
 (не превышает значение 0.85…0.90)\n\n"
 %M_w1);
report.write("25. Относительная скорость w1 на среднем диаметре входа:\
 \n$$\n M_{w1} = \sqrt{c_{1\\tau}^2 + u_{1}^2} = %0.3f\quad м/c \n$$\n\n"
 %w_1);
report.write("26. Потери (удельная работа потерь) во входном вращающемся направляющем\
 аппарате колеса оцениваются коэффициентом потерь $$\zeta_{ва}$$,\
 который лежит в пределах 0.1…0.3. Выберем значение $$\zeta_{ва} = %0.3f$$. Тогда\
 \n$$\n \Delta L_{ва} = \zeta_{ва}{w_{1}^2 \over 2} = %1.2f \quad Дж/кг \n$$\n\n"
 %(dzeta_BA, L_BA) );
report.write("27. Радиальная составляющая $$c_{2r}$$ абсолютной скорости,\
 тождественно равная радиальной составляющей $$w_{2r}$$ относительной скорости на\
 выходе из колеса (рисунок 2), близка по значению к  $$c_{1a}$$ и составляет обычно\
 $$(0.9…1.2)c_{1a}$$. Принимая $$c_{2r} = %0.2fс_{1a}$$ , получаем:\
 \n$$\n c_{2r} \equiv w_{2r} = %1.3f\quad м/c \n$$\n\n"
 %(relW_2rToC_1a, c_2r) );
report.write("28. Потери $$\Delta L_{пт}$$ на поворот и трение в межлопаточных каналах\
 рабочего колеса оцениваются коэффициентом потерь $$\zeta_{пт}$$, значение которого\
 изменяется в пределах 0.1…0.2. Примем $$\zeta_{пт} = %0.3f$$. Тогда\
 \n$$\n \Delta L_{пт} = \zeta_{пт}{c_{2r}^2 \over 2} = %1.2f \quad Дж/кг \n$$\n\n"
 %(dzeta_TF, L_TF) );
report.write("29. Потери на трение диска колеса о воздух в сумме с вентиляционными\
 потерями вычисляются по формуле:\
 \n$$\n \Delta L_{тв} = \\alpha u_{2}^2 = %0.2f \quad Дж/кг \n$$\n\
 где _α_ — коэффициент дисковых потерь, лежащий в пределах 0.04…0.08. В данном случае\
 выберем _α_ = %1.3f.\n\n"
 %(L_TB, alpha_wh) );
report.write("30. Число лопаток колеса принимаем как $$z_{K} = %0.f.$$\n\n"
 %z_K);
report.write("31. Коэффициент мощности μ, учитывающий число лопаток, угол их наклона\
 на выходе и соотношение диаметров колеса, вычисляем по формуле:\
 \n$$\n \mu = { 1 \over 1 + {2 \over 3}{\pi \over z_{K}}{sin \\beta_{2л}\
 \over 1-(D_{1}/D_{2})} } = %0.6f \n$$\n\n"
 %mu);
report.write("32. Температура воздуха за колесом:\
 \n$$\n T_{2} = T_{1} + (\mu + \\alpha - 0.5\mu^2){u_2^2 \over c_{p}}\
 = %0.3f\quad К \n$$\n\n"
 %T_2);
report.write("33. Показатель политропы сжатия в колесе определяется уравнением:\
 \n$$\n {n_{2} \over n_{2} - 1} = {k \over k - 1} -\
 {\Delta L_{ва} + \Delta L_{пт} + \Delta L_{тв} \over R(T_{2} - T_{1})} \n$$\n\
 Тогда, решив уравнение методом последовательных приближений, получим $$n_{2} = %0.5f$$\n\n"
 %n_2);
report.write("34. Давление на выходе из колеса\
 \n$$\n p_{2} = p_{1} \left( {T_{2} \over T_{1}} \\right)^{n_{1} \over n_{1}-1}\
 = %1.f \quad Па \n$$\n\n"
 %p_2);
report.write("35. Плотность на выходе из колеса:\
  \n$$\n \\rho_{2} = {p_{2} \over RT_{2}} = %0.5f \quad кг/м^{3} \n$$\n\n"
  %rho_2);
report.write("36. Окружная составляющая абсолютной скорости на выходе:\
 \n$$\n c_{2u} = \mu \left( u_{2} - c_{2r} \over tg\\beta_{2л} \\right)\
 = %0.3f\quad м/с \n$$\n\n"
 %c_2u);
report.write("37. Абсолютная скорость на выходе из колеса:\
 \n$$\n c_{2} = \sqrt{c_{2u}^2 + c_{2r}^2} = %0.3f\quad м/c\n$$\n\n"
 %c_2);
report.write("38. Окружная составляющая относительной скорости на выходе из колеса:\
 \n$$\n w_{2u} = u_{2} - c_{2u} = %0.3f\quad м/c\n$$\n\n"
 %w_2u);
report.write("39. Относительная скорость w2 на выходе из колеса:\
 \n$$\n w_{2} = \sqrt{w_{2u}^2 + w_{2r}^2} = %0.3f\quad м/c\n$$\n\n"
 %w_2);
report.write("40. Угол между векторами относительной и окружной скорости\
 на выходе из колеса можно выразить в виде:\
 \n$$\n \\beta_{2} = arccos \left( w_{2u} \over w_{2} \\right) = %0.4f°\n$$\n\n"
 %beta_2);
report.write("41. Угол между векторами абсолютной и окружной скорости на выходе:\
 \n$$\n \\alpha_{2} = arccos \left( c_{2u} \over c_{2} \\right) = %0.4f°\n$$\n"
 %alpha_2);
report.write(
"![alt text](outWheel.png)\n\
<center>\
<b> Рисунок 2 </b> - <i>Векторный план скоростей на выходе из рабочего колеса компрессора</i>\
</center>\n\n"
);
report.write("42. При расчете ширины $$b_{2}$$ колеса на выходе необходимо учитывать\
 загромождение (стеснение) проходного сечения, обусловленное реальной толщиной лопаток.\
 В результате имеем:\
 \n$$\n b_{2} = {G_{K} \over \pi D_{2}c_{2r} \\rho_{2} \\tau_{2} } = %0.7f\quad м,\n$$\n\
 где $$\\tau_{2} = %1.3f$$ — коэффициент загромождения, который рекомендуется выбирать\
 в пределах 0.92…0.96\n\n"
 %(b_2, tau_2) );
report.write("43. Температура заторможенного потока на выходе из колеса:\
 \n$$\n T_{2}^{*} = T_{2} + {c_{2}^2 \over 2c_{p}} = %0.3f\quad К\n$$\n\n"
 %T_2Stagn);
report.write("44. В малоразмерных турбокомпрессорах обычно применяют безлопаточные диффузоры.\
 При этом промежуточное сечение 3−3 в диффузоре (см. рис. 3), очевидно, будет отсутствовать.\n\
Ширина безлопаточного диффузора на выходе может изменяться в пределах $$b_{4} = (0.7…1.0)b_{2}$$.\
 Выберем коэффициент %0.2f. Тогда:\
 \n$$\n b_{4} = %0.2f b_{2} = %1.8f\quad м\n$$\n\n"
 %(diffuserWideCoef, diffuserWideCoef, b_4) );
report.write("45. Наружный диаметр безлопаточного диффузора выбирают в пределах $$(1.6…1.9)D_{2}$$.\
 Принимаем значение коэффициента %0.2f. В результате:\
 \n$$\n D_{4} = %0.2f D_{2} = %1.4f\quad м\n$$\n\n"
 %(diffuserDiamCoef, diffuserDiamCoef, D_4) );
report.write(
"![alt text](dimensionedAxisCut.png)\n\
<center>\
<b> Рисунок 3 </b> - <i>Схема проточной части компрессора</i>\
</center>\n\n"
);
report.write("46. Показатель политропы сжатия в диффузоре вычислим с помощью уравнения,\
 в котором $$\eta_{д} = %0.3f$$ — политропный КПД диффузора (который должен лежать в пределах 0.55…0.78):\
 \n$$\n {n_{4} \over n_{4} - 1} = \eta_{д}{k \over k - 1} \n$$\n\
 Тогда, решив уравнение методом последовательных приближений, получим $$n_{4} = %1.4f$$\n\n"
 %(eta_diff, n_4) );
report.write("47. Температура Т4 на выходе из диффузора определяется методом последовательных\
 приближений из уравнения:\
 \n$$\n {1 \over \\beta^{m}} + {\\beta - 1 \over \sigma q} -\
 - {1 \over q} = 0,\n$$\n где $$ \\beta = T_{4}/T_{2};\quad\
 q = \left({ D_{2}b_{2} \over D_{4}b_{4} }\\right)^2;\quad\
 m = {2 \over n_{4} - 1}.$$\nВ результате решения имеем: $$T_{4} = \\beta T_{2} = %0.3f\quad К$$\n\n"
 %T_4);
report.write("48. Давление на выходе из диффузора:\
 \n$$\n p_{4} = p_{2} \left( {T_{4} \over T_{2}} \\right)^{n_{4} \over n_{4}-1}\
 = %1.f \quad Па \n$$\n\n"
 %p_4);
report.write("49. Плотность на выходе:\
  \n$$\n \\rho_{4} = {p_{4} \over RT_{4}} = %0.5f \quad кг/м^{3} \n$$\n\n"
  %rho_4);
report.write("50. Скорость на выходе из диффузора:\
 \n$$\n c_{4} = c_{2}{D_{2}b_{2}\\rho_{2} \over D_{4}b_{4}\\rho_{4}}\
 = %0.3f\quad м/с \n$$\n\n"
 %c_4);
report.write("51. В данном случае имеем автомобильный турбокомпрессор с коротким выпускным патрубком,\
 и отдельно сечение 5−5 входа в патрубок можно не рассматривать. Скорость на выходе из компрессора\
 $$с_{K}$$ обычно в 1.3…1.4 раза меньше скорости на выходе из диффузора. Примем значение $$с_{K} = %0.2f$$, тогда:\
 \n$$\n c_{K} = {c_{4} \over %1.2f} = %2.3f\quad м/с \n$$\n\n"
 %(relDiffOutToCompOut, relDiffOutToCompOut, c_K) );
report.write("52. Температура на выходе из компрессора:\
 \n$$\n T_{4}^{*} = T_{4} + {c_{4}^{2} - c_{K}^{2} \over 2c_{p}} = %0.3f\quad К\n$$\n\n"
 %T_K);
report.write("53. Показатель $$n_{ул}$$ политропы сжатия в воздухосборнике (улитке) составляет обычно\
 1.85…2.2. Примем значение $$n_{ул} = %0.1f$$.\n\n"
 %n_housing);
report.write("54. Тогда давление на выходе из компрессора:\
 \n$$\n p_{K} = p_{4} \left( {T_{K} \over T_{4}} \\right)^{n_{ул} \over n_{ул}-1}\
 = %1.f \quad Па \n$$\n\n"
 %p_K);
report.write("55. Температура заторможенного потока на выходе:\
 \n$$\n T_{K}^{*} = T_{K} + {c_{K}^{2} \over 2c_{p}} = %0.3f\quad К\n$$\n\n"
 %T_KStagn);
report.write("56. Давление заторможенного потока на выходе:\
 \n$$\n p_{K}^{*} = p_{K} \left( {T_{K}^{*} \over T_{K}} \\right)^{k \over k-1}\
 = %1.f \quad Па \n$$\n\n"
 %p_KStagn);
report.write("57. Действительная степень повышения давления компрессоре:\
 \n$$\n \pi_{K} = {p_{K}^{*} \over p_{0}^{*}} = %0.4f \n$$\n\n"
 %Pi_KStagn);
report.write("58. Изоэнтропная работа по расчетной степени повышения давления:\
 \n$$\n {L'}_{КS}^{*} = c_{p}T_{0}^{*} \left( (\pi_К^{*})^{k \over k-1} - 1\\right)\
 = %0.1f \quad Дж/кг \n$$\n\n"
 %L_KsStagn);
report.write("59. Расчетный изоэнтропный КПД по заторможенным параметрам:\
 \n$$\n {\eta'}_{КS}^{*} = {(\pi_К^{*})^{k \over k-1} - 1   \over\
 T_{K}^{*}/T_{0}^{*} - 1} = %0.5f \n$$\n\n"
 %eta_KsStagnRated);
report.write("60. Расхождение с заданным КПД компрессора составляет:\
 \n$$\n {\mid {\eta'}_{КS}^{*} - \eta_{КS}^{*} \mid \over \eta_{КS}^{*}}\
 = %0.3f \%% \n$$\n\n"
 %differenceEta);
report.write("61. Расчетный коэффициент напора по заторможенным параметрам:\
 \n$$\n {H'}_{КS}^{*} = {{L'}_{КS}^{*} \over u_{2}^2} = %0.5f \n$$\n\n"
 %differenceEta);
report.write("62. Расхождение с заданным коэффициентом напора составляет:\
 \n$$\n {\mid {H'}_{КS}^{*} - H_{КS}^{*} \mid \over H_{КS}^{*}}\
 = %0.3f \%% \n$$\n\n"
 %differenceH);
report.write("63. Мощность, затрачиваемая на привод компрессора:\
 \n$$\n N_{K} = {G_{K}{L'}_{КS}^{*} \over {\eta'}_{КS}^{*}} = %0.f\quad Вт \n$$\n\n"
 %N_K);
report.write("64. Полное давление перед впускными клапанами поршневой части:\
 \n$$\n p_{v}^{*} = \sigma_{c} \sigma_{v} p_{K}^{*} = %0.f\quad Па \n$$\n\n"
 %p_vStagn);


## Editing pictures
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Loading Fonts
font = ImageFont.truetype("../programFiles/fontGOST.ttf", 22);
 
# Add dimensions to the first picture (axisCut)
imageFile = "../programFiles/compressor/axisCut.png";   imageWheel=Image.open(imageFile)
 
# Drawing the text on the picture
draw = ImageDraw.Draw(imageWheel)
b_4 = round(b_4*1e+03, 2);    draw.text((331, 49), str(b_4), (0,0,0), font=font);
# b_3 = round(b_3*1e+03, 2);    draw.text((331, 115), str(b_3), (0,0,0), font=font);
b_2 = round(b_2*1e+03, 2);    draw.text((217, 150), str(b_2), (0,0,0), font=font);
imageWheel.rotate(-90).save("dimensionedAxisCut.png");  imageFile = "dimensionedAxisCut.png";   imageWheel=Image.open(imageFile);
draw = ImageDraw.Draw(imageWheel)
D_1H = round(D_1H, 2);    draw.text((75, 67), str(D_1H), (0,0,0), font=font);
D_1 = round(D_1*1e+03, 2);    draw.text((75, 113), str(D_1), (0,0,0), font=font);
D_1B = round(D_1B, 2);    draw.text((75, 150), str(D_1B), (0,0,0), font=font);
D_2 = round(D_2, 2);    draw.text((75, 335), str(D_2), (0,0,0), font=font);
# D_3 = round(D_3, 2);    draw.text((75, 370), str(D_3), (0,0,0), font=font);
D_4 = round(D_4*1e+03, 2);    draw.text((75, 409), str(D_4), (0,0,0), font=font);

imageWheel.rotate(90).save("dimensionedAxisCut.png")

# Add dimensions to the second picture (perpendicularCut)
# imageFile = "perpendicularCut.png";   imageWheel=Image.open(imageFile)
# Drawing the text on the picture
# draw = ImageDraw.Draw(imageWheel)
# draw.text((?, ?), str(alpha_3), (0,0,0), font=font);
# draw.text((?, ?), str(alpha_4), (0,0,0), font=font);
# imageWheel.save("dimensionedPerpendicularCut.png")

# Add dimensions to the blades picture
imageFile = "../programFiles/compressor/blades.png";   imageWheel=Image.open(imageFile)
# Drawing the text on the picture
draw = ImageDraw.Draw(imageWheel)
beta_1Blade = round(beta_1Blade, 2);
draw.text((38, 98), str(beta_1Blade), (0,0,0), font=font);
beta_1 = round(beta_1, 2);
draw.text((95, 120), str(beta_1), (0,0,0), font=font);
iDeg = round(iDeg, 2);
draw.text((180, 35), str(iDeg), (0,0,0), font=font);
c_1 = round(c_1, 1);                    c_1 = "{0} m/s" .format(c_1);   
draw.text((238, 143), str(c_1), (0,0,0), font=font);
u_1 = round(u_1, 1);                    u_1 = "{0} m/s" .format(u_1); 
draw.text((307, 172), str(u_1), (0,0,0), font=font);
w_1 = round(w_1, 1);                    w_1 = "{0} m/s" .format(w_1);
draw.text((430, 160), str(w_1), (0,0,0), font=font);
imageWheel.save("dimensionedBlades.png")

# Add speeds to the outlet from the wheel
# Loading Fonts
font = ImageFont.truetype("../programFiles/fontGOST.ttf", 12);

imageFile = "../programFiles/compressor/outWheel.png";   imageWheel=Image.open(imageFile)
# Drawing the text on the picture
draw = ImageDraw.Draw(imageWheel)
beta_2Blade = round(beta_2Blade, 2); beta_2Blade = "{0} deg" .format(beta_2Blade);
draw.text((10, 80), str(beta_2Blade), (0,0,0), font=font);
beta_2 = round(beta_2, 1);           beta_2 = "{0} deg" .format(beta_2);
draw.text((40, 120), str(beta_2), (0,0,0), font=font);
alpha_2 = round(alpha_2, 2);         alpha_2 = "{0} deg" .format(alpha_2);
draw.text((238, 160), str(alpha_2), (0,0,0), font=font);
c_2 = round(c_2, 2);                 c_2 = "{0} m/s" .format(c_2);
draw.text((290, 85), str(c_2), (0,0,0), font=font);
c_2r = round(c_2r, 2);               c_2r = "{0} m/s" .format(c_2r);
draw.text((198, 105), str(c_2r), (0,0,0), font=font);
c_2u = round(c_2u, 2);               c_2u = "{0} m/s" .format(c_2u);
draw.text((295, 184), str(c_2u), (0,0,0), font=font);
w_2 = round(w_2, 2);                 w_2 = "{0} m/s" .format(w_2);
draw.text((100, 85), str(w_2), (0,0,0), font=font);
w_2u = round(w_2u, 2);               w_2u = "{0} m/s" .format(w_2u);
draw.text((115, 162), str(w_2u), (0,0,0), font=font);
u_2 = round(u_2, 2);                 u_2 = "{0} m/s" .format(u_2);
draw.text((380, 184), str(u_2), (0,0,0), font=font);
n_tCh = round(n_tCh);                n_tCh =" = {0} RPM" .format(n_tCh);
draw.text((250, 393), str(n_tCh), (0,0,0), font=font);
imageWheel.save("outWheel.png")


## Saving the results to the resultsFolder
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os, shutil

if not os.path.exists("compressorResults"):   os.makedirs("compressorResults"); # Creating dir of needed

shutil.copyfile("compressorDict.py", "compressorResults/compressorDict.py");
os.rename("solvedParameters.py", "../turbine/solvedParameters.py");
os.rename("compressorReport.md", "compressorResults/compressorReport.md");
os.rename("dimensionedAxisCut.png", "compressorResults/dimensionedAxisCut.png");
os.rename("dimensionedBlades.png", "compressorResults/dimensionedBlades.png");
os.rename("outWheel.png", "compressorResults/outWheel.png");








