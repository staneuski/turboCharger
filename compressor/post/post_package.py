def post(project, engine, compressor, Compressor):
    ''' Post-processing calculated radial compressor data
    '''
    from compressor.post.output import output
    from compressor.post.report import report
    from compressor.post.edit_pictures import edit_pictures
    from compressor.post.save_results import save_results
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    output(compressor, Compressor)

    report(project, engine, compressor, Compressor)

    edit_pictures(compressor, Compressor)

    save_results(compressor)


# ''' (C) 2018-2020 Stanislau Stasheuski '''