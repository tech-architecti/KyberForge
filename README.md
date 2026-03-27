# KyberForge

[![License](https://img.shields.io/badge/License-Qubit%2C%20LLC-blue.svg)](LICENCE)
[![Python](https://img.shields.io/badge/python-3.12.6-blue.svg)](https://www.python.org/downloads/)
[![Conda](https://img.shields.io/badge/conda-environment-green.svg)](https://docs.conda.io/en/latest/)

KyberForge is an advanced AI-driven Network Engineering and Architecture Support system. It gives network engineers
AI-powered design, optimization, troubleshooting, and security implementation — built on a Docker-based GenAI
infrastructure that's production-ready from day one.

## Introduction

KyberForge brings AI to the network engineering workflow — from initial topology design through troubleshooting and
security hardening. Instead of assembling infrastructure from scratch, you get a containerized system with an
event-driven pipeline engine, background task processing, and built-in support for LLM integration and vector search.

The architecture is modular and extension-ready. Define a new pipeline, wire it into the registry, and KyberForge
handles routing, task execution, and persistence. The infrastructure adapts to your use case, not the other way around.

## Overview

KyberForge runs on a proven stack designed for production AI workloads:

- **FastAPI** for the API layer — event ingestion, routing, and validation
- **Celery** for background task processing — pipeline execution runs asynchronously
- **PostgreSQL** for persistent storage, including embeddings
- **Redis** for task queue management
- **Caddy** for reverse proxy and automatic HTTPS
- **Alembic** for database migrations
- **Jinja2** for prompt templates

All services are containerized with Docker. An event arrives via the API, gets dispatched to the pipeline registry,
and Celery picks it up for processing. Pipeline steps can invoke LLMs, query the vector store, or apply prompt
templates — results persist to PostgreSQL.

## Key Features

- **Network Design Assistant**: Create and optimize network architectures using the pipeline engine and LLM integration.
- **Technology Insight Engine**: Surface up-to-date networking best practices through retrieval-augmented generation
  (RAG) and the vector store.
- **Troubleshooting AI**: Run diagnostic pipelines that isolate and resolve complex network issues step by step.
- **Security Implementation Guide**: Generate security recommendations grounded in your actual network architecture.
- **Automation Scripts**: Customizable scripts for repeatable network operations.
- **Event-Driven Architecture**: A pipeline registry routes incoming events to the correct processing pipeline
  automatically — no manual dispatch.
- **Playground**: Sandbox environment for testing pipelines, prompts, RAG workflows, and LLM configurations in
  isolation from production.
- **Production-Ready Deployment**: Docker-based containerization with Caddy reverse proxy, ready for real environments.

## Installation

### Conda (recommended)

```bash
# Create the environment (uses conda-forge + pip fallbacks)
conda env create -f environment.yml
conda activate kyberforge

# Install the project in editable mode
pip install -e .
```

### pip only

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

### Docker

```bash
cd docker && ./start.sh
```

## Quick Start

```python
from kyberforge.models import NetworkDesign

# Initialize and create a redundant topology
network = NetworkDesign()
topology = network.create_topology(nodes=5, redundancy=True)

# Run a security analysis against the topology
security_score = network.analyze_security(topology)
```

For full installation and setup instructions, see the [Installation guide](docs/installation.md).

## Documentation

Full documentation is available in the [`docs/`](docs/) directory, covering:

- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [API Reference](docs/api_reference.md)
- [Deployment](docs/deployment.md)

## Project Structure

KyberForge follows a modular, event-driven project structure:

```text
├── app
│   ├── alembic/          # Database migration scripts
│   ├── api/              # API endpoints, routing, and event schemas
│   ├── config/           # Celery, database, LLM, and application settings
│   ├── core/             # Base classes, LLM core, pipeline engine, validation
│   ├── database/         # Models, repositories, sessions, event persistence
│   ├── pipelines/        # AI pipeline definitions (customer, internal)
│   ├── prompts/          # Jinja2 prompt templates
│   ├── services/         # LLM factory, prompt loader, vector store
│   ├── tasks/            # Celery task definitions
│   └── utils/            # Event factory, vector insertion, pipeline visualization
├── data/                 # Datasets
├── docker/               # Docker configs, Caddyfile, Compose
├── docs/                 # Documentation
├── playground/           # Experimentation sandbox and tests
└── requests/             # Event definitions and sender scripts
```

## Support

For questions, bug reports, and collaboration:

- **GitHub Issues**: Open an issue on the [KyberForge repository](https://github.com/tech-architecti/KyberForge/issues)
  for bugs, feature requests, and technical questions.
- **Email**: For private inquiries, reach us at [info@techarchitecti.com](mailto:info@techarchitecti.com).

## License

This project is licensed under the Qubit, LLC License. See the [LICENSE](LICENCE) file for details.

### Key Points

- You can use KyberForge for your own internal business operations.
- You can modify and expand the code to fit your internal needs.
- You cannot use KyberForge to build products or services for third parties.
- You cannot resell or redistribute this code as a template, package, or course.
- The software is provided "AS IS", without warranty of any kind.

For the full license text, refer to the [LICENSE](LICENCE) file in the repository.

---

See [Code of Conduct](CODE_OF_CONDUCT.md) and [Governance](GOVERNANCE.md) for contribution and project guidelines.
