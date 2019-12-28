import matplotlib.pyplot as plt
import mglearn
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import Lasso
from sklearn.model_selection import train_test_split

X,y=mglearn.datasets.make_wave(n_samples=60)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42)

lr=LinearRegression().fit(X_train,y_train)
ridge=Ridge().fit(X_train,y_train)
