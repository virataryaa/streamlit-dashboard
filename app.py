import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Team Dashboard")

x = np.arange(10)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sample Plot")

st.pyplot(fig)
