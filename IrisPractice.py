import numpy as np
from sklearn import neighbors
from sklearn import datasets

#Load Data
#The class of each Iris observation is stored in the .target attribute
iris = datasets.load_iris()
allData = iris.data
allTarget = iris.target

# Data Division for each class of Iris
# Concatenate - Join a sequence of arrays along an existing axis.
# Note Using 80% of data as trainData 
# The first 50 is Iris Setosa,
# then the next 50 is Iris Versicolor, and the last 50 are Iris Virginica
# We get 80% of each 50 to use as Training data

# Train Data consists of records that have known class labels
# The Train data is used to build a classification model which is 
# subsequently applied to the test set.

trainData = np.concatenate((allData[:40, :], allData[50:90, :], allData[100:140, :]), axis = 0)
trainTarget = np.concatenate((allTarget[:40], allTarget[50:90], allTarget[100:140]), axis=0)

# Using the 20% as TestData
# Use the remaining 20% of each sets of 50 as testing data
# The test data is a set of records with unknown class labels.
# 40 - 50 are the first 10 features of the Iris Setosa Class
# 90 - 100 are the next 10 features that belongs to the Iris Versicolor
# 140 - 150 are the final 10 features that belong to the Iris Virginica

testData = np.concatenate((allData[40:50], allData[90:100], allData[140:150]), axis=0)

# 2 datapoints 
numOfNeighbors = 5
nn = neighbors.KNeighborsClassifier(numOfNeighbors)
nn.fit(trainData, trainTarget)

# The 10 datapoints are predicted into what class they belong in
# 0 - Iris Setosa
# 1 - Iris Versicolor
# 2 - Iris Virginica
# The 30 features are shown which class they belong to
decisions = nn.predict(testData)
print(decisions)
