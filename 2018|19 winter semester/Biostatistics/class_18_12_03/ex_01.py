# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:27:18 2018

@author: kkowalska
"""

import numpy as np
from scipy.stats import t

test = (-2/(4/(np.sqrt(10))))
print(test)

t = t.ppf(0.05, 9)

# (alfa i n-1)
# n-1 liczba stopni swoobdy
print(t)

p = t.cdf(test, 9)
# (x i n-1)
print(p)