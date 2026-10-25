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

Los enlaces de Zoom y las claves de acceso se añaden directamente en «Recursos de la Semana → Sesión Síncrona» de cada `modulo_N.qmd`. Los módulos 1–3 ya contienen los datos proporcionados por el estudiante.

El estudiante autorizó explícitamente el 24 de octubre de 2026 guardar estos datos en el repositorio privado para sincronizarlos entre equipos. Las claves se escriben entre comillas invertidas para conservar sus caracteres especiales. La excepción se limita a grabaciones de clase, según `AGENTS.md`.

Las copias previas de `recursos_privados/` se conservan localmente como respaldo y siguen excluidas de Git y de los recursos Quarto; el libro usa los datos incorporados en los módulos.

Las grabaciones adicionales se enlazan en «Sesiones complementarias». No es necesario descargar ni guardar los videos en este repositorio.

## Comprobación

Desde la raíz del proyecto, ejecuta `quarto render` y abre el módulo para comprobar sus enlaces. No edites los archivos generados en `docs/`.
