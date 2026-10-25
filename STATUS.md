# STATUS.md

## Cierre y publicación autorizada — 2026-10-24

- **Base:** `main`, `922c2a8`; fetch correcto y comparación con `origin/main`: `0 0`. El estudiante solicita guardar y actualizar el repositorio, autorizando commit y push; se comunicó el resumen antes de publicar.
- Se guardan el avance académico confirmado, la organización de recursos para ocho semanas, las referencias locales a las grabaciones 1–3 y su exclusión de Git y de los recursos Quarto. Se encontraron cuatro presentaciones aportadas por el estudiante (`semana1.pdf` a `semana4.pdf`), conservadas sin alterar y enlazadas desde sus módulos. Las semanas 5–8 mantienen su espacio pendiente.
- **Verificación de cierre:** cuatro archivos con cabecera PDF válida y enlaces a rutas existentes; Quarto 1.8.27, renderizado completo de 12 páginas correcto; presentaciones copiadas a la salida y datos privados ausentes. Revisión del diff y `git diff --check` correctos. Sin cambios de dependencias; no se incluyen salidas generadas ni archivos privados.
- **Siguiente paso:** completar los dos laboratorios de bandidos para el 27 de octubre de forma independiente conforme a la restricción registrada; después MDPs para el 3 de noviembre. Las grabaciones y claves permanecen únicamente en este equipo y requieren traslado privado para consultarlas en otro.

## Grabaciones de los módulos 1–3 registradas — 2026-10-24

- **Base:** `main`, `922c2a8`; fetch correcto y comparación con `origin/main`: `0 0`. Se preservan los cambios locales de seguimiento y organización de recursos.
- Se registraron los enlaces y claves aportados por el estudiante en `recursos_privados/modulo_1/grabaciones.md` a `recursos_privados/modulo_3/grabaciones.md`, con permisos de lectura/escritura solo para el propietario. La entidad HTML final de la clave del módulo 1 se interpretó como espacio de formato, conservando el ampersand anterior como parte de la clave. No se verificó el acceso en Zoom.
- Las tres páginas del libro indican la ubicación local correspondiente. Se excluyó la carpeta privada mediante `.gitignore` y de los recursos Quarto; documentación de uso actualizada. Los archivos privados no se sincronizan mediante GitHub y deben trasladarse por un medio privado si se necesitan en otro equipo.
- **Verificación:** Quarto 1.8.27, renderizado completo de 12 páginas correcto; tres archivos ignorados por Git, carpeta privada no copiada a `docs/` y ausencia de enlaces y claves en las salidas textuales del libro. Diff revisado y `git diff --check` correcto. Sin commit ni push.
- **Siguiente paso:** comprobar personalmente el acceso a las grabaciones y añadir las presentaciones de cada semana. Se mantienen los pendientes académicos registrados.

## Organización de presentaciones y grabaciones — 2026-10-24

- **Base:** `main`, `922c2a8`; fetch correcto y comparación con `origin/main`: `0 0`. Se conservan las dos entradas locales anteriores de seguimiento.
- A solicitud del estudiante, se revisó la organización de otras materias y se preparó `recursos/modulo_1/presentaciones/` a `recursos/modulo_8/presentaciones/`, siguiendo el patrón de Machine Learning No Supervisado. Se añadieron instrucciones generales y por carpeta y se documentó la convención en `PROJECT.md`.
- Los ocho módulos conservan su sección de sesión síncrona y sus campos de grabación y sesiones complementarias; ahora indican dónde guardar la presentación e incluyen un ejemplo comentado para enlazarla cuando exista. No se añadieron enlaces activos a archivos inexistentes, presentaciones ni grabaciones inventadas. Se mantienen los ocho módulos y su orden.
- **Verificación:** Quarto 1.8.27; renderizado completo correcto de las 12 páginas. Diff revisado y `git diff --check` correcto; salidas generadas ignoradas. Sin cambios de dependencias, commit ni push.
- **Pendiente y siguiente paso:** guardar las presentaciones reales en su carpeta y completar los enlaces de grabaciones en el módulo correspondiente. Se mantienen los pendientes académicos de la entrada siguiente.

## Avance confirmado mediante captura — 2026-10-24

