def turbine(project, ambient, engine,
        compressor, Compressor,
        turbine):
    """Calculate turbine part of the turbocharger."""

    from turbine.pre.pre_package import pre
    from turbine.run.run_package import run
    from turbine.post.post_package import post

    pre(project, engine,
        compressor, turbine)

    (turbine, Turbine) = run(ambient, engine,
                             compressor, Compressor,
                             turbine)

    post(project, engine,
         compressor, Compressor,
         turbine, Turbine)

    return Turbine

# ''' (C) 2020 Stanislau Stasheuski '''