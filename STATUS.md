# STATUS.md

## Punto de control

- **Actualizado:** 2026-10-16, zona horaria America/Bogota.
- **Rama y commit base:** `main`, `f233f35` — `feat: add Pacman experiment workspace`.
- **Sincronización VPS (2026-10-16):** `git fetch --prune origin` correcto; rama local un commit detrás de `origin/main`, sin commits divergentes. Existía únicamente una edición local en `STATUS.md` con el punto de control anterior; se conservó en un stash llamado `preserve VPS checkpoint before sync 2026-10-16` antes de integrar mediante `git pull --ff-only origin main` (`5c0b113` → `f233f35`). Su información histórica se recoge abajo; el stash se conserva como respaldo.
- **Punto de control local preservado (2026-10-14):** sincronización VPS mediante avance directo de `eecdd91` a `5c0b113`; comparación final `HEAD...origin/main`: `0 0`, `git diff --check` correcto, sin cambios de dependencias ni fuentes Quarto.
- **Verificación actual:** antes del commit, `HEAD...origin/main`: `0 0`; revisión de `git diff` y `git diff --check` correctas. Mediante `uv run --no-sync python` se extrajeron las métricas de las siete salidas y se completaron `resultados/resumen.csv` y la tabla de resultados de `reporte/reporte_pacman.md`, incluyendo derrotas. Se comprobaron 20 cortes de entrenamiento y 10 partidas de evaluación por caso; cada promedio coincide con sus puntajes y cada conteo de victorias/derrotas con su registro. CSV releído correctamente y siete filas de resultados presentes en el reporte. Las observaciones visuales siguen pendientes. No cambiaron dependencias ni fuentes Quarto; no se ejecutaron experimentos ni se renderizó. El estudiante autorizó guardar y subir los tres archivos a GitHub. La recomendación de parámetros se mantiene únicamente en la conversación.
- Se leyeron `AGENTS.md`, `PROJECT.md` y `STATUS.md`. GitHub sigue siendo la fuente de verdad.
- Se creó la estructura reproducible `laboratorios/modulo_1` a `laboratorios/modulo_8`; cada módulo incluye `originales/` para conservar sin cambios los archivos base descargados de la plataforma. Las copias de trabajo y entregables se guardarán en la raíz del módulo correspondiente.
- Se validó y guardó `AI-Pacman-Projects.zip` en `laboratorios/modulo_1/originales/`; su copia de trabajo se extrajo en `laboratorios/modulo_1/pacman/` y el procedimiento quedó documentado en `laboratorios/modulo_1/README.md`. La copia extraída se ignora en Git porque es material derivado reproducible y el código original contiene numerosos problemas de espacios finales.
- Se consolidaron el enunciado, la preparación, el comando, el resultado de ejemplo y la lista de comprobación de la actividad en `laboratorios/modulo_1/INSTRUCCIONES.md`, sin resolver el análisis solicitado al estudiante.
- Se preparó la estructura de experimentación en `laboratorios/modulo_1/PRUEBAS.md`, `resultados/` y `reporte/`: siete comandos con semilla fija, una matriz CSV vacía y un borrador del reporte con preguntas guía.
- El estudiante ejecutó las siete configuraciones de Pacman con la opción `-f` y confirmó explícitamente el uso de semilla fija. Las siete salidas están completas en `laboratorios/modulo_1/resultados/`, con 20 cortes de entrenamiento y 10 partidas de evaluación por caso. Las métricas de primeras/últimas 100 partidas, promedio de evaluación y victorias/derrotas ya están completas en `resultados/resumen.csv` y en la tabla del reporte; las observaciones visuales siguen pendientes de completar por el estudiante. Las salidas originales se conservaron sin cambios.
- No se modificaron fuentes académicas ni resultados generados de Quarto.

## Estado académico observado

- Libro con portada y ocho módulos; módulo 1 en desarrollo, módulos 2–8 con plantilla pendiente.
- Bibliografías con marcadores; `laboratorios/` contiene la estructura de los ocho módulos y el laboratorio de Pacman del módulo 1, con ZIP original, instrucciones, siete salidas de experimentos y un borrador del reporte. La copia extraída de Pacman está ignorada y debe reconstruirse en cada equipo según el README del laboratorio. Sin notebooks ni scripts Python independientes versionados.
- PDF académico versionado; el punto de control anterior registró 3 páginas sin texto extraíble. No se volvió a inspeccionar.
- No se editaron fuentes académicas ni se renderizó el libro durante la validación del VPS.
- **Avance del curso informado por el estudiante:** semana 2, correspondiente al módulo 2.

## Sesiones recurrentes

- **Zona horaria de referencia:** `America/Bogota` (`UTC-05`).
- **Sesión síncrona con el profesor:** todos los jueves, de 07:00 a 08:30.
- **Tutorías:** lunes, jueves y viernes, de 19:00 a 20:00.
- **Festivos:** el estudiante indicó “sin tener en cuenta los festivos”. Queda pendiente precisar si esto significa que las tutorías se mantienen durante los festivos o que el horario informado todavía no excluye/corrige esas fechas.

