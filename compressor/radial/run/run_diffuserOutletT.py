# -*- coding: utf-8 -*-
def diffuserOutletT(b_2, D_2, T_2, c_2, b_4, D_4, guessedT_4, n_4):  
    '''
        Description:    Calculate diffuser outlet temperature
    '''

    from commonConfig import(k, R)

    q = pow(D_2*b_2/D_4/b_4, 2)
    m = 2/(n_4 - 1)
    sigma = (k - 1)/2 * pow(c_2, 2)/k/R/T_2

    T_4 = T_2*( 1 + sigma*(1 - q*pow(T_2/guessedT_4, m)) )

    return T_4