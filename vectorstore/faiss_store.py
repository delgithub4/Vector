import faiss
import numpy as np


class FAISSStore:

    def __init__(self):

        self.dimension = 384

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

    def add(
        self,
        vectors
    ):

        vectors = np.array(
            vectors,
            dtype="float32"
        )

        self.index.add(vectors)

        return self.index.ntotal

    def search(
        self,
        query,
        k=3
    ):

        query = np.array(
            [query],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query,
            k
        )

        return {

            "indices": indices.tolist(),

            "distances": distances.tolist()

        }
