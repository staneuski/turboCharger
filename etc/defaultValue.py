def defaultValue(parameter, defaultValue):
    "Sets parameter as its default value"
    if issubclass(type(parameter), str):    parameter = defaultValue;
    return parameter;