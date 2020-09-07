# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:31:26 2019

@author: kkowalska
"""

# 8.7

from scipy.stats import f
import numpy as np

THWD = np.array([450, 760, 325, 495, 285, 450, 460, 375, 310, 615, 425])

sd2=(THWD[:]-THWD.mean())**2 #wariancja
sd=np.sqrt(sd2.sum()/10)

THWH=np.array([245, 350, 340, 300, 310, 270, 300, 360, 405, 290])

sh2=(THWH[:]-THWH.mean())**2
sh=np.sqrt(sh2.sum()/9)

print("sd", sd)
print("sh", sh)

print(np.sqrt(THWH.var(ddof=1)))

print("(sd/sh)**2",(sd/sh)**2)

print("gorna", f.ppf(0.995, 10,9))
print("dolna", f.ppf(0.995, 8,9))

print("p_value=",2*f.cdf(f.ppf(0.005, 64,81), 64, 81))

print("p_value", 2*(1-f.cdf(1.015,439,356)))