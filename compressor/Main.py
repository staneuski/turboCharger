#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calculates safety factors for crankshaft and displays the minimum of them

## Loading data & calling some fuctions
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Funcion for math solvers (pi, sin, cos, etc.)
from __future__ import division
import math

# Some self-made fuctions
from piK import piK
from diffOutTemp import diffOutTemp
from standardisedSize import standardisedSize

# Loading input data from project dictionary
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from commonDict import(
    projectType,
    p_a, T_a, k, R, c_p,
    engineType, strokeNumber, engineType, pistonNumber, S, D,
    N_e, n, g_e,
    alpha, eta_v, phi,
    Pi_K, G_K
)

from compressorDict import(
    T_aStagn, p_aStagn, c_0,
    sigma_0, sigma_c, sigma_v,
    eta_KsStagn, H_KsStagn, phi_flow, eta_diff,
    dzeta_inlet, dzeta_BA, dzeta_TF, alpha_wh, tau_2,
    relD_1H, relD_1B, relW_2rToC_1a, diffuserWideCoef, diffuserDiamCoef,
      relDiffOutToCompOut, n_housing,
    iDeg, tau_1, z_K, beta_2Blade,
    E, T_ca
)


## Converting data to SI from dictionary | Перевод в СИ
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

N_e = N_e*1e03; # -> V
g_e = g_e*1e-03; # -> kg/(V*h) or g/(kV*h)
p_aStagn = p_aStagn*1e06; # -> Pa
D = D*1e-02;      S = S*1e-02; # -> m


## Precalculations
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Lower heat of combustion for fuel | Низшая теплота сгорания в зависимости от типа ДВС
if 'SI' in engineType:
    l_0 = 14.28; # kg \\\\\\ проверить!
elif 'DIESEL' in engineType:
    l_0 = 14.31; # kg
else:
    print 'Set type of the engine correctly ("DIESEL" or "SI")\
 in compressorDict.py file!\n';
    exit();
      
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
if u_2 >= 550:    
    print 'Wheel outer diameter circular velocity is too high!'
    print 'Try to increase wheel diameter &/or set other ECE parameters'
    exit();

c_1 = phi_flow*u_2; # | Абсолютная скорость потока на входе в рабочее колесо (6)

T_1 = T_0 + (pow(c_0, 2) - pow(c_1, 2))/2/c_p; # | Температура воздуха на входе в рабочее колесо (7)

# | Расчёт потерь энергии во впускном коллекторе (8)
if issubclass(type(dzeta_inlet), str):    dzeta_inlet = 0.45;    # default dzeta_inlet
L_inlet = dzeta_inlet*pow(c_1, 2)/2;



# [[[[[[[[[[[[[[[[[[[ Compressor wheel | Рабочее колесо ]]]]]]]]]]]]]]]]]]]
n_1 = ( k/(k - 1) - L_inlet/R/(T_1 - T_0) )/ \
( k/(k - 1) - L_inlet/R/(T_1 - T_0) - 1); # | Показатель политропы сжатия в компрессоре (9)

p_1 = p_0*pow(T_1/T_0, n_1/(n_1 - 1)); # | Давление на входе в колесо (10)

ro_1 = p_1/R/T_1; # | Плотность на входе в колесо (11)

F_1 = G_K/c_1/ro_1; # | Площадь поперечного сечения в колесе (12)

D_1H = math.sqrt( 4*F_1/math.pi/(1 - pow(relD_1B/relD_1H, 2)) ); # | Наружный диаметр колеса на входе D_1H (13)

D_1B = relD_1B/relD_1H*D_1H; # | Внутренний диаметер на входе (втулочный диаметр) (14)

# | Наружный диаметр колеса на комперссора на выходе (15)
# D_2 = round(D_1H/relD_1H, 3 );
D_2 = standardisedSize( D_1H/relD_1H*1e+03 ) * 1e-03; # m

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

# | Абсолютная скорость при учёте толщины лопаток (21)
if issubclass(type(tau_1), str):    tau_1 = 0.85;    # default tau_1
c_1Tau = c_1 / tau_1;

u_1H = math.pi*D_1H*n_tCh/60; # | Угол установки лопаток на среднем диаметре (20)

w_1H = math.sqrt(pow(c_1Tau, 2) + pow(u_1H, 2)); # | Относительная скорость на наружном диаметре входа в колесо (23)

# | Число маха на наружном диаметре входа в колесо (24)
M_w1 = w_1H/math.sqrt(k*R*T_1);
if M_w1 > 0.9:
    print 'Warning!\nMach number (M = {0:.2f}) is too high!' .format(M_w1);
    print 'Try to change "tau_1" &/or other parameters.'
    # exit();
      
