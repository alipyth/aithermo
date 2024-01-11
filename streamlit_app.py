#pip install -q -U google-generativeai
#pip install ipython
#pip install pillow
#PIP INSTALL STREAMLIT
import streamlit as st
from PIL import Image
import google.generativeai as genai
from deep_translator.google import GoogleTranslator

#api = st.text_input('put your api')

API = "AIzaSyBIpp1qQ6kNvphSlxHlsRsSFUlpn-LXUko"

genai.configure(api_key=API)
model = genai.GenerativeModel('gemini-pro-vision')
picture = st.camera_input("Take a picture")
pr = 'According to This Picture ,Act Like A Interior Designer and Tell Me How Can I Improve My Design , at the end tell me what you see in this image '
but = st.button('Lets Go')
if picture and but :
    img = Image.open(picture)
    response = model.generate_content([pr , img])
    st.image(img)
    st.markdown(response.text)
    translated = GoogleTranslator(source='auto', target='fa').translate(response.text)
    st.markdown(translated)

st.info('Developed By : Ali Jahani satreyek@gmail.com')
