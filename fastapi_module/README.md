# FastAPI submodule

Standalone FastAPI application that can also be installed into a parent Python project.

## Run locally

From this directory, install the module and start the development server:

```bash
python -m pip install -e .
uvicorn smart_module_api:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive documentation is at
`http://127.0.0.1:8000/docs`.

## Use from a parent project

Install this directory as a dependency (for example, with `pip install -e ./fastapi_module`),
then mount its router in the parent application's FastAPI instance:

```python
from fastapi import FastAPI
from smart_module_api import router

app = FastAPI()
app.include_router(router, prefix="/module")
```

The module exports both `app` for standalone serving and `router` for composition.
