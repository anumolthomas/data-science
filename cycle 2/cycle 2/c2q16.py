import numpy as np
a=np.array([[5,27,32],[14,53,62],[67,88,19]])
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 16-10-2023")
u,s,vt=np.linalg.svd(a)
a_hat=u@np.diag(s)@vt
print("Original matrix a :")
print(a)
print("Singular values :")
print(s)
print("Reconstructed matrix a_hat :")
print(a_hat)