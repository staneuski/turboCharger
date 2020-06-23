def radial_turbine_post(run, engine,
        compressor, u_2K, D_2K, RPM, eta_KsStagnRated, L_KsStagn, N_K, p_vStagn,
        turbine, Turbine):
    '''
        Post-processing calculated radial trubine data
    '''
    from turbine_output import turbine_output
    from edit_pictures import edit_pictures
    from save_results import save_results
    from create_results import create_results
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    turbine_output(turbine, N_K, Turbine)

    create_results(run, engine,
                   compressor, u_2K, D_2K, RPM, eta_KsStagnRated, L_KsStagn, N_K, p_vStagn,
                   turbine, Turbine)

    edit_pictures(RPM, turbine, Turbine)

    save_results()

# ''' (C) 2018-2020 Stanislau Stasheuski '''