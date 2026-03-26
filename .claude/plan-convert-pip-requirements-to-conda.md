## Plan: Convert pip requirements to conda-first environment.yml

TL;DR - Create a conda-first `environment.yml` that installs packages from conda (prefer `conda-forge`) when available and falls back to `pip` for packages not on conda. Use conda packages for build-sensitive libs (psycopg2, pydantic, tokenizers) to avoid local compilation, and list pip-only packages under `pip:`.

**Steps**
1. Inventory dependency declarations (pyproject.toml, requirements files, Dockerfiles). *depends on: discovery*.
2. Map each pip package to a conda package (prefer `conda-forge`) or mark as pip-only. Note packages requiring system binaries or Rust (psycopg2, tiktoken, tokenizers, pydantic-core).
3. Draft `environment.yml` with channels, conda dependencies, and a `pip:` subsection for pip-only packages and pip-preferred wheels.
4. Add guidance/comments in the file for special cases (psycopg2-binary vs psycopg2; tiktoken build behavior; graphviz binary).
5. (Optional) Validate conda availability and exact package names/versions (requires querying conda-forge index or conda search).
6. Commit `environment.yml` to repo and update README or CLAUDE.md instructions to use `conda env create -f environment.yml`.

**Relevant files**
- `pyproject.toml` — primary dependency declarations (root)
- `docker/Dockerfile.api` — references pip install flow
- `docker/Dockerfile.celery` — references watchdog/pip
- `CLAUDE.md` — mentions `environment.yml` usage

**Verification**
1. Run `conda env create -f environment.yml` locally and verify environment builds without pip building Rust/C extensions. If pip builds occur, add missing binary packages to conda section.
2. Run `pip check` inside the environment to ensure no dependency conflicts.
3. Run a minimal smoke test: `python -c "import alembic, fastapi, uvicorn, pydantic, psycopg2, redis"` and run the app startup commands in `app/` to ensure basic modules import.

**Decisions / Assumptions**
- Prefer `conda-forge` channel for prebuilt binaries. Include `defaults` as fallback.
- Replace `psycopg2-binary` with conda `psycopg2` to avoid conflicts.
- Keep `langfuse`, `pydantic-ai`, and `tiktoken` as pip installs unless conda-forge provides reliable binaries for the target platform.

**Further Considerations**
1. Do you want me to create the `environment.yml` file in the repo now? (Yes / No)
2. Should I attempt to query conda-forge for exact package names and versions (requires network)?
3. Which Python minor/patch version should we pin to (e.g., `python=3.13.7` vs `3.13`)?
