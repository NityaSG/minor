import streamlit as st 
from PIL import Image
audio_file = open('flush.mp3', 'rb')
image = Image.open('poop.jpg')
audio_bytes = audio_file.read()

st.title("Haggu Simulator")
st.subheader("Experience the every mornin lively experience of waking upto the splendid sight of a piece of brownie competing you to a staredown")
if st.button("click me to see what's hot! slurp slurp slurp"):
    st.image(image, caption='Sunrise by the mountains')
if st.button('click here for Flush'):
    st.text("you cannot flush this majestic piece of brownie")
    st.audio(audio_bytes, format='audio/mp3',start_time=0)
    







