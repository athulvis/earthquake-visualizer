import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from geopy.distance import geodesic

file_path = 'earthquake.csv'
earthquake_data = pd.read_csv(file_path)

def haversine_distance(coord1, coord2):
    return geodesic(coord1, coord2).km


radius = 100 
region_centers = []


for index, row in earthquake_data.iterrows():
    center = (row['Latitude'], row['Longitude'])
    count = sum(haversine_distance(center, (lat, lon)) <= radius for lat, lon in zip(earthquake_data['Latitude'], earthquake_data['Longitude']))
    region_centers.append([center[0], center[1], count])

region_df = pd.DataFrame(region_centers, columns=['Latitude', 'Longitude', 'Count'])


kmeans = KMeans(n_clusters=3)
region_df['Cluster'] = kmeans.fit_predict(region_df[['Count']])


cluster_labels = {cluster: f"Cluster {cluster}" for cluster in region_df['Cluster'].unique()}
average_counts = region_df.groupby('Cluster')['Count'].mean().sort_values().index

frequency_labels = ['Less Frequent', 'Frequent', 'Very Frequent']
cluster_to_frequency = {cluster: frequency_labels[i] for i, cluster in enumerate(average_counts)}
region_df['Frequency'] = region_df['Cluster'].map(cluster_to_frequency)
region_df.to_csv("cluster_data.csv", index=False)
