# Análisis del agente de Q-learning en Pacman

> Borrador Markdown anterior. La fuente editable del entregable pasa a ser [reporte_pacman.qmd](reporte_pacman.qmd); consultar [README.md](README.md) para generar el PDF. Este archivo se conserva como referencia y no se sincroniza automáticamente con el `.qmd`.

**Estudiante:** [Completar]

**Curso:** Aprendizaje por Refuerzo

**Fecha:** [Completar]

## 1. Introducción

[Explicar brevemente el objetivo del experimento y los parámetros `epsilon`, `alpha` y `gamma`.]

## 2. Metodología

Se utilizó `PacmanQAgent` con 2000 episodios de entrenamiento y 10 de evaluación por configuración (`-x 2000 -n 2010`). Cada ejecución inició un entrenamiento desde cero y utilizó `-f` para fijar la semilla. Durante la evaluación, la implementación desactiva epsilon y alpha.

Los casos 01–07 mantienen `smallGrid` y varían un parámetro respecto al caso base. Los casos 08–11 añaden `mediumGrid` y `mediumClassic` con los parámetros base y con alpha alto. Se compara el efecto del tablero con 01/08/10 y el de alpha dentro de cada entorno con 01/05, 08/09 y 10/11. No se evaluaron todas las combinaciones de parámetros en todos los tableros.

[Describir con tus palabras el agente, su estado, acciones y recompensas en esta implementación, y cómo los relacionas con la política aprendida.]

### Configuraciones evaluadas

| Caso | Tablero | Epsilon | Alpha | Gamma |
|---|---|---:|---:|---:|
| 01_base | smallGrid | 0.10 | 0.30 | 0.70 |
| 02_epsilon_bajo | smallGrid | 0.01 | 0.30 | 0.70 |
| 03_epsilon_alto | smallGrid | 0.50 | 0.30 | 0.70 |
| 04_alpha_bajo | smallGrid | 0.10 | 0.05 | 0.70 |
| 05_alpha_alto | smallGrid | 0.10 | 0.80 | 0.70 |
| 06_gamma_bajo | smallGrid | 0.10 | 0.30 | 0.10 |
| 07_gamma_alto | smallGrid | 0.10 | 0.30 | 0.95 |
| 08_mediumGrid_base | mediumGrid | 0.10 | 0.30 | 0.70 |
| 09_mediumGrid_alpha_alto | mediumGrid | 0.10 | 0.80 | 0.70 |
| 10_mediumClassic_base | mediumClassic | 0.10 | 0.30 | 0.70 |
| 11_mediumClassic_alpha_alto | mediumClassic | 0.10 | 0.80 | 0.70 |

## 3. Resultados

Datos extraídos de las once salidas originales en `../resultados/` y consolidados en [resumen.csv](../resultados/resumen.csv). “Primeras 100” y “Últimas 100” corresponden a las recompensas promedio de los episodios de entrenamiento 1–100 y 1901–2000, respectivamente. El promedio de evaluación, las victorias y las derrotas corresponden a las 10 partidas posteriores al entrenamiento, con epsilon y alpha desactivados.

| Caso | Primeras 100 | Últimas 100 | Promedio de evaluación | Victorias | Derrotas | Observación visual |
|---|---:|---:|---:|---:|---:|---|
| 01_base | -509.49 | -15.11 | 500.5 | 10 | 0 | Pendiente |
| 02_epsilon_bajo | -510.71 | 449.04 | 500.2 | 10 | 0 | Pendiente |
| 03_epsilon_alto | -509.46 | -490.58 | -506.4 | 0 | 10 | Pendiente |
| 04_alpha_bajo | -510.23 | -158.84 | 494.2 | 10 | 0 | Pendiente |
| 05_alpha_alto | -509.51 | 23.42 | 501.6 | 10 | 0 | Pendiente |
| 06_gamma_bajo | -510.27 | -68.34 | 195.1 | 7 | 3 | Pendiente |
| 07_gamma_alto | -499.85 | 125.37 | 499.4 | 10 | 0 | Pendiente |
| 08_mediumGrid_base | -470.67 | -447.06 | -503.7 | 0 | 10 | Pendiente |
| 09_mediumGrid_alpha_alto | -491.25 | -468.71 | -414.7 | 1 | 9 | Pendiente |
| 10_mediumClassic_base | -434.93 | -404.74 | -401.4 | 0 | 10 | Pendiente |
| 11_mediumClassic_alpha_alto | -434.93 | -389.67 | -384.7 | 0 | 10 | Pendiente |

Las observaciones visuales están pendientes de completar por el estudiante; en el CSV esos campos permanecen vacíos. Cada configuración corresponde a una corrida con semilla fija; estos datos no miden variabilidad entre corridas.

## 4. Análisis

### 4.1. Efecto de epsilon

[Comparar epsilon bajo, caso base y epsilon alto. Relacionar los datos con exploración y explotación.]

### 4.2. Efecto de alpha

[Comparar alpha bajo, caso base y alpha alto. Relacionar los datos con la velocidad y estabilidad del aprendizaje.]

### 4.3. Efecto de gamma

[Comparar gamma bajo, caso base y gamma alto. Relacionar los datos con la importancia de recompensas inmediatas y futuras.]

### 4.4. Efecto del tablero

[Comparar 01/08/10 manteniendo los parámetros base. ¿Qué diferencias aparecen en victorias y entrenamiento? ¿Qué cambios del entorno podrían explicarlas? Separar lo observado de las hipótesis. Considerar comida disponible y recorrido antes de comparar puntajes entre mapas.]

### 4.5. Efecto de alpha en distintos tableros

[Comparar 01/05, 08/09 y 10/11. ¿Cambian de la misma manera las métricas de entrenamiento y evaluación? ¿Qué permite concluir una sola corrida y qué requeriría repetir con otras semillas? No atribuir a alpha cambios causados por comparar mapas diferentes.]

## 5. Conclusiones

[Resumir los hallazgos respaldados por los resultados propios e indicar las limitaciones del experimento.]

## Anexo: comandos y evidencias

Los comandos y la identificación de los once casos están en [PRUEBAS.md](../PRUEBAS.md). Las salidas originales y su correspondencia con el CSV se describen en [resultados/README.md](../resultados/README.md).

[Agregar solo las evidencias que aporten al reporte. La ejecución preliminar sin semilla descrita en el README del laboratorio no forma parte de esta comparación.]
