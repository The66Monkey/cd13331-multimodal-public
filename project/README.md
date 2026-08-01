# Overview

This repo contains my completed project for a Udacity course: an AI-powered content moderation system for customer service interactions at a fictional company, ACME Enterprise.

The system:

- Moderates text, images, videos, and audio before they're sent to customers
- Detects PII, unprofessional or unfriendly tone, disturbing content, and low-quality media
- Blocks harmful content and explains why content was flagged

A trainee customer agent interacts with a simulated angry customer (LLM-powered). Every message and attachment is moderated to ensure communication follows company standards.

## Architecture

- **Specialized agents:** Four moderation agents (text, image, video, audio) using Google Gemini with custom prompts (`multimodal_moderation/agents/`).
- **LLM customer:** A customer agent that simulates an upset user (`agents/customer_agent.py`).
- **Structured results:** Pydantic models with flags like `contains_pii`, `is_unfriendly`, plus rationale (`types/moderation_result.py`).
- **Frontend:** Gradio chat UI for multimodal interaction (`gradio_app.py`).
- **Backend:** FastAPI REST API for programmatic moderation (`fastapi_app.py`).
- **Observability:** Phoenix integration for tracing and monitoring (`tracing.py`).
- **Runner:** A convenience entrypoint that starts backend, frontend, and Phoenix together.

## Course context

This project started from a provided scaffold. I implemented the missing pieces (TODOs), wired up the agents and evals, and ensured all tests pass as part of the course workflow.
