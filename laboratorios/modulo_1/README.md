# Laboratorio: agente Q-learning en Pacman

## Material original

- Archivo descargado: `originales/AI-Pacman-Projects.zip`
- SHA-256: `732b04353cee41f0d0c624993befc5945ae5afa9a5ad04fdb19d80da9ae8a1cb`
- Copia de trabajo: `pacman/AI-Pacman-Projects-master/`
- Proyecto utilizado: `Reinforcement/`

El ZIP conservado en `originales/` coincide byte por byte con el archivo del enlace directo de la plataforma y superó la prueba de integridad de `unzip`.

La copia extraída es material derivado y permanece ignorada por Git. Para reconstruirla en otro equipo desde la raíz del repositorio:

```bash
mkdir -p laboratorios/modulo_1/pacman
unzip laboratorios/modulo_1/originales/AI-Pacman-Projects.zip \
  'AI-Pacman-Projects-master/*' \
  -d laboratorios/modulo_1/pacman
```

## Ejecución

Desde `pacman/AI-Pacman-Projects-master/Reinforcement/`:

```bash
uv run python pacman.py \
  -p PacmanQAgent \
  -x 2000 \
  -n 2010 \
  -l smallGrid \
  -a epsilon=0.1,alpha=0.3,gamma=0.7
```

Parámetros:

- Agente: `PacmanQAgent`.
- Episodios de entrenamiento: 2000.
- Episodios totales: 2010; los últimos 10 corresponden a evaluación.
- Entorno: `smallGrid`.
- Exploración: `epsilon=0.1`.
- Tasa de aprendizaje: `alpha=0.3`.
- Factor de descuento: `gamma=0.7`.
- Semilla: no fijada, porque el comando proporcionado por el curso no incluye `-f`.

## Resultado observado

Ejecución realizada el 15 de octubre de 2026:

```text
Training Done (turning off epsilon and alpha)
---------------------------------------------
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Average Score: 499.8
Scores:        503.0, 495.0, 503.0, 495.0, 503.0, 495.0, 495.0, 503.0, 503.0, 503.0
Win Rate:      10/10 (1.00)
Record:        Win, Win, Win, Win, Win, Win, Win, Win, Win, Win
```

Durante el entrenamiento, la recompensa promedio de las primeras 100 partidas fue `-510.22`; en las últimas 100 fue `34.23`. Esto muestra una mejora de la política durante la corrida. Al terminar los 2000 episodios, la implementación desactivó `epsilon` y `alpha`: el agente dejó de explorar y de actualizar los valores Q durante las 10 partidas de evaluación.

Los resultados pueden cambiar entre ejecuciones porque no se fijó una semilla aleatoria.
