from vectorstore.faiss_store import FAISSStore


class VectorService:

    def __init__(self):

        self.store = FAISSStore()

    def index_vectors(
        self,
        vectors
    ):

        return self.store.add(
            vectors
        )
