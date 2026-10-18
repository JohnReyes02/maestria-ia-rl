# STATUS.md

## Planeación conjunta con Deep Learning — 2026-10-18

- Se revisaron `AGENTS.md`, `PROJECT.md` y `STATUS.md` de la materia hermana `deep-learning`, además del seguimiento actual de Refuerzo. Ambos repositorios tienen cambios locales en `STATUS.md`; se preservan. Sus referencias locales de `main` coinciden con `origin/main`; Deep Learning no se volvió a consultar al remoto en esta revisión, por lo que no se afirma una sincronización nueva con GitHub.
- **Semana a planear:** 19–25 de octubre. La propuesta anterior de recuperación de Refuerzo debe ajustarse a la carga conjunta y a los turnos laborales, todavía no disponibles en los documentos consultados. Se solicitó al estudiante la rotación o los turnos diarios con entrada/salida, traslados y descanso tras turnos nocturnos. No hay calendario por horas confirmado.
- **Urgente, 20 oct.:** subir PDF de Pacman y completar cuestionario sumativo de fundamentos de redes neuronales en Deep Learning (45 min), según el avance más reciente. El STATUS de Deep Learning conserva además un pendiente histórico de cuestionario de introducción del módulo 1 (30 min) y lecturas: confirmar si continúa vigente, sin darlo por completado ni ignorarlo por asumir que pertenece al cierre del módulo 2.
- **27 oct.:** cinco evaluaciones pendientes de bandidos (el formulario del equipo ya fue enviado); cuestionario de CNN (45 min) y Laboratorio CNN Parte 2 (3 h). Incluir la preparación y Laboratorio CNN Parte 1 (3 h).
- **3 nov.:** cuestionario y Laboratorio MDPs de Refuerzo; Miniproyecto 1, cuestionario RNN y Laboratorio RNN Parte 2 de Deep Learning. Evitar trasladar todo el inicio del miniproyecto a la semana de entrega.
- **Carga provisional, no disponibilidad:** recuperación de Refuerzo propuesta en 13 h + módulo CNN con miniproyecto registrado en 11 h 14 min + cuestionario anterior de 45 min + primera aproximación a MDPs de 1 h = aproximadamente 26 h de trabajo individual. Las duraciones de plataforma del miniproyecto no garantizan cubrir diseño, experimentación y reporte; faltan lecturas finales de Refuerzo, carga histórica por confirmar y sesiones en vivo.
- **Sesiones fijas registradas, America/Bogota:** Deep Learning miércoles 21, 07:00–08:30; Refuerzo jueves 22, 07:00–08:30. Tutorías disponibles: Deep Learning lunes/martes 17:30–19:00; Refuerzo lunes/jueves/viernes 19:00–20:00. Seleccionar tutorías según dudas y turnos; no asumir asistencia a todas ni disponibilidad fuera de los turnos.
- **Grupos diferentes:** Refuerzo, equipo de dos con Deisy y formulario enviado. Deep Learning, grupo 37 con dos integrantes y búsqueda de una tercera persona según su STATUS actual; no trasladar automáticamente las reglas de un curso al otro.
- **Criterio provisional:** asegurar primero cierres del 20; distribuir bandidos y CNN durante la semana; abrir enunciados de programación temprano para detectar bloqueos; reservar una primera revisión de MDPs y coordinación del miniproyecto. Ajustar metas y uso del 26–27 a la capacidad real, sin sacrificar descanso para encajar el plan anterior.
- **Verificación:** actualización solo en este STATUS, revisión del diff y `git diff --check`; no se modifica el repositorio de Deep Learning ni se hacen commits, push o renderizados. **Siguiente paso:** recibir los turnos laborales y resolver el pendiente histórico de introducción de Deep Learning para preparar el calendario conjunto viable.

## Contenido del módulo 4 — 2026-10-18

