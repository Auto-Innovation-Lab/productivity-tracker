# Productivity Tracker · Innovación Automotriz SpA

## Contexto del equipo
Pod de desarrollo de 3 devs full-stack:
- Javier Velásquez (javelasquezb) — Tech Lead, arquitectura — usa GPT
- Henrique Schraiber (Ecxpectro) — Agentic Engineer — usa Claude Code
- Guilherme Reis (GuilhermeKill) — Agentic QA Engineer — usa Claude Code

## Sistemas bajo ownership
- Spareparts Business / Mi Autoparts (.NET / Azure)
- Digital Workshop / Mi Taller Digital (.NET MAUI / PWA)

## GitHub
- Organización: Auto-Innovation-Lab
- Usuario owner: edesiosantos

## Archivos clave
- data/historial/Sprint_60.xlsx — historial sprints 18–59 sin IA
- data/base/base_estimacion_sprints.xlsx — promedios históricos + Meta Sprint + Desafío IA
- data/sprints/ — carpeta donde se suben nuevos sprints para review

## Escala de puntos (horas reales)
| Pts  | Tiempo           |
|------|------------------|
| 0.5  | ~2 horas         |
| 1    | ~4h (½ día)      |
| 2    | ~8h (1 día)      |
| 3    | ~12h (1½ día)    |
| 5    | ~20h (2½ días)   |
| 8    | ~32h (4 días)    |
| 10   | ~40h (5 días)    |
| ≥8   | Separar con IA   |
| ≥13  | Separar sin IA   |

## Multiplicadores IA por talla
| Talla | Pts   | Multiplicador |
|-------|-------|---------------|
| S     | ≤ 2   | 1.2x          |
| M     | 2–5   | 1.5x          |
| L     | 5–9   | 2.0x          |
| XL    | > 9   | 2.5x          |

## Base histórica por tipo de tarea
| Tipo                      | Hist | Meta | Desafío |
|---------------------------|------|------|---------|
| Configuración             | 2.7  | 2.1  | 1.5     |
| Corrección / Bug          | 2.6  | 2.0  | 1.4     |
| UI / Frontend             | 3.8  | 2.9  | 2.0     |
| Integración API           | 3.7  | 2.8  | 1.9     |
| Módulo / Lógica           | 5.2  | 3.8  | 2.5     |
| Notificaciones / Mensajería| 4.3 | 3.3  | 2.3     |
| Reportes / Export         | 6.1  | 4.5  | 2.9     |
| Migración / Datos         | 6.9  | 5.1  | 3.3     |
| Feature General           | 7.5  | 5.4  | 3.5     |

## Tarea al revisar un sprint nuevo
Lee el archivo en data/sprints/ y para cada tarea:
1. Detecta el tipo según el título
2. Compara con Histórico / Meta Sprint / Desafío IA
3. Clasifica: DESAFÍO ✦ / META ✓ / OK / ALTA ↑ / INFLADA ↑↑
4. Presenta tabla completa con columnas: ID, Título, Est, Tipo, Hist, Meta, Desafío, Estado, Nota
5. Presenta resumen ejecutivo con distribución de estados
6. Identifica tareas candidatas a revisar (ALTA o INFLADA) con explicación
7. Reconoce tareas ya en Desafío IA

## Formato de respuesta al revisar sprint
Responde SOLO en el chat, no modifiques archivos.
Presenta tabla markdown + resumen ejecutivo.
