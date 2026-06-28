from fastapi import APIRouter

from services.vector_service import VectorService

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

vector = VectorService()


@router.post("/")
def search():

    sample_query = [0.15] * 384

    result = vector.search_vectors(
        sample_query
    )

    return result
