#!/usr/bin/env python3

from __future__ import division
import sys
import math
sys.path.append('etc/')
sys.path.extend(['compressor/', 'compressor/radial/'])

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def main():
    '''
        API:            Python 3.x
        Project:        https://github.com/StasF1/turboCharger
        Version:        2.x
        License:        GNU General Public License 3.0 ( see LICENSE )
        Author:         Stanislau Stasheuski

        File:           turbocharger
        Description:    Calculate turbocharger parameters using 0D method

    '''
    from logo import logo
    from engine_extend import engine_extend
    from default_value import default_value
    from output_calc_error import output_calc_error

    from compressor_radial_pre import compressor_radial_pre
    from compressor_radial_run import compressor_radial_run
    # from compressor_radial_post import compressor_radial_post

    # Load input data from project dictionaries
    from commonConfig import run
    from engineConfig import engine
    from compressorConfig import compressor

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    logo()
    engine_extend(engine)


    # Compressor
    # ~~~~~~~~~~
    sys.path.extend(['compressor/radial/pre',
                     'compressor/radial/run',
                     'compressor/radial/post'])

    compressor_radial_pre(run, engine, compressor)
    compressor_radial_run(run, engine, compressor)
    # compressor_radial_post(run, engine, compressor)


if __name__ == '__main__':
    main()


# ''' (C) 2018-2020 Stanislau Stasheuski '''