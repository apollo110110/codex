"""Non-network checks for the starter's actual development capabilities."""

import json
from pathlib import Path
import sqlite3
import ssl
import subprocess
import sys
import tempfile


def main() -> None:
    if sys.version_info < (3, 12):
        raise RuntimeError("Python >= 3.12 required")
    if sys.prefix == sys.base_prefix:
        raise RuntimeError("Run with .venv/bin/python after bash scripts/setup.sh")

    with sqlite3.connect(":memory:") as connection:
        value = connection.execute("SELECT 6 * 7").fetchone()[0]
        if value != 42:
            raise RuntimeError("SQLite operation failed")
    ssl.create_default_context()
    with tempfile.TemporaryDirectory() as directory:
        sample = Path(directory) / "sample.txt"
        sample.write_text("runtime-ok", encoding="utf-8")
        if sample.read_text(encoding="utf-8") != "runtime-ok":
            raise RuntimeError("Temporary file round trip failed")

    node_program = """
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
assert.ok(Number(process.versions.node.split('.')[0]) >= 22, 'Node.js >= 22 required');
assert.equal(typeof fetch, 'function');
assert.equal(crypto.createHash('sha256').update('hello').digest('hex'),
  '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824');
console.log(process.versions.node);
"""
    node_version = subprocess.run(
        ["node", "-e", node_program], check=True, capture_output=True, text=True
    ).stdout.strip()
    git_version = subprocess.run(
        ["git", "--version"], check=True, capture_output=True, text=True
    ).stdout.strip()
    npm_version = subprocess.run(
        ["npm", "--version"], check=True, capture_output=True, text=True
    ).stdout.strip()
    print(json.dumps({
        "status": "PASS",
        "python": sys.version.split()[0],
        "node": node_version,
        "npm": npm_version,
        "git": git_version,
        "checks": ["virtualenv", "sqlite", "tls-context", "temp-file-io", "node-crypto", "fetch-present"],
        "not_checked": ["external-network", "GitHub-push", "Cloud-publication", "GPU", "project-dependencies"],
    }, indent=2))


if __name__ == "__main__":
    main()
