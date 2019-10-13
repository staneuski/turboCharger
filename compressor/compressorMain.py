#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# License
#     This program is free software: you can redistribute it and/or
#     modify it under the terms of the GNU General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#     General Public License for more details.
#
# Script
#     Main
#
# Description
#     Calculates parameters of compressor using 0D method
# 
#-----------------------------------------------------------------------

## Loading data & calling some fuctions

# Funcion for math solvers (pi, sin, cos, etc.) & other
from __future__         import division    
from PIL                import ImageFont, Image, ImageDraw
import math, os, shutil, sys

# Some self-made fuctions
from piK                import piK
from diffOutTemp        import diffOutTemp
from standardisedSize   import standardisedSize
from os                 import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from defaultValue       import defaultValue
from plotToFunction     import zPlot, etaPlot, HPlot, phiPlot,\
                                   relSpeedsPlot, relD_1HPlot, relD_1BPlot

# Loading input data from project dictionaries

from commonDict         import *
from compressorDict     import *

# Converting data to SI from dictionary | Перевод в СИ
N_e = N_e*1e03 # -> V
g_e = g_e*1e-03 # -> kg/(V*h) or g/(kV*h)
p_aStagn = p_aStagn*1e06 # -> Pa
D = D*1e-02;      S = S*1e-02 # -> m

execfile('include/defaultValuesCoefficients.py') # default values
execfile('../etc/logo.py') # printing the logo

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

## Precalculations
# ~~~~~~~~~~~~~~~~
# Теоретическое количество воздуха, необходимое для сгорания 1 кг топлива
if 'SI' in engineType:
    l_0 = 14.84 # kg
elif 'DIESEL' in engineType:
    l_0 = 14.31 # kg
else:   exit('Set type of the engine correctly ("DIESEL" or "SI")\
 in commonDict.py dictionary!\n')
      
# Effective pressure | Среднее эффективное давление
p_e = 0.12*1e03*N_e*strokeNumber/(math.pi*pow(D, 2)*S*n*pistonNumber) # Pa

# Flow volume | Расход
if 'TYPE1' in projectType:
    G_K = N_e*g_e*l_0*alpha*phi/3600 # kg/s

# Wheel diameter | Предварительная оценка диаметра рабочего колеса и установка параметров зависящих от него (2.25)
if issubclass(type(estimD_2), str):
    D_2 = (160*G_K + 40)*1e-03 # m
else:
    D_2 = estimD_2*1e-02 # m

D_2_mm0 = D_2*1e+03 # mm
    

# Calculation pressure degree increase with successive approximation method 
# Определение степени повышения давления методом последовательных приближений
if 'TYPE1' in projectType:
    eta_KsStagn = etaPlot(eta_KsStagn, D_2)
    Pi_K = 1
    validity = 1e-04
    while abs(piK(l_0, p_e, eta_KsStagn, Pi_K) - Pi_K) > validity:
        Pi_K = Pi_K + validity
    else:
        Pi_K = piK(l_0, p_e, eta_KsStagn, Pi_K)
            

## Compressor parameters calculation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stagnation parameters of inlet | Параметры торможения на входе (1)
T_0Stagn = T_aStagn
p_0Stagn = sigma_0*p_aStagn

# Static pressure & temperature of intake in compressor | Статические температура и давление на входе в компрессор (3)
T_0 = T_0Stagn - pow(c_0, 2)/2/c_p
p_0 = p_0Stagn * pow(T_0/T_0Stagn, k/(k - 1)) # Pa
L_KsStagn = c_p*T_0Stagn*(pow(Pi_K, (k - 1)/k) - 1) # Isentropy compression work in compressor | Изоэнтропная работа сжатия в компрессоре (4)

# Wheel outer diameter circular velocity | Окружная скорость на наружном диаметре колеса (5)
H_KsStagn = HPlot(H_KsStagn, D_2)
u_2 = math.sqrt(L_KsStagn / H_KsStagn)
if u_2 >= 550:    exit('Error 5:\n\
 Wheel outer diameter circular velocity is too high!\n\
Try to increase wheel diameter &/or set other ECE parameters')