w_1 = math.sqrt(pow(c_1Tau, 2) + pow(u_1, 2)); # | Относительная скорость на среднем диаметре входа в колесо (25)

# | Удельная работа потерь во входном вращающемся направляющем аппарате колеса (26)
if issubclass(type(dzeta_BA), str):    dzeta_BA = 0.3;   # default dzeta_BA
L_BA = dzeta_BA*pow(w_1, 2)/2;

# | Радиальная составляющая абсолютной скорости / радиальная составляющая относительной скорости на выходе из колеса (27)
if issubclass(type(relW_2rToC_1a), str):    relW_2rToC_1a = 1.05;   # default relW_2rToC_1a
c_2r = relW_2rToC_1a * c_1;

# | Потери на поворот и трение в межлопаточных каналах рабочего колеса (28)
if issubclass(type(dzeta_TF), str):    dzeta_TF = 0.15;   # default dzeta_TF
L_TF = dzeta_TF*pow(c_2r, 2)/2;

# | Потери на трение диска колеса о воздух в сумме с вентиляционными потерями (29)
if issubclass(type(alpha_wh), str):    alpha_wh = 0.06;   # default alpha_wh
L_TB = alpha_wh*pow(u_2, 2);

mu = 1/(1+2/3*math.pi/z_K \
    *math.sin(math.radians(beta_2Blade))/(1 - pow(D_1/D_2, 2)) ); # | Коэффициент мощности учитывабщий число лопаток и проч. (31)

T_2 = T_1 + (mu + alpha_wh - 0.5*pow(mu, 2))*pow(u_2, 2)/c_p; # | Температура воздуха за колесом (32)

n_2 = ( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) )/ \
( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) - 1); # | Показатель политропы сжатия в колесе (33)

p_2 = p_1*pow(T_2/T_1, n_2/(n_2 - 1)); # | Давление на выходе из колеса (34)

ro_2 = p_2/R/T_2; # | Плотность на выходе из колеса (35)

c_2u = mu*(u_2 - c_2r/math.tan(math.radians(beta_2Blade))); # | Окружная составляющая абсолютной скорости на выходе (36)

c_2 = math.sqrt(pow(c_2u, 2) + pow(c_2r, 2)); # | Абсолютная скорость на выходе из колеса

w_2u = u_2 - c_2u; # | Окружная составляющая относительной скорости на выходе из колеса (38)

w_2 = math.sqrt(pow(w_2u, 2) + pow(c_2r, 2)); # | Относительная скорость на выходе из колеса (c_2r = w_2r) (39)

beta_2 = math.degrees(math.acos( w_2u/w_2 )); # | Угол между векторами относительной и окружной скорости на выходе из колеса (40)

alpha_2 = math.degrees(math.acos( c_2u/c_2 )); # | Угол между векторами абсолютной и окружной скорости на выходе из колеса (40)

# | Ширина колеса на выходе из турбины (41)
if issubclass(type(tau_2), str):    tau_2 = 0.94;   # default tau_2
b_2 = G_K/math.pi/D_2/c_2r/ro_2/tau_2;

T_2Stagn = T_2 + pow(c_2, 2)/2/c_p; # | Температура заторможенного потока на выходе из колеса (43)



# [[[[[[[[[[[[[[[[[[[[[[[[[[ Diffuser | Диффузор ]]]]]]]]]]]]]]]]]]]]]]]]]]
# | Ширина безлопаточного диффузора на выходе (44)
if issubclass(type(diffuserWideCoef), str):    diffuserWideCoef = 0.9;   # default diffuserWideCoef
b_4 = diffuserWideCoef * b_2;

# | Диаметр безлопаточного диффузора на выходе (45)
if issubclass(type(diffuserDiamCoef), str):    diffuserDiamCoef = 1.8;   # default diffuserDiamCoef
D_4 = diffuserDiamCoef * D_2;

# | Показатель политропы сжатия в диффузоре (46)
if issubclass(type(eta_diff), str):    eta_diff = 0.75;   # default eta_diff
n_4 = (eta_diff * k/(k - 1))/ \
(eta_diff * k/(k - 1) - 1);

# | Температура на выходе из диффузора (методом последовательных приближений) (47)
T_4 = T_2;
validity = 1e-02;
for i in range(5000):
    if abs(diffOutTemp(b_2, D_2, T_2, c_2, b_4, D_4, T_4, n_4) - T_4) > validity:
        T_4 = T_4 + validity;
    else:
        T_4 = diffOutTemp(b_2, D_2, T_2, c_2, b_4, D_4, T_4, n_4);

