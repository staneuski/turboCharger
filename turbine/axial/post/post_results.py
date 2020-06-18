# -*- coding: utf-8 -*-
# '''
#     Description:    Create folder ../../results/turbine
#                     and move results there
# '''

# Creating dir if needed
if not os.path.exists("../../results/turbine/axial/"):   os.makedirs("../../results/turbine/axial")

shutil.copyfile("../../commonConfig.py",  "../../results/commonConfig.py")

shutil.move("axialTurbineReport.md","../../results/axialTurbineReport.md")
shutil.copyfile("turbineConfig.py",   "../../results/turbine/axial/turbineConfig.py")
shutil.copyfile("../compressorToTurbineConfig.py","../../results/turbine/compressorToTurbineConfig.py")
shutil.move("axisCut.png",          "../../results/turbine/axial/axisCut.png")
shutil.move("radialCut.png",        "../../results/turbine/axial/radialCut.png")