- **Base:** `main`, `2a44caa`; se conservan las ediciones locales de seguimiento de esta sesión. Fuente: dos capturas aportadas por el estudiante hoy.
- **Título:** Planeación. Resumen mostrado: 32 min de videos, 2 h 30 min de lecturas y dos evaluaciones calificadas pendientes. No se observan marcas de completado en los recursos listados; el resaltado de Introducción no se interpreta como finalización.
- **Objetivos:** evaluar las técnicas de progreso de aprendizaje por medio de evaluación e iteración de políticas; desarrollar la técnica de programación dinámica para resolver MDPs.

| Sección | Recurso | Tipo y duración | Vencimiento o estado observado |
|---|---|---|---|
| Introducción | Introducción | Video, 2 min | Sin marca de completado visible |
| Introducción | Lecturas de referencia de la semana | Lectura, 40 min | Sin marca de completado visible |
| Programación dinámica | Programación dinámica | Video, 13 min | Sin marca de completado visible |
| Funciones de valor | Iteración de valores | Video, 5 min | Sin marca de completado visible |
| Funciones de valor | Tutorial Iteración de valores | Laboratorio, 2 h | Sin marca de completado visible |
| Funciones de valor | Ejercicio iteración de valores | Programación, 3 h | Pendiente; 10 nov., 23:59 (-05); peso previo: 6 % |
| Iteración de políticas | Iteración de políticas | Video, 8 min | Sin marca de completado visible |
| Iteración de políticas | Tutorial Iteración de políticas | Laboratorio, 2 h | Sin marca de completado visible |
| Iteración de políticas | Comparación entre valores y políticas | Complemento no calificado, 15 min | Sin marca de completado visible |
| Iteración de políticas | Ejercicio iteración de políticas | Programación, 3 h | Pendiente; 10 nov., 23:59 (-05); peso previo: 6 % |
| Iteración de políticas | Solución Assignment MDPs | Lectura, 10 min | Sin marca de completado visible |
| Cierre de la semana | Cierre | Video, 2 min | Sin marca de completado visible |
| Cierre de la semana | Sesiones de discusión | Lectura, 1 h 30 min | Sin marca de completado visible |
| Cierre de la semana | Grabación Sesión 4 | Lectura, 10 min | Sin marca de completado visible |

- Las duraciones individuales de videos suman 30 min frente a 32 min del resumen; se conservan ambos valores sin explicar la diferencia. Las lecturas suman 2 h 30 min, coincidentes con el resumen.
- **Carga nominal:** 13 h 17 min usando el resumen de videos, lecturas, 4 h de tutoriales, 6 h de evaluaciones y complemento de 15 min. Tiempo orientativo de plataforma; no incluye margen adicional de aprendizaje o depuración. Las fechas no muestran año; se mantiene 2026 como interpretación provisional.
- Las dos evaluaciones se muestran pendientes en las capturas nuevas; sustituyen el estado bloqueado del calendario anterior. No se han recibido enunciados detallados ni notebooks de estas actividades.
- **Implicación para el plan (sugerencia):** priorizar módulo 2 y abrir módulo 3 durante el 19–25 de octubre; concentrar MDPs del 26 de octubre al 1 de noviembre (unas 7 h 26 min nominales, descontando lo adelantado); reservar del 2 al 8 de noviembre para Planeación (unas 13 h 17 min nominales), con margen el 9–10. No son bloques confirmados por el estudiante y deben conciliarse con módulos posteriores, tutorías, proyecto y disponibilidad. Aprovechar los conceptos de MDPs para el diseño del proyecto con Deisy.
- **Verificación:** cambio documental únicamente; revisión del diff y `git diff --check`, sin renderizado, commit ni push. **Continuación:** conocer disponibilidad real, ajustar el plan conjunto y recibir los enunciados de las prácticas de módulo 2 para comenzar la recuperación.

## Registro del equipo y contenido del módulo 3 — 2026-10-18

