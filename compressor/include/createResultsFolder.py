# -*- coding: utf-8 -*-
# '''
#     Description:    Create results/compressor/ folder(s) & move results there
# '''

# Creating directory if needed 
if not os.path.exists("../results/compressor"):
    os.makedirs("../results/compressor")

shutil.copyfile("solvedParameters.py", "../turbine/axial/solvedParameters.py")
shutil.move("solvedParameters.py",   "../turbine/radial/solvedParameters.py")

shutil.move("compressorReport.md",   "../results/compressorReport.md")
shutil.copyfile("compressorConfig.py", "../results/compressor/compressorConfig.py")
shutil.move("axisCut.png",           "../results/compressor/axisCut.png")
shutil.move("blades.png",            "../results/compressor/blades.png")
shutil.move("outWheel.png",          "../results/compressor/outWheel.png")

if 'VANED' in diffuserType:
    shutil.move("perpendicularCut.png",
                "../results/compressor/perpendicularCut.png")