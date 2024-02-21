import streamlit as st
import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    ServiceContext,
)
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.callbacks import CallbackManager
from llama_index.llms.ollama import Ollama


st.set_page_config(page_title="AskHR Chatbot, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("AskHR, powered by LlamaIndex 💬🦙")
st.info("You can ask questions about HR policy documents", icon="📃")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about the different policies!"}
    ]


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing policy documents - hang tight! This should take 1-2 minutes."):
        # check if storage already exists
        PERSIST_DIR = "./storage"
        llm = Ollama(model="phi", request_timeout=120)
        if not os.path.exists(PERSIST_DIR):
            reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
            docs = reader.load_data()
            embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
            callback_manager = CallbackManager()
            index = VectorStoreIndex.from_documents(docs, embed_model=embed_model, callback_manager=callback_manager)
            # store it for later
            index.storage_context.persist(persist_dir=PERSIST_DIR)
            return index, llm
        else:
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
        return index, llm


index, llm = load_data()


if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
    st.session_state.chat_engine = index.as_query_engine(llm=llm, verbose=True, streaming=True, similarity_top_k=1)


if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])


# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response = st.session_state.chat_engine.query(prompt)
        with st.empty():
            output = ''
            for text in response.response_gen:
                output += text + ' '
                st.write(output)
        message = {"role": "assistant", "content": output}
        st.session_state.messages.append(message) # Add response to message history