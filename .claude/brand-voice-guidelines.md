# KyberForge — Brand Voice Guidelines

> **Version**: 1.0
> **Generated**: 2026-03-26
> **Sources**: GenAI Launchpad README, KyberForge README
> **Audience**: LLM agents and human contributors

---

## 1. Brand Identity

**Product Name**: KyberForge (always capitalized as "KyberForge" — not "Kyberforge", "kyberforge", or "Kyber Forge")

**Organization**: tech-architecti
**Contact**: info@techarchitecti.com
**Repository**: github.com/tech-architecti/KyberForge
**License**: MIT

**One-Liner**: KyberForge is an advanced AI-driven Network Engineering and Architecture Support system built on a production-ready GenAI infrastructure.

**Elevator Pitch**: KyberForge is an advanced AI-driven network engineering and architecture support system with AI-powered design, optimization, troubleshooting, and security implementation. Built on the GenAI Launchpad's Docker-based architecture, it gives network engineers a production-ready support system from day one.

---

## 2. Core Objectives

KyberForge exists to:

1. Assist with network design and optimization
2. Provide insights on the latest networking technologies and best practices
3. Help troubleshoot complex network issues
4. Offer guidance on implementing security measures in network architecture

Every piece of content — README, docstring, commit message, or UI copy — should connect back to one or more of these objectives.

---

## 3. Voice Attributes

### We Are / We Are Not

| We Are | We Are Not |
|---|---|
| **Direct and confident** — we state what the tool does without hedging | **Arrogant** — we don't claim to replace engineers or be infallible |
| **Technical and precise** — we use correct networking and AI terminology | **Jargon-heavy for its own sake** — we don't obscure meaning behind buzzwords |
| **Action-oriented** — we emphasize what you can *do*, not what you could theoretically do | **Vaporware-sounding** — we don't oversell capabilities that don't exist yet |
| **Network-engineer-focused** — we speak to network engineering professionals | **Corporate or marketing-heavy** — we don't use empty superlatives |
| **Production-minded** — we care about real deployments, not just demos | **Reckless** — we don't skip over security, reliability, or operational concerns |
| **Extension-ready** — modular architecture inherited from Launchpad; designed to adapt | **Opinionated to the point of rigidity** — we don't force a single way to do things |

**Confidence**: High — both source documents consistently demonstrate these attributes.

---

## 4. Tone-by-Context Matrix

| Context | Tone | Register | Example |
|---|---|---|---|
| **README / Landing** | Confident, direct, understated | Semi-formal | "KyberForge is an advanced AI-driven Network Engineering and Architecture Support system." |
| **Technical Docs** | Precise, instructional, neutral | Formal | "The `NetworkDesign` class exposes `create_topology()` and `analyze_security()` methods." |
| **Code Comments / Docstrings** | Terse, functional | Informal-technical | "Initialize network topology with redundancy support." |
| **Commit Messages** | Imperative, scoped | Terse | "Add pipeline registry for customer and internal ticket routing" |
| **Issue Templates** | Structured, helpful | Semi-formal | "Describe the expected behavior and the actual result." |
| **Error Messages / CLI Output** | Clear, actionable, non-blaming | Neutral | "Connection to Redis failed. Verify REDIS_URL in your .env and confirm the container is running." |
| **Community / Discord** | Friendly, direct, supportive | Casual | "Good question — check the playground/ directory, there's a pipeline visualizer in there." |

**Confidence**: Medium-High — inferred from README tone and project structure; community tone extrapolated from support section patterns.

---

## 5. Technical Stack & Terminology

### Infrastructure (inherited from GenAI Launchpad)

Always reference these correctly and consistently:

| Component | Purpose | Correct Reference |
|---|---|---|
| **FastAPI** | API layer | "FastAPI" (not "fastapi" or "Fast API" in prose) |
| **Celery** | Background task processing | "Celery" (not "celery worker" generically) |
| **PostgreSQL** | Primary database, including embeddings | "PostgreSQL" (not "Postgres" in formal docs; "Postgres" acceptable in casual contexts) |
| **Redis** | Task queue management | "Redis" |
| **Caddy** | Reverse proxy, automatic HTTPS | "Caddy" |
| **Docker** | Containerization and deployment | "Docker" / "Docker-based" |
| **Alembic** | Database migrations | "Alembic" |
| **Jinja2** | Prompt templates (.j2 files) | "Jinja2 templates" |
| **Conda** | Environment management | "Conda" (not "conda" in prose) |

### KyberForge-Specific Terminology

