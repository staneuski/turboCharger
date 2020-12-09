def pre(project, engine,
        compressor,
        turbine):
    """Extend turbine dictionary with its relative parameters and
    precalculate some compressor parameters.
    """

    import math
    from turbine.pre.default_values import default_values
    from turbine.pre.plot2func import eta_plot2func, alpha_plot2func,\
                                  phi_plot2func, psi_plot2func,\
                                  ksi_plot2func, relD_1H, relD_2B

    default_values(turbine)

    # Converting data to SI dimensions
    turbine['geometry']['delta'] *= 1e-03 # -> [m]

    if turbine['type'] == 'radial':
        # Set values using balance coefficients from dictionary
        turbine['efficiency']['eta_Te'] = eta_plot2func(
            turbine['efficiency']['eta_Te'],
            compressor['geometry']['D_2'])
        turbine['geometry']['alpha_1'] = alpha_plot2func(
            turbine['geometry']['alpha_1'],
            compressor['geometry']['D_2'])
        turbine['losses']['phi'] = phi_plot2func(
            turbine['losses']['phi'],
            compressor['geometry']['D_2'])
        turbine['losses']['psi'] = psi_plot2func(
            turbine['losses']['psi'],
            compressor['geometry']['D_2'])
        turbine['geometry']['coefficients']['d_outer_ratio'] = relD_1H(
            turbine['geometry']['coefficients']['d_outer_ratio'],
            compressor['geometry']['D_2'])
        turbine['geometry']['coefficients']['d_inner_ratio'] = relD_2B(
            turbine['geometry']['coefficients']['d_inner_ratio'],
            compressor['geometry']['D_2'])

        # Inlet turbine temperature | Температура перед турбиной
        if 'TYPE2' in project['type']:
            if compressor['geometry']['D_2'] < 0.3:
                engine['heat']['T_0Stagn'] = 923.0 # [K]

            elif (compressor['geometry']['D_2'] > 0.3
                  and compressor['geometry']['D_2'] < 0.64):
                engine['heat']['T_0Stagn'] = 823.0 # [K]

            else:
                exit('\033[91mERROR 0: The diameter of the wheel is too big!')

    return project, engine, turbine


# ''' (C) 2018-2020 Stanislau Stasheuski '''