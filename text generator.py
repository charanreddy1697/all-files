import streamlit as st
import matplotlib.pyplot as plt
import io

st.title("🖼️ Text to Image (Matplotlib)")

# User input
user_text1 = st.text_input("Enter your text for main:", "Hello Streamlit!")
user_text2 = st.text_input("Enter your text for list1:", "Hello Streamlit!")
user_text3 = st.text_input("Enter your text for list2:", "Hello Streamlit!")
user_text4 = st.text_input("Enter your text for list1:", "Hello Streamlit!")

# Button to generate
if st.button("Generate Image"):
    # Create figure
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.text(0.1, 0.7, user_text1, fontsize=24, ha="center", va="center")
    ax.text(0.1, 0.5, user_text2, fontsize=21, ha="center", va="center")
    ax.text(0.1, 0.3, user_text3, fontsize=21, ha="center", va="center")  
    ax.text(0.1, 0.1, user_text4, fontsize=21, ha="center", va="center")  
    
    
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
