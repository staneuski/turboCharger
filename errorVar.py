def printError(errorVariable):
    if errorVariable < 1:
        color = '\033[92m' # green
    else:
        color = '\033[1m\033[91m' # bold red

    print(f'Error of calculation between them is {color}{errorVariable:.3f}%\033[0m\n')