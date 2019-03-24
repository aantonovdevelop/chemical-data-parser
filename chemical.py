import statistics
import numpy as np
from scipy import interpolate


class ChemicalDataParser:
    @staticmethod
    def __normalize(y, min_y, max_y):
        return (2 * (y - min_y) / (max_y - min_y)) - 1

    def __init__(self, data: list, period: float = 0.005):
        self.data = data

        data_x = list(map(lambda v: v[0], data))
        data_y = list(map(lambda v: v[1], data))

        min_point = min(data, key=lambda v: v[1])
        max_point = max(data, key=lambda v: v[1])

        normalized_y = [ChemicalDataParser.__normalize(y, min_point[1], max_point[1]) for y in data_y]

        median = statistics.median(data_y)
        self.median_normalized = statistics.median(normalized_y)

        data_normalized = [[data_x[i], normalized_y[i]] for i in range(len(normalized_y))]

        median_crosses = []
        for i in range(len(data_normalized) - 1):
            if data_normalized[i][1] > period and -period > data_normalized[i + 1][1]:
                median_crosses.append(data_normalized[i])
                median_crosses.append(data_normalized[i + 1])

        f = interpolate.interp1d(data_x, normalized_y)

        interpolated_data = [[x, f(x).tolist()] for x in data_x]
        interpolated_x = list(map(lambda v: v[0], interpolated_data))
        interpolated_y = list(map(lambda v: v[1], interpolated_data))

        self.closest_to_median = []
        for i in range(0, len(median_crosses), 2):
            points = []
            for x in np.arange(median_crosses[i][0], median_crosses[i + 1][0], 0.001):
                points.append([x, abs(f(x).tolist())])
            self.closest_to_median.append(min(points, key=lambda v: v[1]))

        x_difference = 0
        if len(self.closest_to_median) > 1:
            x_difference = self.closest_to_median[1][0] - self.closest_to_median[0][0]

        self.difference = x_difference
        self.normalized_data = data_normalized
