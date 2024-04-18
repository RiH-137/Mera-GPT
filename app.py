from dotenv import load_dotenv
load_dotenv()                      ## loadind all the environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))                  ## configuring the google generative AI



##function to load Gemini Pro model and get responses

model=genai.GenerativeModel("gemini-pro")       #gemini-pro--> text   gemini-pro-vision--> img
def get_gemini_reponse(question):
    response=model.generate_content(question)
    return response.text

##initiliazing the streamlit application
st.set_page_config(page_title="Mera GPT",page_icon="1.png")

st.header("Mera GPT - A LLM Application")
st.write("Ask your questions or ""sawaal"" and get answers or ""jawaab""....")
input=st.text_input("Ask your question or ""Sawaal""....")
submit=st.button("Get Answer or ""Jawaab""....")    


    ##whwn the submit button is clicked
if submit:
    if input:
        response=get_gemini_reponse(input)
        st.subheader("Answer or ""Jawaab""....")
        st.write(response)
    else:
        st.write("Please enter a question or ""sawaal""....")        
            

    












