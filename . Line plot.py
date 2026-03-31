import pandas as pd
import matplotlib.pyplot as plt

data = {'Name': ['ANSH', 'SAHIL', 'JAYAN', 'ANURAG'], 'Age': [21, 23, 20, 24]}
df = pd.DataFrame(data)

plt.plot(df.index, df['Age'])
plt.xlabel('Index')
plt.ylabel('Age')
plt.title('Age Line Plot')
plt.show()