- **Base:** `main`, `2a44caa`; se conservan las ediciones locales anteriores de este archivo. Sin integración ni publicación.
- **Equipo:** el estudiante confirma que Deisy ya envió el formulario de integrantes. Conformación y envío completados según su confirmación; no hay evidencia de calificación todavía. Este dato reemplaza los pendientes anteriores sobre envío del formulario.
- **Fuente del módulo 3:** dos capturas de la plataforma compartidas hoy. Título: **MDPs**. Resumen mostrado: 31 min de videos, 1 h 20 min de lecturas y dos evaluaciones calificadas pendientes. Las fechas no muestran año; se mantiene la interpretación provisional de 2026.

### Objetivos de aprendizaje del módulo 3

1. Definición de los sistemas de recompensas y su uso dentro de los MDP.
2. Expresar el aprendizaje y objetivo de un agente como un problema de recompensa.
3. Definir el problema de aprendizaje como un proceso de Markov.

### Secciones y recursos observados

| Sección | Recurso | Tipo y duración | Estado o vencimiento visible |
|---|---|---|---|
| Introducción | Introducción | Video, 1 min | Sin marca de completado visible |
| Introducción | Lecturas de referencia de la semana | Lectura, 40 min | Sin marca de completado visible |
| MDPs | Procesos de decisión de Markov | Video, 6 min | Sin marca de completado visible |
| MDPs | Pen & paper: MDPs | Práctica, 15 min | Sin calificación visible |
| MDPs | MDPs y recompensas | Video, 12 min | Sin marca de completado visible |
| MDPs | Aprendizaje por refuerzo o no? | Tarea calificable, 20 min | Pendiente; 3 nov., 23:59 (-05); peso previo: 1 % |
| Ejercicios Practicos | Construcción de Agentes | Video, 8 min | Sin marca de completado visible |
| Ejercicios Practicos | Tutorial construcción de MDPs: ambiente de Gridworld | Laboratorio, 2 h | Sin marca de completado visible |
| Ejercicios Practicos | Laboratorio MDPs | Programación, 3 h | Pendiente; 3 nov., 23:59 (-05); peso previo: 5 % |
| Ejercicios Practicos | Solución Assignment Bandidos | Lectura, 20 min | Sin marca de completado visible |
| Cierre de la semana | Cierre | Video, 2 min | Sin marca de completado visible |
| Cierre de la semana | Sesión de discusión | Lectura, 10 min | Sin marca de completado visible |
| Cierre de la semana | Grabación sesión 3 | Lectura, 10 min | Sin marca de completado visible |

- Las duraciones individuales visibles de videos suman 29 min, mientras el resumen muestra 31 min; se conservan ambos datos sin inferir la causa. Las lecturas suman 80 min y coinciden con el resumen.
- **Carga nominal estimada:** 7 h 26 min usando los 31 min del resumen, 80 min de lecturas, práctica de 15 min, tutorial de 2 h y evaluaciones de 3 h 20 min. Es una suma orientativa de tiempos de plataforma, no una garantía de esfuerzo real.
- Las dos evaluaciones ya se muestran pendientes, en lugar del estado bloqueado observado en las capturas anteriores. Actualizar el calendario general con esa evidencia.
- **Relación sugerida con el proyecto:** aprovechar estados, acciones y recompensas de MDPs/Gridworld para preparar la caracterización de la entrega parcial; no se ha definido ni implementado aún la solución del proyecto.
- **Plan provisional:** mantener la recuperación del módulo 2 como prioridad; reservar esta semana un primer bloque de 60–90 min para introducción a MDPs y lectura del enunciado del laboratorio. Ajustar el calendario combinado al recibir módulo 4 y disponibilidad. La actividad de registro del equipo ya no requiere tiempo de ejecución, solo conservar su confirmación.
- **Verificación y continuación:** revisión documental del diff y `git diff --check`, sin renderizado. No se han recibido los enunciados detallados ni archivos del laboratorio del módulo 3. Siguiente paso: recibir módulo 4 y disponibilidad para concretar la planificación. Sin commit ni push.

## Equipo confirmado por el estudiante — 2026-10-18

