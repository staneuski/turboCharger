def toTurbine(compressor, CompCalc):
    '''
        Make dictionary for turbine after compressor run
    '''

    toTurbine = open("compressorToTurbineConfig.py", "w")
    toTurbine.write(f"""\
# '''
#     API:            Python 3.x
#     Project:        https://github.com/StasF1/turboCharger
#     Version:        2.x
#     License:        GNU General Public License 3.0 ( see LICENSE )
#     Author:         Stanislau Stasheuski
#
#     File:           compressorToTurbineConfig
#     Description:    Automatically created dictionary w/
#                     solved parameters from compressor
#
# '''

u_2K = {CompCalc.u_2} # [m/s]

D_2K = {compressor['geometry']['D_2']} # [m]

RPM = {CompCalc.RPM} # [1/min]

eta_KsStagnRated = {CompCalc.eta_KsStagnRated} # [-]

L_KsStagn = {CompCalc.L_KsStagn} # [J/kg]

N_K = {CompCalc.N_K} # [W]

p_vStagn = {CompCalc.p_vStagn} # [Pa]

# ''' (C) 2018-2019 Stanislau Stasheuski '''\
""")

    toTurbine.close