## Contenido observado del módulo 1

- **Título en la plataforma:** Introducción a el aprendizaje por refuerzo.
- **Resumen de progreso mostrado:** quedan 19 min de videos, 1 h 55 min de lecturas y 1 evaluación calificada pendiente.
- **Fuente:** tres capturas de la plataforma del curso aportadas por el estudiante el 2026-10-14.

### Objetivos de aprendizaje

1. Analizar las limitaciones del aprendizaje por refuerzo.
2. Entender los diferentes dominios de aplicación del aprendizaje por refuerzo.
3. Identificar las técnicas del aprendizaje por refuerzo, sus necesidades y sus limitaciones.
4. Identificar los tres componentes fundamentales de los sistemas de aprendizaje por refuerzo.

### Secciones y recursos

- **Bienvenida al curso:** sección marcada como completada; sus elementos internos no se muestran en las capturas.
- **Introducción al Aprendizaje por refuerzo:**
  - Motivación y Teoría de aprendizaje por refuerzo — video, 6 min, completado.
  - Lecturas de referencia de la semana — lectura, 30 min, completada.
  - Aprendizaje por refuerzo en la inteligencia artificial — complemento no calificado, 20 min, completado.
  - Componentes de aprendizaje con refuerzo — video, 9 min, completado.
  - Definición del aprendizaje por refuerzo — tarea calificable, enviada y calificada con 100 %.
  - Aplicaciones del aprendizaje por refuerzo en la industria — tarea calificable por compañeros de práctica, 1 h; no se observa marca de completado.
- **Aprendizaje por refuerzo: modelos y uso:**
  - Modelos — video, 10 min; aparece la opción “Reanudar”.
  - Caracterización del aprendizaje por refuerzo — tarea calificable, enviada y calificada con 100 %.
- **Aplicaciones del aprendizaje por refuerzo:**
  - Videojuegos — video, 5 min.
  - Sector salud — complemento no calificado, 20 min.
  - Ciudades inteligentes — video, 3 min.
  - Otras aplicaciones — complemento no calificado, 20 min.
- **Perspectivas al futuro:**
  - Retos del Aprendizaje por Refuerzo — lectura, 40 min.
  - Direcciones — complemento no calificado, 15 min.
  - Consideraciones éticas del aprendizaje por refuerzo — cuadro de aviso de la discusión, 30 min.
  - Uso de agentes de aprendizaje por refuerzo — tarea calificable, 1 h 30 min, pendiente; vence el 20 de octubre a las 23:59 (`-05`).
- **Proyecto del curso:**
  - Definición del proyecto — lectura, 20 min.
  - Proyecto del curso — lectura, 30 min.
- **Cierre de la semana:**
  - Cierre — video, 1 min, completado.
  - Sesión de discusión — lectura, 15 min.
  - Sesiones de la semana — lectura, 10 min.

## Contenido observado del módulo 2

- **Título en la plataforma:** Bandits!
- **Resumen de progreso mostrado:** quedan 22 min de videos, 2 h de lecturas y 6 evaluaciones calificadas pendientes.
- **Objetivos de aprendizaje:** no visibles en las capturas porque el panel aparece contraído; no se infieren.
- **Fuente:** tres capturas de la plataforma del curso aportadas por el estudiante el 2026-10-14.

### Secciones y recursos

- **Introducción a la semana:**
  - Introducción — video, 1 min.
  - Lecturas de referencia de la semana — lectura, 40 min.
- **Bandidos de k-brazos:**
  - Problemas de optimización de escogencia — video, 8 min.
  - Tutorial: Construcción de bandidos de K-brazos — laboratorio, 1 h.
  - Exploración vs explotación — video, 5 min.
- **Quiz — 2 evaluaciones calificadas pendientes:**
  - Tipos de aprendizaje — tarea calificable, 25 min; vence el 27 de octubre a las 23:59 (`-05`).
  - Exploración v. Explotación — tarea calificable, 15 min; vence el 27 de octubre a las 23:59 (`-05`).
- **Práctica de bandidos 1:**
  - Pen & paper: Bandidos 1 — tarea de práctica, 15 min, sin calificación visible.
  - Respuestas P&P1 — lectura, 10 min.
- **Ética — 1 evaluación calificada pendiente:**
  - Evaluación vs. Instrucciones — lectura, 40 min.
  - Ética en la evaluación de instrucciones — tarea calificable, 20 min; vence el 27 de octubre a las 23:59 (`-05`).
- **Algoritmos:**
  - Bandidos no estacionarios — video, 4 min.
  - Pen & paper: Bandidos 2 — tarea de práctica, 15 min, sin calificación visible.
  - Respuestas P&P2 — lectura, 10 min, bloqueada en la captura.
- **Práctica — 3 evaluaciones calificadas pendientes:**
  - K-Bandidos con epsilon decay — actividad de programación, 3 h; vence el 27 de octubre a las 23:59 (`-05`).
  - K-bandidos no estacionarios — actividad de programación, 3 h; vence el 27 de octubre a las 23:59 (`-05`).
  - Conformación equipos de trabajo — tarea calificable, 5 min; vence el 27 de octubre a las 23:59 (`-05`).
