import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Step 1: Load data
df = pd.read_csv('finance.csv')

# Step 2: Prepare data for clustering (select numeric columns)
X = df[['Revenue', 'Profit', 'Assets', 'Liabilities']]

# Step 3: Apply KMeans clustering with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# Step 4: Plot Histogram of Revenue
plt.figure(figsize=(6,4))
plt.hist(df['Revenue'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.show()

# Step 5: Plot Heatmap of correlation matrix
plt.figure(figsize=(6,5))
corr = df[['Revenue', 'Profit', 'Assets', 'Liabilities']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap of Financial Features Correlation')
plt.show()

# Step 6: Plot clusters (Revenue vs Profit colored by cluster)
plt.figure(figsize=(6,4))
colors = ['red' if c==0 else 'blue' for c in df['Cluster']]
plt.scatter(df['Revenue'], df['Profit'], c=colors)
plt.xlabel('Revenue')
plt.ylabel('Profit')
plt.title('KMeans Clustering of Companies')
plt.show()
