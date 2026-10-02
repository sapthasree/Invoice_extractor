from dotenv import load_dotenv

load_dotenv() # load all env variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini 
model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # read the file into bytes
        byte_data = uploaded_file.getvalue()

        img_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":byte_data
            }
        ]
        return img_parts
    else:
        raise FileNotFoundError("No file uploaded.")

# initializing streamlit app
st.set_page_config(page_title = "Multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")
input = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice..", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as invoice 
and you'll have to answer any questions based on the uploaded invoice image.
"""

if submit:
    img_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, img_data, input)
    st.subheader("Response is:")
    st.write(response)