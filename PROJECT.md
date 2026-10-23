# PROJECT.md

## Identidad del proyecto

- **Materia:** Aprendizaje por Refuerzo.
- **Programa:** Maestría en Inteligencia Artificial, Universidad de los Andes.
- **Repositorio remoto:** `https://github.com/JohnReyes02/maestria-ia-rl.git`.
- **Rama principal y remota predeterminada:** `main` / `origin/main`.
- **Fuente de verdad compartida:** GitHub.
- **Formato principal:** libro HTML de Quarto en español.

## Estructura real

```text
.
├── _quarto.yml                  # Configuración y navegación del libro
├── index.qmd                    # Portada e índice del curso
├── modulo_1.qmd ... modulo_8.qmd
│                                # Fuentes de los ocho módulos
├── references.bib               # Bibliografía general, aún como marcador
├── references_modulo_*.bib      # Bibliografía por módulo
├── styles.css                   # Estilos del libro
├── laboratorios/                # Ocho módulos; Pacman y sus pruebas en modulo_1/
├── autoaprendizaje/rl_lab/      # App local de fundamentos y bandidos
├── S2C2_aprendizaje-por-refuerzo.pdf
│                                # Documento académico fuente de 3 páginas
├── pyproject.toml               # Metadatos y dependencias Python directas
├── uv.lock                      # Resolución reproducible de dependencias
├── requirements.txt             # Exportación derivada de uv, sin hashes
├── .python-version              # Python 3.12.15
└── .vscode/settings.json        # Selección de .venv y uso de uv en VS Code
```

Directorios locales generados e ignorados:

- `.venv/`: entorno virtual creado por `uv`.
- `.quarto/`: caché y metadatos de Quarto.
- `docs/`: salida HTML del libro, configurada mediante `output-dir`.
- `_site/`: salida alternativa de Quarto, si llega a generarse.

No hay actualmente notebooks, datasets, flujo de CI/CD, contenedor ni `Makefile` versionados. `autoaprendizaje/rl_lab/` contiene una aplicación Streamlit independiente del libro, un núcleo Python reutilizable y pruebas automatizadas. `laboratorios/` contiene la estructura de los ocho módulos; `modulo_1/` incluye el ZIP original de Pacman, README, instrucciones, plan de once pruebas, salidas, resumen CSV e informe. La copia extraída del código original permanece ignorada por Git.

El experimento comparativo de Pacman conserva siete configuraciones en `smallGrid` y dos en cada uno de `mediumGrid` y `mediumClassic`, con 2000 episodios de entrenamiento, diez de evaluación y `-f`. Las métricas están consolidadas y el informe `.qmd` contiene análisis, limitaciones y conclusiones, pendientes de lectura final del estudiante. Las capturas ilustran los tableros; no se inventaron observaciones de trayectorias. Consultar `STATUS.md` para el punto de continuación y `laboratorios/modulo_1/PRUEBAS.md` para los comandos.

El entregable de Pacman se redacta en `laboratorios/modulo_1/reporte/reporte_pacman.qmd`. Su configuración local de Quarto genera un PDF con Typst en `reporte/_salida/`, ignorado por Git, sin modificar el libro del curso. El `.md` previo se conserva como referencia. Consultar `reporte/README.md` para completar y exportar la plantilla.

## Laboratorios del módulo 2

El tutorial de construcción de bandidos y los dos laboratorios (epsilon decay y recompensas no estacionarias) tienen páginas `.qmd` en `laboratorios/modulo_2/`, integradas en el menú del módulo 2 y enlazadas desde `modulo_2.qmd`. Siguen la organización del libro de `ml-no-supervisado`. Se muestran sin ejecutar código; los originales y sus conversiones previas permanecen intactos en `originales/`. Las prácticas Pen & Paper conservan sus directorios separados. Consultar `laboratorios/modulo_2/README.md` para las rutas y la restricción académica vigente.

## RL Lab de autoaprendizaje

`autoaprendizaje/rl_lab/` es una aplicación web local en español, separada de la navegación y las fuentes Quarto. Incluye fundamentos, análisis de solo lectura de los once casos de Pacman, comparaciones guiadas de bandidos estacionarios y no estacionarios y un sandbox con descargas CSV/JSON generadas en memoria.

