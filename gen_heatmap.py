import matplotlib.pyplot as plt
import seaborn
from sklearn import preprocessing

def gen_heatmap(data, title):
  plot = seaborn.heatmap(preprocessing.normalize(data))
  fig = plot.get_figure()
  fig.savefig(title)

if '__name__' == '__main__':
  gen_heatmap([[0, 1, 2, 3, 4, 5],[1, 2, 3, 1, 1, 1]])
