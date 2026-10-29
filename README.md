# Gotu AI

Gotu AI is an early-stage agricultural assistant project. The current application consists of a FastAPI backend and a Streamlit page that checks the backend connection. The repository also contains agricultural reference PDFs for banana and tomato, but the documents are not yet integrated into the application.

## Project structure

```text
backend/
├── app/
│   └── main.py           # FastAPI application
├── frontend/
│   └── app.py            # Streamlit status page
├── data/
│   ├── organized/        # Topic-organized banana and tomato references
│   └── raw/              # Source reference PDFs
├── pyproject.toml
└── uv.lock
```

## Requirements

- Python 3.14 (the version specified by `backend/.python-version`)
- [uv](https://docs.astral.sh/uv/)

## Setup

In a terminal, change to the backend directory and install the project dependencies:

```powershell
cd backend
uv sync
```

## Run the application

Start the API in one terminal from the `backend` directory:

```powershell
uv run uvicorn app.main:app --reload
```

The API is available at <http://127.0.0.1:8000>. Its root endpoint (`GET /`) returns:

```json
{"message": "Hello, Team!!!"}
```

FastAPI's interactive API documentation is available at <http://127.0.0.1:8000/docs>.

In a second terminal, also from the `backend` directory, start the Streamlit page:

```powershell
uv run --with requests streamlit run frontend/app.py
```

Open the local URL printed by Streamlit (typically <http://localhost:8501>). The page calls the API at `http://127.0.0.1:8000/`, so keep the backend running while using it.

## Reference data

Agricultural PDFs are stored under `backend/data/`:

- `organized/banana/` and `organized/tomato/` group references by growing stage or topic.
- `raw/` contains source PDFs that have not been organized into those topic folders.

The current API and Streamlit page do not read or search these files.

## Current status

The application currently provides a basic API health/connectivity check. Crop-specific question answering, document retrieval, and other agricultural assistant features are not implemented yet.
