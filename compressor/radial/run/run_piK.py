# -*- coding: utf-8 -*-
def pressureIncreaseRatio(engine, compressor, R, k, pi_K):
    '''
    Description:    Calculate pressure increase ratio
    '''

    # Calculation pressure degree increase
    pi_K = (
        R
        *compressor['initial']['T_aStagn']
        *engine['efficiency']['b_e']
        *engine['combustion']['l_0']
        *engine['combustion']['alpha']
        *engine['efficiency']['p_e']
        *(
            (
                (pow(pi_K,(k - 1)/k) - 1)
                /compressor['efficiency']['eta_KsStagn'] + 1
            )
            *(1 - engine['heat']['E'])
            + engine['heat']['E']*engine['heat']['T_ca']/compressor['initial']['T_aStagn']
        )
        /compressor['initial']['p_aStagn']/3600
        /compressor['initial']['sigma_0']
        /compressor['initial']['sigma_c']
        /compressor['initial']['sigma_v']
    )

    return pi_K