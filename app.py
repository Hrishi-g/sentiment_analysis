from sentiment import SentimentAnalysis
import streamlit as st
import pandas as pd
import emoji
#from IPython.display import Audio
import base64
# Define Streamlit app
#

# # Determine the theme based on the sentiment
#     if sentiment == "Positive":
#         st.experimental_set_query_params(theme="solarized_light")
#         output_sentiment = "Positive"
#     elif sentiment == "Negative":
#         st.experimental_set_query_params(theme="dark")
#         output_sentiment = "Negative"
#     else:
#         st.experimental_set_query_params(theme="default")
#         output_sentiment = "Neutral"
        
#     st.write("The input text is classified as:", output_sentiment)
st.title("Text Classification with Random Forests")
input_text = st.text_input("Enter some text to classify:")
sentiment = SentimentAnalysis(input_text)


def get_emoji(sentiment):
    if sentiment == "Positive":
        return emoji.emojize(":smiling_face_with_heart-eyes:")
    elif sentiment == "Negative":
        return emoji.emojize(":worried_face:")
    else:
        return emoji.emojize(":neutral_face:")
    
font_size = "60px"

def get_audio(score):
    if sentiment == "Positive":
        return "music/happy.mp3"
    elif sentiment == "Negative":
        return "music/sad.mp3"
    # elif score > 0:
    #     return "calm_audio.mp3"
    else:
        return "music/sad.mp3"
    
# def autoplay_audio(file_path: str):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         md = f"""
#             <audio controls autoplay="true">
#             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#             </audio>
#             """
#         st.markdown(
#             md,
#             unsafe_allow_html=True,
#         )

if input_text:
    sentiment = SentimentAnalysis(input_text)
    st.write(f'<span style="font-size:{font_size}">{get_emoji(sentiment)}</span>',  unsafe_allow_html=True)
    
    audio_file = open(get_audio(sentiment), "rb")
    #autoplay_audio(audio_file)
    audio_bytes = audio_file.read()
    #st.audio(audio_bytes, format="audio/mp3")
    audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")
    #b64 = base64.b64encode(data).decode()
    st.markdown(f'<audio controls="controls"><source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3" /></audio>', unsafe_allow_html=True)
