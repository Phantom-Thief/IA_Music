#IA de classification 
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense,Flatten
import tensorflow as tf
from imblearn.over_sampling import SMOTE,ADASYN,RandomOverSampler


# load the dataset
dataset = loadtxt('rawdata_A_4.csv', delimiter=';')



# split into input (X) and output (y) variables
X = dataset[:,0:6]
# X = tf.keras.utils.normalize(
#     X, axis=1, order=2
# )
y = dataset[:,6]
print(y.shape)
y[y==0]=0
y[y==1]=0
y[y==2]=1
y[y==3]=1
print(y.shape)


X_resampled, y_resampled = SMOTE().fit_sample(X, y)

print( (y_resampled==0).sum()/y_resampled.shape )
print( (y_resampled==1).sum()/y_resampled.shape )

# define the keras model
model = Sequential()
model.add(Dense(64, input_dim=6, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()
# input("Press ENTER to continue...")
# compile the keras model

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[tf.keras.metrics.Recall()])

# fit the keras model on the dataset
model.fit(X_resampled, y_resampled, epochs=10000, batch_size=128)

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
for i in range(100):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))



datasetest = loadtxt('rawdata_A_5.csv', delimiter=';')

# split into input (X) and output (y) variables
x_test = datasetest[:,0:6]
# X = tf.keras.utils.normalize(
#     X, axis=1, order=2
# )
y_test = datasetest[:,6]

print('\n# Evaluate on test data')
results = model.evaluate(x_test, y_test, batch_size=128)
<<<<<<< HEAD
print('test loss, test acc:', results)
=======
print('test loss, test acc:', results)
>>>>>>> e2541b68a418b449dd74fc21e6c02256b161673d
