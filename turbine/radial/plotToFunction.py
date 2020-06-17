# Takes data from picture 3.7 using interpolated functions and sets coefficients values

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
def etaPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24): exit('\033[91mError:\
 No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.\n\
Try to calculate axial turbine!' %(D*1e+02))
    return plotValue(balanceCoef,\
    41.6424*pow(D, 3) - 23.8782*pow(D, 2) + 4.65788*D + 0.502197,\
    47.3485*pow(D, 3) - 28.2561*pow(D, 2) + 5.69391*D + 0.318636)

def alphaPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24): exit('\033[91mError:\
 No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.\n\
Try to calculate axial turbine!' %(D*1e+02))
    return plotValue(balanceCoef,\
    607.605*pow(D, 3) - 414.379*pow(D, 2) + 99.4706*D + 21.6024,\
    81.285 *pow(D, 3) - 290.388*pow(D, 2) + 120.468*D + 10.7)
    
def phiPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24): exit('\033[91mError:\
 No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.\n\
Try to calculate axial turbine!' %(D*1e+02))
    return plotValue(balanceCoef,\
    -1.4881*pow(D, 2) + 0.541667*D + 0.931414,\
    -4.7619*pow(D, 2) + 1.83333*D + 0.794286)\
    
def psiPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24): exit('\033[91mError:\
 No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.\n\
Try to calculate axial turbine!' %(D*1e+02))
    return plotValue(balanceCoef,\
    -6.35417*pow(D, 2) + 2.35417*D + 0.746,\
    -5.83333*pow(D, 2) + 2.43333*D + 0.662)

def ksiPlot(balanceCoef, D):
    if (D < 0.04) | (D > 0.24): exit('\033[91mError:\
 No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.\n\
Try to calculate axial turbine!' %(D*1e+02))
    return deltaPlotValue(balanceCoef, 0.09,\
    -2.38095*pow(D, 2) + 1.16667*D + 0.527143)

def relD_1H(balanceCoef, D):
    if (D < 0.04) | (D > 0.24): exit('\033[91mError:\
 No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.\n\
Try to calculate axial turbine!' %(D*1e+02))
    return plotValue(balanceCoef,\
    4.40039*pow(D, 2) - 2.22469*D + 0.981044,\
    73.7665*pow(D, 3) - 37.701*pow(D, 2) + 5.48361*D + 0.39897)
    
def relD_2B(balanceCoef, D):
    if (D < 0.04) | (D > 0.24): exit('\033[91mError:\
 No data for that wheel diameter!\n\
It equals %0.0f cm but must be from 4 to 24 cm.\n\
Try to calculate axial turbine!' %(D*1e+02))
    return deltaPlotValue(balanceCoef, 0.1,
    2.61905*pow(D, 2) - 0.533333*D + 0.227143)
