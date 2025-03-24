# Base Imports
import os
import streamlit as st

# Langchain Imports
from langchain_community.llms import GPT4All
from langchain_core.prompts import PromptTemplate
from langchain_core.callbacks import BaseCallbackHandler

# Local Path for LLm Model
local_path = (
    "C:/Users/Aditya Mangla/AppData/Local/nomic.ai/GPT4All/models/Llama-3.2-1B-Instruct-Q4_0.gguf"  # replace with your local file path
)

# Custom Handler to print tokens processed by LLm
count = 0
class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        global count
        if count < 10:
            # print(f"Token: {token}")
            count += 1


# Verbose is required to pass to the callback manager
llama1B = GPT4All(model=local_path, callbacks=[MyCustomHandler()], streaming=True)



def llm_process(email_text, llm):
    # Prompt_template
    template = """Act as an email traige gatekeeper for loan servicing department for the bank. As a gatekeeper you will get emails, your task is to distinguish them in the below request type.
    These are the request types in which you need to identify the email - Adjustment, Amount Transfer, Closing Notice, Commitment change, Fee Payment, Money Movement- inbound, money movement - outbound.
    Your answer should be the request type mentioned above to whom the email relates the best. Based on above classify this email : {email}. Give confidence score for each request type you predict.
    """
    # Prompt
    prompt = PromptTemplate.from_template(template)
    # LangChain
    if(llm is False):
        llm = llama1B
    chain = prompt | llm
    return chain.invoke({"email": email_text})

def summarize_email(email_text, attachement_text, llm):    
    # Prompt_template
    summarize_prompt = """You are a Language expert specializing in concise and meaningful summaries on the content of the email provided to you. 
    Generate a crisp summary of the email content provided to you which the user can glance at to quickly know the gist of the email without having to
    go through the email. The email is {email} and attachment text is {attachement_text}"""
    # Prompt
    prompt1 = PromptTemplate.from_template(summarize_prompt)
    # LangChain
    if(llm is False):
        llm = llama1B
    chain1 = prompt1 | llm  
    return chain1.invoke({"email": email_text, "attachement_text" : attachement_text})

def spam_flag(email_text, attachement_text, llm):
    # Prompt_template
    spam_prompt = """You are a spam email classifier whose task is to scan an email written to loan servicing team of bank and tell whether it is spam or not. 
    Your output should be only one word SPAM or NOT SPAM. Apply the above to this email is {email} and attachment text is {attachement_text}"""
    # Prompt
    prompt2 = PromptTemplate.from_template(spam_prompt)
    # LangChain
    if(llm is False):
        llm = llama1B
    chain2 = prompt2 | llm  
    return chain2.invoke({"email": email_text, "attachement_text" : attachement_text})

def duplicate_email_check(email_text, attachement_text, llm):
    # Prompt_template
    spam_prompt = """You are a duplicate email detector at a bank, you are task is to go through email and attachment and match it against other 
    emails and see if the data and purpose of any of them match If yes your output should be Duplicate otherwise Not Duplicate.
    The email is {email} and attachment is {attachement_text} compare them against {other_emails}"""
    # Prompt
    prompt3 = PromptTemplate.from_template(spam_prompt)
    # LangChain
    if(llm is False):
        llm = llama1B
    chain3 = prompt3 | llm
    # Fetching other emails to compare against
    other_emails = [""]
    files = [*list(os.listdir("./data/emails/"))]
    for fileName in files:
        file = open("./data/emails/"+fileName, encoding='UTF-8')
        other_emails.append(file.read())
        file.close()
    return chain3.invoke({"email": email_text, "attachement_text" : attachement_text, "other_emails" : other_emails})

# todo : add loggers