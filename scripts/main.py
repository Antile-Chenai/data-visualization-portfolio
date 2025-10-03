# Data Visualization Portfolio
# Author: Antile Kaba
# Date: 2025-10-02

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -------------------------
# 1. Create Sample Dataset
# -------------------------
np.random.seed(42)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'Value1': np.random.randint(10, 100, 100),
    'Value2': np.random.rand(100) * 50,
    'Date': pd.date_range('2025-01-01', periods=100)
})

# -------------------------
# 2. Summary Statistics
# -------------------------
summary = data.groupby('Category').agg({
    'Value1': ['mean', 'sum'],
    'Value2': ['mean', 'sum']
}).reset_index()
print("Summary Statistics:\n", summary)

# -------------------------
# 3. Matplotlib Visualization
# -------------------------
plt.figure(figsize=(10,5))
for cat in data['Category'].unique():
    subset = data[data['Category'] == cat]
    plt.plot(subset['Date'], subset['Value1'], label=f'Cat {cat}')
plt.title('Value1 over Time by Category')
plt.xlabel('Date')
plt.ylabel('Value1')
plt.legend()
plt.savefig('value1_over_time.png')
plt.close()

# -------------------------
# 4. Seaborn Visualization
# -------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Value2', data=data)
plt.title('Value2 Distribution by Category')
plt.savefig('value2_boxplot.png')
plt.close()

# -------------------------
# 5. Plotly Interactive Chart
# -------------------------
fig = px.scatter(data, x='Value1', y='Value2', color='Category', size='Value2',
                 hover_data=['Date'], title='Interactive Scatter Plot')
fig.write_html('interactive_scatter.html')

# -------------------------
# 6. Additional Analytics
# -------------------------
correlations = data[['Value1','Value2']].corr()
print("\nCorrelations:\n", correlations)

category_means = data.groupby('Category').mean()
print("\nMean Values per Category:\n", category_means)

print("\nData Visualization Portfolio Project Completed!")
