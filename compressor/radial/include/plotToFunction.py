# -*- coding: utf-8 -*-
# Method to set the value
def plotValue(balanceCoef, upValue, downValue):
    '''
        Set value using two interpolated functions and balance coefficient
    '''
    if (balanceCoef < 0) | (balanceCoef > 1):
        exit('\033[91mError: Balance coefficient set in the wrong way!')
    return balanceCoef*upValue + (1 - balanceCoef)*downValue

def deltaPlotValue(balanceCoef, delta, downValue):
    '''
        Set value using the interpolated function, range 
        and balance coefficient
    '''
    return downValue + balanceCoef*delta


# Coeficients
def HPlot(balanceCoef, D):
    import math
    if (D < 0.04) | (D > 0.8):
        exit('\033[91mError 5: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 80 cm.' %(D*1e+02))
    return plotValue(balanceCoef,\
    0.0485923*math.log(D) + 0.80737,\
    -2.28399*pow(D, 4) + 5.05698*pow(D, 3) - 4.02875*pow(D, 2) + 1.40783*D + 0.478618)

def phiPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.8):
        exit('\033[91mError 6: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 80 cm.' %(D*1e+02))
    return plotValue(balanceCoef,\
    1.21576*pow(D, 4) - 2.47517*pow(D, 3) + 1.77501*pow(D, 2) - 0.528671*D + 0.365277,\
    0.84364*pow(D, 4) - 1.74951*pow(D, 3) + 1.27749*pow(D, 2) - 0.384933*D + 0.292871)

def etaPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.8):
        exit('\033[91mError 15: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 80 cm.' %(D*1e+02))
    return plotValue(balanceCoef,\
    -1.41956*pow(D, 4) + 3.59445*pow(D, 3) - 3.19974*pow(D, 2) + 1.20019*D + 0.70186,\
    -2.54297*pow(D, 4) + 5.79527*pow(D, 3) - 4.69133*pow(D, 2) + 1.64249*D + 0.603052)
    
def relD_1HPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.8):
        exit('\033[91mError 13: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 80 cm.' %(D*1e+02))
    return plotValue(balanceCoef,\
    -0.05*D + 0.712,\
    -0.35*D + 0.634)

def relD_1BPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.8):
        exit('\033[91mError 13: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 80 cm.' %(D*1e+02))
    return deltaPlotValue(balanceCoef, 0.06,\
    0.260417*pow(D, 2) + 0.0280449*D + 0.198365)
    
def relSpeedsPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.8):
        exit('\033[91mError 27: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 80 cm.' %(D*1e+02))
    return plotValue(balanceCoef,\
    1.71023 *pow(D, 4) - 3.78212*pow(D, 3) + 2.99991*pow(D, 2) - 1.05122*D + 1.23182,\
    -6.37691*pow(D, 4) + 12.3393*pow(D, 3) - 8.57209*pow(D, 2) + 2.54654*D + 0.734892)
    
def zPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.8):
        exit('\033[91mError 30: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 80 cm.' %(D*1e+02))
    return deltaPlotValue(balanceCoef, 9,\
    141.063*pow(D, 3) - 228.472*pow(D, 2) + 134.588*D + 2.44075)
    
    











    