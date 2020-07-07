def compressor_output(compressor, Compressor):
    '''
        Output results in the Terminal window
    '''
    from output_calc_error import output_calc_error
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    print("\033[94m''' Compressor '''\033[0m\n")

    print('Diameter of the wheel is {0:.0f} mm\n'
          .format(compressor['geometry']['D_2']*1e+03)) # (15)

    print('Parameters by cuts:')
    if 'VANELESS' in compressor['diffuser']:
        print('\t1-1: T_1 = {0:.0f} K,  p_1 = {1:.4f} MPa\
              \n\t2-2: T_2 = {2:.0f} K,  p_2 = {3:.4f} MPa\
              \n\t4-4: T_4 = {4:.0f} K,  p_4 = {5:.4f} MPa'
              .format(Compressor.T_1, Compressor.p_1*1e-06,
                      Compressor.T_2, Compressor.p_2*1e-06,
                      Compressor.T_4, Compressor.p_4*1e-06))

    else:
        print('\t1-1: T_1 = {0:.0f} K,  p_1 = {1:.4f} MPa\
              \n\t2-2: T_2 = {2:.0f} K,  p_2 = {3:.4f} MPa\
              \n\t3-3: T_3 = {4:.0f} K,  p_3 = {5:.4f} MPa\
              \n\t4-4: T_4 = {6:.0f} K,  p_4 = {7:.4f} MPa'
              .format(Compressor.T_1, Compressor.p_1*1e-06,
                      Compressor.T_2, Compressor.p_2*1e-06,
                      Compressor.T_3, Compressor.p_3*1e-06,
                      Compressor.T_4, Compressor.p_4*1e-06))

    print('Actual pressure degree increase is {0:.2f}, when\
          \nprecalculated/set pressure degree increase is {1:.2f}'\
          .format(Compressor.pi_KStagn, compressor['pi_K'])) # (57)

    output_calc_error(Compressor.pi_KError) # (60)

    print("Energy conversion efficiency coeficients are:\
        \n\teta_Ks*  = {0:.4f} - set\
        \n\teta_Ks*' = {1:.4f} - rated"
          .format(compressor['efficiency']['eta_KsStagn'],
                  Compressor.eta_KsStagnRated)) # (dict) & (59)
    output_calc_error(Compressor.errorEta) # (60)

    print("Isentropy head coeficients are:\
          \n\tH_Ks*  = {0:.4f} - set\
          \n\tH_Ks*' = {1:.4f} - rated"
          .format(compressor['efficiency']['H_KsStagn'],
                  Compressor.H_KsStagnRated)) # (dict) & (61)

    output_calc_error(Compressor.errorH) # (62)

    print("\n\033[94m''' Turbine ''' \033[0m\n")


# ''' (C) 2018-2020 Stanislau Stasheuski '''