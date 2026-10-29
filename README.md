# Gotu AI

> An early-stage agricultural assistant project.

Gotu AI brings together a small FastAPI backend, a Streamlit page for checking its connection, and reference PDFs about banana and tomato cultivation.

> **Project status:** The PDFs are not connected to the application. Crop-specific question answering, document search, and AI-powered advice are not implemented yet.

## At a glance

| Part | What it does today |
| --- | --- |
| API | `GET /` returns `{"message": "Hello, Team!!!"}` |
| Streamlit page | Calls the API and displays whether it is reachable |
| Reference library | Stores banana and tomato PDFs by topic, plus source documents |

## Get started

### Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

### Install dependencies

Run from the repository root:

```powershell
uv sync
```

### Start the API

In one terminal:

```powershell
uv run uvicorn backend.app.main:app --reload
```

The API is available at <http://127.0.0.1:8000>. The root endpoint is <http://127.0.0.1:8000/>, and interactive API documentation is at <http://127.0.0.1:8000/docs>.

### Start the Streamlit page

In a second terminal:

```powershell
uv run streamlit run frontend/app.py
```

Open the local address printed by Streamlit (usually <http://localhost:8501>). Keep the API running; the page sends its request to `http://127.0.0.1:8000/`.

## Project structure

```text
backend/
└── app/
    └── main.py             FastAPI application
frontend/
└── app.py                  Streamlit connection page
src/
└── gotu_ai/
    └── __init__.py         Python package entry point
data/
├── organized/
│   ├── banana/             References grouped by cultivation topic
│   └── tomato/
└── raw/                    Source PDFs awaiting organization
pyproject.toml              Project metadata and dependencies
uv.lock                     Locked dependency versions
```

## Reference documents

The `data/organized/` directory groups banana and tomato PDFs into cultivation topics such as disease management, irrigation, and soil testing. `data/raw/` holds source PDFs that have not yet been organized into those topic folders. The application does not currently read or search these documents.
