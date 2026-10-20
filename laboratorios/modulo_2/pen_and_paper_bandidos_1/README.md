# Pen & Paper: Bandidos 1

## Propósito

Conservar y desarrollar de forma reproducible la práctica **Pen & Paper:
Bandidos 1** del módulo 2, sobre estimación de recompensas en un bandido de
cuatro brazos y selección de acciones con una estrategia epsilon.

Esta carpeta es una transcripción de trabajo basada en las capturas de la
plataforma. Antes de entregar, las respuestas deben comprobarse en la plataforma,
porque allí solo se muestran los resultados después del envío.

## Relación con aprendizaje por refuerzo

- **Agente:** el transportador que elige un camino.
- **Entorno:** los cuatro caminos entre New Malia y Rose Hills.
- **Estado o contexto:** la hora del viaje, de 7 a 20.
- **Acciones:** escoger `c1`, `c2`, `c3` o `c4`.
- **Recompensa base:** 18, 8, 16 y 12, respectivamente.
- **Dinámica:** si la hora es múltiplo de 4, el puente del camino elegido está
  cerrado y la recompensa observada es 0.
- **Valor de acción:** promedio de las recompensas observadas al seleccionar cada
  camino.
- **Política:** en el primer ejercicio la acción depende de la factorización de
  la hora; en el segundo se combina esa regla con una estrategia epsilon.

## Fórmula de estimación

Para una acción `a`, el valor estimado es el promedio muestral de las recompensas
recibidas las veces que se escogió esa acción:

$$
Q_t(a) =
\frac{\sum_{i=1}^{t-1} r_i \mathbb{1}_{a_i=a}}
     {\sum_{i=1}^{t-1} \mathbb{1}_{a_i=a}}.
$$

La misma estimación puede actualizarse de manera incremental:

$$
Q_{n+1} = Q_n + \frac{1}{n}(r_n-Q_n).
$$

## Ejercicio 1: selección mediante factores primos

Se realiza un viaje por hora entre las 7:00 y las 20:00. La cantidad de factores
de la descomposición prima de la hora determina el camino. Los factores se cuentan
con multiplicidad; por ejemplo, `8 = 2 × 2 × 2`, por lo que se escoge `c3`.

Se debe calcular el valor estimado de recompensa de cada camino a partir de las
recompensas realmente observadas. La respuesta que solicita la plataforma es una
lista de Python llamada `arms`, indexada desde cero y con máximo dos decimales.

Archivo de trabajo: [`ejercicio_1.py`](ejercicio_1.py).

## Ejercicio 2: estrategia epsilon

Se conserva el escenario anterior y se usa `epsilon = 0.5`. Según el enunciado,
cada segunda acción elige el camino con mayor valor estimado; las demás acciones
siguen la regla de selección basada en la cantidad de factores primos de la hora.

Se debe volver a estimar el valor de recompensa de cada camino. La plataforma
también espera una lista de Python llamada `arms`, indexada desde cero y con
máximo dos decimales.

Archivo de trabajo: [`ejercicio_2.py`](ejercicio_2.py).

## Comprobaciones antes de responder

1. Aclarar si el intervalo incluye tanto las 7:00 como las 20:00.
2. Escribir la factorización prima de cada hora y contar factores con
   multiplicidad.
3. Registrar para cada viaje la hora, el camino y la recompensa observada.
4. Separar las recompensas por camino y calcular su promedio muestral.
5. Definir qué ocurre si varias acciones empatan como máximo en el ejercicio 2.
6. Redondear únicamente el resultado final a un máximo de dos decimales.

## Estado

- [x] Enunciado conservado en el repositorio.
- [x] Archivos de respuesta preparados.
- [ ] Convenciones ambiguas confirmadas en la plataforma o con el docente.
- [ ] Ejercicio 1 resuelto y razonado por el estudiante.
- [ ] Ejercicio 2 resuelto y razonado por el estudiante.
- [ ] Respuestas enviadas y resultados comprobados en la plataforma.
