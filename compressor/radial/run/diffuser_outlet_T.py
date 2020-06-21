def diffuser_outlet_T(inlet, D_2, b_2, T_2, c_2, D_out, b_out, T_out, n_out):
    '''
        Calculate diffuser outlet temperature
    '''

    q = pow(D_2*b_2/D_out/b_out, 2)
    m = 2/(n_out - 1)
    sigma = (inlet['k'] - 1)/2 * pow(c_2, 2)/inlet['k']/inlet['R']/T_2

    T_out = T_2*(1 + sigma*(1 - q*pow(T_2/T_out, m)))

    return T_out
