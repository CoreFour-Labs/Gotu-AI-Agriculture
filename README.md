# Gotu AI

Gotu AI is an early-stage agricultural assistant project. It currently includes a FastAPI API and a Streamlit page that checks whether the API is reachable. The repository also contains agricultural reference documents about banana and tomato cultivation; they are not yet connected to the application.

## Project structure

```text
backend/
└── app/
    └── main.py             # FastAPI application
data/
├── organized/
│   ├── banana/             # References arranged by growing stage or topic
│   └── tomato/
└── raw/
    ├── Tomato/             # Source documents
    └── banana/
frontend/
└── app.py                  # Streamlit API-connection page
src/
└── gotu_ai/                # Python package scaffold
pyproject.toml              # Project metadata and dependencies
uv.lock                     # Locked dependency versions
```

## Requirements

- Python 3.14 (the version specified in `.python-version`)
- [uv](https://docs.astral.sh/uv/)

## Install

Run these commands from the repository root:

```powershell
uv sync
```

## Run the application

Start the API from the repository root:

```powershell
uv run uvicorn backend.app.main:app --reload
```

The API listens at <http://127.0.0.1:8000>. Its `GET /` endpoint currently returns:

```json
{"message": "Hello, Team!!!"}
```

Interactive API documentation is available at <http://127.0.0.1:8000/docs>.

In a second terminal, start the Streamlit page, also from the repository root:

```powershell
uv run streamlit run frontend/app.py
```

Open the local URL printed by Streamlit (typically <http://localhost:8501>). The page sends a request to `http://127.0.0.1:8000/`, so keep the API running while using it.

## Reference data

The `data/organized/` directory contains banana and tomato references grouped by cultivation stage or topic. The `data/raw/` directory contains source PDFs that have not been organized into those topic folders. The API and Streamlit page do not currently read, search, or otherwise use these documents.

## Current functionality and limitations

- The FastAPI application exposes only a basic root endpoint.
- The Streamlit page reports whether it can connect to that endpoint and displays the returned message.
- Crop-specific question answering, document retrieval, and other agricultural assistant features are not implemented yet.
