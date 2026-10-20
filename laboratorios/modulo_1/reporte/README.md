# Preparar el PDF de Pacman

La fuente editable del entregable es [reporte_pacman.qmd](reporte_pacman.qmd). El archivo Markdown anterior se conserva como borrador histórico; a partir de esta plantilla, editar el `.qmd` para evitar mantener dos versiones del informe final.

## Estado y revisión final

El texto se completó el 19 de octubre de 2026 a solicitud del estudiante. Incluye análisis de parámetros y tableros, limitaciones y conclusiones basados en las once pruebas. Se retiraron instrucciones pendientes y referencias a otros archivos dentro de la redacción. Las capturas se describen como ilustraciones de los tableros durante la evaluación, sin inventar observaciones de trayectorias.

1. Revisar el nombre en `author` y la fecha del PDF (`date: today` usa la fecha del renderizado).
2. Leer el texto completo y ajustar cualquier explicación que no puedas expresar con tus propias palabras.
3. Revisar las tablas de los once casos. Son una copia del CSV, no se actualizan automáticamente; si cambian los resultados, actualizar ambas fuentes.
4. Añadir únicamente observaciones y capturas propias. Una derrota o un puntaje no permiten inventar movimientos que no observaste.
5. Renderizar otra vez si cambias el texto y revisar el PDF completo antes de subirlo.

El estudiante confirmó el 19 de octubre de 2026 que solo queda subir el taller a la plataforma. El envío todavía no se ha confirmado. Los posibles ajustes de vocabulario a su estilo no cambian las métricas registradas.

## Generar el PDF

Desde la raíz del repositorio:

```bash
quarto --version
quarto render laboratorios/modulo_1/reporte/reporte_pacman.qmd --to typst
```

El PDF queda en:

```text
laboratorios/modulo_1/reporte/_salida/reporte_pacman.pdf
```

También puedes abrir una vista que se actualiza al guardar:

```bash
quarto preview laboratorios/modulo_1/reporte/reporte_pacman.qmd --to typst
```

Quarto utiliza su compilador Typst para generar el PDF. En este flujo se usa `--to typst`, aunque el archivo final sea `.pdf`; `--to pdf` seleccionaría el flujo de LaTeX. No es necesario añadir paquetes a Python para este documento, pues no ejecuta código. Ver [documentación oficial de Quarto para Typst](https://quarto.org/docs/output-formats/typst.html).

La configuración local `_quarto.yml` trata el informe como documento independiente. No modifica los ocho módulos ni el proyecto del libro. `_salida/` y la caché local de Quarto están ignorados en Git; se conservan las fuentes, no las salidas generadas.

## Revisión antes de entregar

- No quedan corchetes de instrucciones, nombre provisional ni aviso de borrador.
- Cada explicación remite a casos y métricas concretos.
- Se distingue entrenamiento de evaluación y observación de hipótesis.
- Tablas, capturas, acentos y números son legibles, sin recortes.
- Se confirma en la plataforma el alcance pedido en tutoría y la fecha límite.
