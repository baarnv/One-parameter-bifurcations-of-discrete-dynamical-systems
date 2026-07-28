import numpy as np
import matplotlib.pyplot as plt

def tent_map(x, r):
    return np.where(x < 0.5, r * x, r * (1.0 - x))

r_min, r_max = 0.0, 2.0
num_r = 2000
rs = np.linspace(r_min, r_max, num_r)

n_iter = 1500
n_transient = 500

xs = np.empty((num_r, n_iter))
xs[:, 0] = 0.5

for n in range(1, n_iter):
    xs[:, n] = tent_map(xs[:, n - 1], rs)

xs_plot = xs[:, n_transient:]
rs_plot = np.repeat(rs, xs_plot.shape[1])
xs_plot = xs_plot.ravel()

plt.figure(figsize=(8, 6), dpi=120)
plt.scatter(rs_plot, xs_plot, s=0.1, color='black')
plt.xlabel(r'$r$')
plt.ylabel(r'$x$')
plt.title('Bifurcation diagram of the tent map')
plt.xlim(r_min, r_max)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()
