# -*- coding: utf-8 -*-
# '''
#     Description:    Make dictionary for turbine after compressor run
# '''

toTurbine = open("solvedParameters.py", "w")
toTurbine.write(
"# -*- coding: utf-8 -*-\n\
# '''\n\
#     API:            Python 3.x\n\
#     Project:        https://github.com/StasF1/turboCharger\n\
#     Version:        2.x\n\
#     License:        GNU General Public License 3.0 ( see LICENSE )\n\
#     Author:         Stanislau Stasheuski\n\
#\n\
#     File:           solvedParameters\n\
#     Description:    Automatically created dictionary w/\n\
#                     solved parameters from compressor\n\
#\n\
# '''\n\n"
)
toTurbine.write("u_2K = %.7f # [m/s]\n\n" %u_2)
toTurbine.write("D_2K = %.3f # [m]\n\n" %D_2)
toTurbine.write("n_TCh = %.2f # [RPM]\n\n" %n_tCh)
toTurbine.write("eta_KsStagnRated = %.7f # [-]\n\n" %eta_KsStagnRated)
toTurbine.write("L_KsStagn = %.7f # [J/kg]\n\n" %L_KsStagn)
toTurbine.write("N_K = %.7f # [W]\n\n" %N_K)
toTurbine.write("p_vStagn = %.7f # [Pa]\n\n" %p_vStagn)

toTurbine.write("# ''' (C) 2018-2019 Stanislau Stasheuski '''")
toTurbine.close()