- **Base:** `main`, `2a44caa`; se conservan las actualizaciones locales anteriores de este archivo.
- El estudiante confirma que ya tiene equipo con su compañera; buscar compañero deja de ser un pendiente.
- **Compañera:** Deisy Yamile Cantor Gómez.
- Los datos institucionales de contacto e identificación se omiten del repositorio por privacidad.
- **Fuente:** captura compartida por el estudiante en esta conversación. No se ha confirmado el envío del formulario de registro del grupo; mantenerlo como asunto por verificar, con un solo envío por equipo según el enunciado.
- **Verificación:** revisión del diff y `git diff --check`; cambio documental, sin renderizado, commit ni push. Siguiente paso: confirmar si el grupo ya quedó registrado y recibir las actividades de los módulos 3 y 4 para ajustar el plan de recuperación.

## Recuperación del módulo 2 y ampliación del proyecto — 2026-10-18

- **Base:** `main`, `2a44caa`. Se conserva la edición local de este archivo realizada en el turno anterior; no hay integración ni sobrescritura de trabajo. La comparación con GitHub se verificó en esta misma sesión.
- **Avance confirmado:** el estudiante no ha empezado el contenido de la semana 2 / módulo 2. Informa que mañana, 19 de octubre, inicia la semana 3. Compartirá a continuación las actividades de los módulos 3 y 4 para ajustar la planificación.
- **Fuente nueva del proyecto:** tres capturas de «Definición del proyecto» compartidas hoy. Complementan el ambiente de obstáculos descrito abajo.
- Los estudiantes deben implementar el problema en su totalidad. Las etapas incluyen formar equipo, diseñar ambiente/acciones/recompensas y estrategia de solución, e implementar con casos de prueba y análisis.
- **Equipo:** exactamente dos personas; no se permiten grupos individuales. Se reporta mediante Google Forms con un solo envío por grupo. La URL del formulario no es recuperable de la captura. La tabla indica semanas 1–2, pero el texto fija conformación al final de la semana 3: hay una discrepancia interna que debe verificarse junto con el vencimiento previamente registrado del 27 de octubre.
- **Entrega parcial, semana 5:** caracterización de la solución con conjunto de estados explícito (descripción, tipo, rango de valores y otras características), todas las acciones y estados donde cada una es aplicable, y función de recompensa con situaciones estado–acción y valores numéricos.
- **Entrega final, semana 8:** video de la aplicación funcionando, Q-tabla con los valores de estados y acciones, y código completo con funciones para guardar y cargar la Q-tabla. El pequeño reporte de pruebas sigue exigido por la descripción previa del ambiente.
- **Evaluación:** equipo 1 %, definición inicial 13 % y entrega final 31 %; suman 45 % de la nota del curso.
- **Asesoría:** canal dedicado en Slack y tutorías; el texto menciona posibles sesiones síncronas para dudas en semanas 3, 5 y 7. Esta mención no sustituye la tabla de entregas ni establece fechas nuevas.

### Estrategia provisional de recuperación — sugerencia, pendiente de disponibilidad

