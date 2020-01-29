# KNN_dating
# Created by JKChang
# 29/01/2020, 10:20
# Tag:
# Description: dating people recommendation

# Feature: 1. Number of frequent flyer miles earned per year
#          2. Percentage of time spent playing video games
#          3. Liters of ice cream consumed per week

# classifies：1. doesn't like
#             2. small like
#             3. large like

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def file2matrix(filename):
    with open(filename, 'r') as f:
        resMatrix = np.zeros((1, 3))
        labels = []

        for line in f.readlines():
            content = line.split('\t')
            lineVector = np.asfarray([content[:3]])
            resMatrix = np.r_[resMatrix, lineVector]
            labels.append(int(content[-1]))

        DataMatrix = np.delete(resMatrix, (0), axis=0)
        return DataMatrix, labels

def autoNorm(dataSet):
    # normalization:
    # nor_value = (old_Value - minimum_value) / (max - min)
    # get list of minimum value for each col
    minValue = dataSet.min(0)
    # get list of maximum value for each col
    maxValue = dataSet.max(0)

    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    # copy the minValue to size(m,1) matrix
    normDataSet = dataSet - np.tile(minValue, (m, 1))
    normDataSet = normDataSet / np.tile(maxValue - minValue, (m, 1))
    return normDataSet, maxValue - minValue, minValue

def viewMatrix(matrix, labels, arg1, arg2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(matrix[:, arg1 - 1], matrix[:, arg2 - 1], 15.0 * np.array(labels), 15.0 * np.array(labels))
    plt.show()

def view3DMatrix(matrix, labels):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    zline = np.linspace(0, 1, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

    # Data for three-dimensional scattered points
    zdata = matrix[:,0]
    xdata = matrix[:,1]
    ydata = matrix[:,2]
    ax.scatter3D(xdata, ydata, zdata, c=labels)
    fig.show()

filename = '../resource/dating/datingTestSet2.txt'
matrix, labels = file2matrix(filename)
norm_matrix, ranges, min = autoNorm(matrix)
view3DMatrix(norm_matrix,labels)
