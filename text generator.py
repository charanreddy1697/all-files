import streamlit as st
import matplotlib.pyplot as plt
import io

st.title("🖼️ Text & Chart Generator")

# Text to Image Section
st.header("Text to Image")
user_text = st.text_input("Enter your text:", "Hello Streamlit!")

if st.button("Generate Image"):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.text(0.5, 0.5, user_text, fontsize=24, ha="center", va="center")
    ax.axis("off")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", transparent=True)
    buf.seek(0)

    st.image(buf, caption="Generated Image", use_column_width=True)
    st.download_button("Download Image", buf, "text_image.png", "image/png")

# Line Chart Section
st.header("Line Chart")
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

fig2, ax2 = plt.subplots()
ax2.plot(x, y, marker="o", linestyle="-", linewidth=2)
ax2.set_title("Simple Line Chart")
ax2.set_xlabel("X Axis")
ax2.set_ylabel("Y Axis")

st.pyplot(fig2)
