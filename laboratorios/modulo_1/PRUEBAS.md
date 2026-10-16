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

- Mantener `PacmanQAgent`, 2000 episodios de entrenamiento, 2010 episodios totales y `smallGrid`.
- Usar `-f` en todas las pruebas para aplicar el mismo criterio de aleatoriedad.
- Cambiar un solo parámetro con respecto al caso base.
- Guardar automáticamente la salida de cada prueba mediante `tee`.
- Completar `resultados/resumen.csv` después de cada ejecución.
- Escribir las observaciones visuales propias mientras se muestran las 10 partidas de evaluación.

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

## Después de cada prueba

Registrar en `resultados/resumen.csv`:

1. Promedio de recompensa de las primeras 100 partidas.
2. Promedio de recompensa de las últimas 100 partidas.
3. Promedio de las 10 partidas de evaluación.
4. Cantidad de victorias y derrotas.
5. Una observación visual concreta escrita por el estudiante.

No interpretar una diferencia como una regla general: los resultados corresponden a esta implementación, este tablero, esta semilla y esta cantidad de entrenamiento.
