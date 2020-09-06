
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate
import math

# Draw function e)

def fun1(x):
    if x < -1:
        return 1/ (x ** 2)

def fun2(x):
    if -1 <= x < 1:
        return 1/2 * x ** 2

def fun3(x):
    if x >= 1:
        return np.exp(-x)


vfun1 = np.vectorize(fun1)

vfun2 = np.vectorize(fun2)

vfun3 = np.vectorize(fun3)

x = np.linspace(-np.pi, np.pi, 100)

y1 = vfun1(x)

y2 = vfun2(x)

y3 = vfun3(x)

# plot the function
plt.figure(figsize=[9, 5])
plt.plot(x, y1, 'k')
plt.plot(x, y2, 'k')
plt.plot(x, y3, 'k')
plt.ylabel("f(x)", fontsize=12)
plt.xlabel("x", fontsize=12)

# show the plot
plt.show()

def fun(x):
    if x < -1:
        return 1/ (x ** 2)
    elif -1 <= x < 1:
        return 1/2 * x ** 2
    elif x >= 1:
        return np.exp(-x)

vfun = np.vectorize(fun)

y = vfun(x)

# plot the function
plt.plot(x, y)

# show the plot
plt.show()

# a_n coefficient

def func1(x, n):
    return fun(x) * np.cos(n * x)

def func2(x, n):
    return fun(x) * np.sin(n * x)

N = 100

a = np.zeros(N+1)
b = np.zeros(N+1)

for n in range(N):
    a[n] = 1/np.pi * scipy.integrate.quad(func1, -np.pi, np.pi, (n + 1))[0]
    b[n] = 1/np.pi * scipy.integrate.quad(func2, -np.pi, np.pi, (n + 1))[0]
    print('n = ', n+1, 'a_n coeff = ', a[n], 'b_n coeff =', b[n])

def funAzero(x):
    return fun(x)

aZero = 1/np.pi * scipy.integrate.quad(funAzero, -np.pi, np.pi)[0]


def FourierSum(x, M):

    suma = 0

    for n in range(M):
        suma = suma + (a[n] * np.cos((n + 1) * x) + b[n] * np.sin((n + 1) * x))

    return aZero/2 + suma

vFourierSum = np.vectorize(FourierSum)

x = np.linspace(-np.pi, np.pi, 100)

plt.figure(figsize=[9, 5])
plt.plot(x, vFourierSum(x, 100))
plt.ylabel("f_N(x)", fontsize=12)
plt.xlabel("x", fontsize=12)

# show the plot
plt.show()

# supremum metric

dsupremum = np.zeros(N+1)

for n in range(N):
    dsupremum[n] = max(abs(vfun(x) - vFourierSum(x, n)))
    # print('n = ', n+1, 'dsupremum = ', dsupremum[n])

x = np.linspace(0, 100, 101)

plt.figure(figsize=[9, 5])
plt.scatter(x, dsupremum)
plt.ylabel("d_inf (f(x), f_N(x))", fontsize=12)
plt.xlabel("N", fontsize=12)

# show the plot
plt.show()

# L^2 metric

def integrand(x, n):
    return abs(vfun(x) - vFourierSum(x, n))**2

dL2 = np.zeros(N+1)

for n in range(N):
    dL2[n] = math.sqrt(scipy.integrate.quad(integrand, -np.pi, np.pi, (n + 1))[0])
    # print('n = ', n+1, 'dL2 = ', dL2[n])

x = np.linspace(0, 100, 101)

plt.figure(figsize=[9, 5])
plt.scatter(x, dL2)
plt.ylabel("d_2(f(x), f_N(x))", fontsize=12)
plt.xlabel("N", fontsize=12)

# show the plot
plt.show()
