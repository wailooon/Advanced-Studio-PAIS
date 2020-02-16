#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:51:59 2019

@author: Williamloo
"""

"""import scipy.io as sio
import pandas as pd

mat_contents1 = sio.loadmat('eeg_raw_data/1/1_20160518')"""

"""mat_contents2 = sio.loadmat('eeg_raw_data/1/2_20150915')"""

import numpy as np
from scipy.io import loadmat  # this is the SciPy module that loads mat-files
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import pandas as pd



mat = loadmat('eeg_raw_data/1/1_20160518.mat')  # load mat-file


mdata = []
matList = []

mdata = mat['cz_eeg1']  # variable in mat file

#for i in mat:
#    if '__' not in i :
#        mdata.append(i)
        
#for i in mdata:
#    matList.append((f'mat[\'{i}\''))
#    matList.append(i)
  

#for i in mdata:
#	if '__' not in i and 'readme' not in i:
#		np.savetxt(("filesforyou/"+i+".csv"),mdata[i],delimiter=',')

df = pd.DataFrame(data=mdata)

df.to_csv('testDF.csv', index=False)


readingDF = pd.read_csv('testDF.csv')

#mat = {k:v for k, v in mat.items() if k[0] != '_'}
#data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.iteritems()})
#data.to_csv("example.csv")

