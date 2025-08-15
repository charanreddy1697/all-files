import streamlit as st

st.title('CHARAN KUMAR REDDY SOMAGARI')

c1,c2,c3 = st.columns([3,1,1])
with c1:
  st.image("charan photo.jpg",)

with c3:
    st.title('welcome')
    st.header('''My self Charan Kumar Reddy, Data Engineer
    by profession skilled in Visualization, Transforming and
    managing the data.
    ''')

    
st.write('print the image bro')
