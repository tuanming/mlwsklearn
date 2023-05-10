import pandas as pd
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# images data  target
digits = load_digits()
print(digits.keys())
X = digits.data            # 64
# images = digits.images   # 8*8
y = digits.target

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3 5 7
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))
# print(X[0].reshape(1,-1))
c = knn.predict(X[1010].reshape(1,-1))
print(c)
