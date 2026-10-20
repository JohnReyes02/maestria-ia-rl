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

## Archivos de trabajo y avance

- [INSTRUCCIONES.md](INSTRUCCIONES.md): enunciado conservado, aclaración de tutoría y comprobaciones para la entrega.
- [PRUEBAS.md](PRUEBAS.md): comandos reproducibles de los once casos con `-f`, 2000 episodios de entrenamiento y 10 de evaluación.
- [Resultados](resultados/README.md) y [resumen.csv](resultados/resumen.csv): siete casos en `smallGrid`, dos en `mediumGrid` y dos en `mediumClassic`, con métricas consolidadas.
- [Informe](reporte/reporte_pacman.qmd) y [guía para generar el PDF](reporte/README.md): metodología, tablas, imágenes ilustrativas, análisis, limitaciones y conclusiones de los once casos, pendientes de lectura final del estudiante. El `.md` anterior se conserva como referencia histórica.

La ampliación de tableros incorpora lo informado por el estudiante tras la tutoría del 19 de octubre de 2026. Falta confirmar si se exige un número concreto de combinaciones por tablero. La entrega registrada es un PDF para el 20 de octubre a las 23:59 (-05), pendiente de comprobar en plataforma.

## Ejecución preliminar sin semilla

El siguiente comando y sus resultados corresponden a una prueba inicial, separada de los once casos comparativos con semilla fija. Para reproducir estos últimos, usar `PRUEBAS.md`.

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
