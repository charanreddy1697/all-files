import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os

st.title("🖼️ Text to Image Converter with Custom Fonts")

# User input
user_text = st.text_area("Enter your text:", "Hello Streamlit!")

# Font size
font_size = st.slider("Font size", 10, 50, 27)

colr = st.selectbox('select color',['white','black','red']) 
a1,a2 = st.columns([1,2])
# Button to generate image
if a1.button("Generate Image"):
    # Create blank white image
    
    img = Image.new("RGB", (450, 300), color=colr)
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default(size=font_size)

    # Handle multi-line text
    lines_limit = [30,90,150,210,270]
    lines = list(user_text.split("\n"))
    if len(lines) > 5:
        st.warning('only 5 lines allowed')
    else:
            
        
        for i in range(len(lines)):
            draw.text((50, lines_limit[i]), lines[i], fill="black", font=font)
        
        # Save to buffer
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
    
        # Display image
        st.image(buf, caption="Generated Image", use_container_width=True)
        
        # Download button
        a2.download_button(
            label="Download Image",
            data=buf,
            file_name="text_image.png",
            mime="image/png"
        )
