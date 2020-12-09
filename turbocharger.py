#!/usr/bin/env python3
'''
    Python:         3.x
    Project:        https://github.com/StasF1/turboCharger
    Version:        2.x
    License:        GNU General Public License 3.0 ( see LICENSE )
    Author:         Stanislau Stasheuski

    File:           turbocharger
    Description:    Calculate turbocharger parameters using 0D method
'''

def main():
    """Calculate turbocharger parameters using 0D method."""

    from etc.logo import logo
    from etc.engine_extend import engine_extend

    from common_config import project, ambient
    from engine_config import engine
    from compressor.compressor_config import compressor
    from turbine.turbine_config import turbine
    from compressor.compressor_package import compressor as turbocharger_compressor
    from turbine.turbine_package import turbine as turbocharger_turbine

    logo()
    engine_extend(engine)
    Compressor = turbocharger_compressor(project, engine, compressor)
    Turbine = turbocharger_turbine(project, ambient, engine, compressor, Compressor,
                                   turbine)

    return compressor, Compressor, turbine, Turbine

if __name__ == '__main__':
    main()


# ''' (C) 2020 Stanislau Stasheuski '''