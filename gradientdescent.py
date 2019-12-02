#How can you derive this linear equation (ie. the best fit line goinging through all the datapoints)
#1. Draw any random line, from the actual data point, calculate the error of the datapoint and the line 
#2. Sum them up and divide by n 
#3. Mean squared error, or a cost function 

import numpy as np

def gradient_descent(x,y):
    mbegin = bbegin = 0
    #start with some value of m and b to reach the global minima
    iterations = 10000
    #define how many steps you are going to do 
    n = len(x)
    learning_rate = 0.08
    #start with some arbitrary value for the learning rate 


    for i in range(iterations):
        y_predicted = mbegin * x + bbegin
        #calculate the predicted value of y through the line of the equation 

        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        # to understand how well you are doing, you need to print out the costs, you need to print out your costs 

        md = -(2/n)*sum(x*(y-y_predicted))
        #calculating the derivative of m from the mean square function 

        bd = -(2/n)*sum(y-y_predicted)
        #calculating the derivative of b from the mean square function 

        m_curr = mbegin - learning_rate * md
        #we need learning rate 

        b_curr = bbegin - learning_rate * bd
        #similar for b  

        print ("m {}, b {}, cost {} iteration {}".format(mbegin,bbegin,cost, i))
        #print the values 

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)


