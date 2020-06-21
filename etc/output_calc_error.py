def output_calc_error(calc_error):
    if abs(calc_error) < 1:
        color = '\033[92m' # green
    else:
        color = '\033[1m\033[91m' # bold red

    print(f'Error of calculation between them is {color}{calc_error:.3f}%\033[0m\n')