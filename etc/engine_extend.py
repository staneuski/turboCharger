def engine_extend(engine):
    '''
        Extend engine dictionary with its relative parameters
    '''
    import math
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # Convert data to SI dimensions
    engine['geometry']['bore']   *= 1e-02 # -> [m]
    engine['geometry']['stroke'] *= 1e-02 # -> [m]
    engine['efficiency']['N_e']  *= 1e+03 # -> [W]
    engine['efficiency']['b_e']  *= 1e-03 # -> [kg/W/h] or [g/engine['inlet']['k']W/h]

    # Теоретическое количество воздуха, необходимое для сгорания 1 кг топлива
    if 'SI' in engine['combustion']['ignition']:
        engine['combustion']['l_0'] = 14.84 # [kg]
    elif 'CI' in engine['combustion']['ignition']:
        engine['combustion']['l_0'] = 14.31 # [kg]
    else:
        exit(f"\033[91mERROR:\
             Variable engine['combustion']['ignition'] is incorrect!\
             \nValid values are 'SI' and 'CI'"
             .replace('             ', ' '))

    # Effective pressure | Среднее эффективное давление
    engine['efficiency']['p_e'] = (
        0.12*1e03*engine['efficiency']['N_e']*engine['combustion']['strokeNo']
        /math.pi/engine['geometry']['bore']**2
        /engine['geometry']['stroke']
        /engine['efficiency']['RPM']
        /engine['geometry']['pistonNo']
    # [Pa]
    )

    return engine