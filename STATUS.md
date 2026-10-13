# STATUS.md

## Punto de control

- **Actualizado:** 2026-10-12, zona horaria America/Bogota.
- **Rama:** `main`.
- **Commit base:** `7592be4` — `docs: add shared Codex project context`.
- **Sincronización:** al iniciar, el árbol de trabajo estaba limpio. Tras actualizar el remoto, había `0` commits locales y `1` remoto pendiente. Se integró `origin/main` mediante `git merge --ff-only origin/main`, desde `70d742c` hasta `7592be4`; comparación final: `0 0`.
- **Estado de la validación:** se leyeron `AGENTS.md`, `PROJECT.md` y `STATUS.md`, se sincronizó la rama y se verificó el entorno sin ejecutar entrenamientos. La revisión posterior confirmó que el cambio se limita a este archivo y contiene información técnica para la continuidad del proyecto; el usuario autorizó su commit y push con el mensaje `docs: validate Mac mini environment`.

## Estado académico observado

- El libro tiene una portada y ocho módulos declarados en `_quarto.yml`.
- `modulo_1.qmd` está en desarrollo: contiene objetivos concretos y una lista de videos parcialmente marcada como terminada, pero aún conserva campos y secciones por completar.
- `modulo_2.qmd` a `modulo_8.qmd` conservan la plantilla inicial con objetivos, fechas, recursos, notas y síntesis pendientes.
- Los nueve archivos `.bib` solo contienen marcadores; aún no hay entradas bibliográficas.
- `laboratorios/` no contiene laboratorios todavía.
- No existen notebooks, datasets ni scripts Python versionados.
- El PDF `S2C2_aprendizaje-por-refuerzo.pdf` está versionado. El punto de control anterior registró 3 páginas sin texto extraíble; no se volvió a inspeccionar en esta sesión.

## Verificaciones realizadas

- `git fetch --prune origin`: remoto actualizado.
- Integración por avance directo, sin conflictos ni descarte de trabajo; comparación final `HEAD...origin/main`: `0 0`.
- `uv lock --check`: correcta; resolvió 153 paquetes.
- `uv sync --locked --dry-run`: el entorno no requería cambios; comprobó 131 paquetes instalados.
- `uv pip check`: los 131 paquetes instalados son compatibles.
- `uv export --locked --format requirements.txt --no-hashes`: las 152 líneas de requisitos coinciden con `requirements.txt` al excluir comentarios y líneas vacías. Solo difiere el comentario del comando de generación; no se modificó la exportación.
- Importaciones mediante `uv run --locked python`, con backend gráfico no interactivo: todas correctas y con versiones idénticas al lock.

  | Dependencia | Versión instalada |
  | --- | --- |
  | gymnasium | 1.4.0 |
  | jupyter | 1.1.1 |
  | matplotlib | 3.11.2 |
  | numpy | 2.5.4 |
  | pandas | 3.0.6 |
  | pygame | 2.6.1 |
  | scikit-learn | 1.9.1 |
  | seaborn | 0.13.2 |
  | stable-baselines3 | 2.9.0 |
  | tensorboard | 2.21.0 |
  | torch | 2.14.1 |

- Importaciones adicionales de `PPO`, `DQN`, `A2C`, `torch.utils.tensorboard.SummaryWriter`, `ipykernel`, `nbformat` y `jupyterlab`: correctas, sin crear agentes ni iniciar entrenamientos.
- Entorno del proyecto: CPython `3.12.15`, arquitectura `arm64`, ejecutado desde `.venv/`; cumple `.python-version` y el rango `>=3.12,<3.13`.
- Herramientas locales: `uv 0.13.0` y Quarto `1.8.27`. La versión de Quarto registrada anteriormente (`1.10.18`) corresponde al punto de control previo.
- `quarto check`, con `QUARTO_PYTHON` apuntando temporalmente al Python del proyecto: instalación, dependencias binarias, render básico de Markdown e integración/render de Jupyter correctos. R no está instalado; no se requiere para el proyecto actual.
- No se renderizó el libro completo en esta sesión, ya que no cambiaron sus fuentes. El render de las 9 páginas registrado anteriormente no se volvió a validar.
- `git diff --check`: correcto; revisión del diff limitada a `STATUS.md`.

## Hallazgos de entorno y portabilidad

- Equipo verificado: Apple M4, macOS `26.6.2`, arquitectura nativa `arm64` y 24 GiB de memoria. Los ejecutables de Python del proyecto y `uv` son nativos `arm64`.
- El Python global observado es `3.13.7`, fuera del rango del proyecto. Usar `uv run ...`, que selecciona correctamente Python `3.12.15`; no se modificó el Python global.
- PyTorch informa MPS compilado y disponible; CUDA no disponible en este equipo. Solo se consultó disponibilidad, sin realizar cálculos ni entrenamiento en GPU.
- El entorno `.venv/` local ocupa aproximadamente 1.1 GB y no está versionado; la sincronización simulada no requiere instalaciones ni cambios.
- Quarto es una dependencia externa y no tiene una versión fijada dentro del repositorio.
- En Linux, el lock y la exportación actual de PyTorch incluyen dependencias CUDA. Esto puede ser costoso en un VPS sin GPU.
- `pygame` y el renderizado visual de entornos pueden necesitar configuración adicional en un VPS sin interfaz gráfica.
- La carpeta `docs/` se usa como salida de Quarto, pero está ignorada y no existe automatización de GitHub Pages o CI/CD.
- El árbol de trabajo estaba limpio al iniciar. No se modificaron archivos académicos, configuración ni dependencias.

## Alcance revisado

- `AGENTS.md` y `PROJECT.md` ya están versionados en el commit base traído desde `origin/main`.
- `STATUS.md`: único archivo incluido en el commit autorizado de la validación del Mac mini. No hay cambios de dependencias pendientes.

## Siguiente paso

El entorno está listo para continuar con el módulo 1 mediante `uv run ...`. En el siguiente equipo, actualizar desde `origin/main` y comprobar el entorno antes de continuar. Antes de modificar contenido del libro, verificar los pendientes académicos con el estudiante; después de editar las fuentes, ejecutar `quarto render`.