- **Base:** `main`, `922c2a8`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`. Se conserva la actualización local anterior de este archivo.
- **Fuente:** captura de calificaciones aportada por el estudiante hoy. Tipos de aprendizaje, Exploración v. Explotación y Ética en la evaluación de instrucciones aparecen calificadas con **100 %** cada una (peso individual: 1 %). Reemplaza el registro anterior de cinco evaluaciones pendientes del módulo 2.
- **Pendientes del 27 de octubre, 23:59 (-05):** K-Bandidos con epsilon decay y K-bandidos no estacionarios, peso 6 % cada uno; ambos sin estado de envío ni calificación visibles. Se mantiene la restricción académica registrada para su desarrollo independiente.
- Uso de agentes de aprendizaje por refuerzo (Pacman) y Conformación equipos de trabajo aparecen como **Enviado**, todavía sin calificación. Definición y Caracterización del aprendizaje por refuerzo mantienen **100 %** cada una.
- Para el **3 de noviembre, 23:59 (-05)**, Aprendizaje por refuerzo o no? (1 %) y Laboratorio MDPs (5 %) aparecen sin estado de envío ni calificación. La captura no confirma avance en tutoriales, prácticas o lecturas. Las fechas no muestran año; se mantiene la interpretación provisional de 2026.
- **Verificación:** transcripción contrastada con la captura, revisión del diff y `git diff --check` correctos; cambio de seguimiento únicamente, sin renderizado, commit ni push.
- **Siguiente paso:** priorizar los dos laboratorios de bandidos y confirmar su formato de entrega; después continuar con MDPs. Permanecen pendientes de confirmar las notas de los dos envíos y las lecturas finales del módulo 1.

## Revisión de sincronización y pendientes — 2026-10-24

- **Base:** `main`, `922c2a8`; árbol limpio al inicio. `git fetch --prune origin` correcto y comparación `HEAD...origin/main`: `0 0`, sin commits por traer ni publicar.
- Se revisaron las instrucciones, el contexto y el seguimiento, priorizando las confirmaciones más recientes sobre las entradas históricas. Continúan registradas cinco evaluaciones del módulo 2 para el 27 de octubre: Tipos de aprendizaje, Exploración v. Explotación, Ética en la evaluación de instrucciones y los dos laboratorios de bandidos. El formulario del equipo ya fue enviado y Pacman ya fue entregado; sus calificaciones siguen sin confirmar. No se consultó nuevamente la plataforma ni se modificaron estados académicos.
- **Verificación:** revisión documental y del diff; `git diff --check` correcto. Solo se actualiza este seguimiento local, sin renderizado, commit ni push.
- **Siguiente paso:** continuar el tutorial de construcción de bandidos y completar las evaluaciones del módulo 2 de forma independiente, conforme a la restricción registrada; confirmar formato de entrega y pendientes reales en plataforma. Después siguen MDPs (3 de noviembre) y Planeación (10 de noviembre). Las lecturas finales del módulo 1 siguen pendientes de identificación y confirmación.

## Cierre de sesión y publicación autorizada — 2026-10-22

- **Base:** `main`, `c954f52`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`. Había ocho archivos locales pendientes de la integración del módulo 2; se revisaron y conservaron. El estudiante solicita guardar lo pendiente y actualizar el repositorio antes de descansar, autorizando commit y push. Se comunicó el resumen antes de publicar.
- Se guardan las tres páginas de lectura de bandidos, su README, la navegación del libro, los enlaces del módulo 2 y la documentación de contexto y seguimiento. No se cambian respuestas, resultados ni estados de finalización académica.
- **Verificación de cierre:** Quarto 1.8.27; nuevo renderizado completo correcto de las 12 páginas, sin ejecutar el código de los laboratorios. Revisión de los ocho archivos y `git diff --check` correctos. Las salidas generadas permanecen ignoradas; no cambian dependencias.
- **Pendientes y siguiente paso:** al retomar, sincronizar desde GitHub si se cambia de equipo y continuar el tutorial de construcción de bandidos desde el módulo 2. Desarrollar las evaluaciones de forma independiente, respetando la restricción académica registrada, y confirmar el formato de entrega en plataforma. Se mantienen los pendientes del 27 de octubre; la nota de Pacman y las lecturas finales del módulo 1 siguen pendientes de confirmación.

## Laboratorios del módulo 2 integrados en el libro — 2026-10-22

- **Base:** `main`, `c954f52`; árbol limpio al inicio, `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`.
- A solicitud del estudiante, se tomó como referencia la organización de `ml-no-supervisado`: páginas Quarto en la raíz de `laboratorios/modulo_2/` e integración en el menú del módulo. Se añadieron el tutorial de construcción de bandidos, epsilon decay y recompensas no estacionarias; se enlazaron desde `modulo_2.qmd`, junto con las guías existentes de Pen & Paper. Se documentó la organización en el README del módulo y en `PROJECT.md`. Se mantienen los ocho módulos y su orden.
- Se convirtieron mecánicamente las celdas del tutorial y se reutilizaron las conversiones previas de los dos laboratorios. Las copias de lectura ajustan título, metadatos y avisos sobre imágenes ausentes (`Banner.jpg` y `slots.png`). Los originales, las conversiones previas y los archivos de trabajo permanecen intactos. No se completaron ni corrigieron ejercicios, ni se ejecutó código de los laboratorios; `execute.enabled: false` evita ejecutarlo al renderizar. Se mantiene la restricción académica registrada y ninguna actividad se marca como completada.
- **Verificación:** Quarto 1.8.27; renderizado completo del libro correcto (12 páginas). Comparación de las 25 celdas de código con los tres notebooks originales: contenido conservado, salvo espacios finales de presentación. Enlaces locales de las páginas a laboratorios, originales y guías comprobados; `git diff --check` y revisión del diff correctos. Sin cambios de dependencias, commit ni push.
- **Pendientes y siguiente paso:** abrir `quarto preview` y continuar el tutorial; desarrollar las evaluaciones de forma independiente y confirmar el formato de entrega en plataforma, pues Quarto no conserva todos los metadatos `nbgrader`. Los cambios quedan locales para revisión del estudiante.

## Lectura de retos integrada y publicación autorizada — 2026-10-22

- **Base:** `main`, sincronizada con `origin/main` (`0 0`) y árbol limpio al inicio.
- Se ajustó e integró en `modulo_1.qmd` la lectura aportada por el estudiante sobre nueve retos del aprendizaje por refuerzo en el mundo real. Se corrigieron redacción, ortografía y terminología; se organizó el contenido por reto, se añadió una síntesis que conecta agente, entorno, estado, acción, recompensa, política, valor y dinámica, y se incorporaron cinco preguntas de comprensión. Tras un guardado externo que reemplazó temporalmente la sección, se restauró la lectura conservando las marcas de videos completados por el estudiante.
- Se sustituyó el marcador «Lectura 1» por un enlace interno a la lectura y se registraron en `references_modulo_1.bib` las dos referencias indicadas en el texto fuente. En la revisión posterior se verificaron y completaron el evento de 2019 y las páginas y DOI del artículo de 2021 con las fichas académicas disponibles.
- El estudiante solicita actualizar el repositorio y autoriza el commit y push de `modulo_1.qmd`, `references_modulo_1.bib` y `STATUS.md`.
- **Verificación:** Quarto 1.10.18; renderizado completo del libro correcto y citas resueltas en la salida HTML. `git diff --check` y revisión final del diff correctos.
- **Siguiente paso:** lectura y validación académica del estudiante; después, marcarla como completada cuando corresponda.

