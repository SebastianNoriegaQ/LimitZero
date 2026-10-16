import math
import random


# variable para guardar aciertos
aciertos = 0

# inicializar LimitZero

bandera = str(input("Bienvenido a LimitZero, ¿Deseas practicar? (s/n)"))

while bandera != "s" and bandera != "n":
    print("Entrada inválida, intenta de nuevo")
    bandera = str(input("Bienvenido a LimitZero, ¿Deseas practicar? (s/n)"))


# definir el template de las funciones

def select_trig():
    """
    (uso de funciones, uso de listas)
    devuelve: funcion trigonometrica
    """
    opciones_trig = ["sin", "cos", "tan", "cot", "sec", "csc"]
    trig_num = random.randint(0, 5)
    trig = opciones_trig[trig_num]
    return trig


def generar_coeficientes():
    a = random.randint(-9, 9)
    b = random.randint(-9, 9)
    c = random.randint(-9, 9)
    return a, b, c

def generar_exponentes():
    m = random.randint(1, 9)
    n = random.randint(1, 9)
    return m, n


def generar_funcion_polinomial():
    a, b, c = generar_coeficientes()
    m, n = generar_exponentes()
    fun1 = f"{a}x^{m} + {b}x^{n} + {c}"
    return fun1


def generar_funcion_producto():
    a, b, c = generar_coeficientes()
    m, n = generar_exponentes()
    fun2 = f"({a}x^{m}) * ({b}x^{n})"
    return fun2


def generar_funcion_cociente():
    a, b, c = generar_coeficientes()
    m, n = generar_exponentes()
    fun3 = f"({a}x^{m}) / ({b}x^{n})"
    return fun3


def generar_funcion_trig1():
    a, b, c = generar_coeficientes()
    trig = select_trig()
    fun4 = f"{a}{trig}(x) + {c}"
    return fun4


def generar_funcion_trig2():
    a, b, c = generar_coeficientes()
    m, n = generar_exponentes()
    trig = select_trig()
    fun5 = f"{a}{trig}(x^{m} + {b}x^{n}) + {c}"
    return fun5


def calcular_aciertos(num_aciertos):
    return num_aciertos / 5


def seleccionar_pool(nivel_dificultad):
    """
    (uso de estrucutras de decisión, uso de funciones)
    devuelve: funcion a utilizar
    """
    if nivel_dificultad == 1:
        fun1 = generar_funcion_polinomial()
    elif nivel_dificultad == 2:
        fun1 = generar_funcion_cociente()
    elif nivel_dificultad == 3:
        fun1 = generar_funcion_trig1()
    return fun1


def lista_ejercicios(lista, cantidad, dificultad):
    """
    (uso de estrucutras de repetición, uso de listas)
    devuelve: lista con las funciones seleccionadas
    """
    i = 0
    while i < cantidad:
        lista.append(seleccionar_pool(dificultad))
        i = i + 1
    return lista


# codigo principal

while bandera == "s":
    funciones = []
    # variable de dificultad
    dificultad = int(input("¿Qué grado de dificultad quieres practicar? (1-3)"))

    while dificultad < 1 or dificultad > 3:
        print("Grado de dificultad fuera del rango")
        dificultad = int(input("¿Qué grado de dificultad quieres practicar? (1-3)"))

    qty = int(input("¿Cuántos ejercicios quieres practicar?"))

    print(lista_ejercicios(funciones, qty, dificultad))

    bandera = str(input("¿Quieres seguir practicando? (s/n)"))
    while bandera != "s" and bandera != "n":
        print("Entrada inválida, intenta de nuevo")
        bandera = str(input("¿Quieres seguir practicando? (s/n)"))
