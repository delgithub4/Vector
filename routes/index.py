from fastapi import APIRouter

router = APIRouter(
    prefix="/index",
    tags=["Index"]
)


@router.post("/")
def create_index():

    return {

        "status": "index created"

    }
