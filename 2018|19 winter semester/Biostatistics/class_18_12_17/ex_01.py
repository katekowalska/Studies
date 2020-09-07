# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:54:13 2018

@author: kkowalska
"""

import numpy as np
from scipy.stats import t

mu0 = 15
mu = 13
s = 4
n = 10

test = (mu-mu0)/(s/np.sqrt(n))

print("t=", test)

alpha = 0.05

print("tl=", t.ppf(alpha/2, n-1))
print("th=", t.ppf(1-alpha/2,n-1))

print("p-value=", 2*t.cdf(test,n-1) )# p-value

