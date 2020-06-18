# -*- coding: utf-8 -*-
def pressureIncreaseRatio(comressor, l_0, p_e, pi_K):
    '''
    Description:    Calculate pressure increase ratio
    '''

    from commonConfig import(
        R, g_e, alpha, k, E, T_ca, eta_v
    )

    # Converting data to SI dimensions
    g_e *= 1e-03 # -> [kg/W/h] or [g/kW/h]

    initial    = comressor['initial']
    efficiency = comressor['efficiency']

    # Calculation pressure degree increase
    pi_K = (
        R*initial['T_aStagn']*g_e*l_0*alpha*p_e
        *(
            ( (pow(pi_K,(k - 1)/k) - 1)/efficiency['eta_KsStagn'] + 1 )
            *(1 - E)+E*T_ca/initial['T_aStagn']
        )
        /
        initial['p_aStagn']/3600/initial['sigma_0']/initial['sigma_c']/initial['sigma_v']
    )

    return pi_K