import numpy as np
a=np.array([[7,5,9],
            [2,11,3]])
b=np.array([[7,8],
            [9,10],
            [11,12]])
c=np.array([[13,14],
            [15,16]])
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 10-10-2023")
result=np.dot(np.dot(a,b),c)
print(("Result of matrix multiplication(a*b*c) :"))
print(result)