import matplotlib.pyplot as plt
month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
affordable_segment = [173,153,195,147,120,144,148,109,174,130,172,131]
luxury_segment = [189,189,105,112,173,109,151,197,174,145,177,161]
super_luxury_segment = [185,185,126,134,196,153,112,133,200,145,167,110]
plt.figure(figsize=(10, 6))
plt.scatter(month,affordable_segment,color='cyan',label='Affordable',s=100)
plt.scatter(month,luxury_segment,color='orange',label='Luxury',s=100)
plt.scatter(month,super_luxury_segment,color='pink',label='Super Luxury',s=100)
plt.xlabel('Months of Year', fontsize=18)
plt.ylabel('Sales of Segments')
plt.title('Sales Data', fontsize=18)
plt.legend()
plt.show()