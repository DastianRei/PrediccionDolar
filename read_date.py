
YEAR = 1990
MONTH = 1
DAY = 1


class Entrada:
    def __init__(self, anio, mes, dia):
        self.anio = anio
        self.mes = mes
        self.dia = dia

    def converitr(self):
        cont = 0
        contBisiesto = 0
        for i in (YEAR, self.anio):
            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                contBisiesto += 1
        cont = (self.anio - YEAR) * 365 + (self.mes - MONTH) * 30 + (self.dia - DAY) + contBisiesto
        return cont

    def verificar(self):
        if self.anio <= 2030 and self.anio >= 1990:
            if self.mes >= 1 and self.mes <= 12:
                if self.dia >= 1 and self.dia <= 31:
                    return True
        return False
