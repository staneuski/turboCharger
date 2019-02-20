# -*- coding: utf-8 -*-
# Method to set the value
def plotValue(balanceCoef, upValue, downValue):
    """
    Sets value using two interpolated functions and balance coefficient
    """
    if (balanceCoef < 0) | (balanceCoef > 1):
        exit('Error: Balance coefficient setted in the wrong way!')
    return balanceCoef*upValue + (1 - balanceCoef)*downValue

def deltaPlotValue(balanceCoef, delta, downValue):
    """
    Sets value using the interpolated function, range 
    and balance coefficient
    """
    return downValue + balanceCoef*delta


# Coeficients
def zPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24):
        exit('Error: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.' %(D*1e+02));
    return deltaPlotValue(balanceCoef, 9,\
    -150*pow(D, 2) + 127*D + 2.16)

def etaPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24):
        exit('Error: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.' %(D*1e+02));
    return plotValue(balanceCoef,\
    24.4221*pow(D, 3) - 14.4807*pow(D, 2) + 2.86602*D + 0.638529,\
    13.6396*pow(D, 3) - 10.5443*pow(D, 2) + 2.74411*D + 0.552028)

def HPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24):
        exit('Error: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.' %(D*1e+02));
    return plotValue(balanceCoef,\
    -2.3    *pow(D, 2) + 1.094  *D + 0.60992,\
    -1.90476*pow(D, 2) + 1.13333*D + 0.487714)
    
def phiPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24):
        exit('Error: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.' %(D*1e+02));
    return plotValue(balanceCoef,\
    1.60098*pow(D, 2) - 0.639744*D + 0.372266,\
    0.49986*pow(D, 2) - 0.216037*D + 0.283293)
    
def relSpeedsPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24):
        exit('Error: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.' %(D*1e+02));
    return plotValue(balanceCoef,\
    2.94803 *pow(D, 2) - 1.29351*D + 1.23615,\
    -2.95225*pow(D, 2) + 1.61242*D + 0.774654)

def relD_1HPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24):
        exit('Error: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.' %(D*1e+02));
    return plotValue(balanceCoef,\
    -0.05*D + 0.712,\
    -0.35*D + 0.634)

def relD_1BPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24):
        exit('Error: No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.' %(D*1e+02));
    return deltaPlotValue(balanceCoef, 0.06,\
    0.297619*pow(D, 2) + 0.132184*D + 0.192685)
    
    











    