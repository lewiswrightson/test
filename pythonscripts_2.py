#Exercise 1

#activity 1
import numpy as np
x=list(range(1,11))

a1=np.array(x,np.int32)
a2=np.array(x,np.float64)

print(a1.dtype)
print(a2.dtype)

#activity 2

arr1 = np.zeros((2,3,4))
arr2 = np.ones((2,3,4))
arr3 = np.arange(1000)

#activity 3
a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print(a[1])
print(a[1:4])

#Exercise 2

#activity 1
arr = np.array([range(4),range(10,14)])

print(np.shape(arr))
print(np.size(arr))
print(np.max(arr))
print(np.min(arr))

#activity 2

print(np.reshape(arr,[2,2,2])
print(np.transpose(arr))
print(np.ravel(arr))

#similar to np.ravel
flat_arr = arr.flatten() 

print(arr.astype(np.float64))a


a2 = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],[1, 22, 4, 0.1, 5.3, -9],[3, 1, 2.1, 21, 1.1, -2]])

print(a2[:,3])
print(a2[1:4, 0:4])
print(a2[1:, 2])

#Exercise 2 interrogating and manipulating arrays

#activity 1
import numpy as np

arr = np.array([range(4),range(10,14)])

print(np.shape(arr))
print(np.size(arr))
print(np.max(arr))
print(np.min(arr))

#activity 2

print(np.reshape(arr,(2,2,2)))

#Exercise 3 Array calculation and operations

#activity 1
a = np.array([range(4), range(10,14)])
b=np.array([2,-1,1,0])
c = a * b
b1=b*100
b2=b*100.0

print(b1 == b2)
print(b1.dtype,b2.dtype)

#activity 2

arr = np.array(range(1,10))
print(arr<3)
print(np.less(arr,3))

condition = np.logical_or(arr<3, arr>8)
arr2 = np.where(condition, arr*5, arr*-5)

#activity 3
def windspeed(u,v,minmag = 0.1):
    mag = ((u**2)+(v**2))**0.5
    output = np.where(mag>minmag,mag,minmag)
    return output

u = np.array([[4,5,6],[2,3,4]])
v = np.array([[2,2,2],[1,1,1]])

wind = windspeed(u,v)

print(wind)

u1 = np.array([[4,5,0.01],[2,3,4]])
v1 = np.array([[2,2,0.03],[1,1,1]])

wind1 = windspeed(u1,v1)

print(wind1)

#Exercise 4 working with missing values

#activity 1

import numpy.ma as MA
marr = MA.array(range(10),fill_value = -99999)
print(marr,marr.fill_value)

marr[2] = MA.masked

print(marr)

print(marr,marr.mask)

narr = MA.masked_where(marr>6,marr)
print(narr)

x = MA.filled(narr)

print(x)
print(type(x))

#activity 2
m1 = MA.array(range(1,9))
m2 = MA.reshape(m1,[2,4])
print(m2)
m3 = MA.masked_where(m2>6,m2)
print(m3)
print(m3*100)

import numpy as np

n1 = np.ones([2,4])
answer = m3 - n1

print(type(answer))


