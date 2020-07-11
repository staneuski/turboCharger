def set_standard(size):
    '''
        Get the size and return it standartized with using Russian ISO (GOST)

        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 20, 22, 24, 26,
        28, 30, 32, 34, 36, 38, 40, 42, 45, 48, 50, 52, 55, 58, 60, 65, 70, 75,
        80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150,
        155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220,
        225, 230, 235, 240, 245, 250, 260, 270, 280, 290, 300, 310...990, 1000
    '''
    if size < 1:
        print("\033[93mWARNING:\
              Size is too small to be standartized!\
              \nIt was set like 1 mm.\033[0m"
              .replace('              ', ' '))
        size = 1

    elif (size >= 1) and (size < 16):
        if (size >= 12.5) and (size < 13):    size = 12
        size = round(size)

    elif (size >= 16) and (size < 42.5):
        size = round(size)
        if size%2 != 0:    size = size + 1

    elif (size >= 42.5) and (size < 47.5):
        size = 45
    elif (size >= 47.5) and (size < 49):
        size = 48
    elif (size >= 49) and (size < 51):
        size = 50
    elif (size >= 51) and (size < 53.5):
        size = 52
    elif (size >= 53.5) and (size < 57.5):
        size = 55
    elif (size >= 57.5) and (size < 59):
        size = 58
    elif (size >= 59) and (size < 62.5):
        size = 60
    elif (size >= 60) and (size < 250):
        size = round(size*2, -1)/2
    else:
        size = round(size/10)*10

    return size