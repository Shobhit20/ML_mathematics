''' The code contains implementation of K-means clustering algorithm'''

import sys
import numpy as np

def init_centroids(points, k):
	"""Returns the randomly initiated centroid values. For bounding the initial estimate the 
	values are chosen between the max and the minimum values

	Argument: 
	1) Points: input parsed in proper format
	2) k: total no. of clusters
	
	Return:
	centroids: Randomly initiated centroid values"""
	max_val = max(map(max, points))
	min_val = min(map(min, points))
	centroids = {}

	for i in range(k):
		centroids[i] = np.random.uniform(low=min_val, high=max_val, size=(points.shape[1])) #Random initialization of centroid points
	
	return centroids

def clustering(points, centroid, k):
	"""Return list of cluster to which the given point belongs to. The distance metric taken 
	into consideration is euclidean distance
	
	Argument: 
	1) Points: input parsed in proper format
	2) centroid: entroid based on the cluster
	3) k: total no. of clusters
	
	Return:
	point_cluster: The cluster to which each point belongs to
	"""
	point_cluster = []
	for i in range(points.shape[0]):
		dist = []
		for j in range(k):
			dist.append(np.linalg.norm(points[i]-centroid[j])) #Euclidean distance calculated	
		point_cluster.append(dist.index(min(dist))) #Choosing minimum euclidean distance to identify the cluster

	return point_cluster
	
def update_centroid(points, centroid, point_cluster, k):
	"""Returns the updated estimate of centroid at each stage. The  algorithm stops when the 
	current estimate is equal to the previous estimate

	Argument: 
	1) Points: input parsed in proper format
	2) centroid: entroid based on the cluster
	3) k: total no. of clusters
	4) point_cluster: The cluster to which each point belongs to
	
	Return:
	updated_centroid: The updated value of centroids"""
	updated_centroid = {}
	
	for i in range(k):
		point_cluster = np.array(point_cluster)
		cluster = np.where(point_cluster == i)[0]
		total_sum = np.zeros(points.shape[1])
		if len(cluster) != 0:
			for j in range(len(cluster)):
				
				total_sum+=points[cluster[j]]

			updated_centroid[i] = np.array(total_sum/len(cluster)) # Average of all the points present in cluster to identify new cluster
		else:
			updated_centroid = init_centroids(points, k)

	return updated_centroid
	

if __name__=="__main__":
	fname = sys.argv[1]
	k_classes = int(sys.argv[2])
 	# Reading the input file passed as argument 1
	with open(fname) as f:
		data = f.readlines()

	str_points = [x.strip() for x in data] 
	points = np.array([x.split(" ") for x in str_points])
	points = points.astype(np.float)
	centroid = init_centroids(points, k_classes)
	point_clusters = clustering(points, centroid, k_classes)
	updated_centroid = update_centroid(points, centroid, point_clusters, k_classes)
	j = 0
	check = True
	
	while check == True:
		j=0

		# Verifying that the centroid value doesnot change
		for i in range(k_classes):
			if centroid[i].all() == updated_centroid[i].all():
				j+=1
			if j == k_classes:
				check = False
			centroid = updated_centroid
	for i in range(k_classes):
		sarr = str(centroid[i])
		print sarr[1:-1]
		 
	
	
