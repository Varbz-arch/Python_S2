import numpy as np
# Arr3= np.array([[[0,1],[2,3]],[[4,5],[6,7]],[[99,88],[77,66]],[[111,222],[333,444]]])
# print(Arr3[3,0,1]) #222
# print(Arr3[3,:,:]) # last matrix  [[111,222],[333,444]]

# A2=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
# print(A2[::2,1::2]) #1 3 9 11
# print(A2[::2,:3:2]) #0 2 8 10
# print(A2[::2,3:2:]) # empty
# print(A2[::2,3:2:-1]) #3 11
# num = (A2[1,::3])   #4 7
# print(np.sum(num))
#[START:STOP:STEP]
#arr[1,-1] second row, last column 2d array

#slicing
# arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr1[3:])
# print(arr1[3:7])
# print(arr1[1::2])
# print(arr1[1::3])

# arr2 = np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(arr2[2,2])
# print(arr2[1,1:])
# print(arr2[1:3,0:2])
# print(arr2[::2,::2])

# arr2 = np.array([[10,20,30,100],[40,50,60,200],[70,80,90,300],[400,500,800,560]])
# print(arr2[1:3,1:3])
# print(arr2[:2,:4:3])
# print(arr2[:4:3,:4:3])
# array1=np.arange(1,8,3)
# print(array1)

# arr=np.array([10,20,30,40,50,60,70])
# print(arr[-1:-3:-1]) #70 60

arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d[:,:,:2])
print(arr3d[0,1,1], arr3d[1,0,1])
print(arr3d[1:2:1, :2:3,:2])
