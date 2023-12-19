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
    As an Honors Student at Columbia University, I am passionate about Computer Science. 
    More specifically, I have a keen focus on the Intelligent Systems Track. 
    My journey in the world of technology has been marked by a diverse range of experiences 
    that have honed my skills and knowledge.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

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

