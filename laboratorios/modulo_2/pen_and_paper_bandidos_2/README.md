# Pen & Paper: Bandidos 2

## Propósito

Conservar y desarrollar de forma reproducible la segunda práctica de bandidos
del módulo 2. El ejercicio trabaja con recompensas no estacionarias y actualiza
las estimaciones mediante un tamaño de paso constante.

Esta carpeta es una transcripción de trabajo basada en las capturas de la
plataforma. El resultado de la ejecución solo se muestra después del envío, por
lo que la respuesta debe razonarse y comprobarse antes de entregarla.

## Relación con aprendizaje por refuerzo

- **Agente:** el sistema que recomienda películas.
- **Entorno:** los 20 clientes de una plataforma de alquiler.
- **Acciones o brazos:** recomendar `p1`, `p2`, `p3` o `p4`.
- **Recompensa:** el pago obtenido después de una recomendación.
- **Valor inicial:** las cuatro películas comienzan con una estimación de 10.
- **Dinámica:** la recompensa cambia según el cliente, la película recomendada
  y si al cliente le gusta o no.
- **Estimación:** cada película mantiene su propio valor y se actualiza solamente
  cuando es recomendada.

## Actualización con tamaño de paso constante

El enunciado presenta la forma expandida de la actualización:

$$
Q_{n+1} = (1-\alpha)^n Q_1
          + \sum_{i=1}^{n} \alpha(1-\alpha)^{n-i}r_i.
$$

Para desarrollar el ejercicio puede aplicarse de forma incremental, después de
cada recompensa observada para la película seleccionada:

$$
Q_{n+1} = Q_n + \alpha(r_n-Q_n),
$$

con `alpha = 0.1`.

## Escenario

Se recomiendan cuatro películas a 20 clientes. Todas las estimaciones comienzan
en 10. Los clientes `1, 3, 4, 11, 12, 13 y 18` no disfrutarán la película y su
recompensa será 0. Los demás clientes pagarán el valor de la película más una
propina.

La propina indicada por el enunciado es:

```text
min(número de cliente × número de película / 2, 5)
```

La interpretación directa es que, cuando la película gusta, la recompensa es
`10 + propina`; conviene comprobar esta interpretación con los ejemplos o la
retroalimentación de la plataforma antes del envío definitivo.

El orden de recomendaciones para los clientes 1 a 20 es:

```python
[4, 2, 3, 3, 3, 1, 4, 2, 1, 2, 3, 3, 2, 2, 3, 4, 4, 4, 3, 1]
```

## Respuesta solicitada

La plataforma espera una lista de Python llamada `movies` con las estimaciones
finales de `p1`, `p2`, `p3` y `p4`, en ese orden y con máximo dos decimales.

Archivo de trabajo: [`ejercicio_1.py`](ejercicio_1.py).

## Comprobaciones antes de responder

1. Numerar los clientes desde 1, no desde 0.
2. Confirmar que la lista contiene exactamente 20 recomendaciones.
3. Asignar recompensa 0 a los siete clientes indicados.
4. Para los demás, calcular la propina usando el número de película recomendado.
5. Actualizar únicamente el valor de la película recomendada en cada paso.
6. Mantener precisión completa durante las actualizaciones y redondear solo los
   cuatro resultados finales.

## Estado

- [x] Enunciado conservado en el repositorio.
- [x] Archivo de respuesta preparado.
- [ ] Interpretación exacta de la recompensa confirmada.
- [ ] Tabla cliente–película–recompensa construida por el estudiante.
- [ ] Actualizaciones calculadas y razonadas por el estudiante.
- [ ] Respuesta enviada y resultado comprobado en la plataforma.
