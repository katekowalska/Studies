
import scipy.integrate
import numpy
import matplotlib.pyplot as plt

# ODEs

def SIR_model(y, t, N, alpha, beta):

    S, I, R = y

    dS_dt = -alpha*S*I
    dI_dt = alpha*S*I - beta*I
    dR_dt = beta*I

    return([dS_dt, dI_dt, dR_dt])

# Initial conditions

N = 100
I0, R0 = 1, 0
S0 = N - I0 - R0
alpha, beta = 0.01, 0.1

# Time vector
t = numpy.linspace(0, 30, 10000)

# Result
solution = scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args=(N, alpha, beta))
solution = numpy.array(solution)

# Plot result
plt.figure(figsize=[9, 5])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.legend()
plt.ylabel("S(t), I(t) i R(t)", fontsize=12)
plt.xlabel("Czas [dni]", fontsize=12)
plt.show()
import scipy.integrate
import numpy
import matplotlib.pyplot as plt

# ODEs

def SIR_model(y, t, N, alpha, beta):

    S, I, R = y

    dS_dt = -alpha*S*I
    dI_dt = alpha*S*I - beta*I
    dR_dt = beta*I

    return([dS_dt, dI_dt, dR_dt])

# Initial conditions

N = 100
I0, R0 = 1, 0
S0 = N - I0 - R0
alpha, beta = 0.01, 0.1

# Time vector
t = numpy.linspace(0, 30, 10000)

# Result
solution = scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args=(N, alpha, beta))
solution = numpy.array(solution)

# Plot result
plt.figure(figsize=[9, 5])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")
plt.legend()
plt.ylabel("S(t), I(t) i R(t)", fontsize=12)
plt.xlabel("Czas [dni]", fontsize=12)
plt.show()