p_4 = p_2*pow(T_4/T_2, n_4/(n_4 - 1)); # | Давление на выходе из колеса (48)

ro_4 = p_4/R/T_4; # | Плотность на выходе из колеса (49)

c_4 = c_2*D_2*b_2*ro_2/D_4/b_4/ro_4; # | Скорость на выходе из диффузора (50)



# [[[[[[[[[[[[[[[[[[[[[[[[[[[ Housing | Улитка ]]]]]]]]]]]]]]]]]]]]]]]]]]]
# | Скорость на выходе из компрессора (51)
if issubclass(type(relDiffOutToCompOut), str):    relDiffOutToCompOut = 1.4;   # default relDiffOutToCompOut
c_K = c_4/relDiffOutToCompOut;

# | Температура на выходе из компрессора (52)
T_K = T_4 + (pow(c_4, 2) - pow(c_K, 2))/2/c_p;

# | Давление на выходе из компрессора (54)
if issubclass(type(n_housing), str):    n_housing = 1.9;   # default n_housing
p_K = p_4*pow(T_K/T_4, n_housing/(n_housing - 1));

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


## Displaying the results
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Display some results right in the Terminal window
print 'Diameter of the wheel is {D_2_mm} mm\n' .format(D_2_mm = D_2*1e+03); # (15)
print 'Actual pressure degree increase is {0:.2f}' .format(Pi_KStagn); # (57)
print 'When precalculated (or setted, if it is a homework) pressure degree\
 increase is {0:.1f}' .format(Pi_K)
print 'Error of calculation between them is {0:.3f}%\n' .format(differencePi_K); # (60)
    
print "Energy conversion efficiency coeficients are:\n    eta_Ks*  = {0}   - setted\n\
    eta_Ks*' = {1:.4f}  - rated" .format(eta_KsStagn, eta_KsStagnRated); # (dict) & (59)
print 'Error of calculation between them is {0:.3f}%\n' .format(differenceEta); # (60)

print "Isentropy head coeficients are:\n    H_Ks*  = {0}   - setted\n\
    H_Ks*' = {1:.4f}  - rated" .format(H_KsStagn, H_KsStagnRated); # (dict) & (61)
print 'Error of calculation between them is {0:.2f}%\n' .format(differenceH); # (62)

# Save report
report = open("compressorReport.md", "w")

if 'termPaper' in projectType:
    report.write("#Предварительные расчёты\n");
    report.write("- Среднее эффективное давление: \n$$\n");    p_e_MPa = p_e*1e-06;
    report.write("p_{e} = {0,12*10^{3}*N_{e}*\\tau \over \pi D^{2}Sni} = \
        %.4f \quad МПа,\n$$\n\n" %p_e_MPa)
    report.write("- Расход: \n$$\n")
    report.write("G_{к} = {N_{e}g_{e}l_{0}\\alpha*\\phi \over 3600} = \
        %.4f \quad кг/с, \n$$\n\n" %G_K)
    report.write("- Предварительная оценка диаметра колеса:\n$$\n")
    report.write("D_{2} = 160*G_{K} + 40 = %.0f \quad мм, \n$$\n\n" %D_2_mm0)
    report.write("- Cтепень повышения давления полученная методом\
 последовательных приближений: \n$$\n");
    report.write("\pi_{к} = %.4f, \n$$\n\n" %Pi_K)
else:
    report.write("#Условия домашнего задания\n");
    report.write("- Расход: \n$$\n");
    report.write("G_{к} = %.2f \quad кг/с, \n$$\n\n" %G_K)
    report.write("- Cтепень повышения давления: \n$$\n");
    report.write("\pi_{к} = %.2f, \n$$\n\n" %Pi_K)


report.write("#Рассчитанные параметры\n");

report.write("##Общие параметры\n");
report.write("- Изоэнтропная работа сжатия в компрессоре: \n$$\n");
report.write("L_{КS}^{*} = %.0f \quad Дж/кг, \n$$\n\n" %L_KsStagn);

report.write("- Окружная скорость на наружном диаметре колеса: \n$$\n");
report.write("u_{2} = %.2f \quad м/с \quad < \quad 550 \quad м/с , \n$$\n" %u_2);
report.write("Окружная скорость не превышает допустимое значение.\n\n");

report.write("- Частота вращения ротора турокомпрессора: \n$$\n");
report.write("n_{TK} = %.0f \quad мин^{-1}, \n$$\n" %n_tCh);

