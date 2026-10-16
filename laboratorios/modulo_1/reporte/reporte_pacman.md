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

[Transferir aquí los datos registrados en `../resultados/resumen.csv`. Presentar primero los resultados sin anticipar las conclusiones.]

| Caso | Primeras 100 | Últimas 100 | Promedio de evaluación | Victorias | Observación visual |
|---|---:|---:|---:|---:|---|
| Base | | | | | |
| Epsilon bajo | | | | | |
| Epsilon alto | | | | | |
| Alpha bajo | | | | | |
| Alpha alto | | | | | |
| Gamma bajo | | | | | |
| Gamma alto | | | | | |

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