## Tutorial de bandidos conservado y publicación autorizada — 2026-10-20

- **Base:** `main`, `2f5d754`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`. El único archivo pendiente era `laboratorios/modulo_2/originales/Tutorial-bandidos.ipynb`. El estudiante solicita guardar y actualizar el repositorio, autorizando commit y push.
- Se incorpora el notebook tal como estaba en el directorio de originales, sin modificarlo ni ejecutarlo. Su incorporación no implica que el tutorial ni las evaluaciones del módulo 2 estén completados.
- **Verificación:** formato validado con `nbformat` mediante `uv run --no-sync python`: 14 celdas, nueve de código y ninguna con salidas. SHA-256 del original: `2c65d619a573a2941a3a6e2212ab67aef746ece24fb0717ed057610ebe4f45cb`. Revisión del diff y comprobación de espacios antes del commit; no cambian dependencias ni fuentes Quarto, por lo que no se requiere renderizado.
- **Pendientes y siguiente paso:** retomar el tutorial y los pendientes del módulo 2 para el 27 de octubre, respetando la restricción académica registrada para los laboratorios calificables. Continúan pendientes de confirmación la nota de Pacman y las lecturas finales del módulo 1.

## Cierre de sesión y publicación autorizada — 2026-10-20

- **Base:** `main`, `b94993c`; fetch correcto y comparación con `origin/main`: `0 0`. El estudiante solicita actualizar el repositorio y cerrar la sesión, autorizando commit y push de los tres archivos pendientes.
- Se guardan la fecha fija, el nombre personalizado y la precisión de semilla del informe, su guía actualizada y el seguimiento de entrega y calificaciones. Pacman figura como enviado; las dos primeras actividades tienen 100 % cada una. La nota de Pacman no está confirmada.
- **Verificación:** renderizado Quarto/Typst y revisión visual de las seis páginas completados en esta sesión; la versión con nombre personalizado es visualmente idéntica. Diff revisado y `git diff --check` correcto. No se incluyen PDF ni cachés generados.
- **Continuación:** retomar los pendientes del módulo 2 para el 27 de octubre, respetando las restricciones académicas ya registradas. Las lecturas finales del módulo 1 siguen pendientes de identificar y confirmar.

## Calificaciones confirmadas en plataforma — 2026-10-20

- **Fuente:** captura de la plataforma aportada por el estudiante. «Definición del aprendizaje por refuerzo» y «Caracterización del aprendizaje por refuerzo» figuran como **Calificado**, ambas con **100 %** y peso de **1 %** cada una. «Uso de agentes de aprendizaje por refuerzo» figura como **Enviado**, con peso de **1 %** y sin calificación visible (`--`). La captura confirma el envío del informe de Pacman.
- **Base:** `main`, `b94993c`; fetch correcto y comparación con `origin/main`: `0 0`. Se preservan los cambios locales anteriores.
- **Verificación:** registro documental contrastado con la captura, diff revisado y `git diff --check` correcto. Sin commit ni push.
- **Siguiente paso:** retomar los pendientes del módulo 2; la nota de Pacman queda pendiente de confirmación.

## Informe de Pacman entregado — 2026-10-20

- **Confirmación del estudiante:** el informe `reporte_pacman_edwin.pdf` ya fue entregado en la plataforma. La actividad «Uso de agentes de aprendizaje por refuerzo» queda registrada como entregada; calificación pendiente de confirmación. Esta confirmación reemplaza los pendientes históricos de subir el informe.
- **Base:** `main`, `b94993c`; fetch correcto y comparación con `origin/main`: `0 0`. Se preservan los cambios locales anteriores del informe y su documentación.
- **Verificación:** actualización documental, diff revisado y `git diff --check` correcto. Sin commit ni push.
- **Siguiente paso:** retomar los pendientes del módulo 2 para el 27 de octubre, respetando las restricciones académicas registradas para los laboratorios calificables. Las lecturas finales del módulo 1 siguen pendientes de identificar y confirmar.

## Nombre personalizado del PDF de Pacman — 2026-10-20

- **Base:** `main`, `b94993c`; fetch correcto y comparación con `origin/main`: `0 0`. Se preservan los tres archivos con cambios locales de la revisión anterior.
- A petición del estudiante, el nombre de salida y la guía se ajustaron a `reporte_pacman_edwin.pdf`. PDF regenerado con Quarto/Typst y comprobado con Poppler: seis páginas A4. `git diff --check` correcto; diff revisado. Sin commit ni push.
- **Siguiente paso:** subir `laboratorios/modulo_1/reporte/_salida/reporte_pacman_edwin.pdf` y confirmar el envío.

## Revisión final y regeneración del PDF de Pacman — 2026-10-20

- **Base:** `main`, `b94993c`; árbol limpio al inicio, `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`.
- A solicitud del estudiante se revisó el informe completo contra el enunciado local, el plan de pruebas, el CSV y las once salidas originales. Coinciden los parámetros documentados, los 220 cortes de entrenamiento, las 110 evaluaciones, las recompensas iniciales/finales, los promedios recalculados y las victorias/derrotas. Ambas tablas coinciden con el CSV y las tres imágenes existen. No se encontraron marcadores pendientes ni inconsistencias en el análisis; se distinguen resultados e hipótesis y se conservan las limitaciones de una semilla y diez evaluaciones por caso.
- Se fijó la fecha del informe en `2026-10-20` y se precisó que `-f` aplica la semilla `cs188`, comprobado en la implementación suministrada. Se actualizó la indicación de fecha en el README. No se modificaron métricas, experimentos ni código del agente.
- **Verificación:** Quarto 1.8.27, renderizado independiente con Typst correcto; PDF de seis páginas A4 sin cifrado, inspeccionado visualmente en su totalidad con Poppler. Tablas, imágenes, texto y numeración legibles, sin recortes ni superposiciones. `git diff --check` correcto y diff revisado. PDF y cachés permanecen ignorados. Sin commit ni push.
- **Siguiente paso concreto:** subir el PDF regenerado en `laboratorios/modulo_1/reporte/_salida/reporte_pacman.pdf` y confirmar el envío. Esta revisión usa el enunciado conservado localmente; no se volvió a consultar la plataforma ni se confirmó una rúbrica adicional de tutoría. El envío sigue pendiente.

## Revisión integral y publicación autorizada — 2026-10-20

- **Base:** `main`, `9239b55`; `git fetch --prune origin` correcto y comparación previa con `origin/main`: `0 0`.
- El estudiante autorizó revisar y publicar el conjunto completo de cambios locales: RL Lab de autoaprendizaje, dependencia Streamlit y archivos derivados, documentación, transcripciones de trabajo de Pen & Paper y conversión mecánica de los dos notebooks calificables a Quarto. Se mantiene la restricción de no usar IA para resolver esos laboratorios.
- **Verificación de cierre:** 12 pruebas automatizadas correctas; `uv lock --check` y `uv sync --locked --dry-run` correctos; `requirements.txt` coincide con una exportación nueva de `uv`; los tres archivos Python de trabajo compilan; los dos `.qmd` coinciden exactamente con una conversión nueva mediante Quarto; renderizado completo del libro correcto; búsqueda de credenciales sin hallazgos; `git diff --check` y estado final revisados antes de guardar.
- **Siguiente paso concreto:** usar el RL Lab como material de autoaprendizaje y desarrollar las evaluaciones calificables de forma independiente, respetando el código de ética de la plataforma.

## Conversión fiel de notebooks calificables a Quarto — 2026-10-20

- **Base:** `main`, `9239b55`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`. Se preservan sin modificar todos los cambios locales anteriores.
- **Restricción académica confirmada por el estudiante:** las instrucciones de ambos laboratorios incluyen una declaración de no haber utilizado inteligencia artificial ni otros medios no autorizados para resolver la evaluación. En consecuencia, la asistencia queda limitada a la conversión mecánica de formato ya solicitada; no se completarán, corregirán, diagnosticarán ni sugerirán respuestas para estos ejercicios. Los conceptos generales solo podrán estudiarse mediante ejemplos independientes que no resuelvan el material evaluable.
- Se convirtieron mecánicamente `laboratorios/modulo_2/originales/bandidos_epsilon.ipynb` y `laboratorios/modulo_2/originales/bandidos-variables.ipynb` a archivos `.qmd` en el mismo directorio mediante Quarto 1.10.18. No se ejecutaron para la validación final, no se completaron respuestas y no se corrigieron textos, código, pruebas ni metadatos de calificación.
- **Inconsistencias observadas, no corregidas:** ambos documentos referencian `Banner.jpg`, ausente del directorio; el notebook de epsilon contiene errores tipográficos y dice que reducir epsilon inicia la exploración; el de recompensas variables alterna nombres singulares/plurales de funciones, escribe `cummulative_rewards` en el texto aunque la versión anterior usa `cumulative_rewards`, y su descripción de la sumatoria combina el rango 1 a n con los primeros n-1 valores. Los metadatos de los notebooks registran Python 3.10.6, mientras el proyecto usa Python 3.12.x.
- **Verificación:** las salidas guardadas coinciden byte por byte con `quarto convert`; ambas copias temporales renderizaron correctamente a HTML con `--no-execute`. Los notebooks originales permanecen sin cambios y todas sus celdas carecen de salidas y conteos de ejecución. La conversión inversa conserva las 10 y 12 celdas, respectivamente, así como el texto y los metadatos `nbgrader` de las celdas de código; Quarto no conserva los metadatos `nbgrader` de las celdas Markdown. `git diff --check` es correcto para los archivos versionados; los `.qmd` mantienen espacios finales presentes en las fuentes por fidelidad. Diff final revisado. Sin commit ni push.
- **Siguiente paso concreto:** el estudiante puede trabajar sobre los `.qmd` conservando los `.ipynb` originales como referencia; si la plataforma exige entrega `nbgrader`, confirmar el formato aceptado antes de sustituir los notebooks.

