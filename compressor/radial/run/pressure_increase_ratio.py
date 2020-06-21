def pressure_increase_ratio(engine, compressor):
    '''
        Calculate compressor pressure increase ratio
    '''

    # Calculation pressure degree increase
    compressor['pi_K'] = (
        engine['inlet']['R']
        *compressor['initial']['T_aStagn']
        *engine['efficiency']['b_e']
        *engine['combustion']['l_0']
        *engine['combustion']['alpha']
        *engine['efficiency']['p_e']
        *(
            (
                (
                    pow(
                        compressor['pi_K'],
                        (engine['inlet']['k'] - 1)/engine['inlet']['k']
                    ) - 1
                )/compressor['efficiency']['eta_KsStagn'] + 1
            )
            *(1 - engine['heat']['E'])
            + engine['heat']['E']*engine['heat']['T_ca']/compressor['initial']['T_aStagn']
        )
        /compressor['initial']['p_aStagn']/3600
        /compressor['losses']['sigma_0']
        /compressor['losses']['sigma_c']
        /compressor['losses']['sigma_v']
    )

    return compressor['pi_K']