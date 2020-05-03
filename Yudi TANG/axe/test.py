# test
# Created by JKChang
# 27/01/2020, 15:58
# Tag:
# Description: 

from numpy import *
import operator
from os import listdir
import matplotlib.pyplot as plt



# simulating a pandas df['type'] column
types = ['apple', 'orange', 'apple', 'pear', 'apple', 'orange', 'apple', 'pear']
x_coords = [10, 10, 5, 4, 3, 20, 19, 21]
y_coords = [21, 23, 12, 21, 10, 20, 14, 2]

for i, type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='x', color='red')
    plt.text(x + 0.3, y + 0.3, type, fontsize=9)
plt.show()


# group, labels = createDataSet()
#
# for column,label in zip(group,labels):
#     plt.plot(group , label=label)
#
# plt.legend()
# plt.show()

# arr = np.random.random((10, 5))
# ax.plot(arr)
#
# labels = ['a', 'b', 'c', 'd', 'e']
#
# for column, label in zip(arr.T, labels):
#     ax.plot(column, label=label)