import numpy as np
print("Name : ANUMOL THOMAS\nREG no : SJC22MCA-2011\nCourse Code: 20MCA241\nCourse : Data Science Lab\nDate : 10-10-2023")
even_numbers=np.arange(2,32,2)
print(even_numbers)
elements_from_2_to_8_step_2=even_numbers[2:9:2]
print("a. Elements fromindex 2 to 8 with step 2 :",elements_from_2_to_8_step_2)
last_3_elements=even_numbers[-3:]
print("b. Last 3 elements using negative index :",last_3_elements)
alternate_elements=even_numbers[::2]
print("c. Alternate elements of the array :",alternate_elements)
last_3_alternate_elements=even_numbers[-1::-2][:3]
print("d. Last alternate elements of the array :",last_3_alternate_elements)