import matplotlib.pyplot as plt
import mglearn
import numpy as np
import pandas as pd

from sklearn.datasets import load_boston
boston=load_boston()

print("Data shape:{}".format(boston.data.shape))

X,y=mglearn.datasets.load_extended_boston()
print("X.shape:{}".format(X.shape))