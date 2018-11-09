# -*- coding: utf-8 -*-
# Creates folder with compressorResults and move them there

# Creating directory if needed 
if not os.path.exists("compressorResults"):   os.makedirs("compressorResults");

shutil.copyfile("compressorDict.py",   "compressorResults/compressorDict.py");
shutil.move("solvedParameters.py",     "../turbine/solvedParameters.py");
shutil.move("compressorReport.md",     "compressorResults/compressorReport.md");
shutil.move("dimensionedAxisCut.png",  "compressorResults/dimensionedAxisCut.png");
shutil.move("dimensionedBlades.png",   "compressorResults/dimensionedBlades.png");
shutil.move("outWheel.png",            "compressorResults/outWheel.png");