## Segunda práctica de bandidos preparada — 2026-10-20

- **Base:** `main`, `9239b55`; se preservan sin modificar los cambios locales anteriores y la práctica Bandidos 1.
- Se creó `laboratorios/modulo_2/pen_and_paper_bandidos_2/` para la práctica **Pen & Paper: Bandidos 2**, identificada por el estudiante. El README conserva el escenario de recomendación de cuatro películas a 20 clientes, los clientes sin recompensa, la secuencia de recomendaciones, el valor inicial 10, `alpha = 0.1` y las formas expandida e incremental de la actualización con paso constante.
- El archivo Python contiene los datos suministrados y la variable `movies`, pero deja sin resolver la respuesta evaluable. Se señala para confirmación la interpretación de la recompensa como valor base más propina.
- **Verificación:** archivo Python compilado y `git diff --check` correcto. No se modificaron Bandidos 1, `modulo_2.qmd`, dependencias, resultados previos ni material original. Sin commit ni push.
- **Siguiente paso concreto:** construir la tabla cliente–película–recompensa y aplicar una actualización secuencial únicamente al valor de la película recomendada.

## Práctica de bandidos del módulo 2 preparada — 2026-10-20

- **Base:** `main`, `9239b55`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`. Se preservan sin modificar los cambios locales previos de RL Lab, dependencias y documentación.
- A petición del estudiante se creó `laboratorios/modulo_2/pen_and_paper_bandidos_1/` con una transcripción de trabajo de los dos ejercicios de la práctica **Pen & Paper: Bandidos 1** observados en las capturas: estimación de recompensas de cuatro caminos y variante con `epsilon = 0.5`.
- El README relaciona el escenario con agente, entorno, estado, acciones, recompensas, dinámica, valor y política; conserva las fórmulas de promedio muestral y actualización incremental y señala las convenciones que deben confirmarse. Los dos archivos Python contienen constantes y la variable `arms`, pero dejan las respuestas evaluables sin resolver.
- **Verificación:** archivos revisados, compilación de ambos módulos Python y `git diff --check`. No se modificaron `modulo_2.qmd`, la estructura de los ocho módulos, dependencias, resultados previos ni material original. Sin commit ni push.
- **Siguiente paso concreto:** construir la tabla hora–factorización–camino–recompensa del ejercicio 1 y confirmar si el intervalo 7–20 incluye ambos extremos antes de calcular `arms`.

## RL Lab independiente de autoaprendizaje — 2026-10-20

- **Base:** `main`, `9239b55`; árbol limpio al inicio, `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`.
- Se creó `autoaprendizaje/rl_lab/` como aplicación web local en español, separada del libro Quarto. Incluye fundamentos con comprobación guiada, análisis de solo lectura de los once casos de Pacman, cuatro comparaciones guiadas de bandidos y un sandbox con historial de sesión y descargas CSV/JSON en memoria.
- El núcleo Python independiente de Streamlit implementa configuraciones reproducibles, políticas greedy, epsilon-greedy y epsilon decay, promedio muestral y alpha constante, bandidos estacionarios y no estacionarios con deriva aleatoria, métricas por paso y resúmenes. La app no escribe resultados automáticamente.
- Se añadió `streamlit>=1.66.0` mediante `uv`; `pyproject.toml` y `uv.lock` son canónicos y `requirements.txt` fue regenerado con `uv export`. `PROJECT.md` y el README propio de la app documentan la arquitectura y ejecución. No se modificaron `_quarto.yml`, los ocho módulos, bibliografías, estilos, `docs/`, código de Pacman ni resultados académicos.
- **Verificación:** 12 pruebas automatizadas correctas, incluidas reproducibilidad, actualizaciones, epsilon decay, deriva no estacionaria, métricas, contrato de los once casos de Pacman, apertura de Streamlit, comparación guiada no estacionaria y descargas del sandbox. Revisión visual local de las cuatro secciones y corrección de cuadrícula/contraste. `uv lock --check`, `uv sync --locked --dry-run`, compilación de los módulos y `git diff --check` correctos; la sincronización seca no propone cambios.
- **Pendiente:** revisión y uso personal del estudiante para decidir ajustes didácticos. No se realizó commit ni push. **Siguiente paso concreto:** iniciar con `uv run streamlit run autoaprendizaje/rl_lab/app.py`, recorrer Fundamentos y ejecutar la comparación «Adaptarse a la no estacionariedad» antes de usar el sandbox; futuras extensiones de MDP/Gridworld permanecerán separadas del libro.

## Cierre del taller de Pacman y autorización de publicación — 2026-10-19

- **Base:** `main`, `f6c2d10`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0` antes de guardar. El estudiante autoriza actualizar el repositorio con los cambios de esta sesión, incluido commit y push.
- **Estado confirmado por el estudiante:** el taller está terminado y solo queda subir el PDF a la plataforma. No se registra como entregado todavía. Considera posibles ajustes de palabras a su estilo; no solicita cambios adicionales de redacción en este cierre.
- Se guardan el informe Quarto completo y su configuración, las capturas, las cuatro pruebas adicionales, el resumen de once casos y la documentación actualizada. Se preserva la salida actual del caso 07, cuya diferencia respecto a HEAD se verificó como tiempos de ejecución únicamente. Los PDF generados y cachés permanecen ignorados; en otro equipo debe regenerarse el PDF con el comando del README del informe.
- **Verificación de cierre:** renderizado Quarto/Typst correcto, métricas de los once casos y tablas verificadas durante esta sesión, PDF de seis páginas revisado visualmente, revisión del diff y `git diff --check`. Sin cambios de dependencias ni a la estructura de los ocho módulos.
- **Siguiente paso único del taller:** subir `laboratorios/modulo_1/reporte/_salida/reporte_pacman.pdf` a la plataforma antes del plazo registrado del 20 de octubre, 23:59 (-05), y confirmar el envío. Después retomar los pendientes del módulo 2 conforme al plan académico; no se consideran completados por este cierre.

