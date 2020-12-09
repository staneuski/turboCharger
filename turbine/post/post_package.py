def post(project, engine,
         compressor, Compressor,
         turbine, Turbine):
    """Post-processing calculated radial trubine data."""

    from turbine.post.output import output
    from turbine.post.edit_pictures import edit_pictures
    from turbine.post.report import report
    from turbine.post.save_results import save_results

    output(Compressor,
           turbine, Turbine)

    report(project, engine,
           compressor, Compressor,
           turbine, Turbine)

    edit_pictures(Compressor,
                  turbine, Turbine)

    save_results(turbine)


# ''' (C) 2018-2020 Stanislau Stasheuski '''