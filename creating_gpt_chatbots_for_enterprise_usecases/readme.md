# 🦙📚 AskHR Chatbot, powered by LlamaIndex

Build an HR policy chatbot powered by LlamaIndex that augments works on Ollama app with ph model with the contents of the Streamlit docs (or your own data).

## Overview of the App

<img src="app.png" width="75%">

- Takes user queries via Streamlit's `st.chat_input` and displays both user queries and model responses with `st.chat_message`
- Uses LlamaIndex to load and index data and create a chat engine that will retrieve context from that data to respond to each user query

## How to use the app

1. Install Ollama from here: https://github.com/ollama/ollama
2. Pull the phi2 model. You can pull a bigger model in case you have GPU and memory.

    ollama pull phi

In case you download a bigger model make the code change in the streamlit_app.py

    llm = Ollama(model="phi", request_timeout=120)

3.


You can get your own OpenAI API key by following the following instructions:
1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

## Try out the app

Once the app is loaded, enter your question about the Streamlit library and wait for a response.