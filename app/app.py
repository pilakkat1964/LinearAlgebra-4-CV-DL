import streamlit as st
import numpy as np
from sklearn.decomposition import PCA

st.title("PCA Visualizer")
X=np.random.rand(100,20)
k=st.slider("Components",2,10,5)
pca=PCA(n_components=k)
Xr=pca.inverse_transform(pca.fit_transform(X))
st.write("Error:",((X-Xr)**2).mean())
