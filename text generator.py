import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import os

st.title("Text to Image Converter")


c1,c2 = st.columns([1,1])
# Font size
font_size = c1.slider("Font size", 10, 50, 27)
colr = c2.color_picker("Pick a background color", "#FFFFFF")

b1,b2 = st.columns(2)
image_width = b1.number_input('Weidth',100,900,600)
image_height = b2.number_input('Height',100,600,300)
try:
        
    # User input
    user_text = st.text_area("Enter your text:[ allows only 5 lines ]", "Tyep Here...")
    a1,a2,a3 = st.columns(3)
    img = Image.new("RGB", (image_width,image_height), color=colr)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default(size=font_size)
    
    # Handle multi-line text
    lines_limit = [30,90,150,210,270]
    lines = list(user_text.split("\n"))
    
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
except:
    st.write('your have typed more than 5 lines')
