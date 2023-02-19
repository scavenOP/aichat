
import openai
import streamlit as st
import time
import datetime
import datetime 

openai.api_key= "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" 
model_engine = "text-davinci-002"


def ai(prompt):

    
    completion = openai.Completion.create( 
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n= 1,
        stop=None,
        temperature=0.9,
        )


    response = completion.choices[0].text
    return response


st.header("Chat GPT ka chota vai")


promt=st.text_input("Ask anything" ,)

if len(promt)>0:
    st.write(ai(promt))