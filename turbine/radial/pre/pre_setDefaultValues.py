def setDefaultValues(exhaust, turbine):
    '''
        Description:    Default coefficients values
    '''

    from defaultValue import defaultValue

    exhaust['dragInletRatio'] = defaultValue(
        exhaust['dragInletRatio'],
        1.017
    )


    # [efficiency]
    turbine['efficiency']['eta_Te'] = defaultValue(
        turbine['efficiency']['eta_Te'],
        0.73
    )
    turbine['efficiency']['sigma_esc'] = defaultValue(
        turbine['efficiency']['sigma_esc'],
        0.99
    )
    turbine['efficiency']['dzeta'] = defaultValue(
        turbine['efficiency']['dzeta'],
        1.3
    )
    turbine['efficiency']['eta_m'] = defaultValue(
        turbine['efficiency']['eta_m'],
        0.94
    )
    turbine['efficiency']['rho'] = defaultValue(
        turbine['efficiency']['rho'],
        0.52
    )


    # [geometry]
    turbine['geometry']['alpha_1'] = defaultValue(
        turbine['geometry']['alpha_1'],
        0
    ) #(18)
    turbine['geometry']['beta_1Blade'] = defaultValue(
        turbine['geometry']['beta_1Blade'],
        90
    )
    turbine['geometry']['delta'] = defaultValue(
        turbine['geometry']['delta'],
        3*1e-04
    )

    #- [geometry][coefficients]
    turbine['geometry']['coefficients']['outerDiamRatio'] = defaultValue(
        turbine['geometry']['coefficients']['outerDiamRatio'],
        0.8
    )
    turbine['geometry']['coefficients']['innerDiamRatio'] = defaultValue(
        turbine['geometry']['coefficients']['innerDiamRatio'],
        0.95
    )
    turbine['geometry']['coefficients']['diameterRatio'] = defaultValue(
        turbine['geometry']['coefficients']['diameterRatio'],
        1
    )
    turbine['geometry']['coefficients']['beta'] = defaultValue(
        turbine['geometry']['coefficients']['beta'],
        4.6
    )


    # [losses]
    turbine['losses']['phi'] = defaultValue(
        turbine['losses']['phi'],
        1
    ) #(16)
    turbine['losses']['psi'] = defaultValue(
        turbine['losses']['psi'], 
        0.96
    ) #(29)

    return exhaust, turbine
