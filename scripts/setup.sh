#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

for executable in python3 node npm git; do
  if ! command -v "$executable" >/dev/null 2>&1; then
    echo "Missing required tool: $executable" >&2
    exit 1
  fi
done

python3 -c 'import sys; assert sys.version_info >= (3, 12), "Python >= 3.12 required"'
node -e 'if (Number(process.versions.node.split(".")[0]) < 22) throw new Error("Node.js >= 22 required")'

if [[ ! -x .venv/bin/python ]]; then
  python3 -m venv .venv
fi
.venv/bin/python scripts/check_environment.py
