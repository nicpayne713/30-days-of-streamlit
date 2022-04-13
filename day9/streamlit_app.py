import numpy as np
import pandas as pd
from plotly import express as px
import streamlit as st

st.header("Line chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


# plotly is better

st.plotly_chart(px.line(chart_data, height=400, width=800))
