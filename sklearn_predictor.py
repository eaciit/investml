import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = np.load("data/generated/1Y.npy")
X = data[:, :-1]
y = data[:, -1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print accuracy
print clf.predict(X_test[0:10, :])
