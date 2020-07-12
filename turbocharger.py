#!/usr/bin/env python3
'''
    API:            Python 3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           turbocharger
    Description:    Calculate turbocharger parameters using 0D method

'''

def turbocharger_compressor(run, engine, compressor):
    '''
        Calculate compressor part of the turbocharger
    '''
    from compressor.compressor_pre import compressor_pre
    from compressor.compressor_run import compressor_run
    from compressor.compressor_post import compressor_post
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 
    compressor_pre(run, engine, compressor)

    (compressor, Compressor) = compressor_run(run, engine, 
                                              compressor)

    compressor_post(run, engine,
                    compressor, Compressor)

    return Compressor


def turbocharger_turbine(run, ambient, engine,
        compressor, Compressor,
        turbine):
    '''
        Calculate turbine part of the turbocharger
    '''
    from turbine.turbine_pre import turbine_pre
    from turbine.turbine_run import turbine_run
    from turbine.turbine_post import turbine_post
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    turbine_pre(run, engine, compressor, turbine)

    (turbine, Turbine) = turbine_run(ambient, engine,
                                     compressor, Compressor,
                                     turbine)

    turbine_post(run, engine,
                 compressor, Compressor,
                 turbine, Turbine)

    return Turbine


def main():
    '''
        Calculate turbocharger parameters using 0D method
    '''
    from etc.logo import logo
    from etc.engine_extend import engine_extend

    from commonConfig import run, ambient
    from engineConfig import engine
    from compressor.compressorConfig import compressor
    from turbine.turbineConfig import turbine
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    logo()
    engine_extend(engine)


    Compressor = turbocharger_compressor(run, engine,
                                         compressor)


    Turbine = turbocharger_turbine(run, ambient, engine,
                                   compressor, Compressor,
                                   turbine)

    return compressor, Compressor, turbine, Turbine


if __name__ == '__main__':
    main()


# ''' (C) 2018-2020 Stanislau Stasheuski '''