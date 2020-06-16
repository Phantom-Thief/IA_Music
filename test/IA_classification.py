#IA de classification 
import tensorflow as tf
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense


# load the dataset
dataset = loadtxt('rawdata_A_6.csv', delimiter=';')

# split into input (X) and output (y) variables
X = dataset[:,0:6]
X = tf.keras.utils.normalize(
    X, axis=1, order=2
)
y = dataset[:,-1]

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=6, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(4, activation='softmax'))

# compile the keras model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=100, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# make probability predictions with the model
predictions = model.predict(X)
# round predictions 
rounded = [round(x[0]) for x in predictions]

# make class predictions with the model
predictions = model.predict_classes(X)

# summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))