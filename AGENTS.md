# AGENTS.md

Game-automation app built on the [ok-script](https://github.com/ok-oldking/ok-script) framework (`ok` Python package), for the Windows game 燕云十六声 (Where Winds Meet). Automation logic lives in tasks driven by a central config dict — not a conventional web/CLI app.

## Environment

- Requires **Python 3.12**. Use the repo-local venv interpreter `.\.venv\Scripts\python.exe` when it exists; fall back to `python` otherwise (see `.agents/skills/use-local-venv`).
- Dependencies are declared in `pyproject.toml`. The lockfiles `requirements.txt` (Qt profile), `requirements-web.txt` (web), `requirements-docs.txt` are **generated — do not hand-edit**. Install with `--no-deps`:
  ```powershell
  pip install --index-url https://pypi.org/simple/ --no-deps -r requirements.txt
  ```
- Regenerate locks with `python -m piptools compile --extra qt --strip-extras --no-header --output-file requirements.txt pyproject.toml` (and `web`/`docs` variants). After compiling, keep `pyside6-essentials` but delete the generated `pyside6` and `pyside6-addons` entries.

## Run

- `python main_debug.py` — Qt GUI with `debug=True` (dev entry point).
- `python web_main_debug.py` / `python web_main.py` — web profile (note: these import `from config import config`, unlike `main.py` which uses `from src.config import config`).
- `python -m pytest` is **not** the test runner. Use unittest:
  ```powershell
  .\.venv\Scripts\python.exe -m unittest tests.TestMain
  ```
  or `.\run_tests.ps1` (runs every `tests\*.py`).

## Architecture

- `src/config.py` holds the single app `config` dict: runtime target (`windows`/`adb`/`browser`), capture/interaction methods, `supported_resolution`, `gui_title`, `links`, and task registration. `windows.exe` is fixed to `yysls.exe`.
- Tasks are the unit of work. One-time tasks extend `BaseTask`; background tasks extend `TriggerTask`; shared helpers go in `src/tasks/MyBaseTask.py` (the project base — prefer it over `BaseTask`).
- Register a task by adding `["src.tasks.ModuleName", "ClassName"]` to `onetime_tasks` or `trigger_tasks` in `src/config.py`. `custom_tasks` is enabled, so users can also author scripts in the gitignored `ok_tasks/` dir.
- Task API: set `name`/`description`/`default_config`/`config_description`/`config_type` in `__init__` (call `super().__init__` first); implement `run()`. Use `self.ocr`, `self.find_one`, `self.wait_until`, `self.next_frame`, `self.click_box`, `self.info_set`, `self.log_info(notify=True)`.

## i18n

- gettext catalogs live at `i18n/<locale>/LC_MESSAGES/ok.po`. After editing `.po`, recompile the committed `.mo` (no `msgfmt` on this box; use `python -m ...` compile via the `ok-script-i18n` skill or an equivalent). Task names, descriptions, and config keys are translated; keep config **keys** stable (they persist as JSON).

## Repo-local Skills

Load these with the `skill` tool before task/i18n/codegen work: `ok-script-tasks`, `ok-script-codegen`, `ok-script-i18n`, `use-local-venv`, `initialize-ok-script-app` (already applied), `deploy` (tag + push release).

## Build & Release

- `.github/workflows/build.yml` triggers only on `v*` tags (not branch pushes); it runs tests, packages via pyappify, and creates a GitHub release. MirrorChyan and CNB integrations were removed.
- Docs render with MkDocs: `python -m mkdocs serve` / `python -m mkdocs build --strict`. Docs are bilingual (`docs/` zh, `docs/en/` en) and must stay structurally aligned; update `mkdocs.yml` `nav` when pages change.