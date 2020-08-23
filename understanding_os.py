import os
print(os.getcwd())
# os.chdir('C://')
# print(os.getcwd())
f=open('nabbin.txt.txt')
print(f)
# c=0
# for data in f:
#     print(data)
#     c+=1
# print(c)
# os.mkdir('new')


ar=[1,2,3,4]
even=[x for x in ar if x%2==0]
print(even)
print(os.listdir('dataset'))
path = '/home/User/Desktop'
d=os.path.split(path)
# print(d[0])
# print(d[1])
# print(d[2])
print(d)
path='dataset'
imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
print(imagePaths)
data=os.path.split(imagePaths[0])
print(data[-1])
new_data=data[-1].split('.')
print(new_data)
arr=[1,2,3,4,-1,-2]
import numpy as np
np_arr=np.array(arr,'uint8')
print(np_arr)
