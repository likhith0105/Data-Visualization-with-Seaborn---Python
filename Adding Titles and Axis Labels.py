import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)

# Add plot title and axis labels
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()