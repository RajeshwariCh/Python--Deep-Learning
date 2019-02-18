import numpy as np

array = np.random.randint(0,21,15)#we import numpy as np
print(array)#create a variable names array and set it to np.random.rand
#here 0 is inclusive 21 is exclusive
counts = np.bincount(array)#here we use numpy
print (np.argmax(counts))#get the most repeated value here