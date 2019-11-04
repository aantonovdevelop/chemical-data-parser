import data_fetcher as df
import chemical

from scipy import stats
import matplotlib.pyplot as plt


class RawView:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def plot(x, y):
        plt.plot(x, y)
        plt.plot([x[0], x[-1]],  [0, 0])

        # plt.show()


data_fetcher = df.DataFetcher("/home/aantonov/Source/Python/chem-data-parser/data")

result = data_fetcher.fetch()

for row in result[0]:
    print(row)

# RawView.plot([point[0] for point in result[0]], [point[1] for point in result[0]])
parsed = chemical.ChemicalDataParser(result[0])

RawView.plot(parsed.interpolated_x, parsed.interpolated_y)

data_x = [point[0] for point in result[0]]
data_y = [point[1] for point in result[1]]

rectangles = []
for s_x in range(0, len(data_x), 1):
    a1 = (data_x[s_x], 0)
    a2 = (data_x[s_x], data_y[s_x])
    a3 = (data_x[s_x] + 0.05, data_y[s_x])

    plt.plot([a1[0], a2[0], a3[0]], [a1[1], a2[1], a3[1]])

    # rectangles.append([(data_x[s_x], data_y[s_x]), (data_x[s_x] + 2, 0)])

plt.show()
