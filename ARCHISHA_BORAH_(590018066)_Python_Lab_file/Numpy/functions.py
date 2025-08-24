import numpy as np

# arr4d = np.arange(16).reshape(2,2,2,2)
# print(arr4d)
# print(arr4d.size)
# print(arr4d.T) #transpose

# evena = np.arange(2,21,2)
# print(evena)

# lst = [1,2,3]  #to print list to numpy array
# arr=np.array(lst)
# print(type(arr))

# arr2 = np.linspace(-10,10,15,dtype = int)
# #np.linspace() first creates floats, and then if you give dtype=int, 
# #it converts them into integers by truncating (removing decimals).
# print(arr2)

# ar = np.array([1,2,3,4,5,6,7,8,9])
# print(ar[-3])
 
# lst = [1,2,3]  #* means repeat the elements
# print(lst*2)
# lst=np.array([1,2,3])
# print(lst*2)
#or
# lst2=[x*2 for x in lst]
# print(lst2)

# attributes = size,dtype,shape(vector shape),ndim(gives dimensions)
# for zero matrix = np.zeroes(3,4)
# for 333 eg ,full = np.full((2,3),3)
# values generate btw 0 and 1 np.random.random((2,3))
# to flatten array .flatten
# for transpose arr2D.T

# full3=np.full((2,3),3)
# print(full3)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# flattened_arr = arr.flatten()
# print(flattened_arr)

# ar2d = np.array([[10,20,130,100],[40,50,60,200],[70,80,90,300],[400,800,1200,1600]])
# print(ar2d[1:3,1:3])

# arr1 = np.array([1,7,5])
# l1 = [1,7,5]
# print(arr1)
# print(arr1*2)
# print(l1*2)

#odd
# arr1 = np.arange(1,20,2)
# print(arr1)

#4 d array  :  tensor

#3 d array
# arr1 = np.array([[[1,2,3],[4,5,6]],[[4,5,6],[1,2,3]]])
# print(arr1)
# print(arr1.size)

# #method 3
# arr1 = np.linspace(-10,10,10,dtype=int)     
# # np.linspace(-10,10,10)  : by fault only float values, here last 10 means no of element not size
# print(arr1)
# print(arr1.size)
# print(arr1.dtype)
# print(arr1.shape)
# print(arr1.ndim)


#to make a 0's array
# np.zero(3,4)

# specific syntax
# full = np.full((2,2),3)

#generate randomm array
# np.random.random((2,3))   #range 0 and 1

# flatten array 4 d to 1 d

# transpose
# arr1.T

# array1 = np.arange(11, 19)

# # Target reshape dimensions
# target_shape = (2, 3)

# # Check if the number of elements in array1 can fit the target shape
# if array1.size != target_shape[0] * target_shape[1]:
#     print(f"Error: The values won't fit into the shape {target_shape}.")
# else:
#     # If they fit, reshape the array
#     reshaped_array = array1.reshape(target_shape)
#     print(reshaped_array)
# target_shape is a tuple that specifies the new dimensions (rows and columns) of the array.
# target_shape[0] represents the number of rows.
# target_shape[1] represents the number of columns.

# arr=np.array([10,20,30,40,50])
# print(np.ndim(arr))
# print(arr.dtype)
# print(arr.itemsize)

# list1=[[[1,2,3,4],[5,6,7,8]],[[12,22,34,56],[11,22,33,44]]]
# arr=np.array(list1)
# # print(arr)
# # print(type(arr))
# # print(arr.ndim)
# # print(arr.dtype)
# # print(arr.itemsize)
# print(np.sum(arr))
# print(np.mean(arr))

# arr=np.random.random((2,2))
# print(arr)

# arr=np.random.randint(5,10,(2,2))
# print(arr)

# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# print(np.dot(a,b))  #multiply

# arr = np.array([1,2,3,4])
# print(np.std(arr))    # Spread of numbers

# print(np.empty((2,3)))

# array1=np.linspace(1,8,3)
# array2=np.arange(1,8,3)
# print(array1)
# print(array2)

# a=np.random.normal(3,7,(2,2,3)) #mean std size
# print(a)

# arr=np.array([22,4,1,66,99,2])
# print(np.sort(arr))
# print(np.where(arr==2))

#np.argsort
# arr = np.array([40, 10, 30, 20])
# print(np.argsort(arr))  #indixes sort

#np.searchsort
# arr = np.array([10, 20, 30, 40, 50])
# print(np.searchsorted(arr, 2))  #Tell me where a number should go in a sorted array

#broadcasting
#1
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([[1], [2], [3]])
# result = arr1 + arr2
# print(result)

#2
# arr = np.array([22, 2, 3])
# print(arr + 5)

#copy numpy
# a = np.array([1, 2, 3])
# b = a.copy()   # Deep copy
# c = a        
# a[0] = 100
# print("a:", a) 
# print("b:", b) 
# print("c:", c)  
#new memory is allocated

#copy() = Clone (new and separate)
# view() = Mirror (same thing, different angle)

#view numpy
a = np.array([1, 2, 3])
b = a.view()
a[0] = 100
print("a:", a)  
print("b:", b)  # Changes reflect in view
#if you make changes to a view, it will affect 
# the original array—because a view shares the same data buffer 
# as the original array. Only the metadata (like shape or dtype) might differ.