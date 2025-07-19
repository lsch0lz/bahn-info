from fastapi import FastAPI

from backend.app.api import main
app = FastAPI(
    title="DB-Info",
    description="Die Backend-API für die Website db-info.lukasscholz.de.",
    version="0.1.0"
)

app.include_router(main.api_router)