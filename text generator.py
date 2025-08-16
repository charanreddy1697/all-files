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
    st.image(buf, caption="Generated Image", use_column_width=True)

    # Download option
    st.download_button(
        label="Download Image",
        data=buf,
        file_name="text_image.png",
        mime="image/png"
    )

