import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris_data = pd.read_csv('iris.csv')

# Set the style for the pairplot
sns.set(style="whitegrid")
pairplot = sns.pairplot(iris_data, hue="variety", markers=["o", "s", "D"], kind="reg")
# Show the pairplot
plt.show()