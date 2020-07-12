def turbine_post(run, engine,
        compressor, Compressor,
        turbine, Turbine):
    '''
        Post-processing calculated radial trubine data
    '''
    from turbine.post.turbine_output import turbine_output
    from turbine.post.turbine_edit_pictures import turbine_edit_pictures
    from turbine.post.turbine_report import turbine_report
    from turbine.post.turbine_save_results import turbine_save_results
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    turbine_output(Compressor,
                   turbine, Turbine)

    turbine_report(run, engine,
                   compressor, Compressor,
                   turbine, Turbine)

    turbine_edit_pictures(Compressor, turbine, Turbine)

    turbine_save_results(turbine)


# ''' (C) 2018-2020 Stanislau Stasheuski '''