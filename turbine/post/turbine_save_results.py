def turbine_save_results(turbine):
    '''
        Create folder results/turbine and move results there
    '''
    import os, shutil
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    shutil.copyfile("commonConfig.py",
                    "results/commonConfig.py")

    if turbine['type'] == 'radial':
        # Creating directory if required
        if not os.path.exists("results/turbine/radial/"):
            os.makedirs("results/turbine/radial/")

        shutil.copyfile("turbine/turbineConfig.py",
                        "results/turbine/radial/turbineConfig.py")

        shutil.move("radialTurbineReport.md",
                    "results/radialTurbineReport.md")
        shutil.move("axisCut.png",
                    "results/turbine/radial/axisCut.png")
        shutil.move("inTurbineWheel.png",
                    "results/turbine/radial/inTurbineWheel.png")
        shutil.move("outTurbineWheel.png",
                    "results/turbine/radial/outTurbineWheel.png")
        shutil.copyfile("etc/turbine/radial/i-sPlot.png",
                        "results/turbine/radial/i-sPlot.png")

    elif turbine['type'] == 'axial':
        # Creating directory if required
        if not os.path.exists("results/turbine/axial/"):
            os.makedirs("results/turbine/axial")

        shutil.copyfile("turbine/turbineConfig.py",
                        "results/turbine/axial/turbineConfig.py")

        shutil.move("axialTurbineReport.md",
                    "results/axialTurbineReport.md")
        shutil.move("axisCut.png",
                    "results/turbine/axial/axisCut.png")
        shutil.move("radialCut.png",
                    "results/turbine/axial/radialCut.png")

    else: None


# ''' (C) 2018-2020 Stanislau Stasheuski '''