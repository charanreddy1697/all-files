import streamlit as st

st.title('WELCOME')

c1,c2 = st.columns([3,1])
with c1:
  st.image("charan photo.jpg",)

with c2:
    st.markdown(
        "<p style='font-size:24px;'>CHARAN<br>KUMAR<br>REDDY<br>SOMAGARI</p>",
        unsafe_allow_html=True
    )

    
    
st.write('print the image bro')
