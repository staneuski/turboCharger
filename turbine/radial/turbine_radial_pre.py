def turbine_radial_pre(run, ambient, engine,
        compressor,
        turbine):
    '''
        Extend turbine dictionary with its relative parameters and
        precalculate some compressor parameters
    '''
    import math

    from default_value import default_value
    from turbine_radial_set_default_values import set_default_values
    from turbine_radial_plot2func import eta_plot2func, alpha_plot2func,\
                                         phi_plot2func, psi_plot2func,\
                                         ksi_plot2func, relD_1H, relD_2B
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # Converting data to SI dimensions
    if issubclass(type(turbine['geometry']['delta']), float):
        turbine['geometry']['delta'] *= 1e-03 # -> [m]

    set_default_values(engine['exhaust'], turbine)

    # Set values using balance coefficients from dictionary
    turbine['efficiency']['eta_Te'] = eta_plot2func(
        turbine['efficiency']['eta_Te'], compressor['geometry']['D_2']
    )
    turbine['geometry']['alpha_1'] = alpha_plot2func(
        turbine['geometry']['alpha_1'], compressor['geometry']['D_2']
    )
    turbine['losses']['phi'] = phi_plot2func(
        turbine['losses']['phi'], compressor['geometry']['D_2']
    )
    turbine['losses']['psi'] = psi_plot2func(
        turbine['losses']['psi'], compressor['geometry']['D_2']
    )
    turbine['geometry']['coefficients']['outerDiamRatio'] = relD_1H(
        turbine['geometry']['coefficients']['outerDiamRatio'], compressor['geometry']['D_2']
    )
    turbine['geometry']['coefficients']['innerDiamRatio'] = relD_2B(
        turbine['geometry']['coefficients']['innerDiamRatio'], compressor['geometry']['D_2']
    )

    # Inlet turbine temperature | Температура перед турбиной
    if 'TYPE2' in run['type']:
        if compressor['geometry']['D_2'] < 0.3:
            engine['heat']['T_0Stagn'] = 923.0 # [K]
        elif (compressor['geometry']['D_2'] > 0.3) & (compressor['geometry']['D_2'] < 0.64):
            engine['heat']['T_0Stagn'] = 823.0 # [K]
        else:
            exit("\033[91mError 0: The diameter of the wheel is too big!")

    return run, ambient, engine, turbine


# ''' (C) 2018-2020 Stanislau Stasheuski '''