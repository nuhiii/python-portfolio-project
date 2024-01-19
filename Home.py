import streamlit as st
import pandas

# configurations for the page
st.set_page_config(layout="wide")

# to create the columns
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Nuhirath Rafthia")
    content = """
    I possess a deep passion for technology, holding a degree in Computer Science from Columbia University—
    an esteemed Ivy League Institution consistently ranked among the top 5 universities globally.
    Throughout my academic journey, I immersed myself in the realm of Artificial 
    Intelligence, by pursuing the Intelligent Systems track and diving into various coursework and projects. 
    I took part in internship roles, partnering with further renowned institutions, that allowed me to bridge the gap 
    between a theoretical learning approach and active hands on research. I took the knowledge I gained from
    university and applied them to real world scenarios, at companies seeking to make an impact on the world. As such,
    I had the privilege of conducting research projects with CERN, Amazon, and IBM to name a few.
    Beyond formal education, I actively pursued self-learning, through open source. All in all, my journey in the world 
    of technology has been marked by a diverse range of experiences that have honed my skills and knowledge. Below are 
    a few of the projects I have worked on to showcase my technical proficiency, especially with the Python 
    programming language. In any case, feel free to contact me!
    """
    st.info(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df.iterrows():
        if index % 2 == 1:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

