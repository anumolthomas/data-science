import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
affordable_segment = [173,153,195,147,120,144,148,109,174,130,172,131]
luxury_segment = [189,189,105,112,173,109,151,197,174,145,177,161]
super_luxury_segment = [185,185,126,134,196,153,112,133,200,145,167,110]
plt.figure(figsize=(10, 6))
plt.plot(months, affordable_segment, label='Affordable', color='purple', linestyle='-', marker='o')
plt.plot(months, luxury_segment, label='Luxury', color='red', linestyle='--', marker='s')
plt.plot(months, super_luxury_segment, label='Super Luxury', color='pink', linestyle='-.', marker='^')
plt.xlabel('Months of Year')
plt.ylabel('Sales of Segments')
plt.title('Sales Data')
plt.legend(loc='upper right')
plt.show()