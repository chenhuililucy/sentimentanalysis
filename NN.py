"""     

Deep learning textbook notes 


# Sequence of deep learning 

# •	Inputs 
# •	Weighted layers of data transformation 
# •	=> predictions 
# •	=> loss function (objective function) 
# •	=> loss score 
# •	Optimizer implement backpropagation algorithm 

"""


#a tensor that contains only 1 number is called a scalar, n dimensional vector  

#eg

import numpy as np 
x=np.array(1)
print(x.ndim) 


list1=[1,2,3,4,5,6]
y=np.asarray(list1)
x=np.array(y)
print(x.ndim)

from keras.datasets import mnist 

(trainimages, trainlables),(testimages,testlabels)=mnist.load_data()
trainimages.shape

train_images=trainimages

my_slice=train_images[10:100]
my_slice.shape
my_slice=train_images[10:100,0:28,0:28]
my_slice.shape


#=======# 

#The notion of data batches 

batch=train_images[:,7:-7,7:-7]

#in general, the first axis will always be the samples axis 
#deep-learning takes sample in batches 

for n in range(0,10): 
    batch=train_images[128*n:128*(n+1)]

#when considering such a batch tensor, the first aixs is the batch axis 
#the second axis is the batch dimension


""" 
# prints array of a list of the test labels and a dtyoe 
print(trainlabels)

""" 

from keras import models 
from keras import layers

network= models.Sequential()




network.add(layers.Dense(512,activation='relu',input_shape=(28*28,))) 
network.add(layers.Dense(10,activation='softmax'))

""" 
Key concepts  
Layer: a data processing module that filters the data 
"""

# Loss function is how the network will be able to measure the performance on the training
# And thus how it will be able to steer itself in the right direction 
# Optimizer is the mechaniesm through whcih the network will update itself based on the 
# data it sees and its loss function 
# Mertics to monitor during training and testing 


# => I am not sure what the metric means here 
network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metric=['accuracy'])


"""

Reshape images: preprocess the data by reshaping it into the shape the network expects and scaling it so that 
the all values are in the interval [0,1] interval interval

"""

test_images=testimages

train_images=train_images.reshape((60000,28*28))
train_images=train_images.astype("float32")/225 

test_images=test_images.reshape(10000,28*28)
test_images=test_images.astype('float32')/225



""" 
preparing the labels 

""" 

train_labels=trainlables
test_labels=testlabels
from keras.utils import to_categorical 
train_labels=to_categorical(train_labels)
test_labels=to_categorical(test_labels)

# a keras layer can be interpreted as a function, it takes an input 
keras.layers.Dense(512,activation="relu")
# we have 2 tensors, if we take the dot produyct of 2 2D tensors and apply an additive b 
output=relu(dot(W,input)+b) 


class Naivebayesclassifier(object):
    def __init__(self): 
        pass 

    def elementwiseop(x,self): 
        assert len(x.shape)==2 #x is a 2 d vector
        # prevent overwriting of file 
        x=x.copy() 
        for i in range(x.shape[0]): # look at the dimenison of the first element of the list or np.array (?)
            for j in range(x.shape[1]): 
                x[i,j]=max(x[i,j],0) #important! assert the optimal dimension of the vector 
        return x


""" 

 __init__ method
"__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

Find out the cost of a rectangular field with breadth(b=120), length(l=160). It costs x (2000) rupees per 1 square unit

class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s sq units" % (r.get_area()))
This gives the output

Area of Rectangle: 19200 sq units
Cost of rectangular field: Rs.38400000

""" 

