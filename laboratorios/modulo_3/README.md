# Laboratorios del módulo 3: MDPs

Las páginas Quarto se encuentran en la raíz del módulo y aparecen en el menú del libro, con la misma organización del módulo 2.

| Actividad | Página de lectura | Notebook original |
|---|---|---|
| Tutorial: Definición de un MDP para Gridworld | [gridworld_mdps_tutorial.qmd](gridworld_mdps_tutorial.qmd) | [gridworld_mdps_tutorial.ipynb](originales/gridworld_mdps_tutorial.ipynb) |
| Laboratorio MDPs: Construcción de MDPs | [car.qmd](car.qmd) | [car.ipynb](originales/car.ipynb) |

Los archivos de `originales/` (`gridworld_mdps_tutorial.ipynb`, `car.ipynb`, `Banner.jpg`, `cars_mdp.png`, `gridworld.png` y `table.png`) se conservan sin modificar. Las páginas de lectura solo ajustan metadatos, título y rutas de imágenes; no completan ni corrige el contenido académico.

El código no se ejecuta al renderizar las páginas (`execute.enabled: false`). Para verlas dentro del libro, desde la raíz del repositorio:

```bash
quarto preview
```

La salida se genera en `docs/` y no se versiona. Las páginas de lectura no indican que las actividades estén completadas.

El tutorial es de consulta (sus celdas de prueba tienen 0 puntos). El laboratorio es calificable (5 %, 3 de noviembre de 2026, según el calendario registrado en `STATUS.md`) y conserva la restricción académica registrada: trabajo independiente del estudiante; el acompañamiento se limita a orientación y diagnóstico. Quarto no conserva todos los metadatos `nbgrader` del notebook; confirmar el formato aceptado por la plataforma antes de preparar la entrega.
