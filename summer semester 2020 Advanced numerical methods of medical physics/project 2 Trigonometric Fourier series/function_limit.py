
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate

def fun(x):
    if x < -1:
        return 1/ (x ** 2)
    elif -1 <= x < 1:
        return 1/2 * x ** 2
    elif x >= 1:
        return np.exp(-x)

vfun = np.vectorize(fun)

x = np.linspace(-np.pi, np.pi, 100)

y = vfun(x)

# plot the function
# plt.plot(x, y)

# show the plot
# plt.show()

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
    # print('n = ', n+1, 'a_n coeff = ', a[n], 'b_n coeff =', b[n])

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

# plt.figure(figsize=[9, 5])
# plt.plot(x, vFourierSum(x, 100))
# plt.ylabel("f_N(x)", fontsize=12)
# plt.xlabel("x", fontsize=12)

# show the plot
# plt.show()

# function limit point of continuity

valA = np.zeros(N)

for n in range(N):
    x = -2
    valA[n] = abs(vFourierSum(x, n) - vfun(x))
    # print(valA[n])

x = np.linspace(0, 100, 100)

plt.figure(figsize=[9, 5])
plt.scatter(x, valA)
plt.ylabel("|f_N(x) - A|", fontsize=12)
plt.xlabel("N", fontsize=12)

# show the plot
plt.show()

# function limit point of discontinuity

valB = np.zeros(N)

k = (1 + 0.5)/2

for n in range(N):
    x = -1
    valB[n] = abs(vFourierSum(x, n) - k)
    # print(valB[n])

x = np.linspace(0, 100, 100)

plt.figure(figsize=[9, 5])
plt.scatter(x, valB)
plt.ylabel("|f_N(x) - A|", fontsize=12)
plt.xlabel("N", fontsize=12)

# show the plot
plt.show()

# second method

valFA = np.zeros(N)

for n in range(N):
    x = -1
    valFA[n] =  vFourierSum(x, n)
    # print(valFA)

x = np.linspace(0, 100, 100)

plt.figure(figsize=[9, 5])
plt.scatter(x, valFA)
plt.ylabel("f_N(x)", fontsize=12)
plt.xlabel("N", fontsize=12)

# show the plot
plt.show()
