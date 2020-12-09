# Method to set the value
def value_btw_two_plots(balance_coef, upper_value, lower_value):
    """Set value using two interpolated functions and balance coefficient."""
    if (balance_coef < 0) | (balance_coef > 1):
        exit('\033[91mERROR: Balance coefficient is incorrect!\n'
             'Valid values are from 0.0 to 1.0')

    return balance_coef*upper_value + (1 - balance_coef)*lower_value

def value_range_of_plot(balance_coef, delta, lower_value):
    """Set value using the interpolated function, range 
    and balance coefficient.
    """

    return lower_value + balance_coef*delta

def checkWheelDiameter(D):
    if (D < 0.04) | (D > 0.24):
        exit('\033[91mERROR: No data for that wheel diameter!\n'
             f'It equals {D*1e+02:.0f} cm but must be from 4 to 24 cm.\n'
             'May be try to calculate axial turbine!')


# Coeficients
def eta_plot2func(balance_coef, D):
    checkWheelDiameter(D)
    return value_btw_two_plots(balance_coef,
                               41.6424*D**3 - 23.8782*D**2 + 4.65788*D + 0.502197,
                               47.3485*D**3 - 28.2561*D**2 + 5.69391*D + 0.318636)

def alpha_plot2func(balance_coef, D):
    checkWheelDiameter(D)
    return value_btw_two_plots(balance_coef,
                               607.605*D**3 - 414.379*D**2 + 99.4706*D + 21.6024,
                               81.285 *D**3 - 290.388*D**2 + 120.468*D + 10.7)

def phi_plot2func(balance_coef, D):
    checkWheelDiameter(D)
    return value_btw_two_plots(balance_coef,
                               -1.4881*D**2 + 0.541667*D + 0.931414,
                               -4.7619*D**2 + 1.83333*D + 0.794286)

def psi_plot2func(balance_coef, D):
    checkWheelDiameter(D)
    return value_btw_two_plots(balance_coef,
                               -6.35417*D**2 + 2.35417*D + 0.746,
                               -5.83333*D**2 + 2.43333*D + 0.662)

def ksi_plot2func(balance_coef, D):
    checkWheelDiameter(D)
    return value_range_of_plot(balance_coef,
                               0.09,
                               -2.38095*D**2 + 1.16667*D + 0.527143)

def relD_1H(balance_coef, D):
    checkWheelDiameter(D)
    return value_btw_two_plots(balance_coef,
                               4.40039*D**2 - 2.22469*D + 0.981044,
                               73.7665*D**3 - 37.701*D**2 + 5.48361*D + 0.39897)

def relD_2B(balance_coef, D):
    checkWheelDiameter(D)
    return value_range_of_plot(balance_coef,
                               0.1,
                               2.61905*D**2 - 0.533333*D + 0.227143)
