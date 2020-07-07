def set_default_values(turbine):
    '''
        Default coefficients values
    '''
    from default_value import default_value

    turbine['losses']['dragInletRatio'] = default_value(
        turbine['losses']['dragInletRatio'],
        1.046) # (0)

    # [efficiency]
    turbine['efficiency']['sigma_esc'] = default_value(
        turbine['efficiency']['sigma_esc'],
        0.99) # (1)
    turbine['efficiency']['eta_Te'] = default_value(
        turbine['efficiency']['eta_Te'],
        0.795) # (2)
    turbine['efficiency']['ksi'] = default_value(
        turbine['efficiency']['ksi'],
        0.56) # (5)
    turbine['efficiency']['rho'] = default_value(
        turbine['efficiency']['rho'],
        0.38) # (6)
    turbine['efficiency']['c_u1'] = default_value(
        turbine['efficiency']['c_u1'],
        0.95) # (27)
    turbine['efficiency']['c_u2'] = default_value(
        turbine['efficiency']['c_u2'],
        0.85) # (27)
    turbine['efficiency']['eta_m'] = default_value(
        turbine['efficiency']['eta_m'],
        0.97) # (66)

    # [geometry]
    turbine['geometry']['alpha_1'] = default_value(
        turbine['geometry']['alpha_1'],
        16) # (11)
    turbine['geometry']['beta_1Blade'] = default_value(
        turbine['geometry']['beta_1Blade'],
        90) # (16)
    turbine['geometry']['alpha_0'] = default_value(
        turbine['geometry']['alpha_0'],
        90) # (27)
    turbine['geometry']['delta'] = default_value(
        turbine['geometry']['delta'],
        0.8*1e-03) # (38)

    # [geometry][coefficients]
    turbine['geometry']['coefficients']['t1Tol1'] = default_value(
        turbine['geometry']['coefficients']['t1Tol1'],
        0.88) # (22)
    turbine['geometry']['coefficients']['m'] = default_value(
        turbine['geometry']['coefficients']['m'],
        1.08) # (26)
    turbine['geometry']['coefficients']['t2Tol2'] = default_value(
        turbine['geometry']['coefficients']['t2Tol2'],
        0.81) # (45)
    turbine['geometry']['coefficients']['beta'] = default_value(
        turbine['geometry']['coefficients']['beta'],
        2) # (61)

    # [losses]
    turbine['losses']['phi'] = default_value(
        turbine['losses']['phi'], 
        0.97) # (10)
    turbine['losses']['psi'] = default_value(
        turbine['losses']['psi'],
        0.95) # (29)

    return turbine