from sklearn.cluster import KMeans
import sys
import numpy as np

if __name__ == "__main__":
	fname = sys.argv[1]
	k_classes = int(sys.argv[2])

	with open(fname) as f:
		data = f.readlines()

	str_points = [x.strip() for x in data] 
	points = np.array([x.split(" ") for x in str_points])
	points = points.astype(np.float)

	kmeans = KMeans(n_clusters=k_classes, random_state=0).fit(points)
	centroid = kmeans.cluster_centers_
	sarr = [str(a) for a in centroid]
	for i in range(k_classes):
		 print(str(sarr[i])[1:-1])
