import streamlit as st

st.title('WELCOME')

c1,c2 = st.columns([3,1])
with c1:
  st.image("charan photo.jpg",)

with c2:
    st.title('''CHARAN
    KUMAR
    REDDY
    SOMAGARI''')
    
    
st.write('print the image bro')
