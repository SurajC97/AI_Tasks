openai_key ='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'

## Integrate our code OpenAI API
import os
# from constants import openai_key
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Langchain Demo With OPENAI API')
# input_text=st.text_input("Hi i am orderbot")

## OPENAI LLMS
# llm=OpenAI(temperature=0.8)
chat = ChatOpenAI(temperature=0)

# messages = [
#     SystemMessage(
#         content="You are a helpful assistant that translates English to hindi."
#     ),
#     HumanMessage(
#         content="Translate this sentence from English to Hindi. I love programming."
#     ),
# ]

def collect_messages(inp):
    prompt = inp
    input_text = ''
    messages.append(HumanMessage(content= f"{prompt}"))
    response = chat(messages).content
    messages.append(AIMessage(content= f"{response}"))
    return response

messages =  [
SystemMessage(content="""You are OrderBot, an automated service to collect orders for a pizza restaurant. \
            You first greet the customer, then collects the order, and then asks if it's a pickup or delivery.""")]
# HumanMessage(content='Hi, my name is Isa')  ]

input_text='hi'
while input_text:
    # st.write(chat(messages).content)
    input_text=st.text_input("Hi i am Orderbot", key= input_text)
    st.write(collect_messages(input_text))
    
