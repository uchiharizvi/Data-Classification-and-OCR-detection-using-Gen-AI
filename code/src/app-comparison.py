# App dev framework
import streamlit as st
import os
import logging

# Import depdencies 
from langchain_community.llms import GPT4All
from langchain_core.prompts import PromptTemplate
from lib.attachments import extract_attachments
from llm import summarize_email, llm_process, spam_flag, duplicate_email_check
from Utils.Util import saveEmailAttachement
# from lib.spam_detection import detect_spam

# Define Logger
logger = logging.getLogger("app_comparison.py")

# Path to weights 
BASE_PATH = 'C:/Users/Aditya Mangla/AppData/Local/nomic.ai/GPT4All/models/'

#  callback method
from langchain_core.callbacks import BaseCallbackHandler
count = 0
class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        global count
        if count < 10:
            print(f"Token: {token}")
            count += 1

# Title 
st.title('# Welcome to Email Triage Gatekeeper! 👋')

with st.sidebar:
    st.info('This is an email traige gatekeeper that uses LLM to tell which team this email should be routed to, along with summary from attachment and email.')
    option = st.radio('Choose your task', ['Base Gen', 'Summarization', 'Spam Check', 'Duplicate Check'])
    # Model Options to select from Locally available models
    models =  [*list(os.listdir(BASE_PATH))]
    model = st.radio('Choose your model', models)
    st.write(model)
    # Path For model selected
    PATH = f'{BASE_PATH}{model}'
    # Instance of llm
    llm = GPT4All(model=(PATH), callbacks=[MyCustomHandler()], streaming=True) 
        # , verbose=True, temp=0.1, n_predict=4096, top_p=.95, top_k=40, n_batch=9, repeat_penalty=1.1, repeat_last_n=1.1        

if option=='Base Gen': 
    st.info('Use this application to perform email traige routing to return Request Type.')
    # Input
    email_text = st.text_input("Enter your email which you want to classify", placeholder="Email")
    uploaded_file = st.file_uploader("Upload email attachment")
      
    if uploaded_file and email_text is not None:
        attachments_text = extract_attachments(uploaded_file)
        logger.info("Got email : {} and Attachment : {}".format(email_text, attachments_text))
        saveEmailAttachement(email_text, attachments_text, uploaded_file.name)
        logger.info("Saved email and attachment")
        # Pass the prompt to the LLM Chain
        response = llm_process(email_text, llm)
        logger.info("Response post processing from LLM : "+response)
        # do this
        st.write(response)    

       
if option=='Spam Check': 
    st.info('Use this application to check whether the mail is spam or not.')
    # Input
    email_text = st.text_input("Enter your email which you want to classify", placeholder="Email")
    uploaded_file = st.file_uploader("Upload email attachment")
 
    if uploaded_file and email_text is not None:
        attachments_text = extract_attachments(uploaded_file)
        logger.info("Got email : {} and Attachment : {}".format(email_text, attachments_text))
        saveEmailAttachement(email_text, attachments_text, uploaded_file.name)
        logger.info("Saved email and attachment")
        # Pass the prompt to the LLM Chain
        response = spam_flag(email_text, attachments_text, llm)
        # Pass the email to ML Model
        # is_spam = detect_spam(email_text)        
        logger.info("Response post processing from LLM : "+response)
        # do this
        st.write(response)    

if option=='Summarization': 
    st.info('Use this application to perform summarization on blocks of text.')
    # Input
    email_text = st.text_input("Enter your email which you want to classify", placeholder="Email")
    uploaded_file = st.file_uploader("Upload email attachment")

    if uploaded_file and email_text is not None:
        attachments_text = extract_attachments(uploaded_file)
        logger.info("Got email : {} and Attachment : {}".format(email_text, attachments_text))
        saveEmailAttachement(email_text, attachments_text, uploaded_file.name)
        logger.info("Saved email and attachment")
        # Pass the prompt to the LLM Chain
        response = summarize_email(email_text,attachments_text, llm)
        logger.info("Response post processing from LLM : "+response)
        # do this
        st.write(response)  

if option=='Duplicate Check':     
    st.info('Use this application to perform duplicate check on the email or attachment')
    # Input
    email_text = st.text_input("Enter your email which you want to classify", placeholder="Email")
    uploaded_file = st.file_uploader("Upload email attachment")

    if uploaded_file and email_text is not None:
        attachments_text = extract_attachments(uploaded_file)
        logger.info("Got email : {} and Attachment : {}".format(email_text, attachments_text))
        saveEmailAttachement(email_text, attachments_text, uploaded_file.name)
        logger.info("Saved email and attachment")
        # Pass the prompt to the LLM Chain
        response = duplicate_email_check(email_text,attachments_text, llm)
        logger.info("Response post processing from LLM : "+response)
        # do this
        st.write(response)