import sys
import numpy as np

def init_centroids(points, k):
	max_val = max(map(max, points))
	min_val = min(map(min, points))
	centroids = {}

	for i in range(k):
		centroids[i] = np.random.uniform(low=min_val, high=max_val, size=(points.shape[1]))
	
	return centroids

def clustering(points, centroid, k):
	point_cluster = []
	for i in range(points.shape[0]):
		dist = []
		for j in range(k):
			dist.append(np.linalg.norm(points[i]-centroid[j]))	
		point_cluster.append(dist.index(min(dist)))

	return point_cluster
	
def update_centroid(points, centroid, point_cluster, k):
	updated_centroid = {}
	
	for i in range(k):
		point_cluster = np.array(point_cluster)
		cluster = np.where(point_cluster == i)[0]
		total_sum = np.zeros(points.shape[1])
		if len(cluster) != 0:
			for j in range(len(cluster)):
				
				total_sum+=points[cluster[j]]

			updated_centroid[i] = np.array(total_sum/len(cluster))
		else:
			updated_centroid = init_centroids(points, k)

	return updated_centroid
	
	

if __name__=="__main__":
	fname = sys.argv[1]
	k_classes = int(sys.argv[2])

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
		for i in range(k_classes):
			if centroid[i].all() == updated_centroid[i].all():
				j+=1
			if j == k_classes:
				check = False
			centroid = updated_centroid
	for i in range(k_classes):
		sarr = str(centroid[i])
		print sarr[1:-1]
		 
	
	
