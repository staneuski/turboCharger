# -*- coding: utf-8 -*-
def piK(l_0, p_e, guessedPiK):
    "Calculates pressure degree increase"

    # Import data
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from commonDict import(R, g_e, alpha, k, E, T_ca, eta_v);
    
    
    from compressorDict import(
        T_aStagn, eta_KsStagn, T_aStagn,
        p_aStagn, sigma_0, sigma_c, sigma_v
    );

    # Converting data to SI from dictionary | Перевод в СИ
    g_e = g_e*1e-03; # -> kg/(V*h) or g/(kV*h)
    p_aStagn = p_aStagn*1e06; # -> Pa

    # Calculation pressure degree increase
    solvedPiK = R*T_aStagn*g_e*l_0*alpha* \
        ( ( (pow(guessedPiK,(k - 1)/k) - 1)/eta_KsStagn + 1 )*(1 - E)+E*T_ca/T_aStagn)* \
        p_e/p_aStagn/3600/eta_v/sigma_0/sigma_c/sigma_v;
    return solvedPiK
