def turbine_output(Compressor,
        turbine, Turbine):
    '''
        Output results in the Terminal window
    '''
    from output_calc_error import output_calc_error
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # Display some results right in the Terminal window
    print("Energy conversion efficiency coeficients are:\
          \n\teta_Te  = {0:.4f} - set\
          \n\teta_Te' = {1:.4f} - rated"\
          .format(turbine['efficiency']['eta_Te'],
                  Turbine.eta_TeRated)) # (dict) & (60)
    output_calc_error(Turbine.errorEta) # (61)

    print("Power consumption:\
          \n\tN_c = {N_K_kW:.3f} kW - of compressor\
          \n\tN_t = {N_T_kW:.3f} kW - of turbine"\
          .format(N_K_kW = Compressor.N_K*1e-03,
                  N_T_kW = Turbine.N_T*1e-03)) # (compressor) & (63)
    output_calc_error(Turbine.errorN) # (62)

    print("If something doesn't work correctly make a new issue or check the others:\
    \nhttps://github.com/StasF1/turboCharger/issues")


# ''' (C) 2018-2020 Stanislau Stasheuski '''