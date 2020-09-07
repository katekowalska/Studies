# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:27:41 2018

@author: kkowalska
"""

"""
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
"""


from scipy.stats import binom

n=20
p=0.5

P = binom.cdf(14,n,p)
print(1-P)