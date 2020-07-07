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
import sys
import math

sys.path.extend(['etc/', 'compressor/', 'turbine/'])
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def turbocharger_compressor(run, engine, compressor):
    '''
        Calculate compressor part of the turbocharger
    '''
    from compressor_pre import compressor_pre
    from compressor_run import compressor_run
    from compressor_post import compressor_post

    sys.path.extend(['compressor/pre', 'compressor/post'])
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
    from turbine_pre import turbine_pre
    from turbine_run import turbine_run
    from turbine_post import turbine_post

    sys.path.extend(['turbine/pre', 'turbine/post'])
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
    from logo import logo
    from engine_extend import engine_extend

    from commonConfig import run, ambient
    from engineConfig import engine
    from compressorConfig import compressor
    from turbineConfig import turbine
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