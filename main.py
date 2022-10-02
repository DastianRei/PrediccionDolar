from asyncio import DatagramProtocol
from turtle import bgcolor, color
import pandas
from sklearn.metrics import precision_recall_curve
from read_data import Data
from machine_learning_model import Modelo
from read_date import Entrada
import matplotlib.pyplot as plt
from tkinter import *
import math as mat

PORCENTAJE = 0.95


def truncate(numero, cifras):
    posiciones = pow(10.0, cifras)
    return mat.trunc(posiciones * numero) / posiciones


def leerDatos():
    dato = Data("D:\precio.csv")
    dato.delete_null()
    dato.delete_columns()
    return dato


def ingresarFecha():
    anio = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el dia: "))
    return (anio, mes, dia)


def convertirEjes():
    id = leerDatos().return_column("ID")
    precio = leerDatos().return_column("BUY")
    return (id, precio)


def crearModelo():
    modelo = Modelo(leerDatos())
    (id, precio) = convertirEjes()
    X = modelo.convertirEjeX(id)
    Y = modelo.convertirEjeY(precio)
    return modelo


def entrenarModelo(porcentaje):
    modelo = crearModelo()
    modelo.entrenar(float(porcentaje))
    return modelo


def graficar():
    modelo = crearModelo()
    plt.cla()
    X = modelo.getX()
    Y = modelo.getY()
    datos = Data('D:/Predecido.csv')
    datos.delete_null()
    X1 = datos.return_column("ID")
    Y1 = datos.return_column("PRECIO")
    dato1 = Data('D:/Antecedente.csv')
    dato1.delete_null()
    X2 = dato1.return_column("ID")
    Y2 = dato1.return_column("PRECIO")
    plt.plot(Y1, X1, color="green")
    plt.plot(Y2, X2, color="orange")
    plt.plot(Y, X, color='red')
    plt.xlabel('PRECIO')
    try:
        plt.plot(PREDECIDO, ID, marker="o", color="blue")
    except:
        pass
    plt.ylabel('TIEMPO')
    plt.title('Verde = PREDECIDO \n Rojo = DATOS REALES \n Naranja = PREDECIDO COMPARACION')
    plt.show()


def graficarPredecir():
    plt.cla()
    datos = Data('D:/grafica.csv')
    datos.delete_null()
    X = datos.return_column("ID")
    Y = datos.return_column("PRECIO")
    Y1 = datos.return_column("PRECIO ANT")
    plt.plot(Y, X, color="green")
    plt.plot(Y1, X, color="orange")
    plt.xlabel('PRECIO')
    try:
        plt.plot(PREDECIDO, ID, marker="o", color="blue")
    except:
        pass
    plt.ylabel('TIEMPO')
    plt.title('Verde = DATOS PREDECIDO \n Naranja = PREDECIDO COMPARACION')
    plt.show()


def historiagrama():
    modelo = crearModelo()
    plt.cla()
    Y = modelo.getY()
    plt.title('Verde = PREDECIDO \n Rojo = DATOS REALES \n Naranja = PREDECIDO COMPARACION')
    datos = Data('D:/Predecido.csv')
    datos.delete_null()
    dato1 = Data('D:/Antecedente.csv')
    dato1.delete_null()
    Y2 = dato1.return_column("PRECIO")
    Y1 = datos.return_column("PRECIO")
    plt.hist(Y, bins=20, color='red')
    plt.hist(Y1, bins=20, color='green')
    plt.hist(Y2, bins=20, color='orange')
    plt.xlabel('Precio del Dolar')
    plt.ylabel('Frecuencia del precio')
    plt.show()


def historiagramaPredecido():
    plt.cla()
    plt.title('Verde = PREDECIDO \n Naranja = PREDECIDO COMPARACION')
    datos = Data('D:/grafica.csv')
    datos.delete_null()
    Y2 = datos.return_column("PRECIO")
    Y1 = datos.return_column("PRECIO ANT")
    plt.hist(Y1, bins=20, color='green')
    plt.hist(Y2, bins=20, color='orange')
    plt.xlabel('Precio del Dolar')
    plt.ylabel('Frecuencia del precio')
    plt.show()


def predecir():
    (anio, mes, dia) = convertir()
    ent = Entrada(anio, mes, dia)
    global ID
    global PREDECIDO
    ID = ent.converitr()
    if ent.verificar() == True:
        answer.config(text=f"La fecha es valida")
        answer.grid(column=4, row=8, columnspan=3)
        dolar = float(entrenarModelo(PORCENTAJE).predecir(ent.converitr()))
        msg = truncate(dolar, 2)
        PREDECIDO = msg
        answer.config(text=f"El precio del dolar en {mes}/{dia}/{anio} podria ser: {msg}")
        answer.grid(column=4, row=9, columnspan=3)
        ans = Label()
        ans.config(text="Nota: Es una estimacion no un valor exacto")
        ans.grid(column=4, row=10, columnspan=3)
    else:
        answer.config(text=f"Escriba una fecha valida")
        answer.grid(column=4, row=8, columnspan=3)


def predecirCincuenta():
    f = open('datosPred.txt', 'w')
    for i in range(11324, 14611):
        dolar = float(entrenarModelo(PORCENTAJE).predecir(i))
        msg = truncate(dolar, 2)
        f.write(f"{msg}\n")
    f.close()


def crearVentana():
    window = Tk()
    window.title("PREDICCION DEL DOLAR")
    # window.minsize(width=750, height=750)
    return window


def labels():
    anio_label = Label(text="Año")
    anio_label.grid(column=2, row=0)
    mes_label = Label(text="Mes")
    mes_label.grid(column=2, row=3)
    dia_label = Label(text="Dia")
    dia_label.grid(column=2, row=6)


def inputs():
    anio_input = Entry(width=7)
    anio_input.grid(column=4, row=0)
    mes_input = Entry(width=7)
    mes_input.grid(column=4, row=3)
    dia_input = Entry(width=7)
    dia_input.grid(column=4, row=6)
    return (anio_input, mes_input, dia_input)


def get_value(entryWidget):
    value = entryWidget.get()
    try:
        return int(value)
    except ValueError:
        return None


def convertir():
    anio = get_value(anio_input)
    mes = get_value(mes_input)
    dia = get_value(dia_input)
    return (anio, mes, dia)


window = Tk()
window.title("PREDICCION DEL DOLAR")
window.minsize(width=350, height=150)
anio_label = Label(text="Año")
anio_label.grid(column=2, row=0)
mes_label = Label(text="Mes")
mes_label.grid(column=2, row=3)
dia_label = Label(text="Dia")
dia_label.grid(column=2, row=6)
anio_input = Entry(window, width=7)
anio_input.grid(column=4, row=0)
mes_input = Entry(window, width=7)
mes_input.grid(column=4, row=3)
dia_input = Entry(window, width=7)
dia_input.grid(column=4, row=6)
boton = Button(text="Graficar", command=graficar)
boton.grid(column=5, row=0)
boton = Button(text="GraficarPredecido", command=graficarPredecir)
boton.grid(column=7, row=0)
boton = Button(text="HistoriagramaPredecido", command=historiagramaPredecido)
boton.grid(column=8, row=0)
boton1 = Button(text="Predecir", command=predecir)
boton1.grid(column=6, row=5, rowspan=2, columnspan=2)
botonHistoriagrama = Button(text="Historiagrama", command=historiagrama)
botonHistoriagrama.grid(column=6, row=0)
answer = Label(text=' ')
answer.grid(column=5, row=3)
window.mainloop()
