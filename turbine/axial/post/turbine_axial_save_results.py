def turbine_axial_save_results():
    '''
        Create folder results/turbine and move results there
    '''
    import os, shutil

    if not os.path.exists("results/turbine/axial/"):
        os.makedirs("results/turbine/axial")

    shutil.copyfile("commonConfig.py",
                    "results/commonConfig.py")

    shutil.move("axialTurbineReport.md",
                "results/axialTurbineReport.md")

    shutil.copyfile("turbine/turbineConfig.py",
                    "results/turbine/axial/turbineConfig.py")

    shutil.move("axisCut.png",
                "results/turbine/axial/axisCut.png")

    shutil.move("radialCut.png",
                "results/turbine/axial/radialCut.png")
