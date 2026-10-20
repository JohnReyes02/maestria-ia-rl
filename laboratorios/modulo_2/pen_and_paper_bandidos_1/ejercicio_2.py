"""Respuesta de trabajo para el ejercicio 2 de la práctica de bandidos."""

EPSILON = 0.5
RECOMPENSAS = [18, 8, 16, 12]

# Jornada descrita en el enunciado. Confirma si ambos extremos son inclusivos.
HORAS = range(7, 21)

# Según el enunciado, cada segunda acción selecciona el camino con mayor valor
# estimado; las demás siguen la regla basada en la factorización de la hora.
# TODO: documentar cómo se inicializan los valores y cómo se resuelven empates.

# La plataforma espera una lista con el valor estimado de c1, c2, c3 y c4.
# TODO: calcular cada promedio a partir de las recompensas observadas.
arms = []
