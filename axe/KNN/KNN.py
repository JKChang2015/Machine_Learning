# KNN
# Created by JKChang
# 27/01/2020, 15:53
# Tag:
# Description: 

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


def classify0(inX, deataSet, lables, k):
    pass


group, labels = createDataSet()
drawGraph(group, labels)
