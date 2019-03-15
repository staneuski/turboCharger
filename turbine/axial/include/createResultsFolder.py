# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#	   ___    	 |
#	 _|˚_ |_ 	 |   Language: Python
#	/  ___| \	 |   Version:  2.7
#	\_| ____/	 |   Website:  https://github.com/StasF1/turboCharger
#	  |__˚|  	 |
#-----------------------------------------------------------------------
# Included script
#     createResultsFolder
#
# Description
#     Creates folder ../../results/turbine and move results
#     there
# 
#-----------------------------------------------------------------------

# Creating dir if needed
if not os.path.exists("../../results/turbine/axial/"):   os.makedirs("../../results/turbine/axial")

shutil.copyfile("../../commonDict.py",  "../../results/commonDict.py")

shutil.move("axialTurbineReport.md","../../results/axialTurbineReport.md")
shutil.copyfile("turbineDict.py",   "../../results/turbine/axial/turbineDict.py")
shutil.copyfile("solvedParameters.py","../../results/turbine/axial/solvedParameters.py")
shutil.move("axisCut.png",          "../../results/turbine/axial/axisCut.png")
shutil.move("radialCut.png",        "../../results/turbine/axial/radialCut.png")
