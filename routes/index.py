from fastapi import APIRouter
from services.vector_service import VectorService

vector = VectorService()

router = APIRouter(
    prefix="/index",
    tags=["Index"]
)


@router.post("/")
def create_index():

    sample_vectors = [

        [0.1] * 384,

        [0.2] * 384,

        [0.3] * 384

    ]

    total = vector.index_vectors(
        sample_vectors
    )

    return {

        "status": "success",
    
        "vectors": total
    
    }
