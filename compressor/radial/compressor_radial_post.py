def compressor_radial_post(run, engine, compressor, Compressor):
    '''
        Calculate compressor parameters using 0D method
    '''
    from output_results import output_results
    from post_toTurbine import toTurbine
    from create_report import create_report
    from edit_pictures import edit_pictures
    from save_results import save_results
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    toTurbine(compressor, Compressor)

    output_results(compressor, Compressor)

    create_report(run, engine, compressor, Compressor)

    edit_pictures(compressor, Compressor)

    save_results(compressor)


# ''' (C) 2018-2020 Stanislau Stasheuski '''