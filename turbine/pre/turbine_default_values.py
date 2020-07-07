def turbine_default_values(turbine):
    '''
        Default coefficients values
    '''
    from default_value import default_value

    if turbine['type'] == 'radial':
        turbine['losses']['dragInletRatio'] = default_value(
            turbine['losses']['dragInletRatio'],
            1.017)

        # [efficiency]
        turbine['efficiency']['eta_Te'] = default_value(
            turbine['efficiency']['eta_Te'],
            0.73)
        turbine['efficiency']['sigma_esc'] = default_value(
            turbine['efficiency']['sigma_esc'],
            0.99)
        turbine['efficiency']['dzeta'] = default_value(
            turbine['efficiency']['dzeta'],
            1.24)
        turbine['efficiency']['eta_m'] = default_value(
            turbine['efficiency']['eta_m'],
            0.94)
        turbine['efficiency']['rho'] = default_value(
            turbine['efficiency']['rho'],
            0.52)


        # [geometry]
        turbine['geometry']['alpha_1'] = default_value(
            turbine['geometry']['alpha_1'],
            0.0) #(18)
        turbine['geometry']['beta_1Blade'] = default_value(
            turbine['geometry']['beta_1Blade'],
            90)
        turbine['geometry']['delta'] = default_value(
            turbine['geometry']['delta'],
            3*1e-04)

        #- [geometry][coefficients]
        turbine['geometry']['coefficients']['outerDiamRatio'] = default_value(
            turbine['geometry']['coefficients']['outerDiamRatio'],
            0.8)
        turbine['geometry']['coefficients']['innerDiamRatio'] = default_value(
            turbine['geometry']['coefficients']['innerDiamRatio'],
            0.95)
        turbine['geometry']['coefficients']['diameterRatio'] = default_value(
            turbine['geometry']['coefficients']['diameterRatio'],
            1.0)
        turbine['geometry']['coefficients']['beta'] = default_value(
            turbine['geometry']['coefficients']['beta'],
            4.6)


        # [losses]
        turbine['losses']['phi'] = default_value(
            turbine['losses']['phi'],
            1.0) #(16)
        turbine['losses']['psi'] = default_value(
            turbine['losses']['psi'], 
            0.96) #(29)

    elif turbine['type'] == 'axial':
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

    else: None

    return turbine
