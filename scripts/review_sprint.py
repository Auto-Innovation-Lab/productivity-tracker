"""
Lanza una revisión de estimaciones de un sprint usando Claude Code.

Uso:
    python scripts/review_sprint.py data/sprints/sprint_62.xlsx

El script invoca al CLI de `claude` (Claude Code) en modo no interactivo,
pasando el contexto de CLAUDE.md (ya presente en la raíz del repo) y
pidiendo la revisión del archivo de sprint indicado. La respuesta se
imprime en la consola; no se modifica ningún archivo.

Requisitos:
    - Tener instalado y autenticado el CLI de Claude Code (`claude`).
    - Ejecutar este script desde la raíz del repo `productivity-tracker`.
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python scripts/review_sprint.py data/sprints/sprint_NN.xlsx")
        return 1

    sprint_path = Path(sys.argv[1])
    if not sprint_path.exists():
        print(f"Error: no se encontró el archivo '{sprint_path}'")
        return 1

    sprint_rel = sprint_path.resolve().relative_to(REPO_ROOT)

    prompt = (
        f"Revisa el sprint en {sprint_rel} siguiendo las instrucciones de CLAUDE.md "
        "(sección 'Tarea al revisar un sprint nuevo'). Responde solo en el chat, "
        "no modifiques archivos."
    )

    result = subprocess.run(
        ["claude", "--print", prompt],
        cwd=REPO_ROOT,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
