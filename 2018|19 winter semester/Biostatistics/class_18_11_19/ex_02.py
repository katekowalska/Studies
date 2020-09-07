# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:00:00 2018

@author: kkowalska
"""

import numpy as np

from scipy.stats import norm

a = 1-norm.cdf((19.5-10)/np.sqrt(10))
print(a)