- Objetivo: cerrar módulo 2 el domingo 25 de octubre y reservar 26–27 para contingencias, antes del plazo registrado del 27. Mantener contacto con el módulo 3 durante esta semana; ajustar su tiempo al recibir las actividades.
- Carga nominal conocida del módulo 2: 7 h 5 min de evaluaciones, 2 h 22 min de videos/lecturas, tutorial de 1 h y dos prácticas de 15 min: aproximadamente 11 h. Proponer 13 h con margen, sin incluir lecturas finales del módulo 1 ni trabajo adicional del módulo 3. Las duraciones de plataforma son orientativas y no garantizan el tiempo real.
- Lunes 19 (2 h): fundamentos de bandidos, estimación de valor y exploración/explotación; iniciar tutorial, descargar y revisar ambos enunciados de programación; comenzar gestión de compañero si aún falta.
- Martes 20 (1 h 30 min): terminar tutorial y práctica P&P1, quiz «Tipos de aprendizaje». Subir también el PDF de Pacman antes del plazo; asignarle un bloque adicional breve.
- Miércoles 21 y jueves 22 (2 h cada día): repasar epsilon decay y desarrollar su actividad de programación, comprobar resultados y completar el quiz «Exploración v. Explotación».
- Viernes 23 y sábado 24 (2 h cada día): bandidos no estacionarios, P&P2 y su actividad de programación; conservar tiempo para ejecución y revisión de resultados.
- Domingo 25 (1 h 30 min): lectura y tarea de ética, confirmar registro del equipo, revisar y completar entregas del módulo 2. Distribuir las lecturas de referencia en los bloques temáticos anteriores; si no caben, usar el margen del 26–27 y reajustar.
- Los bloques son propuestas, no compromisos del estudiante. Revisarlos si las prácticas toman más tiempo; priorizar detectar dudas en los notebooks desde el lunes y llevarlas a tutoría.
- **Verificación y continuación:** actualización documental únicamente, revisión del diff y `git diff --check`; sin renderizado, commit ni push. Recibir actividades de módulos 3 y 4 y disponibilidad del estudiante para convertir esta propuesta en un plan combinado.

## Actualización del estudiante y proyecto del curso — 2026-10-18

- **Base:** `main`, `2a44caa`; árbol limpio antes de esta actualización. En esta sesión se ejecutó `git fetch --prune origin` y se comprobó `HEAD...origin/main`: `0 0`.
- **Módulo 1:** el estudiante confirma que solo falta subir el informe en PDF y completar algunas lecturas finales. Esta confirmación reemplaza los pendientes anteriores de elaboración del informe. No se ha recibido ni revisado el PDF final; el borrador local conserva su contenido anterior y no representa necesariamente la versión final del estudiante. Falta identificar cuáles lecturas siguen pendientes.
- **Entrega:** sigue registrada la fecha del 20 de octubre, 23:59 (`-05`), pendiente de comprobar en la plataforma; no se ha confirmado la subida.
- **Fuente del proyecto:** dos capturas de «Proyecto del curso» compartidas por el estudiante el 2026-10-18. Los siguientes puntos recogen el enunciado, no una implementación ni resultados realizados.

### Requisitos observados del proyecto

- Construir y entrenar un agente de aprendizaje por refuerzo, evaluar su ejecución y validar la efectividad del aprendizaje.
- Ambiente: cuarto de 8 × 8; inicio del agente en `(0,0)`, esquina superior izquierda; objetivo en `(7,7)`, esquina inferior derecha.
- Hay cinco obstáculos que aparecen aleatoriamente y se mueven aleatoriamente en cada paso, posiblemente hacia una nueva posición, al mismo tiempo que el agente decide su acción.
- El agente debe alcanzar el objetivo sin chocar con los obstáculos. Una colisión termina el episodio.
- Movimientos descritos: girar 90° a la izquierda, girar 90° a la derecha o avanzar a la casilla inmediatamente al frente, si es posible.
- El equipo debe definir acciones, estados y sistema de recompensas.
- El entrenamiento debe poder exportarse y cargarse en un agente; el programa debe guardar la memoria del agente, descrita como la Q-tabla.
- Conservar la información de las distintas pruebas y presentar sus resultados en un pequeño reporte.

### Aspectos por precisar antes de implementar

- Orientación inicial, observación disponible para el agente y representación del estado, incluida la orientación y la información de los obstáculos.
- Reglas exactas de movimiento de obstáculos, límites, ocupación de inicio/meta y resolución de colisiones o cruces durante movimientos simultáneos.
- Recompensas y posibles límites de pasos; el fragmento no especifica sus valores ni reglas completas de terminación.
- Código base, rúbrica, formato de entrega y requisitos concretos de cada hito: no aparecen en estas capturas.
- El calendario previo registra conformación de equipos el 27 de octubre, «Ambiente, estados y acciones» el 17 de noviembre (13 %) y entrega final el 4 de diciembre (31 %). Estas fechas provienen de las capturas anteriores, no de la descripción nueva.

