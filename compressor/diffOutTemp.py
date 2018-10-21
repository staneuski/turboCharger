# -*- coding: utf-8 -*-
def diffOutTemp(b_2, D_2, T_2, c_2, b_4, D_4, guessedT_4, n_4):  
    "Calculates diffuser output temperature"

    from compressorDict import(k, R);   # Import data from dictionary

    # Precalculations
    q = pow(D_2*b_2/D_4/b_4, 2);
    m = 2/(n_4 - 1);
    sigma = (k - 1)/1 * pow(c_2, 2)/k/R/T_2;
    
    # Calculation diffuser output temperature
    solvedT_4 = T_2*( 1 + sigma*(1 - q*pow(T_2/guessedT_4, m)) ); 
    return solvedT_4
