# Uso de agentes de aprendizaje por refuerzo: Pacman

## Información de la actividad

- **Módulo:** 1 — Introducción al aprendizaje por refuerzo.
- **Actividad:** Uso de agentes de aprendizaje por refuerzo.
- **Tipo:** Tarea calificable.
- **Peso:** 1 % de la calificación del curso.
- **Fecha límite registrada:** 20 de octubre de 2026 a las 23:59 (`-05`).

> Este archivo reúne la información suministrada en la plataforma. Antes de entregar, se debe comprobar en la plataforma si hubo cambios en la fecha, el formato o los criterios de evaluación.

## Introducción

Ahora que conocemos las bases de los agentes de aprendizaje por refuerzo y sus diferentes componentes, exploraremos su potencial en uno de los ejemplos clásicos del área: los juegos de Atari y, en particular, Pacman.

## Material suministrado

La actividad utiliza la implementación de Pacman de Berkeley para explorar algoritmos de aprendizaje por refuerzo.

- ZIP original conservado localmente: `originales/AI-Pacman-Projects.zip`.
- SHA-256 verificado: `732b04353cee41f0d0c624993befc5945ae5afa9a5ad04fdb19d80da9ae8a1cb`.
- Copia de trabajo: `pacman/AI-Pacman-Projects-master/`.
- Carpeta que se debe utilizar: `pacman/AI-Pacman-Projects-master/Reinforcement/`.

El ZIP local fue comparado con el enlace directo temporal de la plataforma y ambos resultaron idénticos. La URL firmada no se conserva aquí porque expira. La plataforma también muestra un enlace de Google Drive, pero el enlace copiado no permitió descargar el archivo.

## Preparación local

La plataforma indica que se necesita Tkinter. En este repositorio se verificó que el Python administrado por `uv` ya incluye Tkinter 9.0, por lo que no se necesita instalar `tk` con `pip` en este equipo.

Desde la raíz del repositorio, entrar a la carpeta del ejercicio:

```bash
cd laboratorios/modulo_1/pacman/AI-Pacman-Projects-master/Reinforcement
```

Todas las ejecuciones de Python deben hacerse mediante `uv run`.

## Comando proporcionado

```bash
uv run python pacman.py \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.1,alpha=0.3,gamma=0.7
```

### Significado de las opciones

- `-p PacmanQAgent`: utiliza el agente de Q-learning para Pacman.
- `-x 2000`: ejecuta 2000 episodios de entrenamiento.
- `-n 2010`: ejecuta 2010 episodios en total; después del entrenamiento quedan 10 partidas de evaluación.
- `-l smallGrid`: utiliza el tablero `smallGrid`. La plataforma menciona también `mediumGrid` y `mediumClassic`.
- `epsilon`: probabilidad de exploración durante el entrenamiento. Con `epsilon=0.1`, el agente elige una acción exploratoria aproximadamente el 10 % de las veces.
- `alpha`: tasa de aprendizaje; controla cuánto influye la información nueva en los valores aprendidos.
- `gamma`: factor de descuento; controla la importancia de las recompensas futuras frente a las inmediatas.

Al terminar el entrenamiento, esta implementación establece `epsilon=0` y `alpha=0`. Por tanto, durante las 10 partidas finales el agente deja de explorar y de aprender, y utiliza la política obtenida durante el entrenamiento.

## Resultado de ejemplo mostrado en la plataforma

Este resultado es únicamente una referencia; no debe presentarse como resultado propio:

```text
Training Done (turning off epsilon and alpha)
---------------------------------------------
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman died! Score: -503
Average Score: 400.8
Scores: 495.0, 503.0, 503.0, 503.0, 495.0, 503.0, 503.0, 503.0, 503.0, -503.0
Win Rate: 9/10 (0.90)
Record: Win, Win, Win, Win, Win, Win, Win, Win, Win, Loss
```

Los resultados pueden variar entre ejecuciones debido a la aleatoriedad del entrenamiento y del entorno.

## Entregable

### Pregunta 1

> Envíe un reporte (en formato PDF) explicando el comportamiento del agente de Pacman para cada combinación de parámetros utilizados, dando un análisis de los resultados observados.
>
> Asegúrese de cubrir distintas combinaciones de los parámetros de aprendizaje, que le permitan observar y explicar las diferencias en el comportamiento del agente a partir de los cambios a los parámetros.

## Trabajo que debe realizar el estudiante

1. Definir varias combinaciones de `epsilon`, `alpha` y `gamma`.
2. Mantener constantes los demás elementos cuando se quiera estudiar el efecto de un parámetro.
3. Ejecutar el agente con cada combinación.
4. Registrar los parámetros y resultados de cada ejecución.
5. Observar el comportamiento de Pacman durante las partidas de evaluación.
6. Comparar los resultados y explicar las diferencias observadas.
7. Preparar y exportar el reporte final en formato PDF.

## Datos que conviene registrar

Para cada combinación:

- `epsilon`, `alpha` y `gamma`.
- Cantidad de episodios de entrenamiento y evaluación.
- Tablero utilizado.
- Uso o no de una semilla fija.
- Recompensa promedio de las primeras 100 partidas de entrenamiento.
- Recompensa promedio de las últimas 100 partidas de entrenamiento.
- Puntuaciones de las 10 partidas de evaluación.
- Puntuación promedio de evaluación.
- Cantidad y proporción de victorias.
- Observaciones cualitativas sobre el movimiento y las decisiones del agente.

Tabla de trabajo sugerida:

| Caso | Epsilon | Alpha | Gamma | Primeras 100 | Últimas 100 | Promedio de evaluación | Victorias | Observaciones |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |

## Estructura sugerida para el reporte

1. **Introducción:** objetivo de la experimentación.
2. **Metodología:** entorno, agente, parámetros, número de episodios y control de la aleatoriedad.
3. **Resultados:** tabla comparativa y evidencias relevantes.
4. **Análisis:** explicación del efecto observado al cambiar cada parámetro.
5. **Conclusiones:** principales aprendizajes y limitaciones del experimento.
6. **Anexo opcional:** comandos y salidas completas.

## Lista de comprobación antes de entregar

- [ ] Se probaron distintas combinaciones de parámetros.
- [ ] Cada combinación está identificada claramente.
- [ ] Los resultados pertenecen a ejecuciones propias.
- [ ] El reporte explica los resultados y no se limita a copiarlos.
- [ ] Se distingue entre entrenamiento y evaluación.
- [ ] Se indica si se utilizó una semilla fija.
- [ ] Las afirmaciones están respaldadas por los datos observados.
- [ ] El archivo final se exportó y revisó en formato PDF.
- [ ] La fecha y las condiciones de entrega se volvieron a comprobar en la plataforma.
