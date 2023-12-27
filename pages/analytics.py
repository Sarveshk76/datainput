import streamlit as st
import numpy as np

st.title("Analytics")

# Add histogram data
x1 = np.random.randn(20) - 2
x2 = np.random.randn(20)
x3 = np.random.randn(20) + 2

# Group data together
hist_data = {'Group 1':x1, 'Group 2':x2, 'Group 3':x3}

group_labels = ['Group 1', 'Group 2', 'Group 3']


# Plot!
col1, col2 = st.columns(2)

with col1:
    st.bar_chart(hist_data)
with col2:
    st.line_chart(hist_data)