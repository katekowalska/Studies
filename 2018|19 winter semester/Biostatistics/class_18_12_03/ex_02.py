# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:42:43 2018

@author: kkowalska
"""

import numpy as np
from scipy.stats import t

test = ((135-130)/(22/(np.sqrt(85))))
print(test)

print("p-value=", 2*(1-t.cdf(test,85-1)) )

#t = t.ppf(0.05, 9)

# (alfa i n-1)
# n-1 liczba stopni swoobdy
#print(t)

#p = t.cdf(test, 9)
# (x i n-1)
#print(p)