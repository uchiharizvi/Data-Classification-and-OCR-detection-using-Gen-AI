import streamlit as st
from langchain_community.llms import GPT4All
from langchain_core.prompts import PromptTemplate
import datetime
import os
from llms.gpt4all.src.lib.attachments import extract_attachments
from llm import summarize_email, llm_process, spam_flag, duplicate_email_check
from Utils.Util import saveEmailAttachement

st.title('# Welcome to Email Triage Gatekeeper! 👋')
st.info('This is an email traige gatekeeper that uses LLM to tell which team this email should be routed to, along with summary from attachment and email.')
email_text = st.text_input("Enter your email which you want to classify", placeholder="Email")
uploaded_file = st.file_uploader("Upload email attachment")

if uploaded_file and email_text is not None:    
    attachments_text = extract_attachments(uploaded_file)
    saveEmailAttachement(email_text, attachments_text, uploaded_file.name)
    st.write(llm_process(email_text, False))
    st.write(summarize_email(email_text,attachments_text, False))
    st.write(spam_flag(email_text, attachments_text, False))
    st.write(duplicate_email_check(email_text, attachments_text, False))
    