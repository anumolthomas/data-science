import numpy as np
matrix_size=3
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 10-10-2023")
random_matrix=np.random.randint(1,11,size=(matrix_size,matrix_size))
print("Random square matrix :")
print(random_matrix)
try:
    inverse_matrix=np.linalg.inv(random_matrix)
    print("Inverse matrix :")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Inverse does not exist for this matrix.")
rank=np.linalg.matrix_rank(random_matrix)
print("Rank of the matrix :",rank)
determinant=np.linalg.det(random_matrix)
print("Determinant of the matrix :",determinant)
matrix_1d=random_matrix.flatten()
print("Matrix as a 1D array :")
print(matrix_1d)
eigenvalues,eigenvectors=np.linalg.eig(random_matrix)
print("Eigenvalues :")
print(eigenvalues)
print("Eigenvectors :")
print(eigenvectors)