# Абсолютная скорость потока на входе в рабочее колесо (6)
phi_flow = phiPlot(phi_flow, D_2)
c_1 = phi_flow*u_2

T_1 = T_0 + (pow(c_0, 2) - pow(c_1, 2))/2/c_p # Температура воздуха на входе в рабочее колесо (7)

L_inlet = dzeta_inlet*pow(c_1, 2)/2 # Расчёт потерь энергии во впускном коллекторе (8)  

n_1 = ( k/(k - 1) - L_inlet/R/(T_1 - T_0) )/ \
( k/(k - 1) - L_inlet/R/(T_1 - T_0) - 1) # Показатель политропы сжатия в компрессоре (9)

p_1 = p_0*pow(T_1/T_0, n_1/(n_1 - 1)) # Давление на входе в колесо (10)

rho_1 = p_1/R/T_1 # Плотность на входе в колесо (11)

F_1 = G_K/c_1/rho_1 # Площадь поперечного сечения в колесе (12)

# Наружный диаметр колеса на входе D_1H (13)
relD_1H = relD_1HPlot(relD_1H, D_2)
relD_1B = relD_1BPlot(relD_1B, D_2)
if relD_1B/relD_1H >= 1:    exit('Error 13:\
 Relation relD_1B/relD_1H = %0.2f > 1.\n\
Square root argument is less than 0!' %(relD_1B/relD_1H) )

D_1H = math.sqrt( 4*F_1/math.pi/(1 - pow(relD_1B/relD_1H, 2)) )

D_1B = relD_1B/relD_1H*D_1H # Внутренний диаметер на входе (втулочный диаметр) (14)

# Наружный диаметр колеса на комперссора на выходе (15)
D_2estimated = D_1H/relD_1H*1e+03 # mm
if 'ON' in roundDiamToSTD:
    D_2 = standardisedSize( D_2estimated ) * 1e-03 # m
else:
    if D_2estimated <= 85:
        D_2 = round( D_2estimated*2, -1 )/2 * 1e-03 # m
    else:
        D_2 = round( D_2estimated, -1 ) * 1e-03 # m

if 'TYPE2' in projectType: eta_KsStagn = etaPlot(eta_KsStagn, D_2)

n_tCh = 60*u_2/math.pi/D_2 # 1/min, | Частота вращения турбокомпрессора (16)

D_1 = math.sqrt(( pow(D_1B, 2) + pow(D_1H, 2) )/2) # Средний диаметр на входе в колесо

u_1 = math.pi*D_1*n_tCh/60 # Окружная скорость на среднем диаметре входа (18)

# Угол входа потока в рабочее колесо на среднем диамметре в относительном движении (19)
beta_1 = math.degrees(math.atan( c_1/u_1 ))
if issubclass(type(iDeg), str):    
    print 'Degree of the wheel inlet flow is {0:.3f}' .format(beta_1)
    print 'Now you can set "i", using recomendations'
    exit()

beta_1Blade = beta_1 + iDeg # Угол установки лопаток на среднем диаметре (20)

c_1Tau = c_1 / tau_1 # Абсолютная скорость при учёте толщины лопаток (21)

u_1H = math.pi*D_1H*n_tCh/60 # Угол установки лопаток на среднем диаметре (20)

w_1H = math.sqrt(pow(c_1Tau, 2) + pow(u_1H, 2)) # Относительная скорость на наружном диаметре входа в колесо (23)

# Число маха на наружном диаметре входа в колесо (24)
M_w1 = w_1H/math.sqrt(k*R*T_1)
if M_w1 > 0.9:    print 'Warning 24:\
 Mach number is too high!\n\
It must be less than 0.9 but it equals {0:.3f}\n\
Try to increase "tau_1", "relD_1H" &/or decrease "phi_flow", "relD_1B".\n' .format(M_w1)
      
w_1 = math.sqrt(pow(c_1Tau, 2) + pow(u_1, 2)) # Относительная скорость на среднем диаметре входа в колесо (25)

L_BA = dzeta_BA*pow(w_1, 2)/2 # Удельная работа потерь во входном вращающемся направляющем аппарате колеса (26)

