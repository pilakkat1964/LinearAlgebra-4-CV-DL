import numpy as np
def compress(A,k):
    U,S,Vt=np.linalg.svd(A)
    return U[:,:k]@np.diag(S[:k])@Vt[:k,:]
