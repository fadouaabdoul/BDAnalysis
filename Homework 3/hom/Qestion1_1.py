import numpy as np

np.random.seed(0)

def random_list(list):
    list = []
    for i in range(10):
        list.append(np.random.randint(100))
    list.sort()
    return list

my_list = np.random.randint(10,size=10)
print("The list created is : ", my_list)


print("The merged and sorted list is : ",random_list(my_list))