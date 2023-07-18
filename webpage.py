import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Google Stock Prediction", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("google.jpg")
img_lottie_animation = Image.open("google (2).jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Presenting you the Stock Market Prediction of ")
    st.title("GOOGLE")
    st.subheader("Using Time-Series Analysis")
    st.write(
        "In this project, we focused on analyzing the stock market data of Google over particular period of time and predicted future stock prices using two different methods: ARIMA (AutoRegressive Integrated Moving Average), SARIMAX (Seasonal AutoRegressive Integrated Moving Average with Exogenous Variables), and Deep Learning techniques including LSTM (Long Short-Term Memory) and RNN (Recurrent Neural Network)."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Why it was needed?")
        st.write("##")
        st.write(
            """
            I have worked on this project to get the most possible accurate results from machine learning models for the following purposes:
            - Accurate time series forecasting helps investors and traders make informed decisions regarding buying, selling, or holding Google stocks. 
            - Forecasting aids in risk management by identifying potential risks associated with Google stocks.
            - Time series forecasting plays a significant role in algorithmic trading strategies. 
            - It  provides valuable insights into the overall market trends and dynamics.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Have a look on the methods used!")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Time Series Forecasting Using ARIMA and SARIMAX")
        st.write(
            """
            Enter the world of Google stocks prediction, where the power of time series forecasting, fueled by the prowess of ARIMA(Auto Regressive Integrated Moving Averages) and SARIMAX(Seasonal ARIMA with Exogenous Variables), unlocks the secrets of market trends. Within the depths of historical stock data, these forecasting techniques weave intricate patterns, capturing the essence of Google's journey.
            """
        )
        st.markdown("[Get the code!](https://github.com/SakshiPorwal/GoogleStocks/blob/main/Google_ML.ipynb)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Time Series Forecasting Using Recurrent Neural Network(LSTM)")
        st.write(
            """
            The project on "Google stocks prediction using time series forecasting using RNN and LSTM" aims to utilize the power of Recurrent Neural Networks (RNN) with Long Short-Term Memory (LSTM) cells to predict future prices of Google stocks. By training the model on historical stock data, it can capture complex temporal patterns and relationships, allowing it to make accurate predictions. 
            """
        )
        st.markdown("[Get the code!](https://github.com/SakshiPorwal/GoogleStocks/blob/main/Google_DL.ipynb)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sakshiporwal2002@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()