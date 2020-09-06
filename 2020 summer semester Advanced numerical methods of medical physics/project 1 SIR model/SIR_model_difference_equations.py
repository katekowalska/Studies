
import numpy as np
import matplotlib.pyplot as plt

D = 30               # Simulate for D days

t = np.linspace(0, D, D+1)
S = np.zeros(D+1)
I = np.zeros(D+1)
R = np.zeros(D+1)

# Initial condition
N = 100
I[0] = 1
R[0] = 0
S[0] = N - I[0] - R[0]

alpha, beta = 0.01, 0.1

# Step equations forward in time
for n in range(D):
    S[n+1] = S[n] - alpha*S[n]*I[n]
    I[n+1] = I[n] + alpha*S[n]*I[n] - beta*I[n]
    R[n+1] = R[n] + beta*I[n]

# Plot result
plt.figure(figsize=[9, 5])
plt.plot(t, S, 'd:', label="S(n)")
plt.plot(t, I, 'o:', label="I(n)")
plt.plot(t, R, 's:', label="R(n)")
plt.legend()
plt.ylabel("S(n), I(n) i R(n)", fontsize=12)
plt.xlabel("Czas [dni]", fontsize=12)
plt.show()
