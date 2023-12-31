import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3), columns = ['a', 'b', 'c']
)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a', y = 'b', tooltip = ['a','b']
)
st.altair_chart(chart, use_container_width = True)

st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
}
""")

st.map()

plt.scatter(data['a'], data['b'])
plt.title("Scatter")
st.pyplot()

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

st.image()
