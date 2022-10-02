import pandas as pd
import numpy as np
import sklearn
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split


class Modelo:

    def __init__(self, datos):
        self.datos = datos

    def convertirEjeX(self, columna):
        self.ejeX = columna
        return self.ejeX

    def getX(self):
        return self.ejeX

    def getY(self):
        return self.ejeY

    def convertirEjeY(self, columna):
        self.ejeY = columna
        return self.ejeY

    def entrenar(self, porcentaje):
        while True:
            self.X = self.ejeX[:, np.newaxis]
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.ejeY)
            self.mlr = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)
            self.mlr.fit(self.X_train, self.y_train)
            if self.mlr.score(self.X_train, self.y_train) >= porcentaje:
                return self.mlr.score(self.X_train, self.y_train)

    def predecir(self, id):
        nuevo = pd.DataFrame(np.array([id]), columns=["ID"])
        predecido = self.mlr.predict(nuevo)
        return predecido
