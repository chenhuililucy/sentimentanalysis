



my_slice=train_images(10:100,:,:)
my_slice.shape
my_slice=train_images[10:100,0:28,0:28]
my_slice.shape

#=======# 

#The notion of data batches 

batch=train_images[:,7:-7,7:-7]

#in general, the first axis will always be the samples axis 
#deep-learning takes sample in batches 

batch=train_image[128*n:128*(n+1)]

#when considering such a batch tensor, the first aixs is the batch axis 
#the second axis is the batch dimension