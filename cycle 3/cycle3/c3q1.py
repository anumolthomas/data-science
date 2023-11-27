import matplotlib.pyplot as plt
year=[2001,2002,2003,2004,2005,2006,2007]
car_value=[24000,22500,19700,17500,14500,10000,5800]
plt.figure(figsize=(8,4))
plt.subplot(1,1,1)
plt.plot(year,car_value,color='red',linestyle='-.',label='car_value')
plt.scatter(year,car_value,color='green',marker='*',s=20,label='data point')
plt.xlabel('year')
plt.ylabel('car value')
plt.title('value depreciation',loc='left')
plt.legend()
plt.show()