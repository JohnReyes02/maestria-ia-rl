# Resultados de las pruebas

Esta carpeta almacena las salidas crudas de las once ejecuciones descritas en [PRUEBAS.md](../PRUEBAS.md): siete en `smallGrid`, dos en `mediumGrid` y dos en `mediumClassic`.

Archivos esperados:

```text
01_base.txt
02_epsilon_bajo.txt
03_epsilon_alto.txt
04_alpha_bajo.txt
05_alpha_alto.txt
06_gamma_bajo.txt
07_gamma_alto.txt
08_mediumGrid_base.txt
09_mediumGrid_alpha_alto.txt
10_mediumClassic_base.txt
11_mediumClassic_alpha_alto.txt
```

[resumen.csv](resumen.csv) contiene las métricas de los once casos: parámetros, criterio de semilla fija, promedios de las primeras y últimas 100 partidas de entrenamiento, promedio de evaluación, victorias, derrotas, observación visual y tablero. Las observaciones visuales siguen vacías y deben completarse con lo observado por el estudiante.

Cada caso utiliza 2000 episodios de entrenamiento y 10 de evaluación, con `-f`. Los parámetros y el tablero se identifican mediante los comandos documentados y los nombres de archivo; las salidas no imprimen esos argumentos.

Las cuatro salidas nuevas se verificaron comprobando 20 cortes de entrenamiento, cierre de entrenamiento, diez puntajes de evaluación, promedio recalculado y conteos de `Record` y `Win Rate`. Las siete primeras habían sido verificadas previamente.

Para comparar tableros con parámetros base, usar 01/08/10. Para comparar alpha dentro de cada tablero, usar 01/05, 08/09 y 10/11. Una corrida por caso y diez evaluaciones no permiten establecer superioridad general.

No editar las salidas crudas para que permanezcan como evidencia de las ejecuciones.

Si se repite una prueba, guardar la nueva salida con otro nombre; `tee` sobrescribe su archivo de destino. La ejecución preliminar sin semilla descrita en el README del laboratorio no forma parte de estos once casos.
