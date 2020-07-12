def compressor(project, engine, compressor):
    ''' Calculate compressor part of the turbocharger
    '''
    from compressor.pre.pre_package import pre
    from compressor.run.run_package import run
    from compressor.post.post_package import post
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 
    pre(project, engine, compressor)

    (compressor, Compressor) = run(project, engine, compressor)

    post(project, engine, compressor, Compressor)

    return Compressor

# ''' (C) 2018-2020 Stanislau Stasheuski '''