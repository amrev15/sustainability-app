# Import Libraries

import openai
import streamlit as st
from streamlit_chat import message
import os

# Open API key

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# openai.api_key = st.secrets["OPENAI_API_KEY"]

# Generating responses from the api

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    messages = completions.choices[0].text
    return messages

# Creating the chatbot interfaces

import streamlit as st

import streamlit as st
from PIL import Image

# Load the image
original_image = Image.open('sustainability.jpg')  # Replace 'image.jpg' with the actual path to your image

# Define a compression ratio (adjust as needed)
compression_ratio = 0.5

# Calculate new dimensions
new_width = int(original_image.width * compression_ratio)
new_height = int(original_image.height * compression_ratio)

# Resize the image
compressed_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)

# Display the compressed image using Streamlit
st.image(compressed_image, caption='Sustainability', use_column_width=True)

st.title("Sustainability AI Chatbot")

# Storing the input

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Creating a function that returns the user's input from a text input field

def get_text():
    input_text = st.text_input("You : ", "Hello, how are you?", key = "input")
    return input_text

# We will generate response using the 'generate response' function and store into variable called output

user_input = get_text()

if user_input:
    output = generate_response(user_input)

    # Store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)


# Finally we display the chat history

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) -1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')










