import numpy as np
m1=np.array([[1,2,3],
             [4,5,6],
             [7,8,9] ])
m2=np.array([[9,8,7],
             [6,5,4],
             [3,2,1]])
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 10-10-2023")
add_result=m1+m2
print("Matrix addition:")
print(add_result)
sub_result=m1-m2
print("Matrix substraction:")
print(sub_result)
mul_result=m1*m2
print("Matrix elementwise multiplication:")
print(mul_result)
div_result=m1/m2
print("Matrix elementwise division:")
print(div_result)
m_mul_result=np.dot(m1,m2)
print("Matrix multiplication:")
print(m_mul_result)
m_trans=np.transpose(m1)
print("Transpose of matrix 1 :")
print(m_trans)
diagonal_sum=np.trace(m1)
print("Sum of diagonal elements:")
print(diagonal_sum)