def turbine_axial_pre(run, ambient, engine,
        compressor,
        turbine):
    '''
        Extend turbine dictionary with its relative parameters and
        precalculate some compressor parameters
    '''
    from turbine_axial_set_default_values import set_default_values
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # Converting data to SI dimensions
    if issubclass(type(turbine['geometry']['delta']), float):
        turbine['geometry']['delta'] *= 1e-03 # -> [m]

    set_default_values(turbine)

    return turbine


# ''' (C) 2018-2020 Stanislau Stasheuski '''