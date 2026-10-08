# Codex development starter

A minimal, reusable starting point for Linux-based Codex Cloud development. This repository contains development infrastructure only. Keep separate applications in separate repositories, with their own dependency locks, tests, and Cloud environments.

## Prepare and check

Requirements: Bash, Git, Python 3.12 or newer, Node.js 22 or newer, and npm.

```sh
bash scripts/setup.sh
.venv/bin/python scripts/check_environment.py
```

The setup creates an isolated Python virtual environment and checks both runtimes. It installs no application packages. Once a project is selected, declare and lock its dependencies in that project's repository.

## Codex Cloud setup

1. Select this repository when creating the environment.
2. Ask setup to provide the required runtimes and run `bash scripts/setup.sh`.
3. Keep environment access set to **Only me**. Start with the **Package managers** network preset and add service hosts only when a project needs them.
4. Record `bash scripts/setup.sh` as the Install script. No service needs to run for this starter.
5. Publish the prepared environment. Start a NEW Cloud task and run both commands above again.
6. Verify a temporary branch can be created and a pull request can be opened before relying on the environment for delivery. Do not merge the verification PR automatically.

Repository access, environment publication, runtime availability, and successful Cloud execution are separate checks. Creating this repository alone does not establish them.

## New projects

Copy the applicable development rules and scripts into a new project repository. Select that repository in a new Cloud environment and publish after its actual dependency installation and tests pass. Do not put unrelated projects into this starter repository or assume one environment automatically includes all repositories in a GitHub account.

## Credentials and data

Never commit credentials, `.env` values, private datasets, account records, or production dumps. Configure narrowly scoped service credentials outside Git, and avoid printing them in commands or logs. An ignore rule does not protect secrets already tracked by Git. This repository may be public; put private application code in private project repositories.

GPU workloads, operating-system-specific dependencies, deployment services, and long-running production jobs require separate validation for each project.
