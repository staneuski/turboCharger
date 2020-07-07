def compressor_post(run, engine, compressor, Compressor):
    '''
        Post-processing calculated radial compressor data
    '''
    from compressor_output import compressor_output
    from compressor_report import compressor_report
    from compressor_edit_pictures import compressor_edit_pictures
    from compressor_save_results import compressor_save_results
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    compressor_output(compressor, Compressor)

    compressor_report(run, engine, compressor, Compressor)

    compressor_edit_pictures(compressor, Compressor)

    compressor_save_results(compressor)


# ''' (C) 2018-2020 Stanislau Stasheuski '''