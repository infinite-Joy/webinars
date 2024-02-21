# 🦙📚 AskHR Chatbot, powered by LlamaIndex

Build an HR policy chatbot powered by LlamaIndex that augments works on Ollama app with ph model with the contents of the Streamlit docs (or your own data).

## Overview of the App

<!-- <img src="app.png" width="75%"> -->

- Takes user queries via Streamlit's `st.chat_input` and displays both user queries and model responses with `st.chat_message`
- Uses LlamaIndex to load and index data and create a chat engine that will retrieve context from that data to respond to each user query

## How to use the app

1. Install Ollama from here: https://github.com/ollama/ollama
2. Pull the phi2 model. You can pull a bigger model in case you have GPU and memory.

    ollama pull phi

In case you download a bigger model make the code change in the streamlit_app.py

    llm = Ollama(model="phi", request_timeout=120)

3. Run the Ollama app.

    ollama serve

4. Clone the app.

    git clone https://github.com/infinite-Joy/webinars.git
    cd creating_gpt_chatbots_for_enterprise_usecases

5. Install all the dependencies

    pip install poetry
    poetry install
    poetry shell

6. Now run the app

    streamlit run streamlit_app.py


## Try out the app

Once the app is loaded, enter your question about different HR related questions and wait for a response.

## Related Resources

This github code is developed for the webinar "Creating GPT chatbots for Enterprise Usecases" on 24 Feb 2024.

* Career guidance in Data Science and Machine Learning: https://topmate.io/joydeep_bhattacharjee
* Mock Machine Learning Interview App: https://vibrantai.academy/interview-trainer/chat?utm_source=github&utm_date=20240221

