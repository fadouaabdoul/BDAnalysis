import numpy as np

def computer(a):
    print("max : "+str(max(a)))
    print("min : "+str(min(a)))
    print("mean : "+str(np.mean(a)))
    print("standard deviation : "+str(np.std(a)))
    print("median : "+str(np.median(a)))
    print("25percentile : "+str((a[1] + a[2] / 2)))
    print("75percentile : "+str((a[6] + a[7] / 2)))
    return([max(a), min(a), np.std(a), np.median(a),(a[1]+a[2])/2,(a[6]+a[7])/2])

three_set_random_number = [3, 18, 27, 28, 29,38, 61, 68, 79, 92]

print("the summary statistics is as follows :",computer(three_set_random_number))