__author__ = 'yutongpang'
from EBICanalysis.rawfileprocess import Rawfilearray
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

filearray = Rawfilearray('../EBIC_measurement/raw.dat', 'little')
filematrix = filearray.get_file_data_in_reshape_matrix(300, 300, 0)

fig = plt.figure(figsize=(6, 3.2))
ax = fig.add_subplot(111)
plt.imshow(filematrix)
plt.show()