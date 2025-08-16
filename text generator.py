import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("🖼️ Text to Image (Pillow)")

# User input
user_text = st.text_input("Enter your text:", "Hello Streamlit!")

if st.button("Generate Image"):
    # Create blank image (white background)
    img = Image.new("RGB", (500, 200), color="white")
    d = ImageDraw.Draw(img)

    # Use default font
    d.text((50, 80), user_text, fill="black")

    # Save to buffer
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    # Display image
    st.image(buf, caption="Generated Image")

    # Download option
    st.download_button(
        label="Download Image",
        data=buf,
        file_name="text_image.png",
        mime="image/png"
    )
