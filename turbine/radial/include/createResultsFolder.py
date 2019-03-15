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
#     Creates folder ../../results/turbine and moves
#     results there
# 
#-----------------------------------------------------------------------

# Creating dir if needed
if not os.path.exists("../../results/turbine"):   os.makedirs("../../results/turbine")

shutil.copyfile("../../commonDict.py",  "../../results/commonDict.py")

shutil.copyfile("turbineDict.py",  "../../results/turbine/turbineDict.py")
# shutil.copyfile("turbine.log",     "../../results/turbine/turbine.log")
shutil.move("turbineReport.md",    "../../results/turbine/turbineReport.md")
shutil.move("axisCut.png",         "../../results/turbine/axisCut.png")
shutil.move("inTurbineWheel.png",  "../../results/turbine/inTurbineWheel.png")
shutil.move("outTurbineWheel.png", "../../results/turbine/outTurbineWheel.png")
shutil.copyfile("../../programFiles/turbine/radial/i-sPlot.png", "../../results/turbine/i-sPlot.png")
