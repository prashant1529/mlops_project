#!/usr/bin/env python
# coding: utf-8
# In[3]:
from keras.datasets import mnist
dataset=mnist.load_data('mymnist.db')
len(dataset)
train , test = dataset
len(train)
X_train , y_train = train
X_train.shape
X_test, y_test = test
X_test.shape
img1 = X_train[0]
img1
img1.shape
img1_label=y_train[0]
img1_label
img_label= y_train[5]
img1d=img1.reshape(28*28)
img1d.shape
X_train.shape
X_train_1d = X_train.reshape(-1 , 28*28)
X_train = X_train_1d.astype('float32')
y_train.shape
from keras.utils.np_utils import to_categorical
y_train_cat=to_categorical(y_train)
y_train_cat
from keras.models import Sequential
from keras.layers import Dense
model =Sequential()
model.add(Dense(units=512, input_dim = 28*28, activation= 'relu'))
model.add(Dense(units=256, activation='relu'))
i=1
for i in range(i):
    model.add(Dense(units=128,activation='relu'))
    
model.add(Dense(units=10, activation='softmax'))
model.summary()
from keras.optimizers import RMSprop
model.compile(optimizer= RMSprop(),loss='categorical_crossentropy', metrics=['accuracy'])
h = model.fit(X_train, y_train_cat,epochs=5)
X_test_1d=X_test.reshape(-1, 28*28)
X_test= X_train_1d.astype('float32')
y_test_cat=to_categorical(y_test)
model.predict(X_test)
y_test_cat
c=h.history['accuracy']
h.history['accuracy'][4]
with open('accuracy.txt', 'w') as f:
    f.write(str(c[4]))

model.save('mlopsmodel.h1')
