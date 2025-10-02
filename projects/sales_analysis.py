import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/sales.csv')
sns.barplot(x='Region', y='Sales', data=df)
plt.title('Sales by Region')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/sales.csv')
sns.barplot(x='Region', y='Sales', data=df)
plt.title('Sales by Region')
plt.show()
