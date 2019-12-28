from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits=load_digits()
print(digits.images.shape)
plt.matshow(digits.images[1])
plt.show()