import matplotlib.pyplot as plt
import mglearn
import numpy as np
import pandas as pd

#mglearn.plots.plot_agglomerative_algorithm()

from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
X,y=make_blobs(random_state=1)

agg=AgglomerativeClustering(n_clusters=3)
assignment=agg.fit_predict(X)

mglearn.discrete_scatter(X[:,0],X[:,1],assignment)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
