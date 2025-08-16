import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os

st.title("🖼️ Text to Image Converter with Custom Fonts")

# User input
user_text = st.text_area("Enter your text:", "Hello Streamlit!")

# Font size
font_size = st.slider("Font size", 10, 100, 40)

# Select font style
font_options = {
    "Sans Serif": "arial.ttf",
    "Serif": "arial.ttf",
    "Monospace": "arial.ttf"
}
selected_font = st.selectbox("Choose font style", list(font_options.keys()))

# Button to generate image
if st.button("Generate Image"):
    # Create blank white image
    img_width, img_height = 600, 400  # Base size; we can adjust height if needed
    img = Image.new("RGB", (img_width, img_height), color="white")
    draw = ImageDraw.Draw(img)

    # Load selected font
    font_path = font_options[selected_font]
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, font_size)
    else:
        st.warning(f"Font file {font_path} not found! Using default font.")
        font = ImageFont.load_default(size=font_size)

    # Handle multi-line text
    lines = user_text.split("\n")
    line_heights = []
    max_width = 0
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        line_heights.append(height)
        if width > max_width:
            max_width = width
    total_height = sum(line_heights) + 10 * (len(lines) - 1)  # 10px spacing

    # Adjust image height if needed
    if total_height > img_height:
        img_height = total_height + 50
        img = Image.new("RGB", (img_width, img_height), color="white")
        draw = ImageDraw.Draw(img)

    # Draw each line centered
    y = (img_height - total_height) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        position = ((img_width - text_width) // 2, y)
        draw.text(position, line, font=font, fill="black")
        y += line_heights[i] + 10

    # Save to buffer
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    # Display image
    st.image(buf, caption="Generated Image", use_container_width=True)

    # Download button
    st.download_button(
        label="Download Image",
        data=buf,
        file_name="text_image.png",
        mime="image/png"
    )
