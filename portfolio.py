import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Charan Kumar Reddy Portfolio", layout="wide")

# ---- HEADER ----
st.title("WELCOME")

# ---- PHOTO + INTRO SECTION ----
c1, c2 = st.columns([1, 2], gap="large")

with c1:
    st.image(
        "https://raw.githubusercontent.com/charanreddy1697/all-files/main/charan%20photo.jpg",
        
    )

with c2:
    st.markdown(
        """
        <h2 style='margin-bottom:0;'>Charan Kumar Reddy Somagari</h2>
        <h4 style='margin-top:0; color:gray;'>Data Engineer</h4>
        <p style='font-size:18px; line-height:1.6;'>
        I’m Charan Kumar Reddy, a skilled Data Engineer with expertise in data visualization, transformation, and management. 
        With a strong background in tools like Tableau, PySpark, Azure Data Factory, and SQL, I specialize in designing and 
        optimizing data pipelines, creating insightful dashboards, and ensuring data accuracy for business decision-making. 
        Passionate about turning raw data into actionable insights, I strive to bridge the gap between complex datasets 
        and clear, impactful business outcomes.
        </p>
        """,
        unsafe_allow_html=True
    )

# ---- SEPARATOR ----
st.markdown("---")

# ---- SKILLS SECTION ----
st.subheader("Skills")
st.write("""
- **Visualization:** Tableau, Power BI  
- **Data Processing:** PySpark, Pandas  
- **ETL & Data Pipelines:** Azure Data Factory, SQL  
- **Big Data:** Hadoop  
- **Cloud:** Azure  
""")

# ---- PROJECTS SECTION ----
st.subheader("Projects")
st.write("""
1. **Financial Performance Dashboard** – Designed an executive-level dashboard to track banking and investment KPIs.  
2. **Superstore Annual Report** – Built an interactive Tableau dashboard to analyze annual sales trends and product performance.  
3. **Automated Data Pipeline** – Created a PySpark-based pipeline integrated with Azure Data Factory for real-time processing.  
""")

# ---- CONTACT SECTION ----
st.subheader("Contact")
st.write("""
📧 Email: charan.kumar@example.com  
🔗 LinkedIn: [linkedin.com/in/charanreddy](https://linkedin.com/in/charanreddy)  
💻 GitHub: [github.com/charanreddy1697](https://github.com/charanreddy1697)  
""")
