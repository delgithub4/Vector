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

    def search_vectors(
        self,
        query
    ):

        return self.store.search(
            query
        )
