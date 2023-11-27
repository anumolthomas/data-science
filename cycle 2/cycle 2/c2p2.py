import numpy as np
complex_array=np.array([[1+2j,2+3j,3+4j],[4+5j,5+6j,6+7j]], dtype=complex)
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 10-10-2023")
print("3D array : ")
print("2D array :")
print(complex_array)
rows,columns=complex_array.shape
print("Number of rows:",rows)
print("Number of columns :",columns)
print("Array dimension :",complex_array.shape)
reshaped_array=complex_array.reshape(3,2)
print("Reshaped 3x2 Array: ")
print(reshaped_array)