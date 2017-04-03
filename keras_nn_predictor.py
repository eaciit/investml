import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

np.random.seed(1)

data = np.load("data/generated/1Y.npy")
X = data[:, :-1]
y = data[:, -1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

init = 'glorot_normal'

model = Sequential()
model.add(Dense(10, input_dim=X.shape[1], init=init))
model.add(Dense(10, init=init))
model.add(Dense(5, init=init))
model.add(Dense(1, init=init))

model.compile(loss='mse', optimizer='rmsprop')
model.fit(X_train, y_train, batch_size=256, nb_epoch=100, verbose=1, validation_data=(X_test, y_test))

score = model.evaluate(X_test, y_test, verbose=0)
print score
