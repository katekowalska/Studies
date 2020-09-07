# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:30:41 2018

@author: kkowalska
"""

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,200)
low=norm.ppf(0.05)
high=norm.ppf(0.95)
print("low=", low, "high=",high)
xp = np.linspace(low,high,200)
fig, ax = plt.subplots(1,1)
ax.plot(x,norm.pdf(x,0,1))
ax.plot(xp,norm.pdf(xp,0,1))

#ax.plot(x,norm.pdf(x,0,2))
#ax.