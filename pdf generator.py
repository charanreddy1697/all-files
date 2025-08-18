import streamlit as st
from fpdf import FPDF

st.title("PDF Maker")

# user input
text = st.text_area("Enter your text here")

a1,a2,a3 = st.columns(3)
font = a1.selectbox('Font Style',['Arial', 'Times', 'Courier'])
Size = a2.number_input('Font Size')

Paper_size = a3.selectbox("Paper Size", ["A4", "Letter", "Custom"])

if Paper_size == "Custom":
    b1,b2 = st.columns(2)
    w = b1.number_input("Width (mm)", 50, 500, 210)
    h = b2.number_input("Height (mm)", 50, 500, 297)
    page_format = (w, h)
else:
    page_format = Size


c1,c2 = st.columns(2)
if c1.button("Generate PDF"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font(font, size=Size)
        pdf.multi_cell(0, 10, text)

        # convert to proper bytes
        pdf_output = bytes(pdf.output(dest="S"))

        c2.download_button(
            label="Download PDF",
            data=pdf_output,
            file_name="output.pdf",
            mime="application/pdf"
        )
