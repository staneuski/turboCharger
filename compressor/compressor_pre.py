def compressor_pre(run, engine, compressor):
    '''
        Extend compressor dictionary with its relative parameters and
        precalculate some compressor parameters
    '''
    from compressor_default_values import compressor_default_values
    from compressor_plot2func import eta_plot2func
    from compressor_run import pressure_increase_ratio
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    compressor_default_values(compressor)

    # Convert data to SI dimensions
    compressor['initial']['p_aStagn'] *= 1e+06 # -> [Pa]

    # Flow volume | Расход
    if 'TYPE1' in run['type']:
        compressor['G_K'] = engine['efficiency']['N_e']\
                            *engine['efficiency']['b_e']\
                            *engine['combustion']['l_0']\
                            *engine['combustion']['alpha']\
                            *engine['combustion']['phi']/3600
                            # [kg/s]

    # Wheel diameter
    # Оценка диаметра рабочего колеса и установка параметров зависящих от него
    if issubclass(type(compressor['geometry']['estimD_2']), str):
        compressor['geometry']['D_2'] = (160*compressor['G_K'] + 40)
                                        *1e-03 # [m]
    else:
        compressor['geometry']['D_2'] = compressor['geometry']['estimD_2']
                                        *1e-02 # [m]

    # Calculation pressure degree increase with successive approximation method
    # Опр. степени повышения давления методом последовательных приближений
    if 'TYPE1' in run['type']:
        compressor['efficiency']['eta_KsStagn'] = eta_plot2func(
            compressor['efficiency']['eta_KsStagn'],
            compressor['geometry']['D_2'])

        compressor['pi_K'] = 1;    validity = 1e-04
        while (abs(pressure_increase_ratio(engine, compressor)
                   - compressor['pi_K']) > validity):
            compressor['pi_K'] += validity

        else:
            pressure_increase_ratio(engine, compressor)

    return compressor


# ''' (C) 2018-2020 Stanislau Stasheuski '''