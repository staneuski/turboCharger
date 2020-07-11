def turbine_default_values(turbine):
    '''
        Default coefficients values
    '''

    if turbine['type'] == 'radial':
        # ['efficiency']
        turbine['efficiency'].setdefault('eta_Te', 0.73)
        turbine['efficiency'].setdefault('sigma_esc', 0.99)
        turbine['efficiency'].setdefault('dzeta', 1.24)
        turbine['efficiency'].setdefault('eta_m', 0.94)
        turbine['efficiency'].setdefault('rho', 0.52)

        # ['geometry']
        turbine['geometry'].setdefault('alpha_1', 0.0) #(18)
        turbine['geometry'].setdefault('beta_1Blade', 90)
        turbine['geometry'].setdefault('delta', 0.3)

        #- ['geometry']['coefficients']
        turbine['geometry']['coefficients'].setdefault('D_ratio', 1.0)
        turbine['geometry']['coefficients'].setdefault('d_outer_ratio', 0.8)
        turbine['geometry']['coefficients'].setdefault('d_inner_ratio', 0.95)
        turbine['geometry']['coefficients'].setdefault('beta', 4.6)

        # ['losses']
        turbine['losses'].setdefault('drag_inlet_ratio', 1.017)
        turbine['losses'].setdefault('phi', 1.0) #(16)
        turbine['losses'].setdefault('psi', 0.96) #(29)

    elif turbine['type'] == 'axial':
        # ['efficiency']
        turbine['efficiency'].setdefault('eta_Te', 0.795) # (2)
        turbine['efficiency'].setdefault('sigma_esc', 0.99) # (1)
        turbine['efficiency'].setdefault('ksi', 0.56) # (5)
        turbine['efficiency'].setdefault('rho', 0.38) # (6)
        turbine['efficiency'].setdefault('c_u1', 0.95) # (27)
        turbine['efficiency'].setdefault('c_u2', 0.85) # (27)
        turbine['efficiency'].setdefault('eta_m', 0.97) # (66)

        # ['geometry']
        turbine['geometry'].setdefault('alpha_1', 16) # (11)
        turbine['geometry'].setdefault('beta_1Blade', 90) # (16)
        turbine['geometry'].setdefault('alpha_0', 90) # (27)
        turbine['geometry'].setdefault('delta', 0.8) # (38)

        # ['geometry']['coefficients']
        turbine['geometry']['coefficients'].setdefault('t1Tol1', 0.88) # (22)
        turbine['geometry']['coefficients'].setdefault('m', 1.08) # (26)
        turbine['geometry']['coefficients'].setdefault('t2Tol2', 0.81) # (45)
        turbine['geometry']['coefficients'].setdefault('beta', 2) # (61)

        # ['losses']
        turbine['losses'].setdefault('drag_inlet_ratio', 1.046) # (0)
        turbine['losses'].setdefault('phi', 0.97) # (10)
        turbine['losses'].setdefault('psi', 0.95) # (29)

    else: None

    return turbine
