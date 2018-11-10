# -*- coding: utf-8 -*-
# Creates folder with results and move them there

# Creating dir if needed
if not os.path.exists("turbineResults"):   os.makedirs("turbineResults")

shutil.copyfile("turbineDict.py",  "turbineResults/turbineDict.py")
shutil.move("turbineReport.md",    "turbineResults/turbineReport.md")
shutil.move("axisCut.png",         "turbineResults/axisCut.png")
shutil.move("inTurbineWheel.png",  "turbineResults/inTurbineWheel.png")
shutil.move("outTurbineWheel.png", "turbineResults/outTurbineWheel.png")
shutil.copyfile("../programFiles/turbine/i-sPlot.png", "turbineResults/i-sPlot.png")