# Радиальная составляющая абсолютной скорости / радиальная составляющая относительной скорости на выходе из колеса (27)
relW_2rToC_1a = relSpeedsPlot(relW_2rToC_1a, D_2)
c_2r = relW_2rToC_1a * c_1

L_TF = dzeta_TF*pow(c_2r, 2)/2 # Потери на поворот и трение в межлопаточных каналах рабочего колеса (28)

L_TB = alpha_wh*pow(u_2, 2) # Потери на трение диска колеса о воздух в сумме с вентиляционными потерями (29)

# Проверка на число лопаток относительно диаметра (рис. 2.2) (30) 
zLower = zPlot(0, D_2)
zUpper = zPlot(1, D_2)
if (z_K < zLower) | (z_K > zUpper): exit('Error 30:\
 Number of blades is not in the allowable diapason!\n\
For diameter of the wheel %0.0fmm this diapason is from %1.0f to %2.0f.'
 %(D_2*1e+03, round(zLower + 0.5), int(zUpper)) )
 
# Коэффициент мощности учитывабщий число лопаток и проч. (31)
mu = 1/(1+2/3*math.pi/z_K \
    *math.sin(math.radians(beta_2Blade))/(1 - pow(D_1/D_2, 2)) )

T_2 = T_1 + (mu + alpha_wh - 0.5*pow(mu, 2))*pow(u_2, 2)/c_p # Температура воздуха за колесом (32)

n_2 = ( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) )/ \
( k/(k - 1) - (L_BA + L_TF + L_TB)/R/(T_2 - T_1) - 1) # Показатель политропы сжатия в колесе (33)

p_2 = p_1*pow(T_2/T_1, n_2/(n_2 - 1)) # Давление на выходе из колеса (34)

rho_2 = p_2/R/T_2 # Плотность на выходе из колеса (35)

c_2u = mu*(u_2 - c_2r/math.tan(math.radians(beta_2Blade))) # Окружная составляющая абсолютной скорости на выходе (36)

c_2 = math.sqrt(pow(c_2u, 2) + pow(c_2r, 2)) # Абсолютная скорость на выходе из колеса

w_2u = u_2 - c_2u # Окружная составляющая относительной скорости на выходе из колеса (38)

w_2 = math.sqrt(pow(w_2u, 2) + pow(c_2r, 2)) # Относительная скорость на выходе из колеса (c_2r = w_2r) (39)

beta_2 = math.degrees(math.acos( w_2u/w_2 )) # Угол между векторами относительной и окружной скорости на выходе из колеса (40)

alpha_2 = math.degrees(math.acos( c_2u/c_2 )) # Угол между векторами абсолютной и окружной скорости на выходе из колеса (40)

b_2 = G_K/math.pi/D_2/c_2r/rho_2/tau_2 # Ширина колеса на выходе из турбины (41)

T_2Stagn = T_2 + pow(c_2, 2)/2/c_p # Температура заторможенного потока на выходе из колеса (43)

if 'VANELESS' in diffuserType: # Расчёт параметров безлопаточного диффузора
    b_4 = vanelessWideCoef * b_2 # Ширина безлопаточного диффузора на выходе (44)

    D_4 = vanelessDiamCoef * D_2 # Диаметр безлопаточного диффузора на выходе (45)

    n_4 = (eta_diff * k/(k - 1))/(eta_diff * k/(k - 1) - 1) # Показатель политропы сжатия в диффузоре (46)
    
    # Температура на выходе из диффузора (методом последовательных приближений) (47)
    T_4 = T_2
    validity = 1e-02
    while abs(diffOutTemp(b_2, D_2, T_2, c_2, b_4, D_4, T_4, n_4) - T_4) > validity:
        T_4 = T_4 + validity
    else:
        T_4 = diffOutTemp(b_2, D_2, T_2, c_2, b_4, D_4, T_4, n_4)

    p_4 = p_2*pow(T_4/T_2, n_4/(n_4 - 1)) # Давление на выходе из диффузора (48)
    
    rho_4 = p_4/R/T_4 # Плотность на выходе из колеса (49)

    c_4 = c_2*D_2*b_2*rho_2/D_4/b_4/rho_4 # Скорость на выходе из диффузора (50)
    
