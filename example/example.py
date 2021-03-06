import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import rand
from sparse_dot_topn import awesome_cossim_topn

N = 10
a = rand(100, 1000000, density=0.005, format='csr')
b = rand(1000000, 200, density=0.005, format='csr')

c = awesome_cossim_topn(a, b, 5, 0.01)
