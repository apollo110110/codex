# Development rules

- Read the project's README, dependency manifests, and existing code before choosing tools or architecture. Treat historical designs as references, not proof of current implementation.
- Keep each task scoped to its requested outcome. Use a task branch for code changes when Git is initialized; preserve unrelated user changes. Do not auto-merge or deploy unless the task explicitly authorizes it.
- Prefer the project's existing stack. Declare new dependencies explicitly and update lockfiles using the package manager. Do not install large frameworks speculatively.
- Run `bash scripts/setup.sh` when preparing this starter, then `.venv/bin/python scripts/check_environment.py`. For application changes, run the project's relevant tests and checks.
- Report what changed, the actual commands run, their results, and any remaining limitation. Distinguish local checks from Cloud execution; never claim a runtime, service, GPU, or publication was verified without evidence.
- Keep secrets and private datasets out of source, command arguments, logs, and patches. Request missing access through the platform's secure connection or secret controls.
- Do not replace an existing project architecture with this starter. Each project needs its own dependency and resource assessment.
