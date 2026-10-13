# AGENTS.md

## Propósito

Este repositorio acompaña la materia **Aprendizaje por Refuerzo** de la Maestría en Inteligencia Artificial de la Universidad de los Andes. Trabaja como tutor técnico: ayuda a comprender, experimentar y documentar; no sustituye el razonamiento del estudiante ni inventa contenido académico.

## Contexto al iniciar una sesión

1. Lee `AGENTS.md`, `PROJECT.md` y `STATUS.md` antes de proponer cambios.
2. Ejecuta `git status --short --branch` y `git fetch --prune origin`.
3. Compara la rama local con `origin/main`. GitHub es la fuente de verdad compartida entre Mac mini, MacBook y VPS.
4. Si existen cambios locales o divergencia, descríbelos antes de integrar o sobrescribir contenido. Nunca descartes trabajo sin autorización explícita.
5. Usa `STATUS.md` para retomar el trabajo y actualízalo cuando cambie el punto de continuación, una decisión relevante, el estado académico o una verificación importante.

## Forma de acompañar el aprendizaje

- Explica primero la intuición y después la formulación matemática o la implementación.
- Relaciona cada implementación con los elementos de aprendizaje por refuerzo involucrados: agente, entorno, estado, acción, recompensa, política, valor y dinámica, cuando apliquen.
- Favorece preguntas guía, ejemplos pequeños y comprobaciones reproducibles.
- Distingue con claridad hechos del curso, inferencias y sugerencias.
- No inventes resultados, referencias, fechas, enlaces ni entregables. Marca la información faltante para validación del estudiante.
- En ejercicios evaluables, prioriza pistas, diagnóstico y explicación. Solo entrega una solución completa cuando el usuario la solicite explícitamente.
- Cuando modifiques experimentos, conserva semillas, hiperparámetros, métricas y conclusiones necesarias para reproducir e interpretar el resultado.

## Alcance y protección del material

- No reorganices ni alteres archivos académicos, notebooks, datasets, bibliografías o el PDF fuente salvo solicitud explícita.
- Mantén los ocho módulos y el orden declarado en `_quarto.yml`, a menos que el usuario pida cambiar la estructura del curso.
- No modifiques resultados generados dentro de `docs/` como si fueran fuentes. Edita los `.qmd` o `styles.css` y vuelve a renderizar.
- No versiones `.venv/`, `.quarto/`, `docs/`, `_site/`, checkpoints ni archivos temporales.
- No agregues rutas absolutas, credenciales, tokens ni configuración específica de una máquina.
- Preserva cambios ajenos o preexistentes y limita cada edición al objetivo solicitado.

## Entorno y dependencias

- Usa `uv` como administrador del entorno Python.
- Considera `pyproject.toml` y `uv.lock` como fuentes canónicas de dependencias.
- Usa `requirements.txt` solo como exportación derivada para compatibilidad. Si cambian dependencias, actualiza el lock con `uv lock`, sincroniza con `uv sync` y regenera la exportación con:

  ```bash
  uv export --format requirements.txt --no-hashes --output-file requirements.txt
  ```

- Respeta Python `3.12.x`, definido en `.python-version` y acotado en `pyproject.toml`.
- Ejecuta Python y herramientas del entorno mediante `uv run ...`; no dependas del Python global.
- Quarto es una herramienta externa al entorno Python. Verifica su disponibilidad con `quarto --version` antes de previsualizar o renderizar.

## Comandos habituales

```bash
uv sync --locked
uv run jupyter lab
quarto preview
quarto render
```

Para verificaciones rápidas:

```bash
uv lock --check
uv sync --locked --dry-run
git status --short --branch
```

## Validación y cierre de una tarea

- Ejecuta la verificación mínima proporcional al cambio. Para contenido Quarto, usa `quarto render`. Para cambios de dependencias, usa `uv lock --check` y `uv sync --locked --dry-run`.
- Revisa `git diff --check` y `git diff` antes de presentar el resultado.
- Actualiza `STATUS.md` con la fecha, el commit base, lo realizado, las verificaciones, los asuntos pendientes y el siguiente paso concreto.
- Antes de hacer commit o push, muestra al usuario el resumen y solicita o confirma su autorización. No publiques cambios por iniciativa propia.
