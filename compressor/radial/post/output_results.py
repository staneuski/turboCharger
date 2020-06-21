def output_results(compressor, CompCalc):
    '''
        Output results in the Terminal window
    '''

    from output_calc_error import output_calc_error

    print('Diameter of the wheel is {0:.0f} mm\n' .format(compressor['geometry']['D_2']*1e+03)) # (15)

    print('Parameters by cuts:')
    if 'VANELESS' in compressor['diffuser']:  print('\
        1-1: T_1 = {0:.0f} K,   p_1 = {1:.4f} MPa\n\
        2-2: T_2 = {2:.0f} K,   p_2 = {3:.4f} MPa\n\
        4-4: T_4 = {4:.0f} K,   p_4 = {5:.4f} MPa\n'
        .format(CompCalc.T_1, CompCalc.p_1*1e-06, CompCalc.T_2, CompCalc.p_2*1e-06, CompCalc.T_4, CompCalc.p_4*1e-06))
    else:   print('\
        1-1: T_1 = {0:.0f} K,   p_1 = {1:.4f} MPa\n\
        2-2: T_2 = {2:.0f} K,   p_2 = {3:.4f} MPa\n\
        3-3: T_3 = {4:.0f} K,   p_3 = {5:.4f} MPa\n\
        4-4: T_4 = {6:.0f} K,   p_4 = {7:.4f} MPa\n'
        .format(CompCalc.T_1, CompCalc.p_1*1e-06, CompCalc.T_2, CompCalc.p_2*1e-06, CompCalc.T_3, p_3*1e-06, CompCalc.T_4, CompCalc.p_4*1e-06))

    print('Actual pressure degree increase is {0:.2f}, when\n\
    precalculated/set pressure degree increase is {1:.2f}'\
        .format(CompCalc.pi_KStagn, compressor['pi_K'])) # (57)
    output_calc_error(CompCalc.pi_KError) # (60)

    print("Energy conversion efficiency coeficients are:\n\
        eta_Ks*  = {0:.4f} - set\n\
        eta_Ks*' = {1:.4f} - rated"
        .format(compressor['efficiency']['eta_KsStagn'], CompCalc.eta_KsStagnRated)) # (dict) & (59)
    output_calc_error(CompCalc.errorEta) # (60)

    print("Isentropy head coeficients are:\n\
        H_Ks*  = {0:.4f} - set\n\
        H_Ks*' = {1:.4f} - rated"
        .format(compressor['efficiency']['H_KsStagn'], CompCalc.H_KsStagnRated)) # (dict) & (61)
    output_calc_error(CompCalc.errorH) # (62)

    print("If something doesn't work correctly make a new issue or check the others:\n\
    https://github.com/StasF1/turboCharger/issues")

