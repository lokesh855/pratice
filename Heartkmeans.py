import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Assuming your dataset is in a CSV file
data = pd.read_csv('heart_disease.csv')

# Select relevant features for clustering
features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'AHD']
X = data[features]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters (e.g., using the elbow method)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Choose the optimal number of clusters based on the elbow plot
n_clusters = 3  # Adjust based on the elbow plot

# Create the K-Means model
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)

# Fit the model to the scaled data
kmeans.fit(X_scaled)

# Add the cluster labels to the original DataFrame
data['cluster'] = kmeans.labels_

# Analyze the clusters
print(data.groupby('cluster').mean())

# Visualize the clusters (if possible, depending on the number of features)
# For example, using a 3D scatter plot for three features:
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 2], c=kmeans.labels_, cmap='rainbow')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
plt.title('K-Means Clustering')
plt.show()