El motor de simulación conserva configuraciones, semillas y métricas sin depender de Streamlit. La aplicación no escribe resultados automáticamente. Para iniciarla desde la raíz:

```bash
uv run streamlit run autoaprendizaje/rl_lab/app.py
```

Las instrucciones y pruebas están documentadas en `autoaprendizaje/rl_lab/README.md`.

## Configuración de Quarto

`_quarto.yml` define un proyecto `book` con:

- idioma español;
- ocho módulos en orden, cada uno como una parte del libro;
- salida en `docs/`;
- ejecución con `freeze: auto`;
- HTML con temas `cosmo` y `darkly`, búsqueda, tabla de contenido y copia de código;
- hoja de estilos `styles.css`.

Las fuentes editables son los archivos `.qmd`, `.bib` y `styles.css`. `docs/` es salida generada y no se versiona con la configuración actual.

## Entorno Python

- **Versión del proyecto:** Python `>=3.12,<3.13`.
- **Versión solicitada localmente:** `3.12.15`.
- **Administrador:** `uv`.
- **Archivos canónicos:** `pyproject.toml` y `uv.lock`.
- **Exportación secundaria:** `requirements.txt`, generado por `uv export`.

Dependencias directas declaradas:

- `gymnasium`
- `jupyter`
- `matplotlib`
- `numpy`
- `pandas`
- `pygame`
- `scikit-learn`
- `seaborn`
- `stable-baselines3`
- `streamlit`
- `tensorboard`
- `torch`

Crear o sincronizar el entorno:

```bash
uv sync --locked
```

Ejecutar herramientas Python dentro del entorno:

```bash
uv run python
uv run jupyter lab
```

Cambiar dependencias:

```bash
uv add <paquete>
uv remove <paquete>
uv lock
uv sync
uv export --format requirements.txt --no-hashes --output-file requirements.txt
```

No edites `uv.lock` ni `requirements.txt` manualmente.

## Trabajo con el libro

Quarto no forma parte de las dependencias Python y debe instalarse por separado en cada equipo.

```bash
quarto --version
quarto preview
quarto render
```

`quarto preview` sirve para edición interactiva. `quarto render` genera el sitio completo en `docs/` y es la validación mínima para cambios en `.qmd`, bibliografías, estilos o `_quarto.yml`.

## Flujo entre equipos

Antes de empezar:

```bash
git status --short --branch
git fetch --prune origin
git rev-list --left-right --count HEAD...origin/main
uv sync --locked
```

El resultado `0 0` del último comando de Git indica que la rama local y `origin/main` coinciden. Si hay cambios locales o divergencia, revísalos antes de ejecutar `git pull`.

Al terminar una unidad de trabajo:

1. Actualiza `STATUS.md` con el punto de continuación.
2. Ejecuta las verificaciones pertinentes.
3. Revisa el diff y confirma que no contiene artefactos generados ni datos sensibles.
4. Haz commit y push solo con autorización explícita.
5. En el siguiente equipo, trae desde GitHub antes de continuar.

## Consideraciones de portabilidad

- `uv` puede instalar la versión de Python solicitada si no existe localmente; el Python global no debe usarse como referencia.
- Quarto se instala fuera de `uv`, por lo que su versión puede variar entre Mac mini, MacBook y VPS. Conviene comprobarla al diagnosticar diferencias de renderizado.
- `pygame` y algunos entornos de Gymnasium requieren librerías gráficas del sistema. En un VPS sin pantalla puede ser necesario ejecutar sin renderizado, usar un backend no interactivo o instalar dependencias del sistema.
- La resolución actual de `torch` incluye paquetes CUDA condicionados a Linux. En un VPS sin GPU esto puede aumentar considerablemente el tiempo, espacio y tráfico de `uv sync`; no debe cambiarse sin comprobar primero las necesidades de los laboratorios.
- El archivo `uv.lock` incluye resoluciones por plataforma y es el mecanismo adecuado para compartir dependencias entre macOS y Linux.
- `docs/` está ignorado. Por tanto, GitHub contiene las fuentes del libro, pero no recibe actualmente el sitio renderizado ni existe un flujo de despliegue automático.
