# Plan de pruebas de Pacman

## Punto de ejecución

Los comandos de este archivo están preparados para ejecutarse desde:

```text
laboratorios/modulo_1/pacman/AI-Pacman-Projects-master/Reinforcement
```

Antes de empezar, comprobar la ubicación:

```bash
pwd
```

La salida debe terminar en:

```text
/laboratorios/modulo_1/pacman/AI-Pacman-Projects-master/Reinforcement
```

## Criterio experimental

- Mantener `PacmanQAgent`, 2000 episodios de entrenamiento y 2010 episodios totales: 10 de evaluación (`n - x`).
- Usar `-f` en todas las pruebas para aplicar el mismo criterio de aleatoriedad.
- Casos 01–07: mantener `smallGrid` y cambiar un solo parámetro con respecto al caso base.
- Casos 08–11: comparar `mediumGrid` y `mediumClassic` con los parámetros base y con alpha alto. Comparar 01/08/10 para el efecto del tablero y 01/05, 08/09 y 10/11 para el efecto de alpha dentro de cada tablero.
- Cada comando inicia un entrenamiento desde cero; no transfiere la tabla Q de otro caso.
- Guardar automáticamente la salida de cada prueba mediante `tee`.
- Completar `resultados/resumen.csv` después de cada ejecución.
- Escribir las observaciones visuales propias mientras se muestran las 10 partidas de evaluación.

Las once salidas ya están disponibles y sus métricas están consolidadas en `resultados/resumen.csv`; faltan las observaciones visuales. Los comandos documentan cómo reproducirlas. `tee` sobrescribe el archivo indicado: para una repetición, usar un nombre nuevo y conservar la evidencia anterior.

La ampliación de tableros responde a la aclaración de tutoría reportada por el estudiante el 19 de octubre de 2026. No constituye una matriz completa de todos los parámetros en todos los tableros; falta confirmar si la tutoría exige un alcance específico.

## Casos

### 01. Caso base

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.1,alpha=0.3,gamma=0.7 \
  | tee ../../../resultados/01_base.txt
```

### 02. Epsilon bajo

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.01,alpha=0.3,gamma=0.7 \
  | tee ../../../resultados/02_epsilon_bajo.txt
```

### 03. Epsilon alto

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.5,alpha=0.3,gamma=0.7 \
  | tee ../../../resultados/03_epsilon_alto.txt
```

### 04. Alpha bajo

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.1,alpha=0.05,gamma=0.7 \
  | tee ../../../resultados/04_alpha_bajo.txt
```

### 05. Alpha alto

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.1,alpha=0.8,gamma=0.7 \
  | tee ../../../resultados/05_alpha_alto.txt
```

### 06. Gamma bajo

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.1,alpha=0.3,gamma=0.1 \
  | tee ../../../resultados/06_gamma_bajo.txt
```

### 07. Gamma alto

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.1,alpha=0.3,gamma=0.95 \
  | tee ../../../resultados/07_gamma_alto.txt
```

### 08. MediumGrid — caso base

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l mediumGrid \
  -a epsilon=0.1,alpha=0.3,gamma=0.7 \
  | tee ../../../resultados/08_mediumGrid_base.txt
```

### 09. MediumGrid — alpha alto

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l mediumGrid \
  -a epsilon=0.1,alpha=0.8,gamma=0.7 \
  | tee ../../../resultados/09_mediumGrid_alpha_alto.txt
```

### 10. MediumClassic — caso base

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l mediumClassic \
  -a epsilon=0.1,alpha=0.3,gamma=0.7 \
  | tee ../../../resultados/10_mediumClassic_base.txt
```

### 11. MediumClassic — alpha alto

```bash
uv run python pacman.py \
  -f \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l mediumClassic \
  -a epsilon=0.1,alpha=0.8,gamma=0.7 \
  | tee ../../../resultados/11_mediumClassic_alpha_alto.txt
```

## Después de cada prueba

Además del identificador, registrar `epsilon`, `alpha`, `gamma`, criterio de semilla y `tablero`. Los argumentos no se imprimen en las salidas actuales: conservar el comando utilizado junto con la identificación del caso.

Registrar en `resultados/resumen.csv`:

1. Promedio de recompensa de las primeras 100 partidas.
2. Promedio de recompensa de las últimas 100 partidas.
3. Promedio de las 10 partidas de evaluación.
4. Cantidad de victorias y derrotas.
5. Una observación visual concreta escrita por el estudiante.

No interpretar una diferencia como una regla general: los resultados corresponden a esta implementación, este tablero, esta semilla y esta cantidad de entrenamiento.

No comparar los puntajes de distintos mapas como si su escala y dificultad fueran equivalentes; considerar también victorias, comida disponible y comportamiento observado. Las recompensas de entrenamiento incluyen exploración y actualizaciones Q; la evaluación se realiza con epsilon y alpha en cero.

Para estudiar un presupuesto mayor, crear un caso adicional con archivo propio y documentar ambos valores: por ejemplo, `-x 5000 -n 5010` mantiene diez evaluaciones. Ese experimento no forma parte de las once pruebas actuales.
