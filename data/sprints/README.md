# Cómo subir un sprint nuevo

Esta carpeta recibe los archivos de sprint que serán revisados por Claude Code contra la base histórica de estimaciones (`data/base/base_estimacion_sprints.xlsx`).

## 1. Formato esperado del archivo

El archivo debe ser un `.xlsx` con al menos las siguientes columnas:

| Columna         | Descripción                                              |
|-----------------|-----------------------------------------------------------|
| `ID`            | Identificador de la tarea/HU (ej. `AUTO-123`)             |
| `Titulo HU`     | Título de la historia de usuario o tarea                 |
| `Estimación`    | Puntos estimados (escala Fibonacci: 0.5, 1, 2, 3, 5, 8, 10, 13...) |

Columnas adicionales (asignado, estado, sprint) pueden incluirse pero no son requeridas para el review.

## 2. Naming convention

Nombra el archivo como `sprint_NN.xlsx`, donde `NN` es el número de sprint:

```
sprint_62.xlsx
sprint_63.xlsx
```

## 3. Cómo ejecutar el review desde Claude Code

Con el archivo ya guardado en esta carpeta:

```bash
python scripts/review_sprint.py data/sprints/sprint_62.xlsx
```

O, desde una sesión de Claude Code abierta en la raíz del repo, simplemente pide:

> "Revisa el sprint en data/sprints/sprint_62.xlsx"

Claude Code usará el contexto de `CLAUDE.md` (escala de puntos, multiplicadores IA, base histórica por tipo de tarea) para clasificar cada tarea y entregar una tabla + resumen ejecutivo en el chat. **No se modifican archivos** durante el review.
