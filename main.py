import streamlit as st

# configurations for the page
st.set_page_config(layout="wide")

# to create the columns
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Nuhirath Rafthia")
    content = """
    As an Honors Student at Columbia University, I am passionate about Computer Science. 
    More specifically, I have a keen focus on the Intelligent Systems Track. 
    My journey in the world of technology has been marked by a diverse range of experiences 
    that have honed my skills and knowledge.
    """
    st.info(content)
