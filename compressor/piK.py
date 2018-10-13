# -*- coding: utf-8 -*-

def piK(l_0, p_e, guessedPiK):
      "Calculates pressure degree increase"
      
      # Import data from dictionary
      from compressorDict import(
      R, T_aStagn, g_e, alpha, k, eta_Ks, E, T_ca, T_aStagn,
      p_aStagn, eta_v, sigma_0, sigma_c, sigma_v
      );
      
      # Converting data to SI from dictionary | Перевод в СИ
      g_e = g_e*1e-03; # -> kg/(V*h) or g/(kV*h)
      p_aStagn = p_aStagn*1e06; # -> Pa
      
      # Calculation pressure degree increase
      solvedPiK = R*T_aStagn*g_e*l_0*alpha* \
            ( ( (pow(guessedPiK,(k - 1)/k) - 1)/eta_Ks + 1 )*(1 - E)+E*T_ca/T_aStagn)* \
            p_e/p_aStagn/3600/eta_v/sigma_0/sigma_c/sigma_v;
            
      return solvedPiK
