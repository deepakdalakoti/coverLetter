from llm import LLM
from parsers import Parser
import streamlit as st
import time
import tempfile
from datetime import datetime


def generate():
    if file is None or jd is None:
        return

    with st.spinner("Generating..."):
        temp_file = tempfile.NamedTemporaryFile()
        temp_file.write(file.getvalue())
        doc_parser = Parser()
        text = doc_parser.parse(file.name, temp_file.name)
        temp_file.close()
        output = LLM().generate_output(text, jd, **{"temperature": add_slider})

    st.session_state["generated_text"] = output
    st.write()


st.set_page_config(page_title="Cover Letter")


st.sidebar.title("Cover letter generater")

file = st.sidebar.file_uploader("Upload CV (pdf/word)", type=["pdf", "docx"])

jd = st.sidebar.text_area(label="Add job description")

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Creativity", 0.0, 1.0, 0.2)
action_button = st.sidebar.button("Generate", on_click=generate)

placeholder = st.empty()
placeholder.text_area(label="Generated Cover Letter", height=800, key="generated_text")
