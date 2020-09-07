# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:51:25 2018

@author: kkowalska
"""

# sensivity versus 1-specificity

import numpy as np
import matplotlib.pyplot as plt

sen = np.array([0, 38/67, 53/67, 58/67, 63/67, 1])
spec = np.array([1, 32/33, 27/33, 23/33, 6/33, 0])
invspec = 1-spec
print(invspec)
plt.plot(invspec, sen)
plt.show()
a = np.trapz(sen,invspec)
print(a)