else: # Расчёт параметров лопаточного диффузора по МУ Федюшкина (F##)
    n_4 = n_diffuser
    # Проверка на число лопаток относительно их количества в РК (F50)
    if (z_diffuser < z_K - 5) | (z_diffuser > z_K + 2):   exit('Error F50:\
 Number of diffuser vanes is not in the allowable diapason!\n\
It must be less than number of %0.0f blades the wheel.' %z_K)
 
    b_3 = vanelessWideCoef * b_2 # Ширина безлопаточной части диффузора на выходе (44)

    D_3 = vanelessDiamCoef * D_2 # Диаметр безлопаточной части диффузора на выходе (45)

    n_3 = (eta_diff * k/(k - 1))/(eta_diff * k/(k - 1) - 1) # Показатель политропы сжатия безлопаточной части диффузора (46)
    
    # Температура на выходе из диффузора (методом последовательных приближений) (47)
    T_3 = T_2 - 40
    validity = 1e-02
    while abs(diffOutTemp(b_2, D_2, T_2, c_2, b_3, D_3, T_3, n_3) - T_3) > validity:
        T_3 = T_3 + validity
    else:
        T_3 = diffOutTemp(b_2, D_2, T_2, c_2, b_3, D_3, T_3, n_3)

    p_3 = p_2*pow(T_3/T_2, n_3/(n_3 - 1)) # Давление на выходе из колеса (48)
    
    rho_3 = p_3/R/T_3 # Плотность на выходе из безлопаточной части диффузора (49)
    
    c_3 = c_2*D_2*b_2*rho_2/D_3/b_3/rho_3 # Скорость на выходе из безлопаточной части диффузора (F46)
        
    D_4 = vanedDiamCoef * D_2 # Диаметр лопаточного диффузора на выходе (F47)
    
    b_4 = vanedWideCoef * b_3 # Ширина лопаточного диффузора на выходе (F48)
    
    alpha_4 = alpha_2 + deltaDegDiff # Угол наклона лопаток на выходе из диффузора (F49)
    
    # Температура на выходе из лопаточной части диффузора (F51)
    T_4 = T_3
    validity = 1e-02
    b_3COEF = b_3*tau_3*math.sin(math.radians(alpha_2))
    b_4COEF = b_4*tau_4*math.sin(math.radians(alpha_4))
    while abs(diffOutTemp(b_3COEF, D_3, T_3, c_3, b_4COEF, D_4, T_4, n_4) - T_4) > validity:
        T_4 = T_4 + validity
    else:
        T_4 = diffOutTemp(b_3COEF, D_3, T_3, c_3, b_4COEF, D_4, T_4, n_4)

    p_4 = p_2*pow(T_4/T_3, n_diffuser/(n_4 - 1)) # Давление на выходе из лопаточной части диффузора (F54)
    
    rho_4 = p_4/R/T_4 # Плотность на выходе из колеса (F54)

    c_4 = c_3*D_3*b_3COEF/D_4/b_4COEF/rho_4 # Скорость на выходе из диффузора (50)

c_K = c_4/relDiffOutToCompOut # Скорость на выходе из компрессора (51)

T_K = T_4 + (pow(c_4, 2) - pow(c_K, 2))/2/c_p # Температура на выходе из компрессора (52)

p_K = p_4*pow(T_K/T_4, n_housing/(n_housing - 1)) # Давление на выходе из компрессора (54)

T_KStagn = T_K + pow(c_K, 2)/2/c_p # Температура заторможенного потока на выходе (55)

p_KStagn = p_K*pow(T_KStagn/T_K, k/(k - 1)) # давление заторможенного потока на выходе (56)

Pi_KStagn = p_KStagn/p_0Stagn # Действительная степень повышения давления в компрессоре (57)

L_KsStagnRated = c_p*T_0Stagn*(pow(Pi_KStagn, (k - 1)/k) - 1) # Изоэнтропная работа по расчётной степени повышения давления (58)

