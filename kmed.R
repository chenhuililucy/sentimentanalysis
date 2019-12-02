
#https://www.youtube.com/watch?v=sAtnX3UJyN0
Iris=read.csv("/Users/lucy/Desktop/assortedcodes/iris.csv")
View(Iris)
Iris.features=Iris 
Iris.features$class<-NULL
#alternatively, can do Iris.feattures<-Iris.features[-1]
View(Iris.features)
str(Iris.features)
#standardise your variables
results <- kmeans(Iris.features,4)
results

