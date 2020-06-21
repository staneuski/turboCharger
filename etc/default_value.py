def default_value(par, default_value):
    '''
        Set default parameter value
    '''
    if issubclass(type(par), str):
        par = default_value

    return par
