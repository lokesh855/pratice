import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Mall_Customers.csv")
data.head()

data.info()

x = data.iloc[:,[3,4]].values
x


from sklearn.cluster import KMeans

wcss_list =[]

for i in range(1,11):
  kmeans = KMeans(n_clusters = i , init = 'k-means++', random_state = 40)

kmeans.fit(x)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x = sc_X.fit_transform (x)
x


wcss_list.append(kmeans.inertia_)



wcss_list = []  # Initialize wcss_list outside the loop

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=40)
    kmeans.fit(x)  # Indent to ensure execution within the loop
    wcss_list.append(kmeans.inertia_)  # Indent to ensure execution within the loop





# Assuming the optimal number of clusters is determined to be 5 (you can change this based on the elbow method result)
optimal_clusters = 5

kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=40)
y_kmeans = kmeans.fit_predict(x)

# Plotting the clusters
plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'cyan', 'magenta']

for i in range(optimal_clusters):
    plt.scatter(x[y_kmeans == i, 0], x[y_kmeans == i, 1], s=100, c=colors[i], label=f'Cluster {i+1}')

# Plotting the centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


initial_centroids = kmeans.cluster_centers_
print(initial_centroids)
