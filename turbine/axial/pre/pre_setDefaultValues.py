def setDefaultValues(exhaust, turbine):
    '''
        Description:    Default coefficients values
    '''

    from defaultValue import defaultValue

    turbine['losses']['dragInletRatio'] = defaultValue(
        turbine['losses']['dragInletRatio'],
        1.046
    ) # (0)

    # [efficiency]
    turbine['efficiency']['sigma_esc'] = defaultValue(
        turbine['efficiency']['sigma_esc'],
        0.99
    ) # (1)
    turbine['efficiency']['eta_Te'] = defaultValue(
        turbine['efficiency']['eta_Te'],
        0.795
    ) # (2)
    turbine['efficiency']['ksi'] = defaultValue(
        turbine['efficiency']['ksi'],
        0.56
    ) # (5)
    turbine['efficiency']['rho'] = defaultValue(
        turbine['efficiency']['rho'],
        0.38
    ) # (6)
    turbine['efficiency']['c_u1'] = defaultValue(
        turbine['efficiency']['c_u1'],
        0.95
    ) # (27)
    turbine['efficiency']['c_u2'] = defaultValue(
        turbine['efficiency']['c_u2'],
        0.85
    ) # (27)
    turbine['efficiency']['eta_m'] = defaultValue(
        turbine['efficiency']['eta_m'],
        0.97
    ) # (66)

    # [geometry]
    turbine['geometry']['alpha_1'] = defaultValue(
        turbine['geometry']['alpha_1'],
        16
    ) # (11)
    turbine['geometry']['beta_1Blade'] = defaultValue(
        turbine['geometry']['beta_1Blade'],
        90
    ) # (16)
    turbine['geometry']['alpha_0'] = defaultValue(
        turbine['geometry']['alpha_0'],
        90
    ) # (27)
    turbine['geometry']['delta'] = defaultValue(
        turbine['geometry']['delta'],
        0.8*1e-03
    ) # (38)

    # [geometry][coefficients]
    turbine['geometry']['coefficients']['t1Tol1'] = defaultValue(
        turbine['geometry']['coefficients']['t1Tol1'],
        0.88
    ) # (22)
    turbine['geometry']['coefficients']['m'] = defaultValue(
        turbine['geometry']['coefficients']['m'],
        1.08
    ) # (26)
    turbine['geometry']['coefficients']['t2Tol2'] = defaultValue(
        turbine['geometry']['coefficients']['t2Tol2'],
        0.81
    ) # (45)
    turbine['geometry']['coefficients']['beta'] = defaultValue(
        turbine['geometry']['coefficients']['beta'],
        2
    ) # (61)

    # [losses]
    turbine['losses']['phi'] = defaultValue(
        turbine['losses']['phi'], 
        0.97
    ) # (10)
    turbine['losses']['psi'] = defaultValue(
        turbine['losses']['psi'],
        0.95
    ) # (29)

    return turbine