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
#     Creates folder turbineResults and move results there
# 
#-----------------------------------------------------------------------

# Creating dir if needed
if not os.path.exists("turbineResults"):   os.makedirs("turbineResults")

shutil.copyfile("turbineDict.py",  "turbineResults/turbineDict.py")
shutil.move("turbineReport.md",    "turbineResults/turbineReport.md")
shutil.move("axisCut.png",         "turbineResults/axisCut.png")
shutil.move("inTurbineWheel.png",  "turbineResults/inTurbineWheel.png")
shutil.move("outTurbineWheel.png", "turbineResults/outTurbineWheel.png")
shutil.copyfile("../../programFiles/turbine/radial/i-sPlot.png", "turbineResults/i-sPlot.png")
