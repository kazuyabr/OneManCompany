# Repository Guidelines

## Project Structure & Module Organization
The application is a Python package under [`src/onemancompany`](src/onemancompany) with the runtime entrypoint defined in [`pyproject.toml`](pyproject.toml:43). The browser UI lives in [`frontend`](frontend), and the shipped company/talent assets live in [`company`](company). Tests are organized under [`tests`](tests) with unit, API, core, agents, and E2E coverage split by domain. Project docs are split between [`docs`](docs) and [`mkdocs-docs`](mkdocs-docs), with the latter used for the generated documentation site.

## Build, Test, and Development Commands
Create a local environment with `python -m venv .venv`, activate it, then install the package in editable mode with `pip install -e .`. Run the app locally with `onemancompany` or the onboarding entrypoint with `onemancompany-init`, both defined in [`pyproject.toml`](pyproject.toml:43). Run tests with `pytest`; for a single test file use `pytest tests/unit/test_main.py`. The repository also includes `start.sh` for Unix-like bootstrap and a Node package wrapper in [`package.json`](package.json:1), but the Python entrypoints are the source of truth for local development.

## Coding Style & Naming Conventions
Use the existing Python layout and module naming already present under [`src/onemancompany`](src/onemancompany). Keep tests aligned with the current split by feature area in [`tests/unit`](tests/unit). No formatter or linter configuration is declared in the repository metadata currently reviewed, so follow the project’s existing style and keep changes consistent with neighboring code.

## Testing Guidelines
`pytest` is configured in [`pyproject.toml`](pyproject.toml:47) with `src` on `pythonpath`, `tests` as the test root, and markers for `unit`, `integration`, and `e2e`. Prefer the narrowest relevant test target first, then expand to broader coverage when behavior crosses subsystems.

## Commit & Pull Request Guidelines
No commit convention file was found in the reviewed root files. Keep pull requests focused on one change set and reference the affected module or feature area in the description. Use clear, imperative commit messages that match the repository’s existing technical style.