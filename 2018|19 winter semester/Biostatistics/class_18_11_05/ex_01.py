# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:01:30 2018

@author: kkowalska
"""

from scipy.stats import binom

n=100
p=0.02
P = binom.pmf(0, n, p)+ binom.pmf(1, n, p)+binom.pmf(2, n, p)+binom.pmf(3, n, p) + binom.pmf(4, n, p)
print(1-P)

P2 = binom.cdf(4,n,p)
print(1-P2)