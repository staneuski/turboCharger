def set_default_values(exhaust, turbine):
    '''
        Default coefficients values
    '''

    from default_value import default_value

    turbine['losses']['dragInletRatio'] = default_value(
        turbine['losses']['dragInletRatio'],
        1.017
    )


    # [efficiency]
    turbine['efficiency']['eta_Te'] = default_value(
        turbine['efficiency']['eta_Te'],
        0.73
    )
    turbine['efficiency']['sigma_esc'] = default_value(
        turbine['efficiency']['sigma_esc'],
        0.99
    )
    turbine['efficiency']['dzeta'] = default_value(
        turbine['efficiency']['dzeta'],
        1.25
    )
    turbine['efficiency']['eta_m'] = default_value(
        turbine['efficiency']['eta_m'],
        0.94
    )
    turbine['efficiency']['rho'] = default_value(
        turbine['efficiency']['rho'],
        0.52
    )


    # [geometry]
    turbine['geometry']['alpha_1'] = default_value(
        turbine['geometry']['alpha_1'],
        0
    ) #(18)
    turbine['geometry']['beta_1Blade'] = default_value(
        turbine['geometry']['beta_1Blade'],
        90
    )
    turbine['geometry']['delta'] = default_value(
        turbine['geometry']['delta'],
        3*1e-04
    )

    #- [geometry][coefficients]
    turbine['geometry']['coefficients']['outerDiamRatio'] = default_value(
        turbine['geometry']['coefficients']['outerDiamRatio'],
        0.8
    )
    turbine['geometry']['coefficients']['innerDiamRatio'] = default_value(
        turbine['geometry']['coefficients']['innerDiamRatio'],
        0.95
    )
    turbine['geometry']['coefficients']['diameterRatio'] = default_value(
        turbine['geometry']['coefficients']['diameterRatio'],
        1
    )
    turbine['geometry']['coefficients']['beta'] = default_value(
        turbine['geometry']['coefficients']['beta'],
        4.6
    )


    # [losses]
    turbine['losses']['phi'] = default_value(
        turbine['losses']['phi'],
        1
    ) #(16)
    turbine['losses']['psi'] = default_value(
        turbine['losses']['psi'], 
        0.96
    ) #(29)

    return exhaust, turbine
