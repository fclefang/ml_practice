from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(fileName):
	#detect the number of the features
	numFeat = len(open(fileName).readline().split('\t')) - 1
	dataMat = [];labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = []
		curLine = line.strip().split('\t')
		for i in xrange(numFeat):
			lineArr.append(float(curLine[i]))
		dataMat.append(lineArr)
		labelMat.append(float(curLine[-1]))
	return dataMat,labelMat

###########################################################
def standRegress(xArr,yArr):
	xMat = mat(xArr); yMat = mat(yArr).T
	xTx = xMat.T*xMat
	#compute the hanglieshi
	if linalg.det(xTx) == 0.0:
		print "This matrix is singular, cannot do inverse"
		return
	ws = xTx.I * (xMat.T*yMat)
	return ws

def plotShow(xArr,yArr):
	ws =  standRegress(xArr,yArr)
	xMat = mat(xArr)
	yMat = mat(yArr)
	yHat = xMat*ws
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
	xCopy = xMat.copy()
	xCopy.sort(0)
	yHat = xCopy*ws
	ax.plot(xCopy[:,1],yHat)
	plt.show()
###################################################

def lwlr(testPoint,xArr,yArr,k=1.0):
	xMat = mat(xArr); yMat = mat(yArr).T
	m = shape(xMat)[0]
	#create diagonal matrix
	weights = mat(eye((m)))
	for j in xrange(m):
		diffMat = testPoint - xMat[j,:]
		weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
	xTx = xMat.T*(weights * xMat)
	if linalg.det(xTx) == 0.0:
		print "This matrix is singular, cannot do inverse"
		return
	ws = xTx.I * (xMat.T * (weights * yMat))
	return testPoint * ws

def lwlrTest(testArr,xArr,yArr,k=1.0):
	m = shape(testArr)[0]
	yHat = zeros(m)
	for i in xrange(m):
	 	yHat[i] = lwlr(testArr[i],xArr,yArr,k)
	return yHat

def plotShow(xArr,yArr,yHat):
	ws =  standRegress(xArr,yArr)
	xMat = mat(xArr)
	yMat = mat(yArr)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0] , s=2, c='red')
	xCopy = xMat.copy()
	xCopy.sort(0)
	ax.plot(xCopy[:,1],yHat[xMat[:,1].argsort(0)])
	plt.show()
####################################################

def ridgeRegres(xMat,yMat,lam=0.2):
    xTx = xMat.T*xMat
    denom = xTx + eye(shape(xMat)[1])*lam
    if linalg.det(denom) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = denom.I * (xMat.T*yMat)
    return ws
    
def ridgeTest(xArr,yArr):
    xMat = mat(xArr); yMat=mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean     #to eliminate X0 take mean off of Y
    #regularize X's
    xMeans = mean(xMat,0)   #calc mean then subtract it off
    xVar = var(xMat,0)      #calc variance of Xi then divide by it
    xMat = (xMat - xMeans)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat,yMat,exp(i-10))
        wMat[i,:]=ws.T
    return wMat

if __name__== "__main__":
	abX,abY=loadDataSet('abalone.txt')
	ridgeWeights = ridgeTest(abX,abY)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(ridgeWeights)
	plt.show()
	
