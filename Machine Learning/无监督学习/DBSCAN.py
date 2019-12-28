import matplotlib.pyplot as plt
import mglearn
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

X,y=make_blobs(random_state=0,n_samples=12)

dbscan=DBSCAN()
#clusters=dbscan.fit_predict(X)
#print("Cluster memberships:\n{}".format(clusters))
mglearn.plots.plot_dbscan()

X,y=make_moons(n_samples=200,noise=0.05,random_state=0)

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

dbscan=DBSCAN()
clusters=dbscan.fit_predict(X_scaled)
plt.scatter(X_scaled[:,0],X_scaled[:,1],c=clusters,cmap=mglearn.cm2,s=60)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")