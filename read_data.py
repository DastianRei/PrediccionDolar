import pandas as pd

class Data:

    def __init__(self, ruta):
        self.data = pd.read_csv(ruta)

    def delete_null(self):
        self.data = self.data.dropna(how='any')

    def delete_columns(self):
        self.data = self.data.drop(columns=["DATE"])

    def display(self):
        print(self.data)

    def return_column(self, columna):
        return self.data[columna]
