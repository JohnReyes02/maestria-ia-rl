# Laboratorios del módulo 2: bandidos

Las páginas Quarto se encuentran en la raíz del módulo y aparecen en el menú del libro, siguiendo la organización de `ml-no-supervisado`.

| Actividad | Página de lectura | Notebook original |
|---|---|---|
| Tutorial: Construcción de bandidos de K-brazos | [Tutorial-bandidos.qmd](Tutorial-bandidos.qmd) | [Tutorial-bandidos.ipynb](originales/Tutorial-bandidos.ipynb) |
| K-Bandidos con epsilon decay | [bandidos_epsilon.qmd](bandidos_epsilon.qmd) | [bandidos_epsilon.ipynb](originales/bandidos_epsilon.ipynb) |
| K-bandidos no estacionarios | [bandidos-variables.qmd](bandidos-variables.qmd) | [bandidos-variables.ipynb](originales/bandidos-variables.ipynb) |

Los archivos de `originales/` se conservan sin modificar, incluidas las dos conversiones Quarto previas. Las páginas de lectura solo ajustan metadatos, título y presentación de imágenes ausentes; no completan ni corrigen el contenido académico. No se recibieron `Banner.jpg` ni `slots.png`.

El código no se ejecuta al renderizar estas páginas (`execute.enabled: false`). Para verlas dentro del libro, desde la raíz del repositorio:

```bash
quarto preview
```

Para validar el libro completo:

```bash
quarto render
```

La salida se genera en `docs/` y no se versiona. Las páginas de lectura no indican que las actividades estén completadas.

Las evaluaciones calificables conservan la restricción académica registrada en `STATUS.md`: trabajo independiente sin IA para resolverlas. Quarto no conserva todos los metadatos `nbgrader` del notebook; confirmar el formato aceptado por la plataforma antes de preparar la entrega.

Las prácticas separadas mantienen sus directorios y archivos de trabajo:

- [Pen & Paper: Bandidos 1](pen_and_paper_bandidos_1/README.md).
- [Pen & Paper: Bandidos 2](pen_and_paper_bandidos_2/README.md).
