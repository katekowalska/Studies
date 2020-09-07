# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:14:33 2018

@author: kkowalska
"""

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(90,1200,20000)
fig, ax = plt.subplots(1,1)
ax.plot(x,(3/10*0.84*np.sqrt(x)+99.5))
ax.plot(x,1/10*x)
