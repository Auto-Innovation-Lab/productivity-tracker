# Productivity Tracker · Innovación Automotriz SpA

Proyecto de revisión de estimaciones de sprints y análisis de productividad del equipo de desarrollo de **Innovación Automotriz SpA** (Vehmax / Spareparts Business / Digital Workshop).

El objetivo es evaluar cómo evolucionan las estimaciones y la productividad del equipo **antes y después de la adopción de IA** (Claude Code) en el flujo de desarrollo, combinando:

- Métricas de actividad en GitHub (commits, líneas de código en ramas de producción)
- Análisis de estimaciones de sprint vs. una base histórica de referencia
- Revisión asistida por Claude Code de nuevos sprints antes de iniciarlos

## Equipo

| Dev | GitHub | Rol | Herramienta IA |
|-----|--------|-----|-----------------|
| Henrique Schraiber | [Ecxpectro](https://github.com/Ecxpectro) | Agentic Engineer | Claude Code |
| Guilherme Reis | [GuilhermeKill](https://github.com/GuilhermeKill) | Agentic QA Engineer | Claude Code |
| Javier Velásquez | [javelasquezb](https://github.com/javelasquezb) | Tech Lead | GPT |

Organización GitHub: [Auto-Innovation-Lab](https://github.com/Auto-Innovation-Lab)

## Estructura del proyecto

```
productivity-tracker/
├── README.md
├── CLAUDE.md                        ← contexto e instrucciones para Claude Code
├── requirements.txt
├── .gitignore
├── data/
│   ├── historial/
│   │   └── Sprint_60.xlsx           ← historial de sprints 18–59 (sin IA)
│   ├── base/
│   │   └── base_estimacion_sprints.xlsx  ← promedios históricos + Meta Sprint + Desafío IA
│   └── sprints/
│       └── README.md                ← cómo subir un sprint nuevo
├── notebooks/
│   ├── 01_github_commits.ipynb      ← análisis de commits por dev
│   ├── 02_lineas_produccion.ipynb   ← líneas de código en ramas de producción
│   └── 03_sprint_review.ipynb       ← análisis de estimaciones por sprint
├── scripts/
│   └── review_sprint.py             ← lanza el review de un sprint con Claude Code
└── reports/
    └── tendencias-equipos-ia.html   ← reporte de tendencias de equipos con IA
```

## Instalación

Requiere Python 3.10+.

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Variables a configurar

Antes de correr los notebooks de GitHub, define las siguientes variables de entorno (o en un archivo `.env` local, que no se sube al repo):

| Variable | Descripción |
|----------|-------------|
| `GITHUB_TOKEN` | Personal Access Token con scope `repo` y `read:org`, para consultar la API de GitHub |
| `GITHUB_ORG` | Organización a analizar (`Auto-Innovation-Lab`) |
| `GITHUB_USERNAME` | Usuario owner (`edesiosantos`) |

## Cómo usar cada notebook

### `notebooks/01_github_commits.ipynb`
Analiza los commits por desarrollador en los repositorios de la organización: cantidad, frecuencia, distribución en el tiempo. Útil para comparar actividad antes/después de adoptar Claude Code.

### `notebooks/02_lineas_produccion.ipynb`
Mide líneas de código agregadas/eliminadas en las ramas de producción (main/master) por dev y por periodo, para complementar el análisis de commits con volumen real de cambios.

### `notebooks/03_sprint_review.ipynb`
Compara las estimaciones de cada sprint contra la base histórica (`data/base/base_estimacion_sprints.xlsx`), calculando desviaciones y tendencias sprint a sprint.

## Cómo agregar un sprint nuevo

1. Exporta el sprint desde la herramienta de gestión (Jira/Azure DevOps/Excel) con las columnas esperadas (ver `data/sprints/README.md`).
2. Guarda el archivo en `data/sprints/` siguiendo la convención `sprint_NN.xlsx` (ej. `sprint_62.xlsx`).
3. Corre el review con Claude Code (ver siguiente sección) o desde `notebooks/03_sprint_review.ipynb`.

## Cómo correr el review de estimaciones con Claude Code

Con el archivo del sprint ya en `data/sprints/`, ejecuta:

```bash
python scripts/review_sprint.py data/sprints/sprint_62.xlsx
```

Esto invoca a Claude Code con el contexto de `CLAUDE.md` para clasificar cada tarea del sprint (DESAFÍO ✦ / META ✓ / OK / ALTA ↑ / INFLADA ↑↑) y generar un resumen ejecutivo directamente en la consola/chat, sin modificar archivos.

Alternativamente, puedes abrir el repo en Claude Code y pedir directamente: *"Revisa el sprint en data/sprints/sprint_62.xlsx"*.
