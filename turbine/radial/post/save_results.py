def save_results():
    '''
        Create folder results/turbine and move results there
    '''
    import os, shutil

    # Creating dir if needed
    if not os.path.exists("../../results/turbine/radial/"):
        os.makedirs("../../results/turbine/radial/")


    shutil.move("radialTurbineReport.md",
                "../../results/radialTurbineReport.md")
    shutil.move("axisCut.png",
                "../../results/turbine/radial/axisCut.png")
    shutil.move("inTurbineWheel.png",
                "../../results/turbine/radial/inTurbineWheel.png")
    shutil.move("outTurbineWheel.png",
                "../../results/turbine/radial/outTurbineWheel.png")

    shutil.copyfile("../../etc/turbine/radial/i-sPlot.png",
                    "../../results/turbine/radial/i-sPlot.png")
    shutil.copyfile("../../commonConfig.py",
                    "../../results/commonConfig.py")
    shutil.copyfile("turbineConfig.py",
                    "../../results/turbine/radial/turbineConfig.py")
    shutil.copyfile("../compressorToTurbineConfig.py",
                    "../../results/turbine/compressorToTurbineConfig.py")