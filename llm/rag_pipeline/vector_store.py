import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

def add_vector(vector):
    index.add(np.array([vector]))

def search(vector):
    return index.search(np.array([vector]), 1)
