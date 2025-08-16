import streamlit as st
pip install matplotlib
import matplotlib.pyplot

st.title("📈 Line Chart Example")

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Create the figure
fig, ax = matplotlib.pyplot.subplots()
ax.plot(x, y, marker='o', linestyle='-', linewidth=2)

# Labels and title
ax.set_title("Simple Line Chart")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

# Display in Streamlit
st.pyplot(fig)
