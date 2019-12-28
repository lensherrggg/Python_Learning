import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mglearn
X,y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X,y,'o')
plt.ylim=(-3,3)
plt.xlabel("Feature")
plt.ylabel("Target")