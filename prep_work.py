import numpy as np
import matplotlib.pyplot as plt


mu1 = np.array([-3, 0])
mu2 = np.array([3, 0])

pi1, pi2 = 0.3, 0.7

sigma = np.array([[2, 0.5],[0.5, 1]])

n = 500

sample1 = np.random.multivariate_normal(mu1, sigma, n)
sample2 = np.random.multivariate_normal(mu2, sigma, n)

sample = pi1*sample1 + pi2*sample2

plt.plot(sample)
plt.show()
