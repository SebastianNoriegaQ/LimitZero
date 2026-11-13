# LimitZero
Este proyecto tiene como propósito servir como guía de estudio y/o repaso de Cálculo 1, sobre todo para la práctica de  diferenciación de funciones. Puede ser útil tanto para estudiantes que recién hayan empezado la materia como para estudiantes avanzados.
El objetivo es generar funciones aleatorias que tengan distintos grados de dificultad y el usuario encuentre la derivada de cada una, para después compararla con el resultado del programa y regresar el total de aciertos. 
Creo que puede ser muy útil para estudiantes nuevos de cálculo 1 que necesiten practicar sus derivadas o para estudiantes avanzados que quieran reforzar sus conocimientos. 

# Requisitos
Es importante tener instaladas las bibliotecas de NumPy y SymPy para que pueda funcionar correctamente la diferenciación de funciones.

# Algoritmo
E0(nivel de dificultad, cantidad de ejercicios, resultado)

dificultad = [1, 2, 3...]

templates_funciones = [ax^n ± bx^m + c, alog(bx^n±c), asin(x^n), etc]

seleccionar un grado de dificultad, randomizar los valores de las funciones que serán generadas (a, b, c, n, m)

desplegar las funciones y esperar el resultado del usuario

comparar el resultado con la derivada calculada por el programa (sp.diff(funcion, x))

desplegar la cantidad y porcentaje de aciertos 
