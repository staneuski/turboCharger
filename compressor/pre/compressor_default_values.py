def compressor_default_values(compressor):
    '''
        Default values for coefficients
    '''
    from commonConfig import ambient
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    compressor.setdefault('diffuser', 'VANELESS')

    # ['initial']
    compressor['initial'].setdefault('p_aStagn', ambient['p'])
    compressor['initial'].setdefault('T_aStagn', ambient['T'])
    compressor['initial'].setdefault('c_0', 40.0)

    # ['efficiency']
    compressor['efficiency'].setdefault('eta_KsStagn', 0.6)
    compressor['efficiency'].setdefault('H_KsStagn', 0.4)
    compressor['efficiency'].setdefault('phi_flow', 0.4)
    compressor['efficiency'].setdefault('eta_diffuser', 0.75)

    # ['geometry']
    compressor['geometry'].setdefault('deltaDiffuser', 14.0)
    compressor['geometry'].setdefault('beta_2Blade', 75.0)

    compressor['geometry']['coefficients'].setdefault('D_1Down_relative', 0.6)
    compressor['geometry']['coefficients'].setdefault('D_1Up_relative', 0.55)
    compressor['geometry']['coefficients'].setdefault('w2r_c1a_ratio', 0.6)

    if 'VANED' in compressor['diffuser']:
        compressor['geometry']['coefficients']['diffuser']\
            .setdefault('vaneless_wide', 0.9)
        compressor['geometry']['coefficients']['diffuser']\
            .setdefault('vaneless_diam', 1.8)

    elif 'VANELESS' in compressor['diffuser']:
        compressor['geometry']['coefficients']['diffuser']\
            .setdefault('vaneless_wide', 1.0)
        compressor['geometry']['coefficients']['diffuser']\
            .setdefault('vaneless_diam', 1.14)

    else:
        exit("\033[91mERROR:\
            Variable compressor['diffuser'] is incorrect!\
            \nValid values are 'VANED' and 'VANELESS'"
            .replace('            ', ' '))

    compressor['geometry']['coefficients']['diffuser']\
        .setdefault('vaned_wide', 1.0)
    compressor['geometry']['coefficients']['diffuser']\
        .setdefault('vaned_diam', 1.6)
    compressor['geometry']['coefficients']['diffuser']\
        .setdefault('c_out_ratio', 1.4)

    # ['losses']
    compressor['losses'].setdefault('sigma_0', 0.98)
    compressor['losses'].setdefault('sigma_c', 0.985)
    compressor['losses'].setdefault('sigma_v', 0.992)
    compressor['losses'].setdefault('dzeta_inlet', 0.04)
    compressor['losses'].setdefault('dzeta_BA', 0.26)
    compressor['losses'].setdefault('dzeta_TF', 0.18)
    compressor['losses'].setdefault('alpha_wh', 0.05)
    compressor['losses'].setdefault('n_housing', 1.9)
    compressor['losses'].setdefault('n_diffuser', 1.55)

    # ['load']
    compressor['load'].setdefault('tau_1', 0.9)
    compressor['load'].setdefault('tau_2', 0.94)
    compressor['load'].setdefault('tau_3', 0.93)
    compressor['load'].setdefault('tau_4', 0.965)

    return compressor


# ''' (C) 2018-2020 Stanislau Stasheuski '''