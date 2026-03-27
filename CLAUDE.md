# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Essential Commands

### Development Environment
```bash
# Create conda environment (conda-forge packages + pip fallbacks)
conda env create -f environment.yml
conda activate kyberforge

# Install the project in editable mode
pip install -e .

# Verify no dependency conflicts
pip check
```

> **Note:** Most dependencies are installed via conda (conda-forge channel).
> `langfuse`, `pydantic-ai`, and `python-frontmatter` are installed via pip
> because they are not available on conda-forge. See `environment.yml` for details.

### Running the Application
```bash
# Local development (from app/ directory)
cd app && uvicorn main:app --host 0.0.0.0 --port 8080 --reload

# Docker development
cd docker && ./start.sh
```

### Database Operations
```bash
# Create migration (from project root)
./app/makemigration.sh "description of changes"

# Apply migrations  
./app/migrate.sh
```

### Code Quality
```bash
# Lint and format code (Ruff is configured)
ruff check app/
ruff format app/

# Run tests (from playground directory)
cd playground && python -m pytest tests/
```

## Architecture Overview

### Core Pipeline System
The system is built around an abstract **Pipeline** framework that processes events through configurable node sequences:

- **Pipeline**: Abstract base class requiring a `pipeline_schema` that defines node flow
- **Node**: Individual processing units (analyze, route, generate, etc.)
- **Router**: Decision points that determine next processing steps
- **TaskContext**: Shared state container passed between nodes

### Event Processing Flow
1. **Event Reception**: FastAPI receives events via `/process` endpoint
2. **Pipeline Selection**: `PipelineRegistry` routes based on email prefix (`support@` vs `helpdesk@`)
3. **Node Execution**: Pipeline executes nodes sequentially with routing decisions
4. **Async Processing**: Celery handles background tasks and LLM operations

### Key Components

**Pipeline Implementations** (`app/pipelines/`):
- `CustomerSupportPipeline`: Ticket analysis → routing → response generation → delivery
- `InternalHelpdeskPipeline`: Internal team communications processing

**LLM Integration** (`app/services/llm_factory.py`):
- Factory pattern supporting OpenAI, Anthropic, and Llama models
- Prompt templates loaded from extensive library in `app/prompts/`

**Data Layer** (`app/database/`):
- PostgreSQL for primary data storage
- TimescaleDB with vector extensions for embeddings and RAG
- Repository pattern with SQLAlchemy models
- Event-sourced architecture for audit trails

## Development Patterns

### Adding New Pipelines
1. Create pipeline class inheriting from `Pipeline`
2. Define `pipeline_schema` with node sequence and connections
3. Register in `PipelineRegistry.pipelines` dictionary
4. Update routing logic in `get_pipeline_type()`

### Creating New Nodes
1. Inherit from `Node` base class
2. Implement `process()` method with `TaskContext` parameter
3. Add to pipeline schema's node configurations
4. Define routing connections to next nodes

### Prompt Management
- Jinja2 templates in `app/prompts/` with extensive fabric-style collection
- Use `PromptLoader` service for dynamic template loading
- Templates support variable substitution and conditional logic

## Environment Configuration
- Environment variables loaded from `.env` file in docker directory
- Key settings: database credentials, LLM API keys, Redis connection
- PostgreSQL and TimescaleDB require vector extension configuration
- Celery worker configuration in `app/config/celery_config.py`