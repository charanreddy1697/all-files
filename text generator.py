import streamlit as st
import matplotlib.pyplot as plt
import io

st.title("🖼️ Text to Image (Matplotlib)")

# User input
user_text1 = st.text_input("Enter your text for main:", "Main Heading")
user_text2 = st.text_input("Enter your text for list1:", "Item 1")
user_text3 = st.text_input("Enter your text for list2:", "Item 2")
user_text4 = st.text_input("Enter your text for list3:", "Item 3")

# Button to generate
if st.button("Generate Image"):
    # Create figure
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Main text (top center)
    ax.text(0.5, 0.8, user_text1, fontsize=24, ha="center", va="center")
    
    # List items (left aligned under main text)
    ax.text(0.2, 0.6, user_text2, fontsize=20, ha="left", va="center")
    ax.text(0.2, 0.45, user_text3, fontsize=20, ha="left", va="center")
    ax.text(0.2, 0.3, user_text4, fontsize=20, ha="left", va="center")
    
    ax.axis("off")  # Hide axes

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    # Display image
    st.image(buf, caption="Generated Image")

    # Download button
    st.download_button(
        label="Download Image",
        data=buf,
        file_name="text_image.png",
        mime="image/png"
    )
