from typing import Any

from pydantic import BaseModel


class EmbeddingRequest(BaseModel):
    text: str
    metadata: dict[str, Any] = {}


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


class VectorResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
