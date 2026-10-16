# Análisis del agente de Q-learning en Pacman

**Estudiante:** [Completar]

**Curso:** Aprendizaje por Refuerzo

**Fecha:** [Completar]

## 1. Introducción

[Explicar brevemente el objetivo del experimento y los parámetros `epsilon`, `alpha` y `gamma`.]

## 2. Metodología

[Describir el agente, el tablero, la cantidad de episodios, las combinaciones evaluadas, el uso de semilla fija y las métricas registradas.]

### Configuraciones evaluadas

| Caso | Epsilon | Alpha | Gamma |
|---|---:|---:|---:|
| Base | 0.10 | 0.30 | 0.70 |
| Epsilon bajo | 0.01 | 0.30 | 0.70 |
| Epsilon alto | 0.50 | 0.30 | 0.70 |
| Alpha bajo | 0.10 | 0.05 | 0.70 |
| Alpha alto | 0.10 | 0.80 | 0.70 |
| Gamma bajo | 0.10 | 0.30 | 0.10 |
| Gamma alto | 0.10 | 0.30 | 0.95 |

## 3. Resultados

Datos extraídos de las siete salidas originales en `../resultados/` y consolidados en [resumen.csv](../resultados/resumen.csv). “Primeras 100” y “Últimas 100” corresponden a las recompensas promedio de los episodios de entrenamiento 1–100 y 1901–2000, respectivamente. El promedio de evaluación, las victorias y las derrotas corresponden a las 10 partidas posteriores al entrenamiento, con epsilon y alpha desactivados.

| Caso | Primeras 100 | Últimas 100 | Promedio de evaluación | Victorias | Derrotas | Observación visual |
|---|---:|---:|---:|---:|---:|---|
| Base | -509.49 | -15.11 | 500.5 | 10 | 0 | Pendiente |
| Epsilon bajo | -510.71 | 449.04 | 500.2 | 10 | 0 | Pendiente |
| Epsilon alto | -509.46 | -490.58 | -506.4 | 0 | 10 | Pendiente |
| Alpha bajo | -510.23 | -158.84 | 494.2 | 10 | 0 | Pendiente |
| Alpha alto | -509.51 | 23.42 | 501.6 | 10 | 0 | Pendiente |
| Gamma bajo | -510.27 | -68.34 | 195.1 | 7 | 3 | Pendiente |
| Gamma alto | -499.85 | 125.37 | 499.4 | 10 | 0 | Pendiente |

Las observaciones visuales están pendientes de completar por el estudiante; en el CSV esos campos permanecen vacíos. Cada configuración corresponde a una corrida con semilla fija; estos datos no miden variabilidad entre corridas.

## 4. Análisis

### 4.1. Efecto de epsilon

[Comparar epsilon bajo, caso base y epsilon alto. Relacionar los datos con exploración y explotación.]

### 4.2. Efecto de alpha

[Comparar alpha bajo, caso base y alpha alto. Relacionar los datos con la velocidad y estabilidad del aprendizaje.]

### 4.3. Efecto de gamma

[Comparar gamma bajo, caso base y gamma alto. Relacionar los datos con la importancia de recompensas inmediatas y futuras.]

## 5. Conclusiones

[Resumir los hallazgos respaldados por los resultados propios e indicar las limitaciones del experimento.]

## Anexo: comandos y evidencias

[Referenciar las salidas conservadas en `../resultados/` y agregar solo las evidencias que aporten al reporte.]
