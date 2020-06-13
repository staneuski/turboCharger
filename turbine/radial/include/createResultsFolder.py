# -*- coding: utf-8 -*-
# '''
#     Description:    Create folder ../../results/turbine and move results there
# '''

# Creating dir if needed
if not os.path.exists("../../results/turbine/radial/"):   os.makedirs("../../results/turbine/radial/")

shutil.copyfile("../../commonDict.py",  "../../results/commonDict.py")

shutil.move("radialTurbineReport.md", "../../results/radialTurbineReport.md")
shutil.copyfile("turbineDict.py",     "../../results/turbine/radial/turbineDict.py")
shutil.copyfile("solvedParameters.py","../../results/turbine/radial/solvedParameters.py")
shutil.move("axisCut.png",            "../../results/turbine/radial/axisCut.png")
shutil.move("inTurbineWheel.png",     "../../results/turbine/radial/inTurbineWheel.png")
shutil.move("outTurbineWheel.png",    "../../results/turbine/radial/outTurbineWheel.png")
shutil.copyfile("../../etc/turbine/radial/i-sPlot.png", "../../results/turbine/radial/i-sPlot.png")
