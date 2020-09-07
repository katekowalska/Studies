# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:54:13 2018

@author: kkowalska
"""

import numpy as np
from scipy.stats import chi2

sigma2 = 16
s = 5
n = 20

alpha = 0.05

test = (n-1)*s**2/sigma2

print("test=", test)

print("tl=", chi2.ppf(alpha/2, n-1))
print("th=", chi2.ppf(1-alpha/2,n-1))

print("pvalue=",(1-(chi2.cdf(test,n-1)))) # p-value
