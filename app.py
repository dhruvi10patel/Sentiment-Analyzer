from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def get_sentiment_analysis(text):
    prompt = f"Analyze the sentiment of the following text and provide a summary with the following parametersin a tabular format strictly:\n" \
             f"- Overall Sentiment\n" \
             f"- Sentiment Score\n" \
             f"- Key Phrases\n" \
             f"- Emotion Categories\n" \
             f"- Confidence Score\n" \
             f"- Polarity\n" \
             f"- Subjectivity\n" \
             f"- Suggestions for Improvement\n" \
             f"- Highlights of Positive/Negative Aspects\n\n" \
             f"Text: {text}"
            
    response = genai.GenerativeModel('gemini-pro').generate_content([prompt])
    return response.text

#######################################################################################################################
# Streamlit app layout

st.set_page_config(page_title="Sentiment Analysis", layout="wide")

avs.add_vertical_space(5) 

col1, col2 = st.columns([3, 2]) 

with col1: 
    st.title("SentimentSense")
    st.header("Uncovering Emotions with Precision")
    st.markdown("""<p style='text-align: justify;'>
                        Introducing SentimentSense – your advanced sentiment analysis assistant powered by 
                        cutting-edge AI technology. Designed to provide detailed and accurate insights into 
                        the emotions and opinions expressed in text, SentimentSense simplifies the process of 
                        understanding textual sentiment. Whether you're a business looking to analyze customer 
                        feedback, a social media manager monitoring brand sentiment, or an educator seeking to 
                        enhance students' understanding of textual emotion, SentimentSense offers tailored 
                        solutions to meet your needs. With its ability to analyze sentiment, identify key phrases, 
                        and offer actionable suggestions for improvement, SentimentSense revolutionizes the way 
                        you interpret and leverage textual data. Experience seamless sentiment analysis with 
                        SentimentSense and unlock new insights into the emotions conveyed in text.
                        </p>""", unsafe_allow_html=True)


 
with col2:
    avs.add_vertical_space(5) 
    img = Image.open("images/icon.png")
    st.image(img, use_column_width=True)


avs.add_vertical_space(10) 

##############################################################################

col1, col2 = st.columns([3, 2])

with col1:
    img1 = Image.open("images/icon1.png")
    st.image(img1, use_column_width=True)

with col2:
    avs.add_vertical_space(4) 
    st.header("Wide Range of Offerings")
    st.write("- Detailed Sentiment Analysis")
    st.write("- Effortless Customer Feedback Analysis")
    st.write("- Real-time Social Media Monitoring")
    st.write("- Educational Assistance")
    st.write("- Tailored Solutions for Different User Needs")
    
avs.add_vertical_space(10)

##########################################################################

col1, col2 = st.columns([3, 2]) 

with col1: 
    st.title("Let's Engage")
    st.header("Share your content for a sentiment analysis synopsis:")
    input_text = st.text_area("Input Text Here", height=100)

    if st.button("Analyze Sentiment"):
        if input_text:
            with st.spinner("Analyzing sentiment..."):
                sentiment_summary = get_sentiment_analysis(input_text)
                st.subheader("Sentiment Analysis Result")
                st.write(sentiment_summary)
        else:
            st.error("Please enter text to analyze the sentiment.")

with col2:
    img2 = Image.open("images/icon2.png")
    st.image(img2, use_column_width=True)
    
avs.add_vertical_space(10)

##########################################################################


col1, col2 = st.columns([2, 3])

with col1:
    avs.add_vertical_space(5)
    img3 = Image.open("images/icon3.png")
    st.image(img3, use_column_width=True)

with col2:
    st.write("Q: What is SentimentSense?")
    st.write("""A: SentimentSense is an advanced project powered by a Large Language Model (LLM) 
             designed to provide detailed and accurate sentiment analysis of text. It simplifies 
             the process of understanding emotions and opinions in text by offering comprehensive 
             insights.""")
    avs.add_vertical_space(3)
    st.write("Q: What insights does SentimentSense provide?")
    st.write("""A: SentimentSense offers insights such as overall sentiment (Positive, Negative, 
             Neutral), sentiment score, key phrases, emotion categories, confidence score, polarity, 
             subjectivity, and suggestions for improvement.""")
    avs.add_vertical_space(3)
    st.write("Q: How can SentimentSense be used in Customer Feedback Analysis?")
    st.write("""A: Businesses can input customer reviews into SentimentSense to obtain an overall 
             sentiment, sentiment score, and highlighted key phrases. This helps in understanding 
             customer satisfaction levels and identifying areas for improvement.""")