## Informe completado para revisión del estudiante — 2026-10-19

- **Base:** `main`, `f6c2d10`; fetch correcto y comparación con `origin/main`: `0 0`. Se preservaron los cambios locales acumulados. Se verificó que la edición previa de `07_gamma_alto.txt` cambia únicamente los tiempos de ejecución; puntajes y recompensas coinciden con la versión de HEAD.
- El estudiante solicitó ayuda explícita para terminar el informe por cansancio y bloqueo, sin referencias a otros archivos dentro de la redacción. Se completaron los cinco apartados de análisis, las limitaciones y las conclusiones en el `.qmd`; se retiraron las instrucciones entre corchetes, comentarios de plantilla, referencias a archivos y el apartado de evidencias que remitía a ellos. Se corrigió «agendes» en el título y se usó «juegos» al describir las evaluaciones.
- No se inventaron observaciones de movimientos. Las tres imágenes se mantienen como ilustraciones de los tableros durante evaluación. La discusión distingue resultados observados de explicaciones posibles, y limita las conclusiones a una semilla y diez juegos por configuración. Se actualizaron PROJECT y los README del laboratorio/informe para reflejar el texto completo.
- **Verificación:** se contrastaron las once filas con las salidas actuales: primeras/últimas 100 recompensas, promedio recalculado de diez puntajes y conteos de victorias/derrotas. Las tablas del `.qmd` se comprobaron contra el CSV; se verificó ausencia de marcadores pendientes y referencias a archivos en el texto. Renderizado Quarto/Typst correcto, PDF revisado visualmente con Poppler, con tabla de resultados completa en una página. Revisión de diff y `git diff --check`. Sin nuevos entrenamientos, cambios de métricas, dependencias, commit ni push.
- **Continuación:** lectura final del estudiante, confirmar alcance exacto de tutoría y plazo en plataforma, y subir el PDF. No se ha confirmado entrega. Las entradas anteriores de redacción pendiente son históricas y quedan reemplazadas por este estado.

