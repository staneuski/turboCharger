def set_default_values(compressor):
    '''
        Default values for coefficients
    '''

    from default_value import default_value


    # [initial]
    compressor['geometry']['beta_2Blade'] = default_value(
        compressor['geometry']['beta_2Blade'], 75.0)
    compressor['initial']['c_0'] = default_value(
        compressor['initial']['c_0'],         40.0)


    # [efficiency]
    compressor['efficiency']['eta_KsStagn'] = default_value(
        compressor['efficiency']['eta_KsStagn'], 0.55)
    compressor['efficiency']['H_KsStagn'] = default_value(
        compressor['efficiency']['H_KsStagn'],   0.4)
    compressor['efficiency']['phi_flow'] = default_value(
        compressor['efficiency']['phi_flow'],    0.4)
    compressor['efficiency']['eta_diff'] = default_value(
        compressor['efficiency']['eta_diff'],    0.75)


    # [geometry]
    compressor['geometry']['deltaDiffuser'] = default_value(
        compressor['geometry']['deltaDiffuser'],                        14.0)

    #- [geometry][coefficients]
    compressor['geometry']['coefficients']['relD_1H'] = default_value(
        compressor['geometry']['coefficients']['relD_1H'],              0.6)
    compressor['geometry']['coefficients']['relD_1B'] = default_value(
        compressor['geometry']['coefficients']['relD_1B'],              0.55)
    compressor['geometry']['coefficients']['relW_2rToC_1a'] = default_value(
        compressor['geometry']['coefficients']['relW_2rToC_1a'],        0.6)
    compressor['geometry']['coefficients']['vanedWideCoef'] = default_value(
        compressor['geometry']['coefficients']['vanedWideCoef'],        1.0)
    compressor['geometry']['coefficients']['vanedDiamCoef'] = default_value(
        compressor['geometry']['coefficients']['vanedDiamCoef'],        1.6)
    compressor['geometry']['coefficients']['relDiffOutToCompOut'] = default_value(
        compressor['geometry']['coefficients']['relDiffOutToCompOut'],  1.4)

    if 'VANELESS' in compressor['diffuser']:
        compressor['geometry']['coefficients']['vanelessWideCoef'] = default_value(
            compressor['geometry']['coefficients']['vanelessWideCoef'], 0.9)
        compressor['geometry']['coefficients']['vanelessDiamCoef'] = default_value(
            compressor['geometry']['coefficients']['vanelessDiamCoef'], 1.8)

    elif 'VANED' in compressor['diffuser']:
        compressor['geometry']['coefficients']['vanelessWideCoef'] = default_value(
            compressor['geometry']['coefficients']['vanelessWideCoef'], 1.0)
        compressor['geometry']['coefficients']['vanelessDiamCoef'] = default_value(
            compressor['geometry']['coefficients']['vanelessDiamCoef'], 1.14)

    else:
        exit('\033[91mError: Set type of the diffuser correctly ("VANED"\
 or "VANELESS") in commonConfig.py dictionary!\n')


    # [losses]
    compressor['losses']['dzeta_inlet'] = default_value(
        compressor['losses']['dzeta_inlet'], 0.04)
    compressor['losses']['dzeta_BA'] = default_value(
        compressor['losses']['dzeta_BA'],    0.26)
    compressor['losses']['dzeta_TF'] = default_value(
        compressor['losses']['dzeta_TF'],    0.18)
    compressor['losses']['alpha_wh'] = default_value(
        compressor['losses']['alpha_wh'],    0.05)
    compressor['losses']['n_housing'] = default_value(
        compressor['losses']['n_housing'],   1.9)
    compressor['losses']['n_diffuser'] = default_value(
        compressor['losses']['n_diffuser'],  1.55)


    # [load]
    compressor['load']['tau_1'] = default_value(
        compressor['load']['tau_1'],   0.9)
    compressor['load']['tau_2'] = default_value(
        compressor['load']['tau_2'],   0.94)
    compressor['load']['tau_3'] = default_value(
        compressor['load']['tau_3'],   0.93)
    compressor['load']['tau_4'] = default_value(
        compressor['load']['tau_4'],   0.965)

    return compressor