
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

b = np.array([0, 500, 1000])

# Oko

oko = np.array([713.07, 143.72, 36.42])

oko_log = np.log(oko)

model_oko = LinearRegression(fit_intercept=True)

model_oko.fit(b[:, np.newaxis], oko_log)

xfit_oko = np.linspace(0, 1000, 1000)
yfit_oko = model_oko.predict(xfit_oko[:, np.newaxis])

plt.scatter(b, oko_log, marker="d", label="oko")

plt.plot(xfit_oko, yfit_oko)

# Plyn

plyn = np.array([873.71, 182.63, 38.8])

plyn_log = np.log(plyn)

model_plyn = LinearRegression(fit_intercept=True)

model_plyn.fit(b[:, np.newaxis], plyn_log)

xfit_plyn = np.linspace(0, 1000, 1000)
yfit_plyn = model_plyn.predict(xfit_plyn[:, np.newaxis])

plt.scatter(b, plyn_log, marker="X", label="plyn")

plt.plot(xfit_plyn, yfit_plyn)

# Istota biała

biala = np.array([243.93, 166.43, 121.14])

biala_log = np.log(biala)

model_biala = LinearRegression(fit_intercept=True)

model_biala.fit(b[:, np.newaxis], biala_log)

xfit_biala = np.linspace(0, 1000, 1000)
yfit_biala = model_biala.predict(xfit_biala[:, np.newaxis])

plt.scatter(b, biala_log, marker="h", label="i.biala")

plt.plot(xfit_biala, yfit_biala)

# Istota szara

szara = np.array([425.33, 272, 188.5])

szara_log = np.log(szara)

model_szara = LinearRegression(fit_intercept=True)

model_szara.fit(b[:, np.newaxis], szara_log)

xfit_szara = np.linspace(0, 1000, 1000)
yfit_szara = model_szara.predict(xfit_szara[:, np.newaxis])

plt.scatter(b, szara_log, marker="^", label="i.szara")

plt.plot(xfit_szara, yfit_szara)

# Guz

guz = np.array([502.25, 318.92, 226.25])

guz_log = np.log(guz)

model_guz = LinearRegression(fit_intercept=True)

model_guz.fit(b[:, np.newaxis], guz_log)

xfit_guz = np.linspace(0, 1000, 1000)
yfit_guz = model_guz.predict(xfit_guz[:, np.newaxis])

plt.scatter(b, guz_log, marker="o", label="guz")

plt.plot(xfit_guz, yfit_guz)


plt.legend()
plt.ylabel("ln(S)", fontsize=12)
plt.xlabel("b [s/mm$^2$]", fontsize=12)
plt.show();
