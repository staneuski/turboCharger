def turbine_axial_post(run, engine,
        compressor, Compressor,
        turbine, Turbine):
    '''
        Post-processing calculated radial trubine data
    '''
    from turbine_output import turbine_output
    from turbine_axial_create_results import turbine_axial_create_results
    from turbine_axial_edit_pictures import turbine_axial_edit_pictures
    from turbine_axial_save_results import turbine_axial_save_results
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    turbine_output(Compressor,
                   turbine, Turbine)

    turbine_axial_create_results(run, engine,
                                 compressor, Compressor,
                                 turbine, Turbine)

    turbine_axial_edit_pictures(turbine, Turbine)

    turbine_axial_save_results()

# ''' (C) 2018-2020 Stanislau Stasheuski '''