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
#     Creates folder compressorResults and move results there
# 
#-----------------------------------------------------------------------

# Creating directory if needed 
if not os.path.exists("compressorResults"):   os.makedirs("compressorResults")

shutil.copyfile("solvedParameters.py", "../turbine/axial/solvedParameters.py")
shutil.move("solvedParameters.py",   "../turbine/radial/solvedParameters.py")

shutil.copyfile("compressorDict.py", "compressorResults/compressorDict.py")
shutil.move("compressorReport.md",   "compressorResults/compressorReport.md")
shutil.move("axisCut.png",           "compressorResults/axisCut.png")
shutil.move("blades.png",            "compressorResults/blades.png")
shutil.move("outWheel.png",          "compressorResults/outWheel.png")