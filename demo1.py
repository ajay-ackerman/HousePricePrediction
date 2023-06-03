import matplotlib as plt
import numpy as np
import sklearn as sk
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 
# 'data_filename', 'target_filename', 'data_module'])
# print(diabetes.keys()) # type: ignore
print(diabetes.data[:,np.newaxis,2]) # type: ignore 