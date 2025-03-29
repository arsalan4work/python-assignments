import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Sample App 2")

# data = pd.DataFrame(
#     np.random.randn(50,3),
#     columns=["A", "B", "C"]
# )
# st.line_chart(data)
# st.bar_chart(data)
# st.area_chart(data)

# data = pd.DataFrame({
#     "Fruits": ["apple", "mango", "banana", "orange", "grapes"],
#     "Amount": [1,50,3,4,2]
# })
# st.subheader("Mango is in demand because summar is coming!")

# figures = px.bar(data, x="Fruits", y="Amount", title="Fruits Sales")
# st.plotly_chart(figures)


data = pd.DataFrame(
    np.random.randn(100,3),
    columns=["A", "B", "C"],
)

plt.figure(figsize=(10,6))
sns.scatterplot(x=data["A"], y= data["B"])
plt.title("Dots 1 to Dots 2")

st.pyplot(plt)