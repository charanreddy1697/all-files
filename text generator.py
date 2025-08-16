import streamlit as st
import matplotlib.pyplot as plt
st.title("🖼️ Text to Image Generator (Matplotlib)")

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Create the figure
fig, ax = plt.subplots()
ax.plot(x, y, marker='o', linestyle='-', linewidth=2)

# Labels and title
ax.set_title("Simple Line Chart")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

# Display in Streamlit
st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt
import io

st.title("🖼️ Text to Image Generator (Matplotlib)")

# User text input
user_text = st.text_input("Enter your text:", "Hello Streamlit!")

# Button to generate image
if st.button("Generate Image"):
    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.text(0.5, 0.5, user_text, fontsize=24, ha='center', va='center')
    ax.axis("off")

    # Save image to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", transparent=True)
    buf.seek(0)

    # Display in Streamlit
    st.image(buf, caption="Generated Image")

    # Download option
    st.download_button(
        label="Download Image",
        data=buf,
        file_name="text_image.png",
        mime="image/png"
    )

