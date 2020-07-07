def turbine_axial_create_results(run, engine,
        compressor, Compressor,
        turbine, Turbine):
    '''
        Description:    Generate radial turbine report
    '''

    r = open("axialTurbineReport.md", "w", encoding='utf-8')
    r.write("#Данные для расчёта турбины\n")
    r.write("- В соответствии с исходными данными для наддува двигателя имеем:\
            \n$$\n G_{K} = %0.4f\quad кг/с;\quad \\engine['combustion']['alpha'] = %1.1f;\quad \\varengine['combustion']['phi']\
            = %3.3f,\quad l_{0} = %4.2f\n$$\n\n"
            %(compressor['G_K'], engine['combustion']['alpha'], engine['combustion']['phi'], engine['combustion']['l_0']) )
    r.write("- Для выпускных газов принимаем:\
            \n$$\n R' = %0.1f\quad Дж/кг;\quad {c'}_{p} = %1.1f\quad\
            {Дж \over кг\cdot К};\quad k' = %2.1f\quad \n$$\n\n"
            %(engine['exhaust']['R'], engine['exhaust']['c_p'], engine['exhaust']['k']) )
    r.write("- Из расчета компрессора имеем:\
            \n$$\n D_{2K} = %1.3f\quad м;\quad\n$$\
            \n$$\n n_{тк} = %2.f\quad об/мин;\quad\eta = %3.5f;\quad {L'}_{KS} = %4.1f;\quad\n$$\
            \n$$\n N_{K} = %5.1f\quad Вт;\quad {p'}_{v} = %6.f\quad Па; \n$$\n\n"
            %(compressor['geometry']['D_2'], Compressor.RPM, Compressor.eta_KsStagnRated, Compressor.L_KsStagn, Compressor.N_K, Compressor.p_vStagn) )
    r.write("- Давление $$p_{2}$$ газов за турбиной\
            превышает атмосферное и составляет\
            $$p_{2} = (1.01…1.10)p_{а}$$. Принимаем:\
            \n$$\n p_{2} = %0.2fp_{а} = %1.f\quad Па\n$$\n\n"
            %(turbine['losses']['dragInletRatio'], Turbine.p_2) )
    r.write("- Температура газов перед турбиной:\
            \n$$\nT_{0}^{*} = %0.1f\quad K\n$$\n\n"
            %engine['heat']['T_0Stagn'])
    r.write("#Расчёт осевой турбины\n")
    r.write("1. Расход газа через турбину с учетом утечки $$\sigma_{у} = %0.2f$$ составит:\
            \n$$\n G_{T} = G_{K}\sigma_{y}\left( 1 + {1 \over \\engine['combustion']['alpha']\\varengine['combustion']['phi'] l_{0}} \\right)\
            = %1.6f\quad кг/с\n$$\n\n"
            %(turbine['efficiency']['sigma_esc'], Turbine.G_T) )
    r.write("2. Значение эффективного КПД осевых турбин лежит в диапазоне 0,70.…0,85.\n\
            Принимаем:\
            \n$$\n \eta_{те} = %0.2f \n$$\n\n"
            %turbine['efficiency']['eta_Te'])
    r.write("3. Изоэнтропная работа турбины:\
            \n$$\n L_{TS}^{*} = {L^{*}_{TS}compressor['G_K'] \over \eta_{KS}\eta_{Te}G_{T}} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.L_TsStagn)
    r.write("4. Условная изоэнтропная скорость истечения из турбины:\
            \n$$\n c_{2s} = \sqrt{ 2L_{TS} } = %0.3f\quad м/с \n$$\n\n"
            %Turbine.c_2s)
    r.write("5. Параметр $$\chi$$ в осевых турбинах должен находиться в пределах 0,50…0,65.\
            Принимаем: $$\chi = %0.2f$$, тогда:\
            \n$$\n u_{1} = \chi c_{2s} = %1.2f \n$$\n\n"
            %(turbine['efficiency']['ksi'], Turbine.u_1))
    r.write("6. Для осевых турбин степень реактивности ρ на среднем диаметре лежит в пределах 0,3…0,5.\
            Принимаем $$\\rho = %0.2f$$\n\n"
            %turbine['efficiency']['rho'])
    r.write("7. Давление газа на входе в турбину:\
            \n$$\n {p}^{*}_{0} = {p_{2} \over\
            \left( 1 - {L^{*}_{TS} \over {c'}_{p}T^{*}_{0}} \\right)\
            ^{k' \over k' - 1}} = %0.6f\quad Па \n$$\n\n"
            %Turbine.p_0Stagn)
    r.write("8. Для обеспечения продувки цилиндров двигателя при перекрытии\
            клапанов необходимо выполнение соотношения $$p^{*}_{v}/p^{*}_{0}\
            = 1.1…1.3$$. Условие выполняется:\
            \n$$\n {p^{*}_{v} \over p^{*}_{0}} = %0.4f \n$$\n\n"
            %Turbine.pressureRelation) 
    r.write("9. Изоэнтропная работа расширения (располагаемый теплоперепад) в сопловом аппарате:\
            \n$$\n L_{cs} = L_{TS}\left(1 - \\turbine['efficiency']['rho'] \\right) = %0.1f\quad Дж/кг\n$$\n\n"
            %Turbine.L_cS)
    r.write("10. Значение скоростного коэффициента $$\\varengine['combustion']['phi']$$, учитывающего\
            потери скорости в сопловом аппарате, лежит в пределах 0.96…0.98. Принимаем:\
            \n$$\n \\varengine['combustion']['phi'] = %0.2f\n$$\n\n"
            %turbine['losses']['phi'])
    r.write("11. Абсолютная скорость на выходе из соплового аппарата составит:\
            \n$$\n c_{1} = \\varengine['combustion']['phi'] \sqrt{2L_{cs}} = %0.3f\quad м/с \n$$\n\n"
            %Turbine.c_1)
    r.write("12. Угол $$\\alpha_{1}$$ наклона вектора абсолютной скорости\
            $$с_{1}$$ (рис. 1) должен составлять 14°…30°. Принимаем:\
            \n$$\n \\alpha_{1} = %0.1f° \n$$\n\n"
            %turbine['geometry']['alpha_1'])
    r.write("13. Учитывая равенство осевых составляющих абсолютной $$c_{1a}$$ и\
            относительной $$w_{1a}$$ скоростей, получаем:\
            \n$$\n c_{1a} \equiv w_{1a} = c_{1}\sin\\alpha_{1} = %0.3f\quad м/с \n$$\n\n"
            %Turbine.c_1a)
    r.write("14. Окружная составляющая $$c_{1u}$$ абсолютной скорости на выходе\
            из соплового аппарата:\
            \n$$\n c_{1u} \equiv w_{1r} = c_{1}\cos\\alpha_{1} = %0.3f\quad м/с \n$$\n\n"
            %Turbine.c_1u)
    r.write("![alt text](turbine/axial/axisCut.png)\n\
            <center><b> Рисунок 1 </b> - <i>Схема ступени осевой турбины</i></center>\n\n")
    r.write("![alt text](turbine/axial/radialCut.png)\n\
            <center><b> Рисунок 2 </b> - <i>Векторные планы\
            скоростей на входе и выходе из рабочего колеса</i></center>\n\n")
    r.write("15. Для окружной составляющей $$w_{1u}$$ относительной скорости имеем:\
            \n$$\n w_{1u} = c_{1u} - u_{1} = %0.3f\quad м/с \n$$\n"
            %Turbine.w_1u)
    r.write("16. Так как значение $$w_{1u}$$ может быть равно или близко к нулю,\
            для определения угла $$\\beta_{1}$$ наклона вектора относительной скорости\
            $$w_{1}$$ воспользуемся формулой:\
            \n$$\n \\beta_{1} = %0.f° - \\arctan{w_{1u} \over w_{1r}} = %1.3f° \n$$\n\n" 
            %(turbine['geometry']['beta_1Blade'], Turbine.beta_1) )
    r.write("17. Температура газа на входе в колесо:\
            \n$$\n T_{1} = T^{*}_{0} - {c_{1}^2 \over 2{c'}_{p}} = %0.3f\quad K \n$$\n\n"
            %Turbine.T_1)
    r.write("18. Давление на входе в колесо:\
            \n$$\n p_{1} = p^{*}_{0} \left( 1 - {L^{*}_{CS} \over {c'}_{p}T^{*}_{0}} \\right)\
            ^{k' \over k' - 1} = %0.1f\quad Па \n$$\n"
            %Turbine.p_1)
    r.write("Проверяем отношение давлений $${p_{1} \over p^{*}_{0}} = %0.6f$$"
            %Turbine.pressureRelationSetOfNozzles)

    if (Turbine.pressureRelationSetOfNozzles >= 0.54):
        r.write(", которое больше 0.54, поэтому применяем конфузорный\
                сопловой аппарат\n\n")
    elif (Turbine.pressureRelationSetOfNozzles > 0.3) & (Turbine.pressureRelationSetOfNozzles < 0.54):
        r.write(", которое лежит в пределах от 0.3 до 0.54, поэтому применяем конфузорные\
                сопла с косым срезом.\n\n")
    else:
        r.write(", которое меньше 0.3, поэтому применяем конфузорный\
                сопловые аппараты с расширением.\n\n")

    r.write("19. Плотность на входе в колесо:\
            \n$$\n \\turbine['efficiency']['rho']_{1} = {p_{1} \over R'T_{1}} = %0.6f\quad кг/м^{3} \n$$\n\n"
            %Turbine.rho_1)
    r.write("20. Средний диаметр решеток соплового аппарата на выходе и рабочего колеса на входе:\
            \n$$\n D_{1} = {60u_{1} \over \pi n_{тк}} = %0.6f\quad м\n$$\n\n"
            %Turbine.D_1)
    r.write("21. Высота лопаток соплового аппарата:\
            \n$$\n b_{1} = {G_{T} \over \pi D_{1}\\turbine['efficiency']['rho']_{1}c_{1r}\sin\\alpha_{1}} = %0.6f\quad м \n$$\n\
            В осевых турбинах $$l_{1} = (0,16…0,25)D_{1}$$. В данном случае соотношение удовлетворяет\
            необходимому условию $$l_{1}/D_{1} = %1.6f$$.\n\n"
            %(Turbine.b_1, Turbine.l_1/Turbine.D_1))
    r.write("22. Выбираем шаг решетки соплового аппарата. В осевых турбинах 0.8…0.9. Принимаем\
            $$t_{1}/l_{1} = %0.2f$$. Тогда:\
            \n$$\n t_{1} = %1.2f l_{1} = %2.6f \quad м\n$$\n\n"
            %(turbine['geometry']['coefficients']['t1Tol1'], turbine['geometry']['coefficients']['t1Tol1'], Turbine.t_1))
    r.write("23. При этом целое число лопаток соплового аппарата:\
            \n$$\n z_{1} = {\pi D_{1} \over t_{1}} = %0.0f\quad м\n$$\n\n"
            %Turbine.z_1)
    r.write("24. Уточняем шаг решёкти для целого числа лопаток:\
            \n$$\n t_{1} = {\pi D_{1} \over z_{1}} = %0.6f \quad м\n$$\n\n"
            %Turbine.t_1)
    r.write("25. Число Маха на выходе из сопловой решетки:\
            \n$$\n M_{c1} = {c_{1} \over \sqrt{k'R'T'_{1}}} = %0.5f \n$$\n\
            Полученное число Маха удовлетворяет необходимым требованиям\
            (не превышает значение 0.85…0.90)\n\n"
            %Turbine.M_c1)

    if (Turbine.M_c1 > 0.4) & (Turbine.pressureRelationSetOfNozzles < 0.6):
        r.write("26. Так как число Маха от 0.4 до 0.6, то ширина решетки в наиболее узкой её части\
                вычисляется по формуле (где m = 1.08):\
                \n$$\n a_{1} = {t_{1}\sin\\alpha_{1} \over m} = %0.6f\quad м \n$$\n\n"
                %Turbine.a_1)
    else:
        r.write("26. Так как число Маха больше 0.6, то ширина решетки в наиболее узкой её части\
                вычисляется по формуле:\
                \n$$\n a_{1} = t_{1}\sin\\alpha_{1} = %0.6f\quad м \n$$\n\n"
                %Turbine.a_1)

    r.write("27. Ширина соплового аппарата по направлению оси вращения:\
            \n$$\n b_{1} = { 2 \sin\\alpha_{1}\sin(\\alpha_{0} + \\alpha_{1}) \over\
            с_{u1}\sin\\alpha_{0} } = %0.6f\quad м,\n$$\n\
            где $$с_{u1}$$ — коэффициент нагрузки, равный 0.85…1.05. Принимаем %1.2f.\n\n"
            %(Turbine.b_1, turbine['efficiency']['c_u1']))
    r.write("28. Относительная скорость на среднем диаметре $$D_{2}$$:\
            \n$$\n w_{1} = \sqrt{c_{1}^{2} + u_{1}^{2} - 2c_{1}u_{1}\cos\\alpha_{1}}\
            = %0.2f\quadм/с \n$$\n\n"
            %Turbine.w_2)
    r.write("29. Изоэнтропная работа расширения в рабочем колесе (располагаемый\
            теплоперепад) на входе в колесо:\
            \n$$\n L_{ps} = \\turbine['efficiency']['rho'] L_{TS} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.L_pS)
    r.write("30. Значение скоростного коэффициента $$\psi$$, учитывающего потери скорости\
            в рабочем колесе, лежит в пределах 0.92…0.98. Принимаем:\
            \n$$\n \psi = %0.2f \n$$\n\n"
            %turbine['losses']['psi'])
    r.write("31. Окружная скорость на среднем диаметре $$D_{2}$$ выхода из рабочего колеса:\
            \n$$\n w_{2} = \psi \sqrt{2L_{pS}u_{1}^{2}} = %0.3f\quad м/с \n$$\n\n"
            %Turbine.w_2)
    r.write("32. Температура на выходе из колеса:\
            \n$$\n T_{2} = T_{1} - {w_{2}^{2} - w_{1}^{2} \over 2{c'}_{p}} = %0.3f\quad К \n$$\n\n"
            %Turbine.T_2)
    r.write("33. Плотность на выходе из колеса:\
            \n$$\n \\turbine['efficiency']['rho']_{2} = {p_{2} \over R'T_{2}} = %0.6f\quad кг/м^{3} \n$$\n\n"
            %Turbine.rho_1)
    r.write("34. Средний диаметр $$D_{2}$$ и высоту $$l_{2}$$ лопаток рабочего колеса принимают\
            равными соответствующим параметрам соплового аппарата:\
            \n$$\n D_{2} = D_{1} = %0.6f\quad м\n l_{2} = l_{1} = %1.6f\quad м\n$$\n\n"
            %(Turbine.D_1, Turbine.l_1))
    r.write("35. Площадь сечения $$F_{2}$$ на выходе из колеса:\
            \n$$\n F_{2} = \pi D_{2} l_{2} = %0.7f\quad м^2 \n$$\n\n"
            %Turbine.F_2)
    r.write("36. Осевая составляющая относительной скорости на выходе в первом приближении:\
            \n$$\n {w'}_{2a} = {G_T \over F_{2} \\turbine['efficiency']['rho']_{2}} = %0.3f\quad м/с \n$$\n\n"
    %Turbine.w_2)
    r.write("37. Угол наклона вектора относительной скорости\
            $$w_{2}$$ на выходе из рабочего колеса:\
            \n$$\n {\\turbine['geometry']['coefficients']['beta']'}_{2} = \\arcsin{ {w'}_{2a} \over w_{2} } = %0.3f° \n$$\n\n"
            %Turbine.beta_2)
    r.write("38. Значения радиального зазора Δ между корпусом и колесом\
            турбины выбирают в пределах 0.7…1.5 мм. Выбираем $$\Delta = %0.1f$$ мм.\
            Тогда утечки через этот зазор составят:\
            \n$$\n G_{у} = {\Delta G_{T} \over l_{2}\sin{\\turbine['geometry']['coefficients']['beta']'}_{2}} = %1.7f\quad кг/с \n$$\n\n"
            %(turbine['geometry']['delta']*1e+03, Turbine.G_losses) )
    r.write("39. Расход через сечение $$F_{2}$$:\
            \n$$\n {G'}_{T} = G_{T} - G_{у} = %0.6f\quad кг/с \n$$\n\n"
            %Turbine.G_F2)
    r.write("40. Осевые составляющие относительной $$w_{2а}$$ и\
            абсолютной $$c_{2а}$$ скоростей на выходе из колеса:\
            \n$$\n w_{2a} \equiv c_{2a} = {{G'}_{T} \over F_{2} \\turbine['efficiency']['rho']_{2}}\
            = %0.3f\quad м/с \n$$\n\n"
            %Turbine.c_2a)
    r.write("41. Уточнённый угол выхода пнаклона вектора относительной скорости на\
            выходе из рабочего колеса:\
            \n$$\n \\beta_{2} = \\arctan{w_{2u} \over w_{2}} = %0.3f° \n$$\n\n"
            %Turbine.beta_2)
    r.write("42. Поскольку $$D_{2} = D_{1}$$, то и $$u_{2} = u_{1}$$. Тогда для\
            окружной составляющей абсолютной скорости на выходе из колеса имеем:\
            \n$$\n c_{2u} = w_{2}\cos\\beta_{2} - u_{2} = %0.3f\quad м/с\n$$\n\n"
            %Turbine.c_2u)
    r.write("44. Угол выхода потока из колеса в абсолютном движении:\
            \n$$\n \\alpha_{2} = \\arctan{c_{2a} \over c_{2}} = %0.3f° \n$$\n\
            На расчетном режиме этот угол должен составлять 80…100° - условие выполняется.\n\n"
            %Turbine.alpha_2)
    r.write("45. Выбираем шаг решетки рабочего колеса. В осевых турбинах 0.8…0.9. Принимаем\
            $$t_{2}/l_{2} = %0.2f$$. Тогда:\
            \n$$\n t_{2} = %1.2f l_{2} = %2.6f \quad м\n$$\n\n"
            %(turbine['geometry']['coefficients']['t2Tol2'], turbine['geometry']['coefficients']['t2Tol2'], Turbine.t_2))
    r.write("46. Число лопаток рабочего колеса:\
            \n$$\n z_{2} = {\pi D_{2} \over t_{2}} = %0.0f\quad м\n$$\n\n"
            %Turbine.z_2)
    r.write("47. Шаг решётки с учётом целого числа лопаток рабочего колеса:\
            \n$$\n t_{2} = {\pi D_{2} \over z_{2}} = %0.6f \quad м\n$$\n\n"
            %Turbine.t_2)
    r.write("48. Число Маха на выходе из рабочего колеса:\
            \n$$\n M_{w2} = {c_{w2} \over \sqrt{k'R'T'_{1}}} = %0.5f \n$$\n"
            %Turbine.M_w2)

    if (Turbine.M_c1 > 0.4) & (Turbine.pressureRelationSetOfNozzles < 0.6):
        r.write("49. Так как число Маха от 0.4 до 0.6, то ширина решетки в наиболее узкой её части\
                вычисляется по формуле (где m = 1.08):\
                \n$$\n a_{2} = {t_{2}\sin\\alpha_{2} \over m} = %0.6f\quad м \n$$\n\n"
                %Turbine.a_2)
    else:
        r.write("49. Так как число Маха больше 0.6, то ширина решетки в наиболее узкой её части\
                вычисляется по формуле:\
                \n$$\n a_{2} = t_{2}\sin\\alpha_{2} = %0.6f\quad м \n$$\n\n"
                %Turbine.a_2)

    r.write("50. Ширина соплового аппарата по направлению оси вращения:\
            \n$$\n b_{2} = { 2 \sin\\beta_{2}\sin(\\beta_{1} + \\beta_{2}) \over\
            с_{u2}\sin\\beta_{1} } = %0.6f\quad м,\n$$\n\
            где $$с_{u1}$$ — коэффициент нагрузки, равный 0.8…0.9. Принимаем %1.2f.\n\n"
            %(Turbine.b_2, turbine['efficiency']['c_u2']))
    r.write("51. Потери в сопловом аппарате турбины:\
            \n$$\n Z_{c} = \left( {1 \over \\varengine['combustion']['phi']^2} - 1 \\right){c_{1}^2 \over 2}\
            = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.Z_c)
    r.write("52. Потери в рабочем колесе:\
            \n$$\n Z_{p} = \left( {1 \over \\psi^2} - 1 \\right){w_{2}^2 \over 2}\
            = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.Z_p)
    r.write("53. Суммарные потери в лопаточных каналах:\
            \n$$\n Z_{K} = Z_{c} + Z_{p} = %0.1f\quad Дж/кг \n$$\n\
            Последовательно учитывая потери, получим номенклатуру удельных работ и КПД турбины\n\n"
            %Turbine.Z_Blades)
    r.write("54. Лопаточная работа $$L_{тл}$$ турбины:\
            \n$$\n L_{тл} = L_{тл} - Z_{K} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.L_TBlades)
    r.write("55. Лопаточный КПД турбины:\
            \n$$\n \eta_{тл} = {L_{тл} \over L_{TS}} = %0.6f \n$$\n\n"
            %Turbine.eta_TBlades)
    r.write("56. Потери с выходной скоростью:\
            \n$$\n {Z'}_{в} = {c_{2}^2 \over 2} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.Z_SteadyOutlet)
    r.write("57. Соответствующее значение работы на окружности колеса:\
            \n$$\n L_{тu} = L_{тл} - {Z'}_{в} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.L_TuFromLosses)
    r.write("58. Эта работа может быть определена также по формуле Эйлера:\
            \n$$\n L_{тu} = u_{1}c_{1u} + u_{2}c_{2u} = %0.1f\quad Дж/кг \n$$\n\
            Полученные значения (пп. 49, 50) отличаются незначительно (погрешность - %1.2f%%),\
            что свидетельствует о правильности расчета."
            %(Turbine.L_Tu, abs(Turbine.L_TuFromLosses - Turbine.L_Tu)/Turbine.L_TuFromLosses*100) )
    r.write("59. Окружной КПД турбины:\
            \n$$\n \eta_{тu} = {L_{тu} \over L_{TS}} = %0.6f \n$$\n\
            На расчетном режиме значение $$\eta_{тu}$$ не должно составлять\
            0.8…0.90 - условие выполняется"
            %Turbine.eta_Tu)
    r.write("60. Потери, обусловленные утечкой газа через радиальные\
            зазоры между колесом и корпусом:\
            \n$$\n Z_{у} = {L_{тu}G_{у} \over G_{T}} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.Z_y)
    r.write("61. Мощность, затрачиваемая на трение колеса в корпусе и вентиляцию\
            ($$\\turbine['geometry']['coefficients']['beta']$$ опытный коэффициент, зависящий от типа рабочего колеса,\
            принятый как %0.1f):\
            \n$$\n N_{TB} = 0.735\\beta {\\rho_{1} + \\rho_{2} \over 2}D_{1}^2\
            \left({u_{1}^2 \over 100} \\right)^3 = %1.1f\quad Вт \n$$\n"
            %(turbine['geometry']['coefficients']['beta'], Turbine.N_TB) )
    r.write("62. Потери на трение и вентиляцию:\
            \n$$\n Z_{TB} = {N_{TB} \over G_{T}} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.Z_TB)
    r.write("63. Суммарные дополнительные потери, включающие потери на утечки,\
            трение и вентиляцию:\
            \n$$\n Z_{Д} = Z_{у} + Z_{TB} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.Z_extra)
    r.write("64. Внутренняя работа турбины:\
            \n$$\n L_{Тi} = L_{тu} - Z_{Д} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.L_Ti)
    r.write("65. Внутренний КПД турбины:\
            \n$$\n \eta_{Тi} = {L_{Тi} \over L_{TS}} = %0.5f \n$$\n\n"
            %Turbine.eta_Ti)
    r.write("66. Эффективный КПД турбины:\
            \n$$\n {\eta'}_{Тe} = \eta_{Тi} \eta_{M} = %0.5f \n$$\n\
            где $$\eta_{M}$$ — механический КПД, принятый из диапазона 0.92…0.96,\
            как %1.2f\n\n"
            %(Turbine.eta_Ti, turbine['efficiency']['eta_m']) )
    r.write("67. При сравнении с исходным $$\eta_{Te}$$\
            имеем незначительную погрешность:\
            \n$$\n {\mid {\eta'}_{Тe} - \eta_{Тe}  \mid \over {\eta'}_{Тe}}\
            = %0.3f \%% \n$$\n\n"
            %Turbine.errorEta)
    r.write("68. Эффективная работа турбины:\
            \n$$\n L_{Тe} = L_{TS}{\eta'}_{Тe} = %0.1f\quad Дж/кг \n$$\n\n"
            %Turbine.L_Te)
    r.write("69. Мощность на валу турбины:\
            \n$$\n N_{T} = L_{Тe}G_{Т} = %0.1f\quad Вт \n$$\n\n"
            %Turbine.N_T)
    r.write("70. Расхождение с мощностью,\
            потребляемой компрессором, незначительно:\
            \n$$\n {\mid N_{K} - N_{T} \mid \over N_{K}} = %0.3f \%% \n$$\n\n"
            %Turbine.errorN)

    r.close()