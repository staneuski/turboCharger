# -*- coding: utf-8 -*-
# '''
#     Description:    Create results/compressor/ folder & move results there
# '''

# Creating directory if needed
resultsFolder = '../../results'
if not os.path.exists(f"{resultsFolder}/compressor"):
    os.makedirs(f"{resultsFolder}/compressor")

shutil.copyfile("solvedParameters.py",
                "../../turbine/axial/solvedParameters.py")
shutil.move("solvedParameters.py", "../../turbine/radial/solvedParameters.py")

shutil.move("compressorReport.md",   f"{resultsFolder}/compressorReport.md")

shutil.copyfile("compressorConfig.py",
               f"{resultsFolder}/compressor/compressorConfig.py")
shutil.move("axisCut.png",           f"{resultsFolder}/compressor/axisCut.png")
shutil.move("blades.png",            f"{resultsFolder}/compressor/blades.png")
shutil.move("outWheel.png",          f"{resultsFolder}/compressor/outWheel.png")

if 'VANED' in diffuserType:
    shutil.move("perpendicularCut.png",
                f"{resultsFolder}/compressor/perpendicularCut.png")