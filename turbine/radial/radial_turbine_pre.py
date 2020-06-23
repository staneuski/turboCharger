def radial_turbine_pre(run, ambient, engine,
        compressor, D_2K,
        turbine):
    '''
        Extend turbine dictionary with its relative parameters and
        precalculate some compressor parameters
    '''
    import math

    from default_value import default_value
    from set_default_values import set_default_values
    from plot2func import eta_plot2func, alpha_plot2func, phi_plot2func,\
                          psi_plot2func, ksi_plot2func, relD_1H, relD_2B
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # Converting data to SI dimensions
    engine['efficiency']['N_e'] *= 1e+03 # -> [W]
    engine['efficiency']['b_e'] *= 1e-03 # -> [kg/W/h] or [g/kW/h]
    if issubclass(type(turbine['geometry']['delta']), float):
        turbine['geometry']['delta'] *= 1e-03 # -> [m]

    set_default_values(engine['exhaust'], turbine)

    # Set values using balance coefficients from dictionary
    turbine['efficiency']['eta_Te'] = eta_plot2func(
        turbine['efficiency']['eta_Te'], D_2K
    )
    turbine['geometry']['alpha_1'] = alpha_plot2func(
        turbine['geometry']['alpha_1'], D_2K
    )
    turbine['losses']['phi'] = phi_plot2func(
        turbine['losses']['phi'], D_2K
    )
    turbine['losses']['psi'] = psi_plot2func(
        turbine['losses']['psi'], D_2K
    )
    turbine['geometry']['coefficients']['outerDiamRatio'] = relD_1H(
        turbine['geometry']['coefficients']['outerDiamRatio'], D_2K
    )
    turbine['geometry']['coefficients']['innerDiamRatio'] = relD_2B(
        turbine['geometry']['coefficients']['innerDiamRatio'], D_2K
    )

    # Теоретическое количество воздуха, необходимое для сгорания 1 кг топлива
    if 'SI' in engine['combustion']['ignition']:
        engine['combustion']['l_0'] = 14.28 # [kg]
    elif 'CI' in engine['combustion']['ignition']:
        engine['combustion']['l_0'] = 14.31 # [kg]
    else:
        exit('Set type of the engine correctly ("DIESEL" or "SI") in commonConfig.py file!\n')

    # Flow volume | Расход
    if 'TYPE1' in run['type']:
        compressor['G_K'] = engine['efficiency']['N_e']\
            *engine['efficiency']['b_e']\
            *engine['combustion']['l_0']\
            *engine['combustion']['alpha']\
            *engine['combustion']['phi']/3600.0
        # [kg/s]

    # Inlet turbine temperature (for HW) | Температура перед турбиной
    if 'TYPE1' in run['type']:
        T_0Stagn = engine['heat']['T_0Stagn']

    else: # run['type'] = 'TYPE1'
        if D_2K < 0.3:
            T_0Stagn = 923.0
        elif (D_2K > 0.3) & (D_2K < 0.64):
            T_0Stagn = 823.0
        else:
            exit("\033[91mError 0: The diameter of the wheel is too big!")

    return run, ambient, engine, turbine, T_0Stagn


# ''' (C) 2018-2020 Stanislau Stasheuski '''