- **Cierre de la semana:**
  - Cierre de la semana — video, 2 min.
  - Sesión de discusión — lectura, 10 min.
  - Sesiones de la semana — lectura, 10 min.

### Carga y relación con los entregables

- Las seis evaluaciones calificadas pendientes coinciden con los seis entregables del 27 de octubre registrados en el calendario general.
- Las duraciones explícitas de esas evaluaciones suman 7 h 5 min: 1 h 5 min de tareas breves y 6 h de actividades de programación.
- La plataforma resume 22 min de videos y 2 h de lecturas pendientes. Las duraciones individuales visibles de los videos suman 20 min; se conserva el resumen de 22 min como dato de la plataforma y se deja la diferencia sin interpretar.

## Calendario de entregables

- **Fuente:** dos capturas de la plataforma del curso aportadas por el estudiante el 2026-10-14.
- Las capturas no muestran el año. Se interpreta provisionalmente que corresponden al ciclo actual de 2026; el año queda pendiente de confirmación.
- Todas las horas están expresadas en el huso `-05` mostrado por la plataforma. Salvo una excepción indicada abajo, la hora límite es 23:59.
- Los pesos observados suman 100 %.

| Fecha límite | Entregable | Tipo | Peso | Estado observado |
|---|---|---|---:|---|
| 20 oct. | Definición del aprendizaje por refuerzo | Tarea calificable | 1 % | Calificado: 100 % |
| 20 oct. | Caracterización del aprendizaje por refuerzo | Tarea calificable | 1 % | Calificado: 100 % |
| 20 oct. | Uso de agentes de aprendizaje por refuerzo | Tarea calificable | 1 % | Sin calificación visible |
| 27 oct. | Tipos de aprendizaje | Tarea calificable | 1 % | Sin calificación visible |
| 27 oct. | Exploración v. Explotación | Tarea calificable | 1 % | Sin calificación visible |
| 27 oct. | Ética en la evaluación de instrucciones | Tarea calificable | 1 % | Sin calificación visible |
| 27 oct. | K-Bandidos con epsilon decay | Actividad de programación | 6 % | Sin calificación visible |
| 27 oct. | K-bandidos no estacionarios | Actividad de programación | 6 % | Sin calificación visible |
| 27 oct. | Conformación equipos de trabajo | Tarea calificable | 1 % | Sin calificación visible |
| 3 nov. | Aprendizaje por refuerzo o no? | Tarea calificable | 1 % | Bloqueado |
| 3 nov. | Laboratorio MDPs | Actividad de programación | 5 % | Bloqueado |
| 10 nov. | Ejercicio iteración de valores | Actividad de programación | 6 % | Bloqueado |
| 10 nov. | Ejercicio iteración de políticas | Actividad de programación | 6 % | Bloqueado |
| 17 nov. | Diferencias entre enfoques basados en modelos y libres de modelos | Tarea calificable | 1 % | Bloqueado |
| 17 nov. | Agentes de Monte Carlo | Actividad de programación | 5 % | Bloqueado |
| 17 nov. | Ambiente, estados y acciones | Tarea en equipo calificable | 13 % | Bloqueado |
| 24 nov. | Aprendizaje utilizando SARSA | Actividad de programación | 6 % | Bloqueado |
| 1 dic. | Implementación agentes de q-learning | Actividad de programación | 6 % | Bloqueado; vence 23:48 -05 |
| 1 dic. | Evaluación agentes de q-learning | Tarea calificable | 1 % | Bloqueado |
| 4 dic. | Entrega final del proyecto | Tarea en equipo calificable | 31 % | Bloqueado |

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

Completar las observaciones visuales del estudiante en `laboratorios/modulo_1/resultados/resumen.csv` y en la tabla de `reporte/reporte_pacman.md`; las métricas numéricas ya están completas y verificadas. Después, desarrollar la introducción, metodología, análisis propio y conclusiones del reporte, exportarlo a PDF y revisar la entrega antes del 20 de octubre. Las siete configuraciones se ejecutaron con `-f`; una única semilla permite reproducibilidad y comparación controlada, pero no mide variabilidad entre corridas. Después, guardar los notebooks originales de las prácticas de bandidos en `laboratorios/modulo_2/originales/` y trabajar sobre copias en `laboratorios/modulo_2/`. El VPS permite pruebas básicas CPU y entornos sin renderizado, pero no está plenamente validado para combinar PyTorch y scikit-learn en el mismo proceso. Consultar al usuario antes de cambiar dependencias o aplicar soluciones para TLS/ARM64. Para retomar desde otro equipo, actualizar desde GitHub. Planificar el módulo 2 dando margen suficiente a sus dos actividades de programación de 3 h, que vencen junto con otras cuatro evaluaciones el 27 de octubre. Ejecutar `quarto render` después de editar fuentes académicas.
