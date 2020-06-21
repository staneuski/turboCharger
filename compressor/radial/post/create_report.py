def create_report(run, engine, compressor, Compressor):
    '''
        Create the report for a compressor
    '''

    report = open("compressorReport.md", "w")

    # Предварительные расчёты
    if 'TYPE1' in run['type']:
        p_e_MPa = engine['efficiency']['p_e']*1e-06
        report.write(
    "# Предварительные расчёты\
    \n- Среднее эффективное давление:\
    \n$$\n p_{e} = {0,12*10^{3}N_{e}\\tau \over \pi D^{2}Sni} = %0.4f \quad МПа,\n$$\
    \n\n- Расход: \n\
    $$\n G_{к} = {N_{e}g_{e}l_{0}\\engine['combustion']['alpha']\\engine['combustion']['phi'] \over 3600} = %1.4f \quad кг/с, \n$$\n\
    \n- Предварительная оценка диаметра колеса:\
    \n$$\n D_{2} = 160G_{K} + 40 = %2.0f \quad мм, \n$$\n\
    \n- Cтепень повышения давления полученная методом последовательных приближений:\
    \n$$\n \pi_{к} = %3.4f, \n$$\n\n" %(p_e_MPa, compressor['G_K'], Compressor.D_2Init*1e+03, compressor['pi_K'])
    )

    else:   report.write(
    "# Данные для расчёта компрессора\n\
    - Расход:\
    \n$$\n G_{к} = %0.2f \quad кг/с, \n$$\n\n\
    - Cтепень повышения давления:\
    \n$$\n \pi_{к} = %1.2f, \n$$\n\n" %(compressor['G_K'], compressor['pi_K'])
    )

    ## Расчёт
    report.write("# Расчёт компрессора\
    \nРасчет был выполнен в следующем порядке.\n\n")
    report.write("1. Температура $$ T_{0}^{*} $$ и давление $$ p_{0}^{*} $$\
    торможения на входе в компрессор ($$ \sigma_{0} = %0.2f$$):\
    \n$$\n T_{0}^{*} = T_{0}^{*} = %1.f\quad К\quad\
    p_{0}^{*} = \sigma_{0}p_{a}^{*} = %2.f\quad  Па \n$$\n\n"
    %(compressor['losses']['sigma_0'], compressor['initial']['T_aStagn'], compressor['initial']['p_aStagn']) )
    report.write("2. Скорость воздуха на входе в компрессор выбирают в пределах 30…80 м/c.\
    Принимаем $$ с_{0} = %0.f $$ м/с.\n\n"
    %compressor['initial']['c_0'])
    report.write("3. Статические температура и давление на входе в компрессор:\
    \n$$\n T_{0} = T_{0}^{*} - {c_{0}^{*} \over 2c_{p}} = %0.3f\quad К\quad\
    p_{0}^{*} = p_{0}^{*} \left( {T_{0} \over T_{0}^{*}} \\right)^{k \over k-1}\
    = %1.0f \quad Па \n$$\n\n"
    %(Compressor.T_0, Compressor.p_0) )
    report.write("4. Изоэнтропная работа сжатия в компрессоре:\
    \n$$\n L_{КS}^{*} = c_{p}T_{0}^{*} \left( (\pi_К^{*})^{k \over k-1} - 1\\right)\
    = %0.1f \quad Дж/кг \n$$\n\n"
    %Compressor.L_KsStagn)
    report.write("5. С помощью зависимостей, приведенных на рисунке 2.2[1],\
    для ожидаемого значения $$ D_{2} = %0.f $$ мм выберем коэффициент напора\
    по заторможенным параметрам (напорный изоэнтропный КПД).\
    Пусть в первом приближении $$ H_{KS}^{*} = %1.2f. $$\
    Окружную скорость на наружном диаметре колеса компрессора вычисляем по формуле:\
    \n$$\n u_{2} = \sqrt{L_{КS}^{*} \over H_{KS}^{*}} = %3.2f  \quad м/с\n$$\n\
    По соображениям прочности рабочего колеса значение окружной скорости должно составлять\
    u2 ≤ 450…550 м/с.\n\n"
    %(Compressor.D_2Init*1e+03, compressor['efficiency']['H_KsStagn'], Compressor.u_2))
    report.write("6. С помощью зависимостей, показанных на рис. 2.2[1],\
    выберем значение отношения осевой составляющей абсолютной скорости\
    потока на входе в рабочее колесо к окружной скорости на выходе — коэффициент расхода\
    $$ \\varengine['combustion']['phi'] = c_{1a}/u_{2} = %0.2f$$. В компрессорах, применяемых для наддува поршневых двигателей,\
    закрутка на входе в рабочее колесо практически не применяется, т. е.\
    $$ c_{1u} = 0 $$ и $$ c_{1} = c_{1a} $$. Тогда\
    \n$$\n c_{1} = \\varengine['combustion']['phi'] u_{2} = %1.2f \quad м/с. \n$$\n\n" %(compressor['efficiency']['phi_flow'], Compressor.c_1))
    report.write("7. Температура воздуха на входе в рабочее колесо\
    \n$$\n T_{1} = T_{0} + {c_{0}^{2}-c_{1}^{2} \over 2c_{p}} = %0.2f \quad K \n$$\n\n"
    %Compressor.T_1)
    report.write("8. Для расчета потерь энергии во впускном патрубке из\
    диапазона 0.03…0.06 выбираем значение $$ \zeta_{вп} = %0.3f $$. Тогда\
    \n$$\n \Delta L_{вп} = \zeta_{вп}{c_{1}^{2} \over 2} = %1.3f \quad Дж/кг \n$$\n\n"
    %(compressor['losses']['dzeta_inlet'], Compressor.L_inlet))
    report.write("9. Показатель политропы при течении во входном устройстве\
    определяем из выражения:\
    \n$$\n {n_{1} \over n_{1} - 1} = {k_{1} \over k_{1} - 1} -\
    {\Delta L_{вп} \over R(T_{1} - T_{0})} \n$$\n Тогда, решив уравнение методом\
    последовательных приближений, получим $$n_{1} = %0.5f$$\n\n"
    %Compressor.n_1)
    report.write("10. Теперь можно определить давление $$p_{1}$$ на входе в колесо:\
    \n$$\n p_{1}^{*} = p_{0} \left( {T_{1} \over T_{1}^{*}} \\right)^{k \over k-1}\
    = %1.0f \quad Па \n$$\n\n"
    %Compressor.p_1)
    report.write("11. Плотность на входе в колесо:\
    \n$$\n \\rho = {p_{1} \over RT_{1}} = %0.4f \quad Па \n$$\n\n"
    %Compressor.rho_1)
    report.write("12. Площадь поперечного сечения входа в колесо колесо:\
    \n$$\n F_{1} = {G_{K} \over c_{1}\\rho_{1}} = %0.6f \quad кг/м^{3} \n$$\n\n"
    %Compressor.F_1)
    report.write("13. Наружный диаметр колеса на входе определяется из соотношения\
    \n$$\n D_{1н} = \sqrt{{F_{1} \over (\pi/4)(1 - \overline{D}^2)}},\n$$\n где\
    $$ \overline{D} =  {\overline{D}_{1в} \over \overline{D}_{1н}} $$\n\
    Выбирая с помощью рис. 2.2[1] для ожидаемого значения диаметра\
    $$ D_{2} = %0.f $$ мм значения $$ \overline{D}_{1в} = %1.3f $$ и\
    $$ \overline{D}_{1н} = %2.3f $$. Тогда $$ D_{1н} = %4.5f $$\n\n"
    %(Compressor.D_2Init*1e+03, compressor['geometry']['coefficients']['relD_1B'], compressor['geometry']['coefficients']['relD_1H'], Compressor.D_1H) )
    report.write("14. Внутренний диаметр на входе (втулочный диаметр):\
    \n$$\n D_{1в} = \overline{D}D_{1н} = %0.5f \n$$\n\n" %Compressor.D_1B)
    if 'ON' in compressor['geometry']['coefficients']['DToSTD']:  report.write("15. Наружный диаметр колеса компрессора на выходе,\
    оценивается по формуле:\
    \n$$\n D_{2} = {D_{1н} \over \overline{D}_{1н}} = %0.4f\quad мм\n$$\n\
    После оценки диаметра, принимается ближайшее значение\
    из ряда нормальных значений: $$ D_2 = %1.f$$ мм\n\n"
    %(Compressor.D_2estimated, compressor['geometry']['D_2']*1e+03) )
    else:   report.write("15. Наружный диаметр колеса компрессора на выходе,\
    оценивается по формуле:\
    \n$$\n D_{2} = {D_{1н} \over \overline{D}_{1н}} = %0.4f\quad мм\n$$\n\
    При округлении до целового, диаметр принимается: $$ D_2 = %1.f$$ мм\n\n"
    %(Compressor.D_2estimated, compressor['geometry']['D_2']*1e+03) )
    report.write("16. Частота вращения ротора турбокомпрессора:\
    \n$$\n n_{тк} = {60u_{2} \over \pi D_{2}} = %0.1f\quad мин^{-1} \n$$\n\n"
    %Compressor.RPM)
    report.write("17. Средний диаметр на входе в колесо:\
    \n$$\n D_{1} = \sqrt{{ D_{1в}^2+D_{1н}^2 \over 2}} = %0.6f\quad м\n$$\n\n"
    %Compressor.D_1)
    report.write("18. Окружная скорость на среднем диаметре входа:\
    \n$$\n u_{1} = \pi D_{1} {n_{тк} \over 60} = %0.3f\quad м/c \n$$\n\n"
    %Compressor.u_1)
    report.write("19. Угол входа потока в рабочее колесо на среднем диаметре\
    в относительном движении:\
    \n$$\n \\beta_{1} = arctg \left({ c_{1} \over u_{1} }\\right) = %0.3f° \n$$\n\n"
    %Compressor.beta_1)
    report.write("20. Угол атаки _i_ на входе в колесо рекомендуется принимать в диапазоне 2…6°.\
    Выберем $$ i = %0.2f° $$, тогда можно назначить угол установки лопаток\
    на среднем диаметре $$ D_{1} $$:\
    \n$$\n \\beta_{1л} = \\beta_{1} + i = %1.3f° \n$$\n\
    Соответствующий план скоростей на входе в колесо показан на развертке\
    цилиндрического сечения, проведенного на диаметре $$D_{1}$$:\n"
    %(compressor['geometry']['iDeg'], Compressor.beta_1Blade) )
    report.write(
    "![alt text](compressor/blades.png)\n\
    <center>\
    <b> Рисунок 1 </b> - <i>Векторный план скоростей на входе в рабочее колесо компрессора</i>\
    </center>\n\n"
    )
    report.write("21. После входа в колесо значения абсолютной скорости $$с_{1}$$\
    возрастают в результате уменьшения проходного сечения вследствие загромождения\
    лопатками. Соответствующий коэффициент загромождения (стеснения)\
    $$\\tau_{1}$$, учитывающий толщину лопаток, составляет обычно 0.8…0.9.\
    Выберем значение $$\\tau_{1} = %0.2f$$. Тогда, с учетом загромождения:\
    \n$$\n c_{1\\tau} = {c_{1} \over \\tau_{1}} = %1.3f\quad м/с \n$$\n\n"
    %(compressor['load']['tau_1'], Compressor.c_1Tau) )
    report.write("22. Окружная скорость на наружном диаметре входа в колесо\
    \n$$\n u_{1н} = \pi D_{1н} {n_{тк} \over 60} = %0.3f\quad м/c \n$$\n\n"
    %Compressor.u_1H)
    report.write("23. Относительная скорость w1н на наружном диаметре входа в колесо\
    \n$$\n w_{1н} = \sqrt{c_{1\\tau}^2 + u_{1н}^2} = %0.3f\quad м/c \n$$\n\n"
    %Compressor.w_1H)
    report.write("24. Соответствующее число Маха:\
    \n$$\n M_{w1} = {w_{1н} \over \sqrt{kRT_{1}}} = %0.5f \n$$\n\
    Полученное число Маха удовлетворяет необходимым требованиям\
    (не превышает значение 0.85…0.90)\n\n"
    %Compressor.M_w1)
    report.write("25. Относительная скорость w1 на среднем диаметре входа:\
    \n$$\n M_{w1} = \sqrt{c_{1\\tau}^2 + u_{1}^2} = %0.3f\quad м/c \n$$\n\n"
    %Compressor.w_1)
    report.write("26. Потери (удельная работа потерь) во входном вращающемся направляющем\
    аппарате колеса оцениваются коэффициентом потерь $$\zeta_{ва}$$,\
    который лежит в пределах 0.1…0.3. Выберем значение $$\zeta_{ва} = %0.3f$$. Тогда\
    \n$$\n \Delta L_{ва} = \zeta_{ва}{w_{1}^2 \over 2} = %1.2f \quad Дж/кг \n$$\n\n"
    %(compressor['losses']['dzeta_BA'], Compressor.L_BA) )
    report.write("27. Радиальная составляющая $$c_{2r}$$ абсолютной скорости,\
    тождественно равная радиальной составляющей $$w_{2r}$$ относительной скорости на\
    выходе из колеса (рисунок 2), близка по значению к  $$c_{1a}$$ и составляет обычно\
    $$(0.9…1.2)c_{1a}$$. Принимая $$c_{2r} = %0.2fс_{1a}$$ , получаем:\
    \n$$\n c_{2r} \equiv w_{2r} = %1.3f\quad м/c \n$$\n\n"
    %(compressor['geometry']['coefficients']['relW_2rToC_1a'], Compressor.c_2r) )
    report.write("28. Потери $$\Delta L_{пт}$$ на поворот и трение в межлопаточных каналах\
    рабочего колеса оцениваются коэффициентом потерь $$\zeta_{пт}$$, значение которого\
    изменяется в пределах 0.1…0.2. Примем $$\zeta_{пт} = %0.3f$$. Тогда\
    \n$$\n \Delta L_{пт} = \zeta_{пт}{c_{2r}^2 \over 2} = %1.2f \quad Дж/кг \n$$\n\n"
    %(compressor['losses']['dzeta_TF'], Compressor.L_TF) )
    report.write("29. Потери на трение диска колеса о воздух в сумме с вентиляционными\
    потерями вычисляются по формуле:\
    \n$$\n \Delta L_{тв} = \\engine['combustion']['alpha'] u_{2}^2 = %0.2f \quad Дж/кг \n$$\n\
    где _α_ — коэффициент дисковых потерь, лежащий в пределах 0.04…0.08. В данном случае\
    выберем _α_ = %1.3f.\n\n"
    %(Compressor.L_TB, compressor['losses']['alpha_wh']) )
    report.write("30. Число лопаток колеса принимаем как $$z_{K} = %0.0f.$$\n\n"
    %compressor['geometry']['z_K'])
    report.write("31. Коэффициент мощности μ, учитывающий число лопаток, угол их наклона\
    на выходе и соотношение диаметров колеса, вычисляем по формуле:\
    \n$$\n \mu = { 1 \over 1 + {2 \over 3}{\pi \over z_{K}}{sin \\beta_{2л}\
    \over 1-(D_{1}/D_{2})} } = %0.6f \n$$\n\n"
    %Compressor.mu)
    report.write("32. Температура воздуха за колесом:\
    \n$$\n T_{2} = T_{1} + (\mu + \\engine['combustion']['alpha'] - 0.5\mu^2){u_2^2 \over c_{p}}\
    = %0.3f\quad К \n$$\n\n"
    %Compressor.T_2)
    report.write("33. Показатель политропы сжатия в колесе определяется уравнением:\
    \n$$\n {n_{2} \over n_{2} - 1} = {k \over k - 1} -\
    {\Delta L_{ва} + \Delta L_{пт} + \Delta L_{тв} \over R(T_{2} - T_{1})} \n$$\n\
    Тогда, решив уравнение методом последовательных приближений, получим $$n_{2} = %0.5f$$\n\n"
    %Compressor.n_2)
    report.write("34. Давление на выходе из колеса\
    \n$$\n p_{2} = p_{1} \left( {T_{2} \over T_{1}} \\right)^{n_{1} \over n_{1}-1}\
    = %1.f \quad Па \n$$\n\n"
    %Compressor.p_2)
    report.write("35. Плотность на выходе из колеса:\
    \n$$\n \\rho_{2} = {p_{2} \over RT_{2}} = %0.5f \quad кг/м^{3} \n$$\n\n"
    %Compressor.rho_2)
    report.write("36. Окружная составляющая абсолютной скорости на выходе:\
    \n$$\n c_{2u} = \mu \left( u_{2} - c_{2r} \over tg\\beta_{2л} \\right)\
    = %0.3f\quad м/с \n$$\n\n"
    %Compressor.c_2u)
    report.write("37. Абсолютная скорость на выходе из колеса:\
    \n$$\n c_{2} = \sqrt{c_{2u}^2 + c_{2r}^2} = %0.3f\quad м/c\n$$\n\n"
    %Compressor.c_2)
    report.write("38. Окружная составляющая относительной скорости на выходе из колеса:\
    \n$$\n w_{2u} = u_{2} - c_{2u} = %0.3f\quad м/c\n$$\n\n"
    %Compressor.w_2u)
    report.write("39. Относительная скорость w2 на выходе из колеса:\
    \n$$\n w_{2} = \sqrt{w_{2u}^2 + w_{2r}^2} = %0.3f\quad м/c\n$$\n\n"
    %Compressor.w_2)
    report.write("40. Угол между векторами относительной и окружной скорости\
    на выходе из колеса можно выразить в виде:\
    \n$$\n \\beta_{2} = arccos \left( w_{2u} \over w_{2} \\right) = %0.4f°\n$$\n\n"
    %Compressor.beta_2)
    report.write("41. Угол между векторами абсолютной и окружной скорости на выходе:\
    \n$$\n \\alpha_{2} = arccos \left( c_{2u} \over c_{2} \\right) = %0.4f°\n$$\n"
    %Compressor.alpha_2)
    report.write(
    "![alt text](compressor/outWheel.png)\n\
    <center>\
    <b> Рисунок 2 </b> - <i>Векторный план скоростей на выходе из рабочего колеса компрессора</i>\
    </center>\n\n"
    )
    report.write("42. При расчете ширины $$b_{2}$$ колеса на выходе необходимо учитывать\
    загромождение (стеснение) проходного сечения, обусловленное реальной толщиной лопаток.\
    В результате имеем:\
    \n$$\n b_{2} = {G_{K} \over \pi D_{2}c_{2r} \\rho_{2} \\tau_{2} } = %0.7f\quad м,\n$$\n\
    где $$\\tau_{2} = %1.3f$$ — коэффициент загромождения, который рекомендуется выбирать\
    в пределах 0.92…0.96\n\n"
    %(Compressor.b_2, compressor['load']['tau_2']) )
    report.write("43. Температура заторможенного потока на выходе из колеса:\
    \n$$\n T_{2}^{*} = T_{2} + {c_{2}^2 \over 2c_{p}} = %0.3f\quad К\n$$\n\n"
    %Compressor.T_2Stagn)

    if 'VANELESS' in compressor['diffuser']: # Vaneless diffuser | БЛД
        report.write("44. В малоразмерных турбокомпрессорах обычно применяют безлопаточные диффузоры.\
        При этом промежуточное сечение 3−3 в диффузоре (см. рис. 3), очевидно, будет отсутствовать.\n\
        Ширина безлопаточного диффузора на выходе может изменяться в пределах $$b_{4} = (0.7…1.0)b_{2}$$.\
        Выберем коэффициент %0.2f. Тогда:\
        \n$$\n b_{4} = %0.2f b_{2} = %1.8f\quad м\n$$\n\n"
        %(compressor['geometry']['coefficients']['vanelessWideCoef'], compressor['geometry']['coefficients']['vanelessWideCoef'], Compressor.b_4) )
        report.write("45. Наружный диаметр безлопаточного диффузора выбирают в пределах $$(1.6…1.9)D_{2}$$.\
        Принимаем значение коэффициента %0.2f. В результате:\
        \n$$\n D_{4} = %0.2f D_{2} = %1.4f\quad м\n$$\n\n"
        %(compressor['geometry']['coefficients']['vanelessDiamCoef'], compressor['geometry']['coefficients']['vanelessDiamCoef'], Compressor.D_4) )
        report.write(
        "![alt text](compressor/axisCut.png)\n\
        <center>\
        <b> Рисунок 3 </b> - <i>Схема проточной части компрессора</i>\
        </center>\n\n"
        )
        report.write("46. Показатель политропы сжатия в диффузоре вычислим с помощью уравнения,\
        в котором $$\eta_{д} = %0.3f$$ — политропный КПД диффузора (который должен лежать в пределах 0.55…0.78):\
        \n$$\n {n_{4} \over n_{4} - 1} = \eta_{д}{k \over k - 1} \n$$\n\
        Тогда, решив уравнение методом последовательных приближений, получим $$n_{4} = %1.4f$$\n\n"
        %(compressor['efficiency']['eta_diff'], Compressor.n_4) )
        report.write("47. Температура на выходе из диффузора определяется методом последовательных\
        приближений из уравнения:\
        \n$$\n {1 \over \\beta^{m}} + {\\beta - 1 \over \sigma q} -\
        - {1 \over q} = 0,\n$$\n где $$ \\beta = T_{4}/T_{2}\quad\
        q = \left({ D_{2}b_{2} \over D_{4}b_{4} }\\right)^2\quad\
        m = {2 \over n_{4} - 1}.$$\nВ результате решения имеем: $$T_{4} = \\beta T_{2} = %0.3f\quad К$$\n\n"
        %Compressor.T_4)
        report.write("48. Давление на выходе из диффузора:\
        \n$$\n p_{4} = p_{2} \left( {T_{4} \over T_{2}} \\right)^{n_{4} \over n_{4}-1}\
        = %1.f \quad Па \n$$\n\n"
        %Compressor.p_4)
        report.write("49. Плотность на выходе:\
        \n$$\n \\rho_{4} = {p_{4} \over RT_{4}} = %0.5f \quad кг/м^{3} \n$$\n\n"
        %Compressor.rho_4)
        report.write("50. Скорость на выходе из диффузора:\
        \n$$\n c_{4} = c_{2}{D_{2}b_{2}\\rho_{2} \over D_{4}b_{4}\\rho_{4}}\
        = %0.3f\quad м/с \n$$\n\n"
        %Compressor.c_4)
        report.write("51. В данном случае имеем автомобильный турбокомпрессор с коротким выпускным патрубком,\
        и отдельно сечение 5−5 входа в патрубок можно не рассматривать. Скорость на выходе из компрессора\
        $$с_{K}$$ обычно в 1.3…1.4 раза меньше скорости на выходе из диффузора. Примем значение $$с_{K} = %0.2f$$, тогда:\
        \n$$\n c_{K} = {c_{4} \over %1.2f} = %2.3f\quad м/с \n$$\n\n"
        %(compressor['geometry']['coefficients']['relDiffOutToCompOut'], compressor['geometry']['coefficients']['relDiffOutToCompOut'], Compressor.c_K) )
        i = 52

    else: # Vaned diffuser | ЛД
        report.write("44. Ширина безлопаточной части диффузора на выходе может изменяться в пределах\
        $$b_{3} = (0.7…1.0)b_{2}$$. Выберем коэффициент %0.2f. Тогда:\
        \n$$\n b_{3} = %0.2f b_{2} = %1.8f\quad м\n$$\n\n"
        %(compressor['geometry']['coefficients']['vanelessWideCoef'], compressor['geometry']['coefficients']['vanelessWideCoef'], Compressor.b_3) )
        report.write("45. Наружный диаметр безлопаточной части диффузора выбирают в пределах $$(1.6…1.9)D_{2}$$.\
        Принимаем значение коэффициента %0.2f. В результате:\
        \n$$\n D_{3} = %0.2f D_{2} = %1.4f\quad м\n$$\n\n"
        %(compressor['geometry']['coefficients']['vanelessDiamCoef'], compressor['geometry']['coefficients']['vanelessDiamCoef'], Compressor.D_3) )
        report.write("46. Показатель политропы сжатия в безлопаточной части диффузора вычислим с помощью уравнения,\
        в котором $$\eta_{д} = %0.3f$$ — политропный КПД диффузора (который должен лежать в пределах 0.55…0.78):\
        \n$$\n {n_{3} \over n_{3} - 1} = \eta_{д}{k \over k - 1} \n$$\n\
        Тогда, решив уравнение методом последовательных приближений, получим $$n_{3} = %1.4f$$\n\n"
        %(compressor['efficiency']['eta_diff'], Compressor.n_3) )
        report.write("47. Температура на выходе из диффузора определяется методом последовательных\
        приближений из уравнения:\
        \n$$\n {1 \over \\beta^{m}} + {\\beta - 1 \over \sigma q} -\
        - {1 \over q} = 0,\n$$\n где $$ \\beta = T_{3}/T_{2}\quad\
        q = \left({ D_{2}b_{2} \over D_{3}b_{3} }\\right)^2\quad\
        m = {2 \over n_{3} - 1}.$$\nВ результате решения имеем: $$T_{3} = \\beta T_{2} = %0.3f\quad К$$\n\n"
        %Compressor.T_3)
        report.write("48. Давление на входе в лопаточную часть диффузора:\
        \n$$\n p_{3} = p_{2} \left( {T_{3} \over T_{2}} \\right)^{n_{3} \over n_{3}-1}\
        = %1.f \quad Па \n$$\n\n"
        %Compressor.p_3)
        report.write("49. Плотность на входе в лопаточную часть диффузора:\
        \n$$\n \\rho_{3} = {p_{3} \over RT_{3}} = %0.5f \quad кг/м^{3} \n$$\n\n"
        %Compressor.rho_3)
        report.write("50. Скорость на входе в лопаточную часть диффузора:\
        \n$$\n c_{4} = c_{2}{D_{2}b_{2}\\rho_{2} \over D_{4}b_{4}\\rho_{4}}\
        = %0.3f\quad м/с \n$$\n\n"
        %Compressor.c_4)
        report.write("51. Ширина лопаточной части диффузора на выходе может изменяться в\
        пределах $$b_{4} = (1…1.3)b_{3}$$. Выберем коэффициент %0.2f. Тогда:\
        \n$$\n b_{4} = %0.2f b_{3} = %1.8f\quad м\n$$\n\n"
        %(compressor['geometry']['coefficients']['vanedWideCoef'], compressor['geometry']['coefficients']['vanedWideCoef'], Compressor.b_4) )
        report.write("52. Наружный диаметр лопаточной части диффузора выбирают в пределах $$(1.35…1.7)D_{2}$$.\
        Принимаем значение коэффициента %0.2f. В результате:\
        \n$$\n D_{4} = %0.2f D_{2} = %1.4f\quad м\n$$\n\n"
        %(compressor['geometry']['coefficients']['vanedDiamCoef'], compressor['geometry']['coefficients']['vanedDiamCoef'], Compressor.D_4) )
        report.write(
        "![alt text](compressor/axisCut.png)\n\
        <center>\
        <b> Рисунок 3 </b> - <i>Схема проточной части компрессора в осевом разрезе</i>\
        </center>\n\n"
        )
        report.write("53. Угол лопаток на выходе из лопаточного диффузора $$\\alpha_{4}=\\alpha_{2}+(12° + 18°)$$:\
        \n$$\n \\alpha_{4}=\\alpha_{2} + %0.1f° = %0.2f \n$$\n\n"
        %(compressor['geometry']['deltaDiffuser'], Compressor.alpha_4) )
        report.write("54. Число лопаток диффузора должно быть некратно числу лопаток $$z_{К} = %0.0f$$ компрессора.\
        Принимаем: $$z_{д} = %0.0f$$.\n\n"
        %(compressor['geometry']['z_K'], compressor['geometry']['z_diffuser']) )
        report.write(
        "![alt text](compressor/perpendicularCut.png)\n\
        <center>\
        <b> Рисунок 4 </b> - <i>Схема проточной части компрессора в поперечном разрезе</i>\
        </center>\n\n"
        )
        report.write("55. Показатель политропы сжатия в лопаточной части диффузора должен лежать в\
        пределах 1.5…1.8: Принимаем: $$n_{4} = %0.0f$$.\n\n"
        %Compressor.n_4)
        report.write("56. Температура на выходе из диффузора определяется методом последовательных\
        приближений из уравнения:\
        \n$$\n {1 \over \\beta^{m}} + {\\beta - 1 \over \sigma q} -\
        - {1 \over q} = 0,\n$$\n где $$ \\beta = T_{4}/T_{3}\quad\
        q = \left({ D_{3}b_{3}\\tau_{3}sin\left(\\alpha_{3}\\right) \over D_{4}b_{4}\\tau_{4}sin\left(\\alpha_{4}\\right) }\\right)^2\quad\
        m = {2 \over n_{4} - 1}.$$\n\
        Здесь $$\\tau_{3} = %0.2f$$ и $$\\tau_{4} = %0.2f$$ - коэффициенты загромождения на входе в лопаточную часть диффузора\
        и на выходе из неё.\nВ результате решения имеем: $$T_{4} = \\beta T_{3} = %0.3f\quad К$$\n\n"
        %(compressor['load']['tau_3'], compressor['load']['tau_4'], Compressor.T_3))
        report.write("57. Давление на входе из лопаточной части диффузора:\
        \n$$\n p_{4} = p_{3} \left( {T_{4} \over T_{3}} \\right)^{n_{4} \over n_{4}-1}\
        = %1.f \quad Па \n$$\n\n"
        %Compressor.p_4)
        report.write("58. Плотность на выходе из лопаточной части диффузора:\
        \n$$\n \\rho_{4} = {p_{4} \over RT_{4}} = %0.5f \quad кг/м^{3} \n$$\n\n"
        %Compressor.rho_4)
        report.write("59. Скорость на выходе из лопаточной части диффузора:\
        \n$$\n c_{4} = c_{3}{D_{3}b_{3}\\tau_{3}sin\left(\\alpha_{3}\\right)\\rho_{3} \over D_{4}b_{4}\\tau_{4}sin\left(\\alpha_{4}\\right)\\rho_{4}}\
        = %0.3f\quad м/с \n$$\n\n"
        %Compressor.c_4)
        report.write("60. В данном случае имеем автомобильный турбокомпрессор с коротким выпускным патрубком,\
        и отдельно сечение 5−5 входа в патрубок можно не рассматривать. Скорость на выходе из компрессора\
        $$c_{K}$$ обычно в 1.3…1.4 раза меньше скорости на выходе из диффузора. Примем значение $$c_{K} = %0.2f$$, тогда:\
        \n$$\n c_{K} = {c_{4} \over %1.2f} = %2.3f\quad м/с \n$$\n\n"
        %(compressor['geometry']['coefficients']['relDiffOutToCompOut'], compressor['geometry']['coefficients']['relDiffOutToCompOut'], Compressor.c_K) )
        i = 61

    report.write("%0.0f. Температура на выходе из компрессора:\
    \n$$\n T_{4}^{*} = T_{4} + {c_{4}^{2} - c_{K}^{2} \over 2c_{p}} = %0.3f\quad К\n$$\n\n"
    %(i, Compressor.T_K)); i += 1
    report.write("%0.0f. Показатель $$n_{ул}$$ политропы сжатия в воздухосборнике (улитке) составляет обычно\
    1.85…2.2. Примем значение $$n_{ул} = %0.1f$$.\n\n"
    %(i, compressor['losses']['n_housing']))
    report.write("%0.0f. Тогда давление на выходе из компрессора:\
    \n$$\n p_{K} = p_{4} \left( {T_{K} \over T_{4}} \\right)^{n_{ул} \over n_{ул}-1}\
    = %1.f \quad Па \n$$\n\n"
    %(i, Compressor.p_K)); i += 1
    report.write("%0.0f. Температура заторможенного потока на выходе:\
    \n$$\n T_{K}^{*} = T_{K} + {c_{K}^{2} \over 2c_{p}} = %0.3f\quad К\n$$\n\n"
    %(i, Compressor.T_KStagn)); i += 1
    report.write("%0.0f. Давление заторможенного потока на выходе:\
    \n$$\n p_{K}^{*} = p_{K} \left( {T_{K}^{*} \over T_{K}} \\right)^{k \over k-1}\
    = %1.f \quad Па \n$$\n\n"
    %(i, Compressor.p_KStagn)); i += 1
    report.write("%0.0f. Действительная степень повышения давления компрессоре:\
    \n$$\n \pi_{K} = {p_{K}^{*} \over p_{0}^{*}} = %0.4f \n$$\n\n"
    %(i, Compressor.pi_KStagn)); i += 1
    report.write("%0.0f. Изоэнтропная работа по расчетной степени повышения давления:\
        \n$$\n {L'}_{КS}^{*} = c_{p}T_{0}^{*} \left( (\pi_К^{*})^{k \over k-1} - 1\\right)\
        = %0.1f \quad Дж/кг \n$$\n\n"
    %(i, Compressor.L_KsStagn)); i += 1
    report.write("%0.0f. Расчетный изоэнтропный КПД по заторможенным параметрам:\
    \n$$\n {\eta'}_{КS}^{*} = {(\pi_К^{*})^{k \over k-1} - 1   \over\
    T_{K}^{*}/T_{0}^{*} - 1} = %0.5f \n$$\n\n"
    %(i, Compressor.eta_KsStagnRated)); i += 1
    report.write("%0.0f. Расхождение с заданным КПД компрессора составляет:\
    \n$$\n {\mid {\eta'}_{КS}^{*} - \eta_{КS}^{*} \mid \over \eta_{КS}^{*}}\
    = %0.3f \%% \n$$\n\n"
    %(i, Compressor.errorEta)); i += 1
    report.write("%0.0f. Расчетный коэффициент напора по заторможенным параметрам:\
    \n$$\n {H'}_{КS}^{*} = {{L'}_{КS}^{*} \over u_{2}^2} = %0.5f \n$$\n\n"
    %(i, Compressor.H_KsStagnRated)); i += 1
    report.write("%0.0f. Расхождение с заданным коэффициентом напора составляет:\
    \n$$\n {\mid {H'}_{КS}^{*} - H_{КS}^{*} \mid \over H_{КS}^{*}}\
    = %0.3f \%% \n$$\n\n"
    %(i, Compressor.errorH)); i += 1
    report.write("%0.0f. Мощность, затрачиваемая на привод компрессора:\
    \n$$\n N_{K} = {G_{K}{L'}_{КS}^{*} \over {\eta'}_{КS}^{*}} = %0.1f\quad Вт \n$$\n\n"
    %(i, Compressor.N_K)); i += 1
    report.write("%0.0f. Полное давление перед впускными клапанами поршневой части:\
    \n$$\n p_{v}^{*} = \sigma_{c} \sigma_{v} p_{K}^{*} = %0.1f\quad Па \n$$\n\n"
    %(i, Compressor.p_vStagn)); i += 1

    report.close()
