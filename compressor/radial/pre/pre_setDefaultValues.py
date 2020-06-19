def setDefaultValues(compressor):
    '''
        Description:    Default values for coefficients
    '''

    from defaultValue import defaultValue


    # [initial]
    compressor['geometry']['beta_2Blade'] = defaultValue(
        compressor['geometry']['beta_2Blade'], 75.0)
    compressor['initial']['c_0'] = defaultValue(
        compressor['initial']['c_0'],         40.0)


    # [efficiency]
    compressor['efficiency']['eta_KsStagn'] = defaultValue(
        compressor['efficiency']['eta_KsStagn'], 0.55)
    compressor['efficiency']['H_KsStagn'] = defaultValue(
        compressor['efficiency']['H_KsStagn'],   0.4)
    compressor['efficiency']['phi_flow'] = defaultValue(
        compressor['efficiency']['phi_flow'],    0.4)
    compressor['efficiency']['eta_diff'] = defaultValue(
        compressor['efficiency']['eta_diff'],    0.75)


    # [geometry]
    compressor['geometry']['deltaDiffuser'] = defaultValue(
        compressor['geometry']['deltaDiffuser'],                        14.0)

    #- [geometry][coefficients]
    compressor['geometry']['coefficients']['relD_1H'] = defaultValue(
        compressor['geometry']['coefficients']['relD_1H'],              0.6)
    compressor['geometry']['coefficients']['relD_1B'] = defaultValue(
        compressor['geometry']['coefficients']['relD_1B'],              0.55)
    compressor['geometry']['coefficients']['relW_2rToC_1a'] = defaultValue(
        compressor['geometry']['coefficients']['relW_2rToC_1a'],        0.6)
    compressor['geometry']['coefficients']['vanedWideCoef'] = defaultValue(
        compressor['geometry']['coefficients']['vanedWideCoef'],        1.0)
    compressor['geometry']['coefficients']['vanedDiamCoef'] = defaultValue(
        compressor['geometry']['coefficients']['vanedDiamCoef'],        1.6)
    compressor['geometry']['coefficients']['relDiffOutToCompOut'] = defaultValue(
        compressor['geometry']['coefficients']['relDiffOutToCompOut'],  1.4)

    if 'VANELESS' in compressor['diffuser']:
        compressor['geometry']['coefficients']['vanelessWideCoef'] = defaultValue(
            compressor['geometry']['coefficients']['vanelessWideCoef'], 0.9)
        compressor['geometry']['coefficients']['vanelessDiamCoef'] = defaultValue(
            compressor['geometry']['coefficients']['vanelessDiamCoef'], 1.8)

    elif 'VANED' in compressor['diffuser']:
        compressor['geometry']['coefficients']['vanelessWideCoef'] = defaultValue(
            compressor['geometry']['coefficients']['vanelessWideCoef'], 1.0)
        compressor['geometry']['coefficients']['vanelessDiamCoef'] = defaultValue(
            compressor['geometry']['coefficients']['vanelessDiamCoef'], 1.14)

    else:
        exit('\033[91mError: Set type of the diffuser correctly ("VANED"\
 or "VANELESS") in commonConfig.py dictionary!\n')


    # [losses]
    compressor['losses']['dzeta_inlet'] = defaultValue(
        compressor['losses']['dzeta_inlet'], 0.04)
    compressor['losses']['dzeta_BA'] = defaultValue(
        compressor['losses']['dzeta_BA'],    0.26)
    compressor['losses']['dzeta_TF'] = defaultValue(
        compressor['losses']['dzeta_TF'],    0.18)
    compressor['losses']['alpha_wh'] = defaultValue(
        compressor['losses']['alpha_wh'],    0.05)
    compressor['losses']['n_housing'] = defaultValue(
        compressor['losses']['n_housing'],   1.9)
    compressor['losses']['n_diffuser'] = defaultValue(
        compressor['losses']['n_diffuser'],  1.55)


    # [load]
    compressor['load']['tau_1'] = defaultValue(
        compressor['load']['tau_1'],   0.9)
    compressor['load']['tau_2'] = defaultValue(
        compressor['load']['tau_2'],   0.94)
    compressor['load']['tau_3'] = defaultValue(
        compressor['load']['tau_3'],   0.93)
    compressor['load']['tau_4'] = defaultValue(
        compressor['load']['tau_4'],   0.965)

    return compressor