## Retiro del aviso de borrador — 2026-10-19

- A petición del estudiante, se retiró el aviso visible «BORRADOR DE TRABAJO» del `.qmd`. Se mantienen las guías de las secciones pendientes; el retiro del aviso no implica que el informe esté terminado.
- **Verificación:** renderizado Quarto/Typst y `git diff --check`. Sin commit ni push. **Continuación:** completar las observaciones, el análisis y las conclusiones con redacción que el estudiante comprenda y pueda explicar.

## Metodología ajustada al alcance introductorio — 2026-10-19

- A petición del estudiante, se simplificó «Agente, entorno y aprendizaje» en el `.qmd`: descripción de los elementos visibles de los tableros, estado y acciones en lenguaje introductorio y separación conceptual de entrenamiento/evaluación. Se retiraron detalles de la representación interna, actualización Q, comportamiento programado de fantasmas y valores exactos de recompensas. Se mantiene que las capturas ilustrativas no demuestran cómo aprende el agente.
- Se eliminó la referencia a nombres `.txt` en «Parámetros y configuraciones» y se simplificó la definición de alpha. Se conservaron las once configuraciones y sus métricas.
- **Base:** `main`, `f6c2d10`; se preservan los cambios locales anteriores. **Verificación:** renderizado Quarto/Typst y `git diff --check`. Sin cambios de resultados, experimentos, dependencias, commit ni push.
- **Continuación:** revisar con el estudiante esta versión introductoria y avanzar en el análisis de los parámetros.

## Metodología completada con la implementación suministrada — 2026-10-19

- **Base:** `main`, `f6c2d10`; fetch correcto y comparación con `origin/main`: `0 0`. Se preservaron los cambios locales, incluida la modificación previa en `resultados/07_gamma_alto.txt`, no editada ni revalidada en esta tarea.
- A solicitud del estudiante, se completó la metodología del `.qmd`: diseño de las once configuraciones, semilla `cs188` aplicada por `-f`, agente tabular, entorno y `RandomGhost`, estado, acciones legales, recompensa como cambio de puntaje, reglas de puntuación, actualización de valores Q, política epsilon-greedy y separación entrenamiento/evaluación. Se definieron epsilon, alpha y gamma y se describió el alcance de las métricas.
- Se contrastó la explicación con `qlearningAgents.py`, `learningAgents.py`, `pacman.py` y `game.py` de la copia suministrada. Se retiraron únicamente las dos guías de metodología ya resueltas; análisis, observaciones y conclusiones siguen pendientes. Los empates aleatorios entre acciones máximas se distinguen de la exploración epsilon-greedy.
- **Verificación:** renderizado Quarto/Typst, revisión visual de metodología y `git diff --check`. Sin cambios a código original, métricas, dependencias, commit ni push.
- **Continuación:** leer y ajustar esta metodología con las palabras del estudiante; redactar el análisis de epsilon usando las métricas observadas. Las capturas siguen siendo ilustraciones de tableros tomadas durante evaluación.

## Propósito y fase de las capturas confirmados — 2026-10-19

- **Base:** `main`, `f6c2d10`; fetch correcto y comparación con `origin/main`: `0 0`. Se preservaron todos los cambios locales, incluida una modificación preexistente en `resultados/07_gamma_alto.txt`, ajena a esta edición y no validada en este turno.
- El estudiante confirma que las tres imágenes fueron capturadas durante evaluación y son representativas de los tableros, no evidencia comparativa de comportamiento. Se creó la sección «Tableros utilizados», se simplificaron sus pies y se aclaró que epsilon y alpha estaban en cero y que los puntajes visibles no son promedios de evaluación. Se retiró la pregunta sobre la fase. Las observaciones propias del comportamiento siguen pendientes en su apartado.
- **Verificación:** renderizado Quarto/Typst y `git diff --check`; se conservaron las imágenes y métricas sin cambios. Sin commit ni push.
- **Continuación:** completar metodología y análisis; no inferir decisiones o superioridad del agente a partir de estas capturas ilustrativas.

## Captura adicional del caso 07 — 2026-10-19

- El estudiante identifica la nueva y última imagen (`reporte/images/paste-4.png`) como caso 07. Se inspeccionó: puntaje mostrado 495. Se añadió encabezado y pie para `smallGrid`, gamma alto, con parámetros de entrenamiento epsilon 0.10, alpha 0.30 y gamma 0.95, centrado y ancho del 38 %. Se conservaron las figuras de los casos 11 y 09.
- **Base:** `main`, `f6c2d10`; se preservan los cambios locales. **Verificación:** renderizado Quarto/Typst, revisión visual de la figura y `git diff --check`. Sin cambios a métricas, experimentos, commit ni push.
- **Pendiente:** confirmar la fase y si el puntaje mostrado corresponde al final de la partida; no se infiere victoria únicamente desde la captura. Completar las observaciones propias.

## Identificación y presentación de capturas — 2026-10-19

