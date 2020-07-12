def save_results(turbine):
    ''' Create turbine results folder and move results there
    '''
    import os, shutil
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # Creating directory if required
    if not os.path.exists(f"results/turbine/{turbine['type']}/"):
        os.makedirs(f"results/turbine/{turbine['type']}/")

    # Save report files
    shutil.move(f"turbine_{turbine['type']}_report.md",
                f"results/turbine_{turbine['type']}_report.md")
    shutil.move("axisCut.png",
                f"results/turbine/{turbine['type']}/axisCut.png")

    if turbine['type'] == 'radial':
        shutil.move("inTurbineWheel.png",
                    "results/turbine/radial/inTurbineWheel.png")
        shutil.move("outTurbineWheel.png",
                    "results/turbine/radial/outTurbineWheel.png")
        shutil.copyfile("etc/turbine/radial/i-sPlot.png",
                        "results/turbine/radial/i-sPlot.png")

    elif turbine['type'] == 'axial':
        shutil.move("axisCut.png",
                    "results/turbine/axial/axisCut.png")
        shutil.move("radialCut.png",
                    "results/turbine/axial/radialCut.png")

    else: None

    # Back up the turbine dictionary
    shutil.copyfile("turbine/turbine_config.py",
                    f"results/turbine/{turbine['type']}/turbine_config.py")


# ''' (C) 2018-2020 Stanislau Stasheuski '''