| Term | Meaning | Usage Notes |
|---|---|---|
| **Pipeline** | A defined sequence of AI processing steps for network engineering tasks (design, troubleshooting, security analysis, etc.) | KyberForge uses "pipelines" as its processing unit (inspired by but structurally distinct from Launchpad's "workflows") |
| **Pipeline Registry** | Central registry mapping event types to pipelines | Located in `app/pipelines/registry.py` |
| **Network Design Assistant** | AI-powered network architecture tooling | Key feature #1 |
| **Technology Insight Engine** | Up-to-date networking knowledge system | Key feature #2 |
| **Troubleshooting AI** | Diagnostic algorithms for network issues | Key feature #3 |
| **Security Implementation Guide** | AI-driven security recommendations | Key feature #4 |
| **Automation Scripts** | Customizable network automation | Key feature #5 |
| **Playground** | Experimental sandbox for testing pipelines, prompts, RAG, and LLMs | Located in `playground/` |
| **Event** | An incoming request that triggers a pipeline | Defined as JSON in `requests/events/` |
| **LLM Factory** | Service for instantiating language model clients | Located in `app/services/llm_factory.py` |
| **Vector Store** | Embedding storage and retrieval service | Located in `app/services/vector_store.py` |

**Confidence**: High — directly extracted from project structure and README content.

---

## 6. Architecture Overview (for context in all content)

KyberForge follows an **event-driven architecture**:

1. An **event** arrives via the **FastAPI** API layer
2. The **API router** validates and dispatches it
3. **Celery** picks up the task for background processing
4. The **pipeline registry** routes to the correct **pipeline**
5. Pipeline steps may invoke the **LLM factory**, **vector store**, or **prompt templates**
6. Results persist to **PostgreSQL**; queue state managed by **Redis**
7. **Caddy** handles reverse proxy and HTTPS termination
8. Everything runs in **Docker** containers

When writing about KyberForge's capabilities, ground descriptions in this architecture. Don't describe features in the abstract — connect them to the components that implement them.

---

## 7. Project Structure Reference

```
kyberforge/
├── app/
│   ├── alembic/          # Database migrations
│   ├── api/              # API endpoints, routing, event schemas
│   ├── config/           # Celery, database, LLM, and app settings
│   ├── core/             # Base classes, LLM core, pipeline engine, validation
│   ├── database/         # Models, repositories, sessions, event persistence
│   ├── pipelines/        # AI pipeline definitions (customer, internal)
│   ├── prompts/          # Jinja2 prompt templates
│   ├── services/         # LLM factory, prompt loader, vector store
│   ├── tasks/            # Celery task definitions
│   └── utils/            # Event factory, vector insertion, pipeline visualization
├── data/                 # Datasets
├── docker/               # Docker configs, Caddyfile, compose
├── docs/                 # Documentation
├── playground/           # Experimentation sandbox and tests
└── requests/             # Event definitions and sender scripts
```

Use this structure when referencing file locations in documentation, issues, or code reviews.

---

## 8. Content Rules

### Do

- Start READMEs and docs with **what it is**, then **what it does**, then **how to use it**
- Use imperative mood in instructions: "Clone the repository" not "You should clone the repository"
- Show code examples early — don't make readers wade through prose to see usage
- Keep badge lines to essential metadata (license, Python version, environment)
- Reference the playground for experimentation; reference `requests/events/` for example payloads

### Don't

- Don't use "just" or "simply" — if it were simple, it wouldn't need documentation
- Don't describe features that aren't implemented yet without explicitly marking them as planned
- Don't use "leverage" when "use" works
- Don't mix Launchpad branding with KyberForge branding — this is KyberForge now
- Don't reference Datalumina, the Launchpad, Datalumina courses, or Datalumina support channels (Discord, launchpad@datalumina.com) in KyberForge content — use tech-architecti contact info (info@techarchitecti.com for inquiries, GitHub Issues for bugs)

### Naming Conventions

- Repository: `kyberforge` (lowercase in paths and package names)
- Brand: `KyberForge` (PascalCase in prose, titles, and UI)
- Organization: `tech-architecti` (lowercase with hyphen)
- Python package imports: `from kyberforge.models import NetworkDesign`

---

## 9. Lineage & Attribution

KyberForge is built on the **GenAI Launchpad** by Datalumina. When appropriate (e.g., CITATION.cff, LICENCE, or architecture docs), acknowledge the Launchpad as the foundational infrastructure. In user-facing product content, lead with KyberForge's identity and domain focus — network engineering — not the underlying framework.

The Launchpad's original architecture provided: FastAPI, Celery, PostgreSQL, Redis, Caddy, Docker containerization, event-driven design, Alembic migrations, and the playground sandbox. KyberForge extends this with network-domain pipelines, LLM configuration management, a pipeline registry pattern, and specialized prompt templates for network engineering use cases.

---

## 10. Open Questions

| # | Question | Recommendation |
|---|---|---|
| 1 | **Tagline**: Does KyberForge have or need a tagline beyond the one-liner? | Consider a short tagline for the repo description and social cards, e.g., "AI-powered network engineering, production-ready." |
| 2 | **Voice in AI outputs**: When KyberForge generates responses to users (e.g., ticket analysis, troubleshooting), what persona should it adopt? | Define a separate "product voice" guide for LLM-generated responses vs. developer documentation voice. |
| 3 | **Visual identity**: Are there logo, color, or typography standards? | Not found in source materials. Create if/when needed. |
| 4 | **Versioning language**: How should releases and changelog entries be written? | Recommend Keep a Changelog format with imperative descriptions. |
| 5 | **Launchpad divergence**: As KyberForge evolves away from the Launchpad base, when should Launchpad references be removed? | Set a threshold (e.g., after v1.0 or when core architecture changes significantly). |

---

*These guidelines should be stored at `.claude/brand-voice-guidelines.md` in the KyberForge repository once a working folder is selected. They will be automatically picked up by `/brand-voice:enforce-voice` in future sessions.*
