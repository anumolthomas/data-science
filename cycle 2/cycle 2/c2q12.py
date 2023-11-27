import numpy as np
a=np.array([[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30]])
b=np.array([[2,3,4],
            [5,6,7],
            [8,9,10]])
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 10-10-2023")
submatrix_a=a[:3,:3]
result=np.dot(submatrix_a,b)
a[:3,:3]=result
print("Updated matrix a :")
print(a)