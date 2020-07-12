def turbine_run(ambient, engine,
        compressor, Compressor,
        turbine):
    '''
        Calculate radial turbine parameters using 0D method
    '''
    import math
    from turbine.pre.turbine_plot2func import ksi_plot2func
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    if turbine['type'] == 'radial':
        class Turbine:
            '''
                Class with calculated turbine parameters
            '''
            # Outlet turbine pressure | Давление за турбиной
            p_2 = turbine['losses']['drag_inlet_ratio']*ambient['p']\
                  *1e+06 # [Pa]

            #1 Расход газа через турбину с учетом утечки
            G_T = compressor['G']*turbine['efficiency']['sigma_esc']\
                *(1 + 1/engine['combustion']['alpha']
                       /engine['combustion']['phi']
                       /engine['combustion']['l_0'])

            #2 Диаметр колеса турбины и окружная скорость на входе в колесо\
            #  турбины
            D_1 = turbine['geometry']['coefficients']['D_ratio']\
                  *compressor['geometry']['D_2']
            u_1 = turbine['geometry']['coefficients']['D_ratio']*Compressor.u_2

            #4 Изоэнтропная работа турбины
            L_TsStagn = Compressor.L_KsStagn*compressor['G']\
                        /Compressor.eta_KsStagnRated\
                        /turbine['efficiency']['eta_Te']\
                        /G_T

            #5 Условная изоэнтропная скорость истечения из турбины
            c_2s = math.sqrt(2*L_TsStagn)

            #6 Расчёт параметра ksi
            ksi = u_1/c_2s
            ksiLower = ksi_plot2func(0, compressor['geometry']['D_2'])
            ksiUpper = ksi_plot2func(1, compressor['geometry']['D_2'])
            if (ksi < ksiLower) | (ksi > ksiUpper):
                exit("\033[91mERROR 6:\
                     Parameter 'ksi' is not in the allowable diapason!\
                     \nIt equals %2.3f but must be from %0.2f to %1.3f."
                     .replace('                     ', ' ')
                     %(ksiLower, ksiUpper, ksi))

            #7 Давление газа на входе в турбину
            p_0Stagn = p_2/pow(1 - L_TsStagn
                                   /engine['exhaust']['c_p']
                                   /engine['heat']['T_0Stagn'],
                               engine['exhaust']['k']\
                               /(engine['exhaust']['k'] - 1))

            #8 Проверка соотношения полного давления перед впускными клапанами
            #  поршневой части и давлением газа на входе в турбину
            pressureRelation = Compressor.p_vStagn/p_0Stagn
            if (pressureRelation < 1.1) | (pressureRelation > 1.3):
                exit("\033[91mERROR 8:\
                     Pressure ratio is not in the allowable diapason!\
                     \nIt equals %0.2f but must be from 1.1 to 1.3.\
                     \nScavenging cannot be happen."
                     .replace('                     ', ' ')
                     %pressureRelation)

            #9 Наружный диаметр рабочего колеса турбины на выходе
            D_2H = turbine['geometry']['coefficients']['d_outer_ratio']*D_1

            #10 Внутренний (втулочный) диаметр колеса
            D_2B = turbine['geometry']['coefficients']['d_inner_ratio']*D_1

            #11 Средний диаметр колеса турбины на выходе
            D_2 = math.sqrt((D_2B**2 + D_2H**2)/2)

            #12 Вычисление параметра µ
            mu = D_2/D_1
            if (mu < 0.5) | (mu > 0.8): 
                exit("\033[91mERROR 12:\
                     Geometeric parameter 'mu' is not in the allowable\
                     diapason! (It equals %0.2f)"
                     .replace('                     ', ' ')
                     %mu)

            #15 Изоэнтропная работа расширения (располагаемый теплоперепад)
            #   в сопловом аппарате
            L_cS = L_TsStagn*(1 - turbine['efficiency']['rho'])

            #17 Абсолютная скорость с1 на выходе из соплового аппарата
            c_1 = turbine['losses']['phi']*math.sqrt(2*L_cS)

            #19 Радиальная составляющая абсолютной скорости (c_1r == w_1r)
            c_1r = c_1*math.sin(math.radians(turbine['geometry']['alpha_1']))

            #20 Окружная составляющая абсолютной скорости
            #   на выходе из соплового аппарата
            c_1u = c_1*math.cos(math.radians(turbine['geometry']['alpha_1']))

            #21 Окружная составляющая относительной скорости
            #   на выходе из соплового аппарата
            w_1u = c_1u - u_1

            #22 Относительная скорость на входе в рабочее колесо
            w_1 = math.sqrt(c_1r**2 - w_1u**2)

            #23 Значение угла β_1 наклона вектора относительной скорости w_1
            beta_1 = turbine['geometry']['beta_1Blade']\
                     - math.degrees(math.atan(w_1u/c_1r))

            if (beta_1 < 80) | (beta_1 > 100):
                exit("\033[91mERROR 23:\
                     Angle 'beta_1' is not in the allowable diapason!\n\
                     \nIt equals %0.1f but must be from 80 to 100 degrees."
                     .replace('                     ', ' ')
                     %beta_1)

            #24 Температура газа на входе в колесо
            T_1 = engine['heat']['T_0Stagn'] - c_1**2/2\
                                               /engine['exhaust']['c_p']

            #25 Давление на входе в колесо
            p_1 = p_0Stagn*pow(1 - L_cS
                                   /engine['exhaust']['c_p']
                                   /engine['heat']['T_0Stagn'],
                               engine['exhaust']['k']\
                               /(engine['exhaust']['k'] - 1))

            #26 Плотность ρ_1 на входе в колесо
            rho_1 = p_1/engine['exhaust']['R']/T_1

            #27 Ширина лопаток b1 на входе в колесо
            b_1 = G_T/math.pi/D_1/rho_1/c_1r

            #28 Изоэнтропная работа расширения в рабочем колесе
            #   (располагаемый теплоперепад) на входе в колесо
            L_pS = turbine['efficiency']['rho']*L_TsStagn

            #30 Окружная скорость на среднем диаметре D_2 выхода из
            #   рабочего колеса
            u_2 = mu*u_1

            #31 Относительная скорость на среднем диаметре D_2
            w_2 = turbine['losses']['psi']\
                  *math.sqrt(2*L_pS + w_1**2 - u_1**2 + u_2**2)

            #32 Температура Т_2 на выходе из колеса
            T_2 = T_1 - ((w_2**2 - u_2**2 - w_1**2 + u_1**2)\
                        /2/engine['exhaust']['c_p'])

            #33 Плотность на выходе из колеса
            rho_2 = p_2/engine['exhaust']['R']/T_2

            #34 Площадь сечения на выходе из колеса
            F_2 = math.pi/4*(D_2H**2 - D_2B**2)

            #35 Утечки через радиальный зазор Δ между корпусом
            #   и колесом турбины
            G_losses = 0.45*2*turbine['geometry']['delta']\
                       *G_T/(D_2H - D_2B)\
                       *(1 + (D_2H - D_2B)/2/D_2)

            #36 Расход через сечение F_2 на выходе из колеса
            G_F2 = G_T - G_losses

            #37 Аксиальные составляющие относительной w_2а и
            #   абсолютной с_2а скоростей на выходе из колеса (w_2a == c_2a)
            w_2a = G_F2/F_2/rho_2

            #38 Окружная составляющая относительной скорости
            #   на выходе из колеса
            if (w_2**2 - w_2a**2) > 0:
                w_2u = math.sqrt(w_2**2 - w_2a**2)

            else:
                exit("\033[91mERROR 38:\
                     Radicand is less then 0!\
                     \nDifference between speeds is %0.3f m/s."
                     .replace('                     ', ' ')
                     %(w_2a - w_2))

            #39 Угол β_2 наклона вектора относительной скорости w2
            #   на выходе из рабочего колеса
            beta_2 = math.degrees(math.asin(w_2a/w_2))

            #40 Окружная составляющая с2u абсолютной скорости на выходе из колеса
            c_2u = w_2u - u_2

            #41 Абсолютная скорость на выходе из колеса
            c_2 = math.sqrt(w_2a**2 + c_2u**2) 

            #42 Угол α_2 выхода потока из колеса в абсолютном движении
            alpha_2 = 90 - math.degrees(math.atan( c_2u/w_2a ))

            if (alpha_2 < 75) or (alpha_2 > 105):
                exit("\033[91mERROR 42:\
                     Angle 'alpha_2' is not in the allowable diapason!\
                     \nIt equals %0.1f but must be from 75 to 105 degrees."
                     .replace('                     ', ' ')
                     %alpha_2)

            #43 Потери в сопловом аппарате турбины
            Z_c = (1/turbine['losses']['phi']**2 - 1)*c_1**2/2

            #44 Потери в рабочем колесе
            Z_p = (1/turbine['losses']['psi']**2 - 1)*w_2**2/2

            #45 Суммарные потери в лопаточных каналах
            Z_Blades = Z_c + Z_p

            #46 Лопаточная работа турбины
            L_TBlades = L_TsStagn - Z_Blades

            #47 Лопаточный КПД η_(т.л) турбины
            eta_TBlades = L_TBlades/L_TsStagn

            #48 Потери в Z′_в с выходной скоростью при условии равномерного
            #   потока на выходе из рабочего колеса
            Z_SteadyOutlet = c_2**2/2

            #49 Работа L′_тu на окружности колеса c учётом потерь
            #   определёная через потери
            L_TuSteadyFromLosses = L_TBlades - Z_SteadyOutlet

            #50 Работа L′_тu на окружности колеса c учётом потерь
            #   определёная с помощью формулы Эйлера
            L_TuSteady = u_1*c_1u + u_2*c_2u

            #51 Действительные потери Z_в с выходной скоростью
            #   (для потока с неравномерностью на выходе)
            Z_UnsteadyOutlet = turbine['efficiency']['dzeta']*Z_SteadyOutlet

            #52 Действительная работа на окружности колеса
            L_Tu = L_TBlades - Z_UnsteadyOutlet

            #53 Окружной КПД η_тu турбины
            eta_Tu = L_Tu/L_TsStagn
            if (eta_Tu < 0.75) or (eta_Tu > 0.9):
                exit("\033[91mERROR 53:\
                     Angle 'eta_Tu' is not in the allowable diapason!\
                     \nIt equals %0.3f but must be from 0.75 to 0.9."
                     .replace('                     ', ' ')
                     %eta_Tu)

            #54 Потери Zу, обусловленные утечкой газа через радиальные зазоры
            #   между колесом и корпусом
            Z_y = L_Tu*G_losses/G_T

            #55 Мощность N_тв, затрачиваемая на трение колеса в корпусе и
            #   вентиляцию
            N_TB = 735.5*turbine['geometry']['coefficients']['beta']\
                   *(rho_1 + rho_2)/2*D_1**2*pow(u_1/100, 3)

            #56 Потери Z_тв на трение и вентиляцию
            Z_TB = N_TB/G_T

            #57 Суммарные дополнительные потери Z_д , включающие потери
            #   на утечки,трение и вентиляцию
            Z_extra = Z_y + Z_TB

            #58 Внутренняя работа L_тi турбины
            L_Ti = L_Tu - Z_extra

            #59 Внутренний КПД η_тi турбины
            eta_Ti = L_Ti/L_TsStagn

            #60 Эффективный КПД η`_тe турбины
            eta_TeRated = turbine['efficiency']['eta_m']*eta_Ti

            #61 Расхождение с заданным КПД турбины
            eta_error = (turbine['efficiency']['eta_Te'] - eta_TeRated)\
                        /turbine['efficiency']['eta_Te']*100 # [%]

            #62 Эффективная работа L_т е турбины
            L_Te = eta_TeRated*L_TsStagn

            #63 Мощность N_т на валу турбины
            N_T = L_Te*G_T

            #64 Расхождение с мощностью N_к, потребляемой компрессором
            N_error = (Compressor.N_K - N_T)/Compressor.N_K*100 # [%]


    elif turbine['type'] == 'axial':
        class Turbine:
            '''
                Class with calculated axial turbine parameters
            '''

            # Outlet turbine pressure | Давление за турбиной
            p_2 = turbine['losses']['drag_inlet_ratio']*ambient['p']\
                  *1e+06 # [Pa]

            # Axial turbine parameters
            # ~~~~~~~~~~~~~~~~~~~~~~~~
            #1 Расход газа через турбину с учетом утечки
            G_T = compressor['G']*turbine['efficiency']['sigma_esc']\
                  *(1 + 1/engine['combustion']['alpha']
                         /engine['combustion']['phi']
                         /engine['combustion']['l_0'])

            #3 Изоэнтропная работа турбины
            L_TsStagn = Compressor.L_KsStagn*compressor['G']\
                        /Compressor.eta_KsStagnRated\
                        /turbine['efficiency']['eta_Te']\
                        /G_T

            #4 Условная изоэнтропная скорость истечения из турбины
            c_2s = math.sqrt(2*L_TsStagn)

            #5  Расчёт скорости на входе
            u_1 = turbine['efficiency']['ksi']*c_2s

            #7 Давление газа на входе в турбину
            p_0Stagn = p_2/pow(1 - L_TsStagn
                                   /engine['exhaust']['c_p']
                                   /engine['heat']['T_0Stagn'],
                               engine['exhaust']['k']\
                               /(engine['exhaust']['k'] - 1))

            #8 Проверка соотношения полного давления перед впускными клапанами
            #  поршневой части и давлением газа на входе в турбину
            pressureRelation = Compressor.p_vStagn/p_0Stagn
            if (pressureRelation <= 1.1):
                exit("\033[91mERROR 8:\
                     Scavenging cannot happen because the pressure ratio is\
                     too small!\
                     \nIt equals %0.2f, but must be more than 1.1\n"
                     .replace('                     ', ' ')
                     %pressureRelation)

            #9 Изоэнтропная работа расширения
            #  (располагаемый теплоперепад) в сопловом аппарате
            L_cS = L_TsStagn*(1 - turbine['efficiency']['rho'])

            #11 Абсолютная скорость с1 на выходе из соплового аппарата
            c_1 = turbine['losses']['phi']*math.sqrt( 2*L_cS )

            #13 Радиальная составляющая абсолютной скорости (c_1a == w_1a)
            c_1a = c_1*math.sin(math.radians(turbine['geometry']['alpha_1']))

            #14 Окружная составляющая абсолютной скорости на выходе
            #   из соплового аппарата
            c_1u = c_1*math.cos(math.radians(turbine['geometry']['alpha_1']))

            #15 Окружная составляющая относительной скорости
            #   на выходе из соплового аппарата
            w_1u = c_1u - u_1

            #16 Значение угла β_1 наклона вектора относительной скорости w_1
            beta_1 = turbine['geometry']['beta_1Blade']\
                - math.degrees(math.atan( w_1u/c_1a ))

            #17 Температура газа на входе в колесо
            T_1 = engine['heat']['T_0Stagn'] - c_1**2/2\
                                               /engine['exhaust']['c_p']

            #18 Давление на входе в колесо
            p_1 = p_0Stagn*pow(1 - L_cS
                                   /engine['exhaust']['c_p']
                                   /engine['heat']['T_0Stagn'],
                               engine['exhaust']['k']\
                               /(engine['exhaust']['k'] - 1))

            pressureRelationSetOfNozzles = p_1/p_0Stagn

            #19 Плотность ρ_1 на входе в колесо
            rho_1 = p_1/engine['exhaust']['R']/T_1

            #20 Средний диаметр решеток соплового аппарата на выходе
            #   и рабочего колеса на входе
            D_1 = 60*u_1/math.pi/Compressor.RPM

            #21 Высота лопаток соплового аппарата
            l_1 = G_T/math.pi/D_1/rho_1/c_1/\
                math.sin(math.radians(turbine['geometry']['alpha_1']))

            if (l_1/D_1 < 0.16) or (l_1/D_1 > 0.25):
                exit("\033[91mERROR 21:\
                     Blade height 'l_1' is not in the allowable diapason!\
                     \nIt equals %0.2f but must be from 0.16 to 0.25"
                     .replace('                     ', ' ')
                     %(l_1/D_1))

            #22 Шаг решётки соплового аппарата
            t_1_0 = turbine['geometry']['coefficients']['t1Tol1']*l_1

            #23 Число лопаток соплового аппарата
            z_1 = round(math.pi*D_1/t_1_0)

            #23 Шаг решётки соплового аппарата с учётом округления числа
            #   лопаток
            t_1 = math.pi*D_1/z_1

            #25 Число Маха на выходе из сопловой решетки
            M_c1 = c_1/math.sqrt(engine['exhaust']['k']
                                 *engine['exhaust']['R']*T_1)

            #26 Ширина решетки в наиболее узкой ее части
            if (M_c1 > 0.4) and (M_c1 < 0.6):
                a_1 = t_1\
                      *math.sin(math.radians(turbine['geometry']['alpha_1']))\
                      /turbine['geometry']['coefficients']['m']

            elif M_c1 >= 0.6:
                a_1 = t_1\
                      *math.sin(math.radians( turbine['geometry']['alpha_1']))

            else:
                exit("\033[91mERROR 26:\
                     Mach number is not in the allowable diapason!\
                     \nIt equals %0.1f but must be at least more then 0.4"
                     .replace('                     ', ' ')
                     %(M_c1))

            #27 Ширина b_1 соплового аппарата по направлению оси вращения
            b_1 = math.sin(math.radians(turbine['geometry']['alpha_1'])*t_1*2)\
                  *math.sin(math.radians(turbine['geometry']['alpha_0']
                            + turbine['geometry']['alpha_1']))\
                  /math.sin(math.radians(turbine['geometry']['alpha_0']))\
                  /turbine['efficiency']['c_u1']

            #28 Относительная скорость w1 на входе в рабочее колесо
            w_1 = math.sqrt(c_1**2 + u_1**2
                            - 2*c_1*u_1*math.cos(math.radians(turbine\
                                                              ['geometry']\
                                                              ['alpha_1'])))

            #29 Изоэнтропная работа расширения в рабочем колесе
            #   (располагаемый теплоперепад) на входе в колесо
            L_pS = turbine['efficiency']['rho']*L_TsStagn

            #31 Относительная скорость на среднем диаметре D_2
            w_2 = turbine['losses']['psi']*math.sqrt(2*L_pS + w_1**2)

            #32 Температура Т_2 на выходе из колеса
            T_2 = T_1 - (w_2**2 - w_1**2)/2/engine['exhaust']['c_p']

            #33 Плотность на выходе из колеса
            rho_2 = p_2/engine['exhaust']['R']/T_2

            #35 Площадь проходного сечения F_2 на выходе из колеса
            F_2 = math.pi*D_1*l_1

            #36 Осевая составляющая относительной скорости
            #   на выходе в первом приближении
            w_2a = G_T/F_2/rho_2

            #37 Угол β_2 наклона вектора относительной скорости w2
            #   на выходе из рабочего колеса
            beta_2_0 = math.degrees(math.asin(w_2a/w_2))

            #38 Утечки через этот радиальный зазор Δ между корпусом
            #   и колесом турбины составят
            G_losses = turbine['geometry']['delta']\
                       *G_T/l_1/math.sin(math.radians(beta_2_0))

            #39 Расход через сечение F_2
            G_F2 = G_T - G_losses

            #40 Осевые составляющие относительной w_2a и абсолютной с_2а
            #   скоростей на выходе из колеса (w_2a == с_2а)
            c_2a = G_F2/F_2/rho_2

            #41 Уточнённый угол β_2 наклона вектора относительной скорости
            #   w2 на выходе из рабочего колеса
            beta_2 = math.degrees(math.asin(c_2a/w_2))

            #42 Окружная составляющая с_2u абсолютной скорости на выходе из
            #   колеса
            c_2u = w_2*math.cos(math.radians(beta_2)) - u_1

            #43 Абсолютная скорость на выходе из колеса
            c_2 = math.sqrt(c_2a**2 + c_2u**2)

            #44 Угол α_2 выхода потока из колеса в абсолютном движении
            alpha_2 = math.degrees(math.asin(c_2a/c_2))
            if (alpha_2 < 80) or (alpha_2 > 100):
                exit("\033[91mERROR 44:\
                     Angle 'alpha_2' is not in the allowable diapason!\
                     \nIt equals %0.1f but must be from 80 to 100 degrees."
                     .replace('                     ', ' ')
                     %alpha_2)

            #45 Шаг решётки рабочего колеса
            t_2_0 = turbine['geometry']['coefficients']['t2Tol2']*l_1

            #46 Число лопаток рабочего колеса
            z_2 = round(math.pi*D_1/t_2_0)

            #47 Шаг решётки рабочего колеса с учётом округления числа лопаток
            t_2 = math.pi*D_1/z_2

            #48 Число Маха на выходе из сопловой решетки
            M_w2 = w_2/math.sqrt(engine['exhaust']['k']
                                 *engine['exhaust']['R']*T_2)

            #49 Ширина решетки в наиболее узкой ее части
            if (M_c1 > 0.4) and (M_c1 < 0.6):
                a_2 = t_2*math.sin(math.radians(beta_2))/m

            elif M_c1 >= 0.6:
                a_2 = t_2*math.sin(math.radians(beta_2))

            else:
                exit("\033[91mERROR 49:\
                     Mach number is not in the allowable diapason!\
                     \nIt equals %0.1f but must be at least more then 0.4"
                     .replace('                     ', ' ')
                     %(M_c1))

            #50 Ширина b_2 рабочего колеса по направлению оси вращения
            b_2 = (2*t_2*math.sin(math.radians(beta_2))
                  /turbine['efficiency']['c_u2']/math.sin(math.radians(beta_1))
                  *math.sin(math.radians(beta_1 + beta_2)))

            #51 Потери в сопловом аппарате турбины
            Z_c = (1/turbine['losses']['phi']**2 - 1)*c_1**2/2

            #52 Потери в рабочем колесе
            Z_p = (1/turbine['losses']['psi']**2 - 1)*w_2**2/2

            #53 Суммарные потери в лопаточных каналах
            Z_Blades = Z_c + Z_p

            #54 Лопаточная работа турбины
            L_TBlades = L_TsStagn - Z_Blades

            #55 Лопаточный КПД η_(т.л) турбины
            eta_TBlades = L_TBlades/L_TsStagn

            #56 Потери в Z′_в с выходной скоростью при условии
            #   равномерного потока на выходе из рабочего колеса
            Z_SteadyOutlet = c_2**2/2

            #57 Работа L′_тu на окружности колеса c учётом потерь
            #   (определёная через потери)
            L_TuFromLosses = L_TBlades - Z_SteadyOutlet

            #58 Работа L′_тu на окружности колеса c учётом потерь
            #   (определёная с помощью формулы Эйлера)
            L_Tu = u_1*(c_1u + c_2u)

            #59 Окружной КПД η_тu турбины
            eta_Tu = L_Tu/L_TsStagn
            if (eta_Tu < 0.8) or (eta_Tu > 0.9):
                exit("\n\033[91mERROR 59:\
                     ECE 'eta_Tu' is not in the allowable diapason!\
                     \nIt equals {0:.3f} but must be from 0.8 to 0.9\n"
                     .replace('                     ', ' ')
                     .format(eta_Tu))

            #60 Потери Z_у, обусловленные утечкой газа через радиальные
            #   зазоры между колесом и корпусом
            Z_y = L_Tu*G_losses/G_T

            #61 Мощность N_тв, затрачиваемая на трение колеса в корпусе и
            #   вентиляцию
            N_TB = 735.5*turbine['geometry']['coefficients']['beta']\
                   *(rho_1 + rho_2)/2*D_1**2*pow(u_1/100, 3)

            #62 Потери Z_тв на трение и вентиляцию
            Z_TB = N_TB/G_T

            #63 Суммарные дополнительные потери Z_д,
            #   включающие потери на утечки, трение и вентиляцию
            Z_extra = Z_y + Z_TB

            #64 Внутренняя работа L_тi турбины
            L_Ti = L_Tu - Z_extra

            #65 Внутренний КПД η_тi турбины
            eta_Ti = L_Ti/L_TsStagn

            #66 Эффективный КПД η`_тe турбины
            eta_TeRated = turbine['efficiency']['eta_m']*eta_Ti

            #67 Расхождение с заданным КПД турбины
            eta_error = (eta_TeRated - turbine['efficiency']['eta_Te'])\
                        /turbine['efficiency']['eta_Te']*100

            #68 Эффективная работа L_те турбины
            L_Te = eta_TeRated*L_TsStagn

            #69 Мощность N_т на валу турбины
            N_T = L_Te*G_T

            #70 Расхождение с мощностью N_к, потребляемой компрессором
            N_error = (Compressor.N_K - N_T)/Compressor.N_K*100

    else: None

    return turbine, Turbine


# ''' (C) 2018-2020 Stanislau Stasheuski '''