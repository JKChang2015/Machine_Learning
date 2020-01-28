# KNN_advance
# Created by JKChang
# 28/01/2020, 10:56
# Tag:
# Description: Advance KNN

import operator

from numpy import *


def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]  # shape[0] stands for the number of rows

    # Step 1: calculate Euclidean distance
    diff = tile(newInput, (numSamples, 1)) - dataSet
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





def img2vector(filename):
    rows = 32
    cols = 32
    imgVector = zeros((1, rows * cols))
    fileIn = open(filename)
    for row in range(rows):
        lineStr = fileIn.readline()
        for col in range(cols):
            imgVector[0, row * 32 + col] = int(lineStr[col])

    return imgVector

filename = '../resource/digits/testDigits/0_0.txt'
res = img2vector(filename)
print(type(res))
print(res)
print()

# from numpy import loadtxt
# lines = loadtxt(filename, comments="#", delimiter=" ", unpack=False)
# print()

# def image2vector2(filename):
#     with open(filename, 'r') as f:
#         vector_list = []
#         for line in f.readlines():
#             vector_list += list(line.strip())
#         print(len(vector_list))
#
#     return asarray(vector_list)
#
# vector = image2vector2(filename)
# print(type(vector))
# print()
