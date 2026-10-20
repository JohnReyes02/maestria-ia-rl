# RL Lab

Aplicación web local para practicar conceptos de aprendizaje por refuerzo sin
modificar ni formar parte del libro Quarto de la materia.

## Contenido

- Fundamentos: agente, entorno, estado, acción, recompensa, política, valor y
  dinámica.
- Caso Pacman: análisis de solo lectura de las once configuraciones existentes.
- Laboratorio guiado: greedy, epsilon-greedy, epsilon decay y bandidos
  estacionarios y no estacionarios.
- Sandbox: experimentos configurables, comparación durante la sesión y descarga
  explícita en CSV o JSON.

## Preparación

Desde la raíz del repositorio:

```bash
uv sync --locked
```

## Ejecución

```bash
uv run streamlit run autoaprendizaje/rl_lab/app.py
```

Streamlit mostrará la dirección local que se debe abrir en el navegador. La
aplicación no requiere conexión externa, autenticación ni base de datos.

## Pruebas

```bash
uv run python -m unittest discover -s autoaprendizaje/rl_lab/tests -v
```

## Persistencia y reproducibilidad

- Cada experimento registra su semilla e hiperparámetros.
- El historial del sandbox se conserva únicamente en la sesión de Streamlit.
- Ningún resultado se escribe automáticamente en el repositorio.
- Las descargas CSV y JSON se generan en memoria y solo se guardan si el usuario
  las solicita desde el navegador.

## Próximas extensiones posibles

El núcleo de simulación está separado de la interfaz para permitir módulos
posteriores de MDP/Gridworld, iteración de valores y políticas, Monte Carlo,
SARSA, Q-learning y el ambiente 8 × 8 del proyecto.
