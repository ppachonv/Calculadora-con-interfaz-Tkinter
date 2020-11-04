import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *


def init_window():
    window = tk.Tk()
    window.title("Mi primera aplicacion")
    window.geometry('400x250')

    etiqueta = tk.Label(window, text='Calculadora', font=('Impact', 20))
    etiqueta.grid(column=0, row=0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    etiqueta_entrada1 = tk.Label(window, text='Ingrese primer numero:', font=('Impact', 15))
    etiqueta_entrada1.grid(column=0, row=1)

    etiqueta_entrada2 = tk.Label(window, text='Ingrese segundo numero:', font=('Impact', 15))
    etiqueta_entrada2.grid(column=0, row=2)

    etiqueta_operador = tk.Label(window, text='Escoja un operador', font=('Impact', 12))
    etiqueta_operador.grid(column=0, row=3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    etiqueta_resultado = tk.Label(window, text='Resultado: ', font=('Impact', 15))
    etiqueta_resultado.grid(column=0, row=5)

    boton = tk.Button(window, command=lambda: click_calcular(etiqueta_resultado, entrada1.get(), entrada2.get(),combo_operadores.get()), text='Calcular', bg='purple',fg='white')
    boton.grid(column=1, row=4)

    botonopciones = tk.Button(window, command=lambda: nuevaventana(), text='Mas opciones ;)', bg='blue', fg='white')
    botonopciones.grid(column=1, row=9)

    botonpreguntas = tk.Button(window, command=lambda: preguntas(), text='Problemas?', bg='green', fg='white')
    botonpreguntas.grid(column=0, row=10)

    def preguntas():
        res = messagebox.showwarning('Preguntas', 'Si el programa no corre intenta reiniciarlo,\npuede que hayas ingresado valores que generar error en la consola\n¿Ya lo has intentado?')

        res = messagebox.showinfo('Preguntas', 'Espero que te haya servido la informacion')


    def nuevaventana():
        window = tk.Tk()
        window.title("Opciones extra ;)")
        window.geometry('400x250')

        etiqueta = tk.Label(window, text='Calculadora de raices', font=('Impact', 20))
        etiqueta.grid(column=0, row=0)

        entrada1 = tk.Entry(window, width=10)

        entrada1.grid(column=1, row=1)

        etiqueta_entrada1 = tk.Label(window, text='Ingrese numero:', font=('Impact', 15))
        etiqueta_entrada1.grid(column=0, row=1)

        etiqueta_operador = tk.Label(window, text='Raiz', font=('Impact', 15))
        etiqueta_operador.grid(column=0, row=3)

        etiqueta_resultado = tk.Label(window, text='Resultado: ', font=('Impact', 15))
        etiqueta_resultado.grid(column=0, row=5)

        boton = tk.Button(window, command=lambda: click_calcular_raiz(etiqueta_resultado, entrada1.get()), text='Calcular raiz', bg='purple', fg='white')
        boton.grid(column=1, row=4)

    window.mainloop()


def calculadora(n, n2, operador):
    if operador == '+':
        resultado = n + n2
    elif operador == '-':
        resultado = n - n2
    elif operador == '*':
        resultado = n * n2
    elif operador == '/':
        if n2 == 0:
            messagebox.showerror("Error!!!!!!!!!!, DIVISION ENTRE CERO", ZeroDivisionError)
        resultado = round(n / n2, 2)
    else:
        resultado = n ** n2

    return resultado


def click_calcular(etiqueta, num, num2, operador):
    valor = float(num)
    valor2 = float(num2)

    res = calculadora(valor, valor2, operador)

    etiqueta.configure(text='Resultado: ' + str(res))


def click_calcular_raiz(etiqueta, num):
    import math
    valor = float(num)
    res = math.sqrt(valor)

    etiqueta.configure(text='Resultado: ' + str(res))


def main():
    init_window()


main()
