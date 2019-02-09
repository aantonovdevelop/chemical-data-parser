import re
import os
import sys
import mainwindow
import chemical

from PyQt5 import QtWidgets


class Application(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.directory = None
        self.parse_objects = {}

        self.btnOpenDirectory.clicked.connect(self.browse_folder)
        self.btnExport.clicked.connect(self.export)
        self.lstFiles.itemClicked.connect(self.preview)

    def browse_folder(self):
        self.lstFiles.clear()

        # noinspection PyCallByClass
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Chose directory")

        if not self.directory:
            return

        files = [file for file in os.listdir(self.directory) if os.path.isfile(self.directory + "/" + file)]

        for file in files:
            data = []
            with open(self.directory + "/" + file, "r") as data_file:
                for line in data_file:
                    data.append(list(map(float, re.sub(" +", " ", line).split(" ")[2:])))
            self.parse_objects[file] = chemical.ChemicalDataParser(data)

            self.lstFiles.addItem(file)

        for parser in self.parse_objects.values():
            print(parser.difference)
            print(parser.normalized_data)

        self.btnExport.setEnabled(True)

    def preview(self, file_name_item):
        parser = self.parse_objects[file_name_item.text()]
        preview_string = "Difference: " + str(parser.difference) + "\n"

        for point in parser.normalized_data:
            preview_string += str(point[0]) + "\t" + str(point[1]) + "\n"

        self.txtResult.setText(preview_string)

    def export(self):
        # noinspection PyCallByClass
        export_directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Chose directory")

        for file_name in self.parse_objects.keys():
            parser = self.parse_objects[file_name]

            with open(export_directory + "/" + "differences.txt", "a+") as file:
                file.write(file_name + " " + str(parser.difference) + "\n")

            with open(export_directory + "/" + file_name + ".dat", "w") as file:
                for point in parser.normalized_data:
                    file.write(str(point[0]) + " " + str(point[1]) + "\n")

        QtWidgets.QMessageBox.information(self, "Export", "Data exported")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()


main()
