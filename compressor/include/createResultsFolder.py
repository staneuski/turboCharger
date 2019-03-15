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
if not os.path.exists("../results/compressor"):   os.makedirs("../results/compressor")

shutil.copyfile("solvedParameters.py", "../turbine/axial/solvedParameters.py")
shutil.move("solvedParameters.py",   "../turbine/radial/solvedParameters.py")

shutil.copyfile("compressorDict.py", "../results/compressor/compressorDict.py")
shutil.copyfile("compressor.log",    "../results/compressor/compressor.log")
shutil.move("compressorReport.md",   "../results/compressor/compressorReport.md")
shutil.move("axisCut.png",           "../results/compressor/axisCut.png")
shutil.move("blades.png",            "../results/compressor/blades.png")
shutil.move("outWheel.png",          "../results/compressor/outWheel.png")
if 'VANED' in diffuserType:
    shutil.move("perpendicularCut.png", "../results/compressor/perpendicularCut.png")