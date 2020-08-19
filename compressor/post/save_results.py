def save_results(compressor):
    ''' Create results/compressor/ folder & move results there
    '''
    import os, shutil
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # Creating directory if needed
    if not os.path.exists("results/compressor"):
        os.makedirs("results/compressor")

    # Save report files
    shutil.move("compressor_report.md",
                "results/compressor_report.md")
    shutil.move("axisCut.png",
                "results/compressor/axisCut.png")
    shutil.move("blades.png",
                "results/compressor/blades.png")
    shutil.move("outWheel.png",
                "results/compressor/outWheel.png")
    if 'VANED' in compressor['diffuser']:
        shutil.move("perpendicularCut.png",
                    "results/compressor/perpendicularCut.png")

    # Back up dictionaries
    shutil.copyfile("common_config.py",
                    "results/common_config.py")
    shutil.copyfile("engine_config.py",
                    "results/engine_config.py")
    shutil.copyfile("compressor/compressor_config.py",
                    "results/compressor/compressor_config.py")




# ''' (C) 2018-2020 Stanislau Stasheuski '''