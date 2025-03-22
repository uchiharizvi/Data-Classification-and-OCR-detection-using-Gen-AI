import streamlit as st
from langchain_community.llms import GPT4All
from langchain_core.prompts import PromptTemplate

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

local_path = (
    "C:/Users/Aditya Mangla/AppData/Local/nomic.ai/GPT4All/Llama-3.2-1B-Instruct-Q4_0.gguf"  # replace with your local file path
)

from langchain_core.callbacks import BaseCallbackHandler

count = 0


class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        global count
        if count < 10:
            print(f"Token: {token}")
            count += 1


# Verbose is required to pass to the callback manager
llm = GPT4All(model=local_path, callbacks=[MyCustomHandler()], streaming=True)

# If you want to use a custom model add the backend parameter
# Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
# llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, streaming=True)

chain = prompt | llm
st.title('🦜🔗 GPT4ALL Y\'All')
st.info('This is using the MPT model!')
prompt = st.text_input('Enter your prompt here!')
# question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

# Streamed tokens will be logged/aggregated via the passed callback
if prompt: 
    response = res = chain.invoke({"question": prompt})
    print(response)
    st.write(response)
# res = chain.invoke({"question": prompt})