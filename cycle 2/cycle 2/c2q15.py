import numpy as np
A = np.array([[2, 3, -1],
              [1, 2, 1],
              [3, 1, -2]])
b = np.array([7, 3, 8])
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 16-10-2023")
try:
    X = np.linalg.solve(A, b)
    print("Solution X:")
    print(X)
except np.linalg.LinAlgError:
    print("Matrix A is singular. The system of equations may not have a unique solution.")