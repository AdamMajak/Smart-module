"""Standalone FastAPI app and routes for the Smart-module submodule."""

from fastapi import APIRouter, FastAPI

router = APIRouter()


@router.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    """Report that the API is ready to receive requests."""
    return {"status": "ok"}


app = FastAPI(title="Smart-module API", version="0.1.0")
app.include_router(router)
