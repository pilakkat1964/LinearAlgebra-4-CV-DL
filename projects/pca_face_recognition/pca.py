import numpy as np
def compute_pca(X,k):
    mean=X.mean(axis=0)
    Xc=X-mean
    cov=np.cov(Xc,rowvar=False)
    eigvals,eigvecs=np.linalg.eigh(cov)
    idx=eigvals.argsort()[::-1]
    return eigvecs[:,idx][:,:k],mean
