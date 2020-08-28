import pickle
from tensorflow.keras.layers import Dense,Flatten,Conv2D,Activation,Activation,MaxPooling2D,Dropout,BatchNormalization
from tensorflow.keras.models import Sequential
from keras.utils import  to_categorical
import numpy as np
import tensorflow as tf

X = np.array(pickle.load(open('X.pickle','rb')))
y = np.array(pickle.load(open('y.pickle','rb')))

test_X = np.array(pickle.load(open('test_X.pickle','rb')))
test_y = np.array(pickle.load(open('test_y.pickle','rb')))

#normalizing the data
X = X/255.0
test_X = test_X/255.0
'''
model = Sequential()

#input layer
model.add(Conv2D(140,(3,3),input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

#second layer
model.add(Conv2D(280,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(420,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(280,activation='relu'))

#output layer
model.add(Dense(140))
model.add(Activation('softmax'))

model.compile(
	loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy']
	)

model.fit(X,y,batch_size=64,epochs=10)
'''

model = Sequential()

model.add(Conv2D(64, (3, 3), padding='same',input_shape=X.shape[1:])) #224X224
model.add(Activation('relu'))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3))) #222x222
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2))) #111x111
model.add(BatchNormalization())
model.add(Dropout(0.35)) #Doesn't appear to be working in the model summary.

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(BatchNormalization()) 

model.add(Conv2D(64, (3, 3))) #109x109
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2))) #54x54
model.add(BatchNormalization())
model.add(Dropout(0.35)) #64 --> 42

model.add(Conv2D(64, (3, 3), padding='same')) #54x54
model.add(Activation('relu'))
model.add(BatchNormalization())

model.add(Flatten()) 
model.add(Dropout(0.5)) 
model.add(Dense(512)) 
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Dense(140)) 
model.add(Activation('softmax'))

#Compile
model.compile(optimizer = tf.keras.optimizers.SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True),
               loss = 'sparse_categorical_crossentropy',
               metrics = ['accuracy'])

model.fit(X,y,batch_size=64,epochs=10)

loss,accuracy = model.evaluate(
	test_X,
	test_y
	)

print(loss,accuracy)


