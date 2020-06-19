#IA de classification 
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Flatten
import tensorflow as tf
from imblearn.over_sampling import SMOTE,ADASYN,RandomOverSampler


# load the dataset
dataset = np.loadtxt('finalreenregistrer.csv', delimiter=';')

index=[]
for i in dataset:
	if i[-1] == 1 or i[-1] == 2:
		index.append(i)
print(dataset.shape)
dataset = np.asarray(index)
print(dataset.shape)

# split into input (X) and output (y) variables
X = dataset[:,0:6]
# X = tf.keras.utils.normalize(
#     X, axis=1, order=2
# )
y = dataset[:,6]
y = y-1


X_resampled, y_resampled = SMOTE().fit_sample(X, y)

tf.keras.utils.normalize(
    X, axis=-1
)

# define the keras model
model = Sequential()
model.add(Dense(128, input_dim=6, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()
# input("Press ENTER to continue...")
# compile the keras model

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[tf.keras.metrics.Recall()])
model.compile(loss=tf.keras.losses.KLDivergence(), optimizer='adam', metrics=[tf.keras.metrics.Recall(),'accuracy'])

# fit the keras model on the dataset
model.fit(X_resampled, y_resampled, epochs=100000, batch_size=64, shuffle=True)

# evaluate the keras model
_, recall_poisson, accuracy_poisson = model.evaluate(X, y)


print('Result with Poisson loss function :   recall: {} accuracy: {}'.format(recall_poisson,accuracy_poisson))


# datasetest = loadtxt('rawdata_A_5.csv', delimiter=';')

# # split into input (X) and output (y) variables
# x_test = datasetest[:,0:6]
# # X = tf.keras.utils.normalize(
# #     X, axis=1, order=2
# # )
# y_test = datasetest[:,6]

# print('\n# Evaluate on test data')
# results = model.evaluate(x_test, y_test, batch_size=128)
# print('test loss, test acc:', results)

model.save("model.h5")
print("Saved model to disk")