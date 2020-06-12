# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|o_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  3.x
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__o|  	 |
#-----------------------------------------------------------------------
# Included script
#     reportGenerator
#
# Description
#     Makes dictionary for turbine
# 
#-----------------------------------------------------------------------

toTurbine = open("solvedParameters.py", "w")
toTurbine.write(
"# -*- coding: utf-8 -*-\n\
#-----------------------------------------------------------------------\n\
#	   ___    	 |\n\
#	 _|˚_ |_ 	 |   Language: Python\n\
#	/  ___| \	 |   Version:  3.x\n\
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger\n\
#	  |__˚|  	 |\n\
#-----------------------------------------------------------------------\n\
# Dictionary\n\
#     solvedParameters\n\
#\n\
# Description\n\
#     Solved parameters from compressor\n\
#     This dictionary compilated automaticaly!\n\
#\n\
#-----------------------------------------------------------------------\n\n"
);
toTurbine.write("u_2K = %.7f # m/s\n\n" %u_2)
toTurbine.write("D_2K = %.3f # m\n\n" %D_2)
toTurbine.write("n_TCh = %.2f # RPM\n\n" %n_tCh)
toTurbine.write("eta_KsStagnRated = %.7f\n\n" %eta_KsStagnRated)
toTurbine.write("L_KsStagn = %.7f # J/kg\n\n" %L_KsStagn)
toTurbine.write("N_K = %.7f # V\n\n" %N_K)
toTurbine.write("p_vStagn = %.7f # Pa\n\n\n\n" %p_vStagn)
toTurbine.close()