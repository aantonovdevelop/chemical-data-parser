import os
import re


class DataFetcher:
    def __init__(self, directory):
        self.directory = directory

    def fetch(self):
        files = [file for file in os.listdir(self.directory) if os.path.isfile(self.directory + "/" + file)]

        data = []
        for file in files:
            file_data = []
            with open(self.directory + "/" + file, "r") as data_file:
                # skip first two lines
                next(data_file)
                next(data_file)

                for line in data_file:
                    file_data.append(list(map(float, re.sub(" +", " ", line).split(" ")[2:])))

            data.append(file_data)

        return data
