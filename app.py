from fastapi import FastAPI

from routes.index import router as index_router
from routes.search import router as search_router

app = FastAPI(
    title="Vector",
    version="1.0.0"
)

app.include_router(index_router)
app.include_router(search_router)


@app.get("/")
def home():

    return {

        "service": "Vector",

        "status": "running"

    }