report.write("- Степень повышения давления: \n$$\n");
report.write("\pi_{к}^{*} = %.3f \quad мин^{-1}, \n$$\n" %Pi_KStagn);
if 'termPaper' in projectType:  report.write("_Разница с оценённой степенью повышения\
 давления составляет:_ **%.1f%%**\n" %differencePi_K);
else:   report.write("_Разница с заданной степенью повышения\
 давления составляет:_ **%.1f%%**\n\n" %differencePi_K);
    

report.write("- Коэффициент напора:\n");
report.write("Заданный:\n$$\n");
report.write("Н_{К}^{*} = %.3f, \n$$\n" %H_KsStagn);
report.write("По заторможенным параметрам: \n$$\n");
report.write("Н_{К}{'}^{*} = %.3f, \n$$\n" %H_KsStagnRated);
report.write("_Расхождение с заданным коэффициентом напора:_ **%.2f%%**\n" %differenceH);

report.write("- КПД компрессора:\n");
report.write("Заданный КПД:\n$$\n");
report.write("\eta_{КS} = %.3f, \n$$\n" %eta_KsStagn);
report.write("Расчётный изоэнтропный КПД: \n$$\n");
report.write("\eta_{КS}^{*} = %.3f, \n$$\n" %eta_KsStagnRated);
report.write("_Расхождение с заданным КПД компрессора:_ **%.2f%%**\n" %differenceEta);


report.write("##Входное устройство\n");
report.write("- Давление на входе в колесо: \n$$\n");   p_1 = p_1*1e-06;
report.write("p_{1} = %.6f \quad МПа, \n$$\n\n" %p_1);

report.write("- Плотность на входе в колесо: \n$$\n");
report.write("ro_{1} = %.4f \quad кг/м^{3}, \n$$\n\n" %ro_1);

report.write("- Площадь поперечного сечения входа в колесо: \n$$\n");
report.write("F_{1} = %.6f \quad м^{2} , \n$$\n\n" %F_1);

report.write("##Колесо компрессора\n");
report.write("- Наружный диаметр колеса на входе: \n$$\n"); D_1H = D_1H*1e03;
report.write("D_{1Н} = %.1f \quad мм, \n$$\n\n" %D_1H);

report.write("- Внутренный диаметр на входе: \n$$\n"); D_1B = D_1B*1e03;
report.write("D_{1В} = %.1f \quad мм, \n$$\n\n" %D_1B);

report.write("- Наружный диаметр колеса на выходе\
 принятый из _ряда нормальных значений_: \n$$\n"); D_2 = D_2*1e03;
report.write("D_{2} = %.1f \quad мм, \n$$\n\n" %D_2);
report.write("![alt text](dimensionedAxisCut.png)\n\n")
report.write("![alt text](dimensionedBlades.png)")




## Editing pictures
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Importing the needed library
import PIL;     from PIL import ImageFont, Image, ImageDraw
 
# Loading Fonts
font = ImageFont.truetype("../forReportGen/fontGOST.ttf", 22);
 
# Add dimensions to the first picture (axisCut)
imageFile = "../forReportGen/compressor/axisCut.png";   imageWheel=Image.open(imageFile)
 
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
imageFile = "../forReportGen/compressor/blades.png";   imageWheel=Image.open(imageFile)
# Drawing the text on the picture
draw = ImageDraw.Draw(imageWheel)
beta_1Blade = round(beta_1Blade, 2);    draw.text((38, 98), str(beta_1Blade), (0,0,0), font=font);
beta_1 = round(beta_1, 2);    draw.text((100, 120), str(beta_1), (0,0,0), font=font);
iDeg = round(iDeg, 2);    draw.text((180, 35), str(iDeg), (0,0,0), font=font);
c_1 = round(c_1, 1);    draw.text((238, 143), str(c_1), (0,0,0), font=font);
u_1 = round(u_1, 1);    draw.text((307, 172), str(u_1), (0,0,0), font=font);
w_1 = round(w_1, 1);    draw.text((430, 160), str(w_1), (0,0,0), font=font);
imageWheel.save("dimensionedBlades.png")


## Saving the results to the resultsFolder
import os, shutil

# Creating dir of needed
if not os.path.exists("compressorResults"):   os.makedirs("compressorResults");


shutil.copyfile("compressorDict.py", "compressorResults/compressorDict.py");
os.rename("compressorReport.md", "compressorResults/compressorReport.md");
os.rename("dimensionedAxisCut.png", "compressorResults/dimensionedAxisCut.png");
os.rename("dimensionedBlades.png", "compressorResults/dimensionedBlades.png");








