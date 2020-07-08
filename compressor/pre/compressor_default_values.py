def compressor_default_values(compressor):
    '''
        Default values for coefficients
    '''
    from default_value import default_value
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # [initial]
    compressor['geometry']['beta_2Blade'] = default_value(
        compressor['geometry']['beta_2Blade'],
        75.0)
    compressor['initial']['c_0'] = default_value(
        compressor['initial']['c_0'],
        40.0)


    # [efficiency]
    compressor['efficiency']['eta_KsStagn'] = default_value(
        compressor['efficiency']['eta_KsStagn'],
        0.6)
    compressor['efficiency']['H_KsStagn'] = default_value(
        compressor['efficiency']['H_KsStagn'],
        0.4)
    compressor['efficiency']['phi_flow'] = default_value(
        compressor['efficiency']['phi_flow'],
        0.4)
    compressor['efficiency']['eta_diffuser'] = default_value(
        compressor['efficiency']['eta_diffuser'],
        0.75)


    # [geometry]
    compressor['geometry']['deltaDiffuser'] = default_value(
        compressor['geometry']['deltaDiffuser'],
        14.0)

    #- [geometry][coefficients]
    compressor['geometry']['coefficients']['D_1Down_relative'] = \
        default_value(compressor['geometry']['coefficients']\
                                ['D_1Down_relative'],
                      0.6)
    compressor['geometry']['coefficients']['D_1Up_relative'] = \
        default_value(compressor['geometry']['coefficients']\
                                ['D_1Up_relative'],
                      0.55)
    compressor['geometry']['coefficients']['w2r_c1a_ratio'] = \
        default_value(compressor['geometry']['coefficients']\
                                ['w2r_c1a_ratio'],
                      0.6)
    compressor['geometry']['coefficients']['diffuser']['vaned_wide'] = \
        default_value(compressor['geometry']['coefficients']\
                                ['diffuser']['vaned_wide'],
                      1.0)
    compressor['geometry']['coefficients']['diffuser']['vaned_diam'] = \
        default_value(compressor['geometry']['coefficients']\
                                ['diffuser']['vaned_diam'],
                      1.6)
    compressor['geometry']['coefficients']['diffuser']['c_out_ratio'] = \
        default_value(compressor['geometry']['coefficients']\
                                ['diffuser']['c_out_ratio'],
                      1.4)

    if 'VANED' in compressor['diffuser']:
        compressor['geometry']['coefficients']['diffuser']['vaneless_wide'] = \
            default_value(compressor['geometry']['coefficients']\
                                    ['diffuser']['vaneless_wide'],
                          0.9)
        compressor['geometry']['coefficients']['diffuser']['vaneless_diam'] = \
            default_value(compressor['geometry']['coefficients']\
                                    ['diffuser']['vaneless_diam'],
                          1.8)

    elif 'VANELESS' in compressor['diffuser']:
        compressor['geometry']['coefficients']['diffuser']['vaneless_wide'] = \
            default_value(compressor['geometry']['coefficients']\
                                    ['diffuser']['vaneless_wide'],
                         1.0)
        compressor['geometry']['coefficients']['diffuser']['vaneless_diam'] = \
            default_value(compressor['geometry']['coefficients']\
                                    ['diffuser']['vaneless_diam'],
                          1.14)

    else:
        exit("\033[91mERROR:\
            Variable compressor['diffuser'] is incorrect!\
            \nValid values are 'VANED' and 'VANELESS'"
            .replace('            ', ' '))


    # [losses]
    compressor['losses']['dzeta_inlet'] = default_value(
        compressor['losses']['dzeta_inlet'],
        0.04)
    compressor['losses']['dzeta_BA'] = default_value(
        compressor['losses']['dzeta_BA'],
        0.26)
    compressor['losses']['dzeta_TF'] = default_value(
        compressor['losses']['dzeta_TF'],
        0.18)
    compressor['losses']['alpha_wh'] = default_value(
        compressor['losses']['alpha_wh'],
        0.05)
    compressor['losses']['n_housing'] = default_value(
        compressor['losses']['n_housing'],
        1.9)
    compressor['losses']['n_diffuser'] = default_value(
        compressor['losses']['n_diffuser'],
        1.55)


    # [load]
    compressor['load']['tau_1'] = default_value(
        compressor['load']['tau_1'],
        0.9)
    compressor['load']['tau_2'] = default_value(
        compressor['load']['tau_2'],
        0.94)
    compressor['load']['tau_3'] = default_value(
        compressor['load']['tau_3'],
        0.93)
    compressor['load']['tau_4'] = default_value(
        compressor['load']['tau_4'],
        0.965)

    return compressor


# ''' (C) 2018-2020 Stanislau Stasheuski '''