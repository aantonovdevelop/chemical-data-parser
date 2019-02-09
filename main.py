import re
import os
import sys
import statistics
import mainwindow
import numpy as np
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
from scipy import interpolate


class Application(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnOpenDirectory.clicked.connect(self.browse_folder)

    def browse_folder(self):
        # noinspection PyCallByClass
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Chose directory")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()


main()


def normalize(y, min_y, max_y):
    return (2*(y - min_y) / (max_y - min_y)) - 1


data = []

with open("data/c13", "r") as data_file:
    for line in data_file:
        data.append(list(map(float, re.sub(" +", " ", line).split(" ")[2:])))

data_x = list(map(lambda v: v[0], data))
data_y = list(map(lambda v: v[1], data))

min_point = min(data, key=lambda v: v[1])
max_point = max(data, key=lambda v: v[1])

normalized_y = [normalize(y, min_point[1], max_point[1]) for y in data_y]

median = statistics.median(data_y)
median_normalized = statistics.median(normalized_y)

data_normalized = [[data_x[i], normalized_y[i]] for i in range(len(normalized_y))]

median_crosses = []
for i in range(len(data_normalized) - 1):
    if data_normalized[i][1] > 0.01 and -0.01 > data_normalized[i + 1][1]:
        median_crosses.append(data_normalized[i])
        median_crosses.append(data_normalized[i + 1])

# [plt.scatter(point[0], point[1]) for point in median_crosses]

f = interpolate.interp1d(data_x, normalized_y)

interpolated_data = [[x, f(x).tolist()] for x in data_x]
interpolated_x = list(map(lambda v: v[0], interpolated_data))
interpolated_y = list(map(lambda v: v[1], interpolated_data))

closest_to_median = []
for i in range(0, len(median_crosses), 2):
    points = []
    for x in np.arange(median_crosses[i][0], median_crosses[i + 1][0], 0.001):
        points.append([x, abs(f(x).tolist())])
    closest_to_median.append(min(points, key=lambda v: v[1]))

[plt.scatter(point[0], point[1]) for point in closest_to_median]

x_difference = 0
if len(closest_to_median) > 1:
    x_difference = closest_to_median[1][0] - closest_to_median[0][0]

print("Difference: ", x_difference)

# plt.plot(interpolated_x, interpolated_y)
plt.plot()

plt.plot(data_x, data_y, alpha=0.3)
plt.plot(data_x, [median] * len(data_x), alpha=0.3)
plt.plot(data_x, [median_normalized] * len(data_x))
plt.plot(data_x, normalized_y)

# plt.scatter(min_point[0], min_point[1])
# plt.scatter(max_point[0], max_point[1])

plt.show()

