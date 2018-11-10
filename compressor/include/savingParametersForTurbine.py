# -*- coding: utf-8 -*-
# Makes dictionary for turbine

toTurbine = open("solvedParameters.py", "w")
toTurbine.write("# -*- coding: utf-8 -*-\n")
toTurbine.write("# This dictionary compilates automaticaly!\n\n")
toTurbine.write("# Solved parameters from compressor\n\n")
toTurbine.write("u_2K = %.7f # m/s\n\n" %u_2)
toTurbine.write("D_2K = %.3f # m\n\n" %D_2)
toTurbine.write("n_TCh = %.2f # RPM\n\n" %n_tCh)
toTurbine.write("eta_KsStagnRated = %.7f\n\n" %eta_KsStagnRated)
toTurbine.write("L_KsStagn = %.7f # J/kg\n\n" %L_KsStagn)
toTurbine.write("N_K = %.7f # V\n\n" %N_K)
toTurbine.write("p_vStagn = %.7f # Pa\n\n\n\n" %p_vStagn)
toTurbine.close()