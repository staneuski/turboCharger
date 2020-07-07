def save_results(compressor):
    '''
        Create results/compressor/ folder & move results there
    '''
    import os, shutil

    resultsFolder = 'results'

    # Creating directory if needed
    if not os.path.exists("results/compressor"):
        os.makedirs("results/compressor")

    shutil.move("compressorReport.md",
                "results/compressorReport.md")

    shutil.copyfile("compressor/compressorConfig.py",
                    "results/compressor/compressorConfig.py")

    shutil.move("axisCut.png",
                "results/compressor/axisCut.png")
    shutil.move("blades.png",
                "results/compressor/blades.png")
    shutil.move("outWheel.png",
                "results/compressor/outWheel.png")

    if 'VANED' in compressor['diffuser']:
        shutil.move("perpendicularCut.png",
                    "results/compressor/perpendicularCut.png")
s