- **Base:** `main`, `f6c2d10`; fetch correcto y comparación con `origin/main`: `0 0`. Se conservaron los cambios locales del estudiante y los archivos de imagen originales.
- Según la identificación del estudiante, la primera imagen del informe (`images/paste-1.png`) corresponde al caso 11, `mediumClassic`, con puntaje parcial 132; la segunda (`images/paste-3.png`) al caso 09, `mediumGrid`, con puntaje parcial -33. Se inspeccionaron ambas imágenes.
- Se ajustaron los tamaños manteniendo las proporciones (70 % y 38 % del ancho), el centrado y los pies numerados con identificadores propios. Se retiraron el pie provisional y la instrucción de inserción ya resuelta. Los parámetros se describen como valores de entrenamiento; sigue pendiente confirmar la fase de cada captura.
- **Verificación:** renderizado Quarto/Typst, revisión visual de las figuras y `git diff --check`. Sin modificar píxeles, resultados o dependencias, ni hacer commit o push.
- **Continuación:** confirmar entrenamiento/evaluación para cada captura y completar las observaciones propias y la metodología pendientes.

## Espacio para captura del caso 11 — 2026-10-19

- **Base:** `main`, `f6c2d10`; consulta al remoto correcta y comparación con `origin/main`: `0 0`. Se preservan los cambios locales anteriores.
- Se añadió en Observaciones del `.qmd` un espacio para la captura de `mediumClassic` que el estudiante identifica como caso 11, con puntaje parcial de 132. Incluye pie propuesto, parámetros usados para entrenar y una nota pendiente para identificar entrenamiento o evaluación. La imagen no se insertó todavía; el comentario del editor indica dónde guardarla y cómo incorporarla sin referencias activas a archivos inexistentes.
- **Verificación:** renderizado Quarto/Typst y `git diff --check`; sin modificar resultados, ejecutar experimentos, commit ni push.
- **Continuación:** insertar la imagen y confirmar la fase de la partida; continuar la redacción propia de metodología y observaciones.

## Revisión de introducción y objetivo — 2026-10-19

- **Base:** `main`, `f6c2d10`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`. Se preservan los cambios locales acumulados, incluida la redacción y los ajustes de metadatos realizados por el estudiante en el `.qmd`.
- Se revisó y conservó la introducción redactada por el estudiante. Se retiró su instrucción entre corchetes, se corrigieron «agente de Q-learning» y «desempeño», se precisó «tableros» y se separó el objetivo en un párrafo. Las guías de secciones pendientes y el aviso general de borrador permanecen.
- **Verificación:** renderizado del `.qmd` con Quarto/Typst, revisión de la sección y `git diff --check`. Sin cambios a resultados, experimentos, dependencias, commit ni push.
- **Siguiente paso:** redactar la descripción de agente, entorno, estados, acciones y recompensas en metodología; revisar esa sección antes de retirar su guía. La introducción y el objetivo ya cuentan con texto propio revisado.

## Plantilla Quarto para el entregable PDF — 2026-10-19

- **Base:** `main`, `f6c2d10`; consulta nueva con `git fetch --prune origin` correcta y comparación `HEAD...origin/main`: `0 0`. Se preservaron los cambios locales y las cuatro salidas nuevas de las tareas anteriores.
- A solicitud del estudiante, se creó `laboratorios/modulo_1/reporte/reporte_pacman.qmd` como fuente editable del entregable: metadatos por completar, metodología, las dos tablas de once casos, observaciones y preguntas guía para análisis, limitaciones y conclusiones. No se completó el razonamiento académico ni se inventaron observaciones.
- Se añadió configuración local `reporte/_quarto.yml` para generar el documento independiente con Typst, y `reporte/README.md` con instrucciones. `.gitignore` excluye `_salida/` y la caché local. Se señalaron la fuente nueva y el carácter histórico del `.md` en los README, instrucciones y PROJECT.
- **Verificación:** Quarto 1.8.27 y Typst 0.13.0 disponibles; `quarto render laboratorios/modulo_1/reporte/reporte_pacman.qmd --to typst` correcto. PDF de tres páginas A4 revisado visualmente mediante Poppler; tablas completas y legibles. Se comprobaron las tablas contra el CSV, exclusión de salidas generadas y `git diff --check`. Sin cambios al libro, experimentos, dependencias, commit ni push.
- **Siguiente paso concreto:** editar el `.qmd`, completar nombre, fecha y todos los textos entre corchetes con la redacción y observaciones del estudiante, quitar el aviso de borrador y volver a renderizar/revisar el PDF antes de entregar. El PDF generado ahora es una vista de la plantilla, no un informe listo para subir. Sigue pendiente confirmar el alcance exacto indicado en tutoría y la entrega en plataforma.

## Documentación actualizada tras ampliar los tableros — 2026-10-19

- **Base:** `main`, `f6c2d10`; consulta nueva con `git fetch --prune origin` correcta, comparación `HEAD...origin/main`: `0 0`. Se conservaron las ediciones locales de STATUS/CSV y las cuatro salidas nuevas, sin integrar ni sobrescribir trabajo previo.
- Se actualizaron `laboratorios/modulo_1/PRUEBAS.md`, `README.md`, `INSTRUCCIONES.md` y `resultados/README.md`: once comandos, correspondencia de casos/tableros, presupuesto constante, entrenamiento desde cero, semilla fija, límites de comparación y conservación de salidas al repetir. La indicación de variar el grid se atribuye al reporte del estudiante sobre la tutoría; la pregunta original del entregable se conserva.
- El README distingue la ejecución preliminar sin semilla de los once casos comparativos. Se corrigió `PROJECT.md`, que todavía describía `laboratorios/` como vacío.
- Se actualizaron metodología, configuraciones, tabla de resultados y enlaces del borrador `reporte/reporte_pacman.md`. Se añadieron preguntas guía para tableros y alpha por entorno; las observaciones visuales, explicaciones y conclusiones siguen pendientes del estudiante. No se generó ni revisó un PDF final.
- **Verificación:** con `uv run --no-sync python` se comprobaron once comandos contra parámetros y tableros del CSV, primeras/últimas 100 partidas, promedio calculado desde diez puntajes y victorias/derrotas de las once salidas, correspondencia exacta de ambas tablas del informe, enlaces locales y cierre de bloques de código. Revisión de `git diff` y `git diff --check`. Cambios Markdown únicamente en esta tarea, sin necesidad de renderizar Quarto; sin entrenamientos, cambios de dependencias, commit ni push.
- **Continuación vigente:** completar las observaciones propias y el análisis del informe; confirmar el alcance exacto de la aclaración de tutoría, revisar/exportar el PDF y subirlo antes del plazo registrado del 20 de octubre, 23:59 (-05), previa comprobación en plataforma. Las entradas anteriores describen avances históricos; ya están consolidadas las cuatro pruebas adicionales y actualizados los documentos que aún figuraban pendientes.

## Consolidación de once pruebas de Pacman — 2026-10-19

- **Base:** `main`, `f6c2d10`; `git fetch --prune origin` correcto y comparación con `origin/main`: `0 0`. Se preservan el seguimiento local anterior y las cuatro salidas nuevas sin versionar.
- A solicitud del estudiante, se agregaron los casos 08–11 a `laboratorios/modulo_1/resultados/resumen.csv`, con parámetros según los comandos propuestos en esta conversación, criterio de semilla fija `-f`, métricas de primeras/últimas 100 partidas, promedio de evaluación y victorias/derrotas. Las salidas no registran los argumentos de ejecución; la configuración se identifica por los comandos y nombres de archivo de esta conversación.
- Se añadió `tablero` al final del CSV: `smallGrid` para los siete casos anteriores, `mediumGrid` para 08–09 y `mediumClassic` para 10–11. Se conservaron las métricas originales y las observaciones visuales vacías.
- **Verificación:** cada salida nueva contiene 20 cortes de entrenamiento hasta 2000 episodios, cierre de entrenamiento y 10 evaluaciones; los promedios se recalcularon desde los puntajes y los conteos coinciden con `Record` y `Win Rate`. CSV releído: 11 casos únicos y 12 columnas. Revisión de `git diff` y `git diff --check`, sin cambios de dependencias, renderizado, commit ni push.
- **Siguiente paso:** completar observaciones propias e incorporar los nuevos tableros y resultados al informe. El borrador del informe todavía presenta solo siete pruebas; el README de resultados y el plan inicial también describen las siete originales.

## Aclaración de tutoría sobre Pacman — 2026-10-19

- **Base:** `main`, `f6c2d10`; árbol inicialmente limpio. `git fetch --prune origin` correcto y comparación `HEAD...origin/main`: `0 0`.
- El estudiante informa que en tutoría indicaron incluir variaciones del grid en el entregable de mañana, 20 de octubre. Se registra como información reportada por el estudiante; falta precisar cuáles tableros y cuántas combinaciones requieren.
- Las siete pruebas existentes utilizan `smallGrid`. El enunciado local menciona también `mediumGrid` y `mediumClassic`, pero la pregunta de entrega transcrita no exige explícitamente una matriz de parámetros por tablero. El plan anterior fijó `smallGrid` para aislar el efecto de los parámetros; debe complementarse según la aclaración de tutoría.
- **Sugerencia, no requisito confirmado:** conservar las siete pruebas y comparar primero los otros tableros con los parámetros del caso base, entrenando desde cero en cada uno con el mismo presupuesto y criterio de semilla. No hay ejecuciones nuevas ni resultados adicionales.
- **Verificación:** revisión documental del diff y `git diff --check`; sin cambios a experimentos, informe o fuentes Quarto, sin renderizado, commit ni push.
- **Siguiente paso:** precisar si la tutoría exige variar parámetros en cada tablero o solamente comparar tableros; después completar la experimentación y actualizar el informe antes de exportar/subir el PDF. El estado anterior de «solo falta subir» queda sujeto a esta nueva aclaración.
- **Avance posterior en esta conversación:** aparecen cuatro salidas nuevas sin versionar, preservadas sin cambios. Sus resúmenes finales muestran: `mediumGrid` base, promedio -503.7 y 0/10 victorias; alpha alto, -414.7 y 1/10; `mediumClassic` base, -401.4 y 0/10; alpha alto, -384.7 y 0/10. Todas muestran cierre de entrenamiento y diez resultados de evaluación. Estas métricas todavía no se incorporan al CSV ni al borrador local del informe.
- **Alcance de la evidencia:** las once pruebas permiten discutir parámetros y tableros, sin demostrar superioridad general con una sola corrida y diez evaluaciones por caso. Se recomienda conservar el presupuesto de entrenamiento para la comparación principal; cualquier aumento sería una prueba adicional con archivo propio. Continuación actual: consolidar las cuatro salidas, añadir observaciones propias y completar el análisis del informe; confirmar el alcance exacto pedido en tutoría.

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
| 20 oct. | Uso de agentes de aprendizaje por refuerzo | Tarea calificable | 1 % | Entregado, confirmado por el estudiante el 20 oct.; calificación pendiente de confirmación |
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

El estudiante confirmó el 2026-10-20 que entregó el informe de Pacman del módulo 1; no queda pendiente subirlo. La calificación no está confirmada. Retomar los pendientes del módulo 2 para el 27 de octubre, con los notebooks originales ya conservados y convertidos mecánicamente a Quarto; respetar la restricción registrada de no usar IA para resolver los laboratorios calificables. El formulario de conformación del equipo ya fue enviado. Las lecturas finales del módulo 1 siguen pendientes de identificar y confirmar. Consultar las entradas más recientes para el estado vigente y actualizar desde GitHub al retomar en otro equipo.
