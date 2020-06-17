# -*- coding: utf-8 -*-
def piK(l_0, p_e, eta_KsStagn, guessedPiK):
    '''
    Description:    Calculate pressure increase ratio
    '''

    from commonConfig import(
        R, g_e, alpha, k, E, T_ca, eta_v
    )
    from compressorConfig import(
        T_aStagn, T_aStagn, p_aStagn, sigma_0, sigma_c, sigma_v
    )

    # Converting data to SI dimensions
    g_e      *= 1e-03 # -> [kg/W/h] or [g/kW/h]
    p_aStagn *= 1e06 # -> [Pa]

    # Calculation pressure degree increase
    pressureIncreaseRatio = (
        R*T_aStagn*g_e*l_0*alpha
        *(
            ( (pow(guessedPiK,(k - 1)/k) - 1)/eta_KsStagn + 1 )
            *(1 - E)+E*T_ca/T_aStagn
        )
        *p_e/p_aStagn/3600/eta_v/sigma_0/sigma_c/sigma_v
    )

    return pressureIncreaseRatio
