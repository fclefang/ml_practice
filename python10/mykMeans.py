from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):
	dataMat= []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float,curLine)
		dataMat.append(fltLine)
	return dataMat

def distEclud(vecA, vecB):
	return sqrt(sum(power(vecA-vecB, 2)))

def randCent(dataSet, k):
	n = shape(dataSet)[1]
	centroids = mat(zeros((k,n)))
	for j in xrange(n):
		minJ = min(dataSet[:,j])
		rangeJ = float(max(dataSet[:,j])-minJ)
		centroids[:,j] = minJ + rangeJ * random.rand(k,1)
	return centroids

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))#create mat to assign data points 
                                      #to a centroid, also holds SE of each point
    centroids = array([[20,60],[80,80]])
	# M1 = [20,60]
	# M2 = [80,80]
    # print centroids
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        print(centroids)
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            print (ptsInClust)
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean
    return centroids, clusterAssment,ptsInClust

if __name__== "__main__": 

	# dataMat = mat(loadDataSet('testSet.txt'))
	data_ = [[2.273,68.367],[27.89,83.127],[30.519,61.07],[62.049,69.343],[29.263,68.748],[62.657,90.094],[75.735,62.761],[24.344,43.816],[17.667,86.765],[68.816,76.874],[69.076,57.829],[85.691,88.114]]
	dataMat = array(data_)
	print (dataMat)

	myCentroids, clustAssing, clustarr = kMeans(dataMat,2)
	print(clustarr)
	# print myCentroids
	# print (dataMat[0],dataMat[1])
	# print (dataMat[0]-dataMat[1])
	# print (sum(dataMat[0]-dataMat[1]))
	# distEclud(dataMat[0],dataMat[1])

	


