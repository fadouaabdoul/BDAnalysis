import numpy as np 
import pandas as pd

wines0 = np.genfromtxt("wine.csv", delimiter=",")
print("first", wines0)


wines1 = np.genfromtxt("wine.csv", delimiter=",", skip_header=1)

print("wines 1", wines1)
print("wines 1 data dimensions" ,wines1.shape)
print("wines 1 data with dtype " ,wines1.dtype)

wines2 = np.genfromtxt("wine.csv", delimiter=",", names = True)

print("wines 2",wines2)
print("wines 2 with dimensions ", wines2.shape)
print("wines 2 data with headers",wines2.dtype)


print("Extracting the quality score of the third red wine :",wines1[2,4])

print("Use a colon to select the first three items in the fourth column:",wines1[:3,3])

print("Extract all the data for the first red wine:",wines1[0,:])





print("flipping the array using - np.transpose(wines1)",np.transpose(wines1))

print("flipping the arrray using - wines1.T",wines1.T)

print("reducing the multidimensional array to one dimension using wines1.ravel()",wines1.ravel())

print("reducing a multidimensional array to one dimension wines1.flatten()",wines1.flatten())

flatten = wines1.flatten()

print("reduced data to one dimension and then changed back to what it was using - flatten.reshape(1599,5)",flatten.reshape(1599,5))




flatten = np.zeros((1599,1))

np.hstack((wines1,flatten))

flatten=np.zeros((1,5))

np.vstack((wines1,flatten))

print("np.concatenate((wines1,np.zeros((1599,1))),axis=1))",np.concatenate((wines1,np.zeros((1599,1))),axis=1))
print("np.concatenate((wines1,np.zeros((1,5))),axis=0))",np.concatenate((wines1,np.zeros((1,5))),axis=0))