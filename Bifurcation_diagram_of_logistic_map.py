import numpy as np
import matplotlib.pyplot as plt

beta_min = 0.0
beta_max = 4.0
beta_step = 0.001
beta_values = np.arange(beta_min, beta_max + beta_step, beta_step)

beta_vals = []
x_vals = []

for beta in beta_values:
    x_old = 0.5
    
    for i in range(2000):
        x_new = beta * (x_old - x_old**2)
        x_old = x_new
        
    x_ss = x_old
    
    for i in range(1000):
        x_new = beta * (x_old - x_old**2)
        if not np.isfinite(x_new):
            break
        x_old = x_new
        beta_vals.append(beta)
        x_vals.append(x_new)
        if abs(x_new - x_ss) < 0.01:
            break

beta_vals = np.array(beta_vals)
x_vals = np.array(x_vals)

plt.figure(figsize=(8, 6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')
plt.plot(beta_vals, x_vals, '.', markersize=1.0, color=(0, 0, 0))
plt.xlabel('beta', color='black')
plt.ylabel('x', color='black')
plt.title('Bifurcation diagram of the logistic map', color='black')
ax.tick_params(colors='black')
plt.xlim(beta_min, beta_max)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()
