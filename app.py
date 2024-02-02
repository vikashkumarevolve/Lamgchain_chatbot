from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

# to load openai model and get response

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv["OPENAI_API_KEY"],model_name='text-davinci-003',template=0.6)
    response=llm(question)
    return response
    
    
### We will Intialize our streamlit app

st.set_page_config(page_title="Q&A demo")
st.header("Langchain Application")

input=st.text_input("Input:",key="input")
response=get_openai_response(input)

submit=st.button("ask the question")

if submit:
    st.subheader("the response is")
    st.write(response)
