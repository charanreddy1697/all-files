import streamlit as st
from fpdf import FPDF

st.title("📝 Simple PDF Maker")

# user input
text = st.text_area("Enter your text here")

if st.button("Generate PDF"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)

        # convert to proper bytes
        pdf_output = bytes(pdf.output(dest="S"))

        st.download_button(
            label="⬇️ Download PDF",
            data=pdf_output,
            file_name="output.pdf",
            mime="application/pdf"
        )
