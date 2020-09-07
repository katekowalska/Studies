# -*- coding: utf-8 -*-
"""
Created on Mon Jan 7 13:31:26 2019

@author: kkowalska
"""

# 8.7

from scipy.stats import t
import numpy as np

LeftArm = np.array([130,120,135,100,98,110,123,136,140,155])
RightArm = np.array([126,124,127,95,102,109,124,132,137,156])

d = np.array([LeftArm - RightArm])

print("d=", d)

n=10

srednie_d = d.sum()/n

print("srednie d=", srednie_d)

sd2 = ((d-srednie_d)**2)/(n-1)

sd = np.sqrt(sd2.sum())

print("sd=", sd)

test = srednie_d/(sd/np.sqrt(n))

print("test=", test)

print(t.ppf(0.025,n-1))
print(t.ppf(0.975,n-1))

p_value = 1 - t.cdf(test,n-1)

print("p-value=", p_value)

delta1 = srednie_d + t.ppf(0.025,n-1) * (sd/np.sqrt(n))
delta2 = srednie_d - t.ppf(0.025,n-1) * (sd/np.sqrt(n))

print("delta=", delta1, delta2)

print("del=", delta2+delta1)

print("p-value", (1-t.cdf(t.ppf(0.975, 64), 64)))