import numpy as np

x = np.array([[ 1, 2,  3,  4],
                [ 5, 6,  7,  8],
                [ 9, 10, 11, 12],
                [13, 14, 15, 16]])

y1 = x[:, 2]; 
print ("Question 1 ", y1)

y2 = x[-1,:2]; 
print ("Question 2", y2)

y3 = x[:, [True, False, False, True]]; 
print ("Question 3 ", y3)

y4 = x[0:2, 0:2]; 
print ("Question 4 ", y4)

y5 = x[[0, 1, 2], [0, 1, 2]]; 
print ("Question 5 ", y5)

y6 = x[0]**2; 
print ("Question 6 ", y6)

y7 = x.max(axis=1); 
print ("Question 7 ", y7)

y8 = x[:2, :2]+x[:2,2:]; 
print ("Question 8 ", y8)

y9 = x[:2, :3].T; 
print ("Question 9 ", y9)

y10 = x[:2, :3].reshape((3, 2)); 
print ("Question 10 ", y10)

y11 = x[:, :2].dot([1, 1]); 
print ("Question 11 ", y11)

y12 = x[:, :2].dot([[3, 0], [0, 2]]); 
print ("Question 12 ", y12)

