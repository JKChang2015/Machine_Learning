# KNN
# Created by JKChang
# 27/01/2020, 15:53
# Tag:
# Description: 

import operator

import matplotlib.pyplot as plt
from numpy import *


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def drawGraph(group, labels):
    for i, label in enumerate(labels):
        x = group[i][0]
        y = group[i][1]
        plt.scatter(x, y, marker='x', color='red')
        plt.text(x + 0.01, y + 0.01, label, fontsize=9)
    plt.show()


def classify(newInput, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    ## step 1: calculate Euclidean distance
    # tile(A, reps): Construct an array by repeating A reps times
    # the following copy numSamples rows for dataSet
    diffMat = tile(newInput, (dataSetSize, 1))- dataSet # Subtract element-wise
    sqDiffMat = diffMat ** 2  # squared for the subtract
    sqDistances = sqDiffMat.sum(axis=1) # sum is performed by row
    distances = sqDistances ** 0.5

    ## step 2: sort the distance
    # argsort() returns the indices that would sort an array in a ascending order
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        ## step 3: choose the min k distance
        voteIlabel = labels[sortedDistIndicies[i]]
        ## step 4: count the times labels occur
        # when the key voteLabel is not in dictionary classCount, get() will return 0
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    ## step 5: the max voted class will return
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


group, labels = createDataSet()
drawGraph(group, labels)
print(classify([0.5, 0.5], group, labels, 2))
