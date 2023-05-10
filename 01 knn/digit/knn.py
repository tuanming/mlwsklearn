from sklearn.datasets import load_digits
import joblib
X = load_digits().data
knn = joblib.load('knn.plk')
c1 = knn.predict(X[0].reshape(1,-1))
c2 = knn.predict(X[1010].reshape(1,-1))
print(c1,c2)
