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
if not os.path.exists("../../results/turbine"):   os.makedirs("../../results/turbine")

shutil.copyfile("../../commonDict.py",  "../../results/commonDict.py")

shutil.copyfile("turbineDict.py",  "../../results/turbine/turbineDict.py")
shutil.copyfile("turbine.log",     "../../results/turbine/turbine.log")
shutil.move("turbineReport.md",    "../../results/turbine/turbineReport.md")
shutil.move("axisCut.png",         "../../results/turbine/axisCut.png")
shutil.move("radialCut.png",       "../../results/turbine/radialCut.png")

if not os.path.exists("../../results"):   os.makedirs("../../results")
