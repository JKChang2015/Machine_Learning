# example
# Created by JKChang
# 27/02/2018, 10:31
# Tag:
# Description: 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()
print(diabetes.items())