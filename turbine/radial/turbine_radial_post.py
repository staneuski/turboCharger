def turbine_radial_post(run, engine,
        compressor, Compressor,
        turbine, Turbine):
    '''
        Post-processing calculated radial trubine data
    '''
    from turbine_output import turbine_output
    from turbine_radial_edit_pictures import edit_pictures
    from create_results import create_results
    from turbine_radial_save_results import save_results
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    turbine_output(Compressor,
                   turbine, Turbine)

    create_results(run, engine,
                   compressor, Compressor,
                   turbine, Turbine)

    edit_pictures(Compressor, turbine, Turbine)

    save_results()

# ''' (C) 2018-2020 Stanislau Stasheuski '''