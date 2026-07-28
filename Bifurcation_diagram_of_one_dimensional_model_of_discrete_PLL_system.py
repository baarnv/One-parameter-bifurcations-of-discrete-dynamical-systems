import numpy as np
import matplotlib.pyplot as plt

alpha_min = 2.0
alpha_max = 4.0
n_alpha = 500
alphas = np.linspace(alpha_min, alpha_max, n_alpha)

n_iter = 1000
n_draw = 200
sigma0 = 0.1

plt.figure(figsize=(10, 6))
for alpha in alphas:
    sigma = sigma0
    trajectory = []
    for i in range(n_iter):
        sigma = sigma - alpha * np.sin(sigma)
        if sigma > np.pi:
            sigma -= 2 * np.pi
        elif sigma < -np.pi:
            sigma += 2 * np.pi
        trajectory.append(sigma)
    plt.plot([alpha] * n_draw, trajectory[-n_draw:], ',k', alpha=0.7)

plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\sigma$')
plt.title('Bifurcation diagram of discrete PLL system')
plt.grid(True)
plt.show()
