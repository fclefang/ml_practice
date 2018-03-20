from numpy import *
import operator
import sys
import matplotlib
import matplotlib.pyplot as plt

# print sys.path

# def createDataSet():
# 	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
# 	labels = ['A','A','B','B']
# 	return group,labels
def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) +1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]



def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat,classLabelVector

#normalized characteristic value
def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals
def datingClassTest():
	hoRatio = 0.10
	#datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
	#normMat,ranges,minVals = autoNorm(datingDataMat)
	n = normMat.shape[0]
	numTestVecs = int(n*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:n,:],datingLabels[numTestVecs:n],3)
		print "the classifier came back with: %d,the real answer is: %d"% (classifierResult,datingLabels[i])
		if(classifierResult != datingLabels[i]): errorCount += 1.0
	print "the total error rate is: %f"% (errorCount/float(numTestVecs))
def calssifyPerson():
	resultList = ['not at all','in small doses','in large doses']
	float percentTats = float(raw_input("percentage of time spent playing video games?"))
	float ffMiles = float(raw_input("frequent flier miles earned per year?"))
	float iceCream = float(raw_input("liters of ice cream consumed per year?"))
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
	print "You will probably like this person: ",resultList[classifierResult - 1]
if __name__== "__main__":    
	# dataset, labels = createDataSet()  
 #    inX = [0.1, 0.1]   
 #    className = classify0(inX, dataset, labels, 3)  
 #    print 'the class of test sample is %s' %className 
 	datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
	#plt.show()
	normMat,ranges,minVals = autoNorm(datingDataMat)
	#datingClassTest()
	calssifyPerson()



