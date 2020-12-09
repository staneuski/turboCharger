def output(compressor, Compressor):
    """Output results in the Terminal window."""

    from etc.output_calc_error import output_calc_error

    print("\033[94m''' Compressor '''\033[0m\n")

    print("Diameter of the wheel is "
          f"{compressor['geometry']['D_2']*1e+03:.0f} mm\n") # (15)

    if 'VANED' in compressor['diffuser']:
        T3_p3 = (f"\t3-3: T_3 = {Compressor.T_3:.0f} K,"
                 f"  p_3 = {Compressor.p_3*1e-06:.4f} MPa\n")
    else:
        T3_p3 = ""

    print("Parameters by cuts:\n"
          f"\t1-1: T_1 = {Compressor.T_1:.0f} K,"
          f"  p_1 = {Compressor.p_1*1e-06:.4f} MPa\n"
          f"\t2-2: T_2 = {Compressor.T_2:.0f} K,"
          f"  p_1 = {Compressor.p_2*1e-06:.4f} MPa\n"
          + T3_p3 +
          f"\t4-4: T_4 = {Compressor.T_4:.0f} K,"
          f"  p_4 = {Compressor.p_4*1e-06:.4f} MPa\n")

    print("Actual pressure degree increase is {0:.2f}, when\n"
          "precalculated/set pressure degree increase is {1:.2f}"
          .format(Compressor.pi_KStagn, compressor['pi'])) # (57)

    output_calc_error(Compressor.pi_KError) # (60)

    print("Energy conversion efficiency coeficients are:\n"
          "\teta_Ks*  = {0:.4f} - set\n"
          "\teta_Ks*' = {1:.4f} - rated"
          .format(compressor['efficiency']['eta_KsStagn'],
                  Compressor.eta_KsStagnRated)) # (dict) & (59)
    output_calc_error(Compressor.eta_error) # (60)

    print("Isentropy head coeficients are:\n"
          "\tH_Ks*  = {0:.4f} - set\n"
          "\tH_Ks*' = {1:.4f} - rated"
          .format(compressor['efficiency']['H_KsStagn'],
                  Compressor.H_KsStagnRated)) # (dict) & (61)
    output_calc_error(Compressor.H_error) # (62)

    print("\n\033[94m''' Turbine ''' \033[0m\n")


# ''' (C) 2018-2020 Stanislau Stasheuski '''