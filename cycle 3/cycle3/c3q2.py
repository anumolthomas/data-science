import matplotlib.pyplot as plt
days=['mon','tues','wed','thurs','fri']
drink_sales=[300,450,150,400,650]
food_sales=[400,500,350,300,500]
plt.figure(figsize=(8,8))
plt.subplot(2,1,1)
plt.plot(days,drink_sales,linestyle='dotted',color='orange',label='sales data1',marker='h',markersize=8,markerfacecolor='magenta',markeredgecolor='black')
plt.xlabel('days of the week')
plt.ylabel('sale of drinks')
plt.title('sales data1',loc='right')
plt.grid(color='blue',linestyle='--')
plt.legend()
plt.subplot(2,1,2)
plt.plot(days,food_sales,linestyle='--',color='green',label='sales data2',marker='d',markersize=8,markerfacecolor='magenta',markeredgecolor='red')
plt.xlabel('days of the week')
plt.ylabel('sales of food')
plt.title('sales data2',loc='center')
plt.grid(color='blue',linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()