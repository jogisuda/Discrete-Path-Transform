# -*- coding: utf-8 -*-

import numpy as np

def DPT(s): #Discrete Path Transform

  M = len(s)
  L = [0] * M
  L[0] = s[0]
  L[M-1] = 0
  
  for i in range(M - 1):
    L[M - 1] += np.sqrt( (s[i+1] - s[i])**2 + 1)

  L[M - 1] *= (1 if (s[M - 1] - s[M - 2]) >= 0 else -1)
  L[1] = np.sqrt( (s[1] - s[0])**2 + 1 )/np.abs(L[M-1])
  L[1] *= (1 if s[1] >= s[0] else -1)

  for k in range(2, M - 1):
    L[k] = (np.sqrt( (s[k] - s[k-1])**2 + 1 )/np.abs(L[M-1]) ) + np.abs(L[k-1])
    L[k] *= (1 if s[k] >= s[k-1] else -1)
  
  return L

def IDPT(L):

  M = len(L)
  s = [0] * M
  s[0] = L[0]
  if ((L[M-1]*np.abs(L[1]))**2 - 1) < 0:
    s[1] = s[0]
  else: #CHECAR
    s[1] = (1 if L[1] >= 0 else -1)* np.sqrt( (L[M-1]*np.abs(L[1]))**2 - 1 ) + s[0]
    
  for k in range(2, M - 1):
    if ((L[M-1]*(np.abs(L[k]) - np.abs(L[k-1])) )**2 - 1) < 0:
      s[k] = s[k-1]
    else:
      s[k] = (1 if L[k] >= 0 else -1)* np.sqrt( (L[M-1]* (np.abs(L[k]) - np.abs(L[k-1])) )**2 - 1 ) + s[k-1]
  
  if ( ((1 - np.abs(L[M-2])) *np.abs(L[M-1]))**2 - 1) < 0:
    s[M-1] = s[M-2]
  else:
    s[M-1] = (1 if L[M-1] >= 0 else -1)* np.sqrt( ((1 - np.abs(L[M-2])) *np.abs(L[M-1]))**2 - 1 ) + s[M-2]

  return s
