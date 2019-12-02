
import matplotlib as mplt
import matplotlib.pyplot as plt
#This chaptyer we will be using the MNIST dataset, which is a set of 70,000 small images of handwritten omages 

from sklearn.datasets import fetch_openml 
mnist=fetch_openml('mnist_784',version=1) 
#print(dir(mnist))
#['DESCR', 'categories', 'data', 'details', 'feature_names', 'target', 'url']
print(mnist.keys())
X,Y= mnist['data'], mnist['target']
C,F,L=mnist['categories'], mnist['feature_names'], mnist['url']
print(X.shape)
#list attribute has on attribute shape 

"""
                 
                Reshape and display 10 randomly selected digit 

""" 

for n in range(0,10):
    somedigit=X[n]
    somedigitimage=somedigit.reshape(28,28)
    plt.imshow(somedigitimage,cmap="binary")
    plt.axis("off")
    plt.show()


""" 

              Splitting the dataset into training and testing data 

""" 

X_train, X_test, Y_train, Y_test= X[:600000], X[600000:], Y[:600000], Y[600000:] 

################## Binary classifier



####### Confusion matrix ### 



from sklearn.model_selection import cross_val_predict 
y_train_pred=cross_val_predict(sgd_clf, X_train,y_train_5,cv=3) 
from sklearn.metrics import confusion_matrix 

skfolds=StratidifedKFold(n_splits=3, random_state=42) 