eta_KsStagnRated = (pow(Pi_KStagn, (k - 1)/k) - 1) / (T_KStagn/T_0Stagn - 1) # Расчётный изоэнтропный КПД по заторможенным параметрам (59)

differenceEta = abs(eta_KsStagnRated - eta_KsStagn)/eta_KsStagn * 100 # Расхождение с заданным КПД компрессора (60)

H_KsStagnRated = L_KsStagnRated/pow(u_2, 2) # Расчётный коэффициент напора по заторможенным параметрам (61)

differenceH = abs(H_KsStagnRated - H_KsStagn)/H_KsStagn*100 # Расхождение с заданным КПД компрессора (62)

N_K = G_K*L_KsStagn/eta_KsStagnRated # Мощность затрачиваемая на привод компрессора (63)

p_vStagn = p_KStagn*sigma_c*sigma_v # Полное давление перед впускными клапанами поршневой части (64)

differencePi_K = abs(Pi_KStagn - Pi_K)/Pi_K * 100 # Расхождение с предварительно оценнёной/заданной степенью повышения давления компрессора (+)


## Displaying the results
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Display some results right in the Terminal window
D_2_mm = D_2*1e+03
print 'Diameter of the wheel is {0:.0f} mm\n' .format(D_2_mm) # (15)

print 'Parameters by cuts:'
if 'VANELESS' in diffuserType:  print '\
    1-1: T_1 = {0:.0f} K,   p_1 = {1:.4f} MPa\n\
    2-2: T_2 = {2:.0f} K,   p_2 = {3:.4f} MPa\n\
    4-4: T_4 = {4:.0f} K,   p_4 = {5:.4f} MPa\n'\
    .format(T_1, p_1*1e-06, T_2, p_2, T_4, p_4*1e-06)
else:   print '\
    1-1: T_1 = {0:.0f} K,   p_1 = {1:.4f} MPa\n\
    2-2: T_2 = {2:.0f} K,   p_2 = {3:.4f} MPa\n\
    3-3: T_3 = {4:.0f} K,   p_3 = {5:.4f} MPa\n\
    4-4: T_4 = {6:.0f} K,   p_4 = {7:.4f} MPa\n'\
    .format(T_1, p_1*1e-06, T_2, p_2*1e-06, T_3, p_3*1e-06, T_4, p_4*1e-06)
        
print 'Actual pressure degree increase is {0:.2f}, when\n\
precalculated/setted pressure degree increase is {1:.2f}' .format(Pi_KStagn, Pi_K) # (57)
print 'Error of calculation between them is {0:.3f}%\n' .format(differencePi_K) # (60)
    
print "Energy conversion efficiency coeficients are:\n\
    eta_Ks*  = {0:.4f} - setted\n\
    eta_Ks*' = {1:.4f} - rated" .format(eta_KsStagn, eta_KsStagnRated) # (dict) & (59)
print 'Error of calculation between them is {0:.3f}%\n' .format(differenceEta) # (60)

print "Isentropy head coeficients are:\n\
    H_Ks*  = {0:.4f} - setted\n\
    H_Ks*' = {1:.4f} - rated" .format(H_KsStagn, H_KsStagnRated) # (dict) & (61)
print 'Error of calculation between them is {0:.3f}%\n' .format(differenceH) # (62)

print "If something doesn't work correctly make the new issue or check the others:\n\
https://github.com/StasF1/turboCharger/issues"
print '2018-2019 Stanislau Stasheuski'#u' \N{COPYRIGHT SIGN}'

execfile('include/savingParametersForTurbine.py') # make extra dictionary for turbine calculation


## Report generation
# ~~~~~~~~~~~~~~~~~~
if 'VANELESS' in diffuserType: # ЛД
    execfile('include/reportGeneratorVANELESS.py') # saving the report for vaneless diffuser
else: # БЛД
    execfile('include/reportGeneratorVANED.py') # saving the report for vaned diffuser

execfile('include/picturesEditor.py') # editing pictures
execfile('include/createResultsFolder.py') # saving the results to the resultsFolder

# *****************************************************************************