- **Trabajo de esta actualización:** se corrigió el seguimiento del módulo 1 y se registraron requisitos y dudas del proyecto en este archivo. Sin cambios al reporte, experimentos, dependencias ni fuentes Quarto. Verificación documental: revisión del diff y `git diff --check`; no requiere renderizado. Sin commit ni push.
- **Continuación:** subir el PDF del módulo 1 y completar las lecturas finales; después, avanzar las actividades del módulo 2 y la conformación del equipo, teniendo presentes los requisitos del proyecto.

## Revisión de resultados en Mac mini — 2026-10-16

- Base de esta revisión: `main`, `143d312` (`docs: complete Pacman experiment results`), integrado desde `f233f35` por avance directo, con árbol inicialmente limpio y comparación posterior con `origin/main`: `0 0`.
- Se contrastaron las siete filas de `resultados/resumen.csv` con sus salidas originales: 20 cortes de entrenamiento y 10 partidas de evaluación por configuración. Coinciden los promedios de las primeras y últimas 100 partidas, los promedios de evaluación y las victorias/derrotas; los promedios de evaluación también se recalcularon desde los puntajes individuales.
- Mejor evaluación observada: `05_alpha_alto`, epsilon 0.10, alpha 0.80, gamma 0.70; promedio 501.6 y 10/10 victorias. El caso base obtuvo 500.5 y 10/10. La diferencia de 1.1 puntos no establece superioridad general con una sola corrida por configuración.
- `02_epsilon_bajo` obtuvo el mejor promedio de las últimas 100 partidas de entrenamiento (449.04) y del entrenamiento completo (135.36), con evaluación 500.2 y 10/10. Comparar entrenamiento y evaluación requiere distinguir las políticas: el código original desactiva epsilon y alpha al terminar el entrenamiento.
- Durante esta revisión no se ejecutaron entrenamientos ni se editaron salidas, CSV, reporte o dependencias. El usuario autorizó publicar esta actualización de `STATUS.md` en `origin/main`.
- Siguiente paso: completar las observaciones visuales y el análisis propio pendientes. Si se desea comprobar la robustez del orden observado, repetir las configuraciones con varias semillas antes de concluir que una es superior de forma general.

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
| 27 oct. | Conformación equipos de trabajo | Tarea calificable | 1 % | Formulario enviado por Deisy, confirmado por el estudiante el 18 oct.; calificación no confirmada |
| 3 nov. | Aprendizaje por refuerzo o no? | Tarea calificable | 1 % | Pendiente, visible en captura del 18 oct. |
| 3 nov. | Laboratorio MDPs | Actividad de programación | 5 % | Pendiente, visible en captura del 18 oct. |
| 10 nov. | Ejercicio iteración de valores | Actividad de programación | 6 % | Pendiente, visible en captura del 18 oct. |
| 10 nov. | Ejercicio iteración de políticas | Actividad de programación | 6 % | Pendiente, visible en captura del 18 oct. |
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

Según la confirmación del estudiante del 2026-10-18, subir el informe PDF del módulo 1 antes del plazo registrado del 20 de octubre y completar algunas lecturas finales aún sin identificar. El borrador local no se actualizó con la versión final. Después, guardar los notebooks originales de las prácticas de bandidos en `laboratorios/modulo_2/originales/` y trabajar sobre copias en `laboratorios/modulo_2/`. Planificar el módulo 2 dando margen a sus dos actividades de programación de 3 h, que vencen junto con otras tres evaluaciones pendientes el 27 de octubre; el formulario de conformación del equipo ya fue enviado. Tener presente la descripción del proyecto registrada al inicio de este archivo y precisar sus reglas antes de implementar. El VPS permite pruebas básicas CPU y entornos sin renderizado, pero no está plenamente validado para combinar PyTorch y scikit-learn en el mismo proceso. Consultar al usuario antes de cambiar dependencias o aplicar soluciones para TLS/ARM64. Para retomar desde otro equipo, actualizar desde GitHub. Ejecutar `quarto render` después de editar fuentes académicas.
