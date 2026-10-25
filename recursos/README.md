# Recursos de las sesiones semanales

Cada semana corresponde al módulo con el mismo número. La organización de presentaciones sigue la usada en la materia Machine Learning No Supervisado:

```text
recursos/
  modulo_1/presentaciones/
  modulo_2/presentaciones/
  ...
  modulo_8/presentaciones/
```

## Presentaciones

1. Guarda el PDF o PPTX en `recursos/modulo_N/presentaciones/`, conservando el contenido original.
2. Abre `modulo_N.qmd`, en «Recursos de la Semana → Sesión Síncrona».
3. Reemplaza la línea de presentación por el enlace al archivo real. Por ejemplo, para la semana 2, si usaste el nombre sugerido:

```markdown
- **Presentación:** [Ver presentación de la semana 2](recursos/modulo_2/presentaciones/semana-02-presentacion-sincronica.pdf)
```

Puedes conservar el nombre original del archivo; en ese caso, usa ese mismo nombre en el enlace. No actives enlaces a archivos que todavía no existen.

## Grabaciones

Los enlaces y claves de las grabaciones se guardan localmente en `recursos_privados/modulo_N/grabaciones.md`. Los módulos 1–3 ya tienen los datos proporcionados por el estudiante. Cada módulo indica la ruta correspondiente en su sección de sesión síncrona.

Esta carpeta se excluye de Git y de los recursos del libro. Sus archivos no se sincronizan mediante GitHub; para usarlos en otro equipo, consérvalos por un medio privado. No copies las claves en los `.qmd` ni en este README.

Las grabaciones adicionales se enlazan en «Sesiones complementarias». No es necesario descargar ni guardar los videos en este repositorio.

## Comprobación

Desde la raíz del proyecto, ejecuta `quarto render` y abre el módulo para comprobar sus enlaces. No edites los archivos generados en `docs/`.
