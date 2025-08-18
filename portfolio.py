import streamlit as st

st.set_page_config(layout="wide")

c1,c2 = st.columns([1,2],gap = "medium")
with c1:
    st.image("charan photo.jpg")

with c2:
    st.header("Hello")
    st.markdown(
        """
        <p style='font-size:18px; text-align:justify;'>
        <br/>
        I’m <b> Charan Kumar Reddy</b>, a skilled Data Engineer with expertise in data visualization, transformation, and management. 
        With a strong background in tools like Tableau, SQL, Python, PySpark and Azure Data Factory, I specialize in designing and 
        optimizing data pipelines, creating insightful dashboards, and ensuring data accuracy for business decision-making. 
        Passionate about turning raw data into actionable insights, I strive to bridge the gap between complex datasets 
        and clear, impactful business outcomes.
        </p>
        """ ,
        unsafe_allow_html=True)


st.markdown('''---''')

st.title('You can try my apps below')
a1,a2,a3,a4 = st.columns(4)

a1.link_button('CSV maker', 'https://charansomagari-csv-generator.streamlit.app/')
a2.link_button('PDF maker', 'https://charansomagari-pdf-generator.streamlit.app/')
a3.link_button('IMAGE maker', 'https://charansomagari-image-generator.streamlit.app/')
a4.link_button('IPL GAME', 'https://charansomagari-cricket-games.streamlit.app/')
