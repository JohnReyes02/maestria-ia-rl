# STATUS.md

## Punto de control

- **Actualizado:** 2026-10-12, zona horaria America/Bogota.
- **Rama y commit base:** `main`, `4b2f20a` — `docs: validate Mac mini environment`.
- **Sincronización VPS:** árbol inicialmente limpio; `git pull --ff-only` integró `35ae916` → `4b2f20a`. `git fetch --prune origin` posterior correcto; comparación `HEAD...origin/main`: `0 0`.
- Se leyeron `AGENTS.md`, `PROJECT.md` y `STATUS.md`. MacBook y Mac mini ya validados; GitHub sigue siendo la fuente de verdad.
- Esta validación modifica únicamente `STATUS.md` entre los archivos versionados; sin commit ni push. La sincronización también actualizó un paquete dentro de `.venv/` (ignorado).

## Estado académico observado

- Libro con portada y ocho módulos; módulo 1 en desarrollo, módulos 2–8 con plantilla pendiente.
- Bibliografías con marcadores; `laboratorios/` vacío salvo `.gitkeep`. Sin notebooks, datasets ni scripts Python versionados.
- PDF académico versionado; el punto de control anterior registró 3 páginas sin texto extraíble. No se volvió a inspeccionar.
- No se editaron fuentes académicas ni se renderizó el libro durante la validación del VPS.

## Validación del VPS

- **Sistema:** Ubuntu 20.04.6 LTS, `aarch64` (ARM64), glibc 2.31; CPU ARM Neoverse-N1, 4 CPU lógicas.
- **Recursos:** 23 GiB RAM (17 GiB disponibles al inicio), 4 GiB swap; disco de 194 GiB con aproximadamente 102 GiB libres al finalizar. `.venv/`: 5.7 GiB.
- **Herramientas:** Python del proyecto 3.12.15; Python global 3.8.10 (`python` global ausente); uv 0.13.0 nativo ARM64; Quarto 1.10.19. Usar `uv run ...`.
- `uv lock --check`: correcto, 153 paquetes resueltos.
- Revisión previa del lock: wheels Linux ARM64 para las dependencias nativas revisadas, incluyendo torch, pygame y Triton; requisitos manylinux compatibles con glibc 2.31. El lock selecciona también paquetes NVIDIA/CUDA en Linux CPU-only; los wheels nativos ARM64 suman aproximadamente 3 GiB comprimidos. Había espacio suficiente.
- `uv sync --locked --dry-run`: proponía reinstalar únicamente `nvidia-cusparselt-cu13==0.8.1`.
- `uv sync --locked`: correcto; reinstaló ese paquete, sin modificar `pyproject.toml` ni `uv.lock` ni configurar CUDA.
- Importaciones correctas: Gymnasium 1.4.0, Jupyter 1.1.1, matplotlib 3.11.2, NumPy 2.5.4, pandas 3.0.6, pygame 2.6.1, scikit-learn 1.9.1, seaborn 0.13.2 y TensorBoard 2.21.0. Matplotlib probado con backend `Agg`.
- **PyTorch:** 2.14.1+cu130; importación aislada y suma de tensor en CPU correctas. Compilado con CUDA 13.0, pero CUDA no disponible, 0 dispositivos CUDA y MPS no disponible. CPU es el dispositivo validado.
- **Gymnasium:** `CartPole-v1`, `render_mode=None`, `reset(seed=42)` y un `step(0)` correctos; observaciones válidas, recompensa 1.0. Sin recursos externos.
- **pygame:** importación, inicialización de display/font y operación sobre `Surface` correctas con `SDL_VIDEODRIVER=dummy` y audio dummy; SDL 2.28.4, sin crear ventana ni superficie de pantalla.
- PPO/DQN/A2C, `SummaryWriter`, ipykernel, nbformat y jupyterlab importan correctamente en proceso separado con torch primero; no se crearon agentes ni se ejecutaron entrenamientos.

## Limitaciones y pendientes

- **TLS estático / orden de importación:** después de importar otras librerías numéricas, torch y Stable Baselines fallaron con `cannot allocate memory in static TLS block` en `libc10.so`. Con torch primero, PyTorch y Stable Baselines funcionan, pero scikit-learn falla después con el mismo error en su `libgomp`. Las importaciones aisladas pasan; el uso conjunto de estas librerías en un proceso aún requiere diagnóstico. No se aplicaron cambios de entorno persistentes ni soluciones al lock.
- **Etiqueta de plataforma NVIDIA:** `uv pip check` comprobó 149 paquetes y reportó una incompatibilidad: `nvidia-cusparselt-cu13` construido para otra plataforma. Su wheel declara `py3-none-manylinux2014_sbsa`, aunque la biblioteca ELF es AArch64 (183). La reinstalación no elimina el aviso; no equivale a un fallo observado en la pequeña prueba CPU de torch.
- El VPS es CPU-only/headless: renderizado gráfico real, audio y GPU no validados. No se instalaron librerías del sistema, ejecutaron entrenamientos, descargaron datasets/recursos externos ni configuraron CUDA.
- Quarto disponible; integración Jupyter y render completo no probados en el VPS. El Mac mini había validado Quarto 1.8.27 y Python 3.12.15 con MPS disponible.
- `git diff --check`: correcto. Sin cambios locales en `AGENTS.md`, `PROJECT.md`, dependencias ni archivos académicos.

## Siguiente paso

El VPS permite pruebas básicas CPU y entornos sin renderizado, pero no está plenamente validado para combinar PyTorch y scikit-learn en el mismo proceso. Consultar al usuario antes de cambiar dependencias o aplicar soluciones para TLS/ARM64. Para retomar desde otro equipo, actualizar desde GitHub; este `STATUS.md` permanece local hasta que se autorice su publicación. Continuar módulo 1 según pendientes académicos y ejecutar `quarto render` después de editar fuentes.
