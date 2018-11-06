import matplotlib.pyplot as pt
from sklearn import datasets
import sklearn.metrics as sm
import pandas as pd
import math
import numpy as np
#load csv file 
train = pd.read_csv('iris.csv')
x=pd.DataFrame(train)
x.columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width','targets']
target=[]
for index, row in x.iterrows():
  
	if row['targets']=='Iris-setosa':
		target.append(0)
	elif row['targets']=='Iris-versicolor':
		target.append(1)
	elif row['targets']=='Iris-virginica':
		target.append(2)
	
targets=np.array(target)

#KMeans Algorithm
np.random.seed(500)
k = 3
i=0
centroidX=[]
centroidY=[]
for i in range(k):
	 centroidX.append(np.random.randint(0,8))
	 centroidY.append(np.random.randint(0,8))

random = pd.DataFrame({
    'x': centroidX,
    'y': centroidY
})
store=[]
storeAX=[]
storeAY=[]
storeBX=[]
storeBY=[]
storeCX=[]
storeCY=[]
def iris(random,x):
	for i in range(3):
		clusterA=[]
		clusterAX=[]
		clusterAY=[]
		clusterB=[]
		clusterBX=[]
		clusterBY=[]
		clusterC=[]
		clusterCX=[]
		clusterCY=[]
		position=[]
		for index, row in x.iterrows():
			dist=[]
			length=[]
			width=[]
			for i in range(k):
				x_axis_var=row['petal_length']-centroidX[i]
				y_axis_var=row['petal_width']-centroidY[i]
				euclX=math.pow(x_axis_var,2)
				euclY=math.pow(y_axis_var,2)
				eucld=euclX+euclY
				sqr=math.sqrt(eucld)
				dist.append(sqr)
				darr = np.array(dist)
				length.append(row['petal_length'])
				width.append(row['petal_width'])
				darr = np.array(dist)
			
			mini=min(darr)
			minpos = dist.index(mini)
			position.append(minpos)
			
			if minpos==0:
				clusterA.append(mini)
				clusterAX.append(length[minpos])
				clusterAY.append(width[minpos])
				
			elif minpos==1:
				clusterB.append(mini)
				clusterBX.append(length[minpos])
				clusterBY.append(width[minpos])
				
			elif minpos==2:
				clusterC.append(mini)
				clusterCX.append(length[minpos])
				clusterCY.append(width[minpos])
			
		try:
			avgA=sum(clusterA)/len(clusterA)
			avgAX=sum(clusterAX)/len(clusterAX)
			avgAY=sum(clusterAY)/len(clusterAY)
		except ZeroDivisionError as err:
			avgAX=0
			avgAY=0
			avgA=0
		try:
			avgB=sum(clusterB)/len(clusterB)
			avgBX=sum(clusterBX)/len(clusterBX)
			avgBY=sum(clusterBY)/len(clusterBY)
		except ZeroDivisionError as err:
			avgBX=0
			avgBY=0
			avgB=0
		try:
			avgC=sum(clusterC)/len(clusterC)
			avgCX=sum(clusterCX)/len(clusterCX)
			avgCY=sum(clusterCY)/len(clusterCY)
		except ZeroDivisionError as err:
			avgCX=0
			avgCY=0
			avgC=0
		storeAX.append(avgAX)
		storeAY.append(avgAX)

		storeBX.append(avgBX)
		storeBY.append(avgBY)

		storeCX.append(avgCX)
		storeCY.append(avgCY)	
		centroidX[0]=avgAX
		centroidY[0]=avgAY
		centroidX[1]=avgBX
		centroidY[1]=avgBY
		centroidX[2]=avgCX
		centroidY[2]=avgCY
		random = pd.DataFrame({

			'x': centroidX,
			'y': centroidY
			})
		color=np.array(['red','green','yellow'])
		pt.scatter(x.petal_length,x.petal_width,c=color[position],s=50)
		pt.show()
		pp=round((avgA+avgB+avgC),3)
		
		return pp
		
		
			
			
			
	
for i in range(20):
	
	pp=iris(random,x)
	
	if pp in store:
		
		samepos = store.index(pp)
		pos=samepos-1	
		centroidX[0]=storeAX[pos]
		centroidY[0]=storeAY[pos]
		centroidX[1]=storeBX[pos]
		centroidY[1]=storeBY[pos]
		centroidX[2]=storeCX[pos]
		centroidY[2]=storeCY[pos]
		random = pd.DataFrame({

			'x': centroidX,
			'y': centroidY
			})
		print(random)
		iris(random,x)	
		break	
		
	else:
		store.append(pp)
		print('false')