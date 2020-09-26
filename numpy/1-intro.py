import numpy

#creating array
arr = numpy.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print(type(arr))
print("numpy version:", numpy.__version__)

# 0-D Arrays
ar = numpy.array(42)

print(ar) 

# 1-D Array
arr = numpy.array([1, 2, 3, 4, 5])

print(arr) 

# 2-D Array
array_2d = numpy.array([[1, 2, 3], [4, 5, 6]])

print(array_2d) 

# 3-D Array
array_3d = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(array_3d) 