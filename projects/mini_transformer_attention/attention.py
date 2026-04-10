import torch
import torch.nn.functional as F
def attention(Q,K,V):
    d=Q.size(-1)
    scores=(Q@K.T)/(d**0.5)
    w=F.softmax(scores,dim=-1)
    return w@V
