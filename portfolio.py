import streamlit as st

st.set_page_config(layout="wide")

c1,c2 = st.columns([1,2],gap = "large")
with c1:
    st.image("charan photo.jpg")

with c2:
    st.markdown(
        """
        <p style='font-size:18px '>
        I’m Charan Kumar Reddy, a skilled Data Engineer with expertise in data visualization, transformation, and management. 
        With a strong background in tools like Tableau, PySpark, Azure Data Factory, and SQL, I specialize in designing and 
        optimizing data pipelines, creating insightful dashboards, and ensuring data accuracy for business decision-making. 
        Passionate about turning raw data into actionable insights, I strive to bridge the gap between complex datasets 
        and clear, impactful business outcomes.
        </p>
        """ )

