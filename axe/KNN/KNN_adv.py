# KNN_advance
# Created by JKChang
# 28/01/2020, 10:56
# Tag:
# Description: Advance KNN

import operator
import os

import numpy as np


def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]  # shape[0] stands for the number of rows

    # Step 1: calculate Euclidean distance
    diff = np.tile(newInput, (numSamples, 1)) - dataSet
    squareDiff = diff ** 2
    squareSum = squareDiff.sum(axis=1)
    distance = squareSum ** 0.5

    # Step 2: Sort distance
    # argsort() returns the indices that would sort an array in a ascending order
    sortedDistIndicies = distance.argsort()

    classCount = {}  # key: label , value: laebl count

    for i in range(k):
        # Step 3: choose the min k distance
        voteLabel = labels[sortedDistIndicies[i]]

        # Step 4: count the label frequency
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    # Step 5: the max voted class label will return
    # Sort the dictionary according to the values
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def image2vector(filename):
    with open(filename, 'r') as f:
        vector_list = []
        for line in f.readlines():
            vector_list += list(line.strip())
        vector_list = [[float(x) for x in vector_list]]
    return np.asarray(vector_list)


def loadDataSet(folderPath):
    print('--- Getting data set from', folderPath, '---')
    trainingFileList = os.listdir(folderPath)
    numSamples = len(trainingFileList)

    DataMatrix = np.zeros((1, 1024))
    labels = []

    for file in trainingFileList:
        num_vector = image2vector(folderPath + file)
        DataMatrix = np.r_[DataMatrix, num_vector]

        labels.append(file.strip('_')[0])

    DataMatrix = np.delete(DataMatrix, (0), axis=0)
    return DataMatrix, labels


def testData(folderPath, dataSet, labels, k):
    print('--- Testing data set from', folderPath, '---')
    testingFileList = os.listdir(folderPath)
    numSamples = len(testingFileList)

    matched_count = 0

    for file in testingFileList:
        vector = image2vector(folderPath + file)
        test_label = kNNClassify(vector, dataSet, labels, k)
        real_label = file.strip('_')[0]
        if test_label == real_label:
            matched_count += 1

    return matched_count / numSamples


training_folderPath = '../resource/digits/trainingDigits/'
testing_folderPath = '../resource/digits/testDigits/'
dataset, labels = loadDataSet(training_folderPath)

res = testData(testing_folderPath,dataset,labels, 3)
print('The classify accuracy is: %.2f%%' % (res * 100))