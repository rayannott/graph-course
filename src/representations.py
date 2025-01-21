import numpy as np
import scipy.sparse as sp

from src.common_types import Edge


def edge_list_to_adj_matrix(edges: list[Edge]) -> np.ndarray:
    """
    Convert a list of undirected edges to an adjacency matrix.
    """
    raise NotImplementedError


def edge_list_to_adj_matrix_sparse(edges: list[Edge]) -> sp.csr_matrix:
    """
    Convert a list of undirected edges to a sparse adjacency matrix.
    """
    raise NotImplementedError
