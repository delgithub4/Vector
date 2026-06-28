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
