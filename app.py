import streamlit as st
import requests
import streamlit_lottie as st_lottie
from streamlit_lottie import st_lottie

# Define the URL of your FastAPI backend
API_URL = "http://localhost:8000/predict"

# Create a function to make a prediction request to the FastAPI backend
def predict_wine(features):
    response = requests.post(API_URL, json=features)
    return response.json()

# Load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animation URL
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_animation = load_lottieurl(lottie_url)

# Streamlit app
st.title("Wine Quality Prediction")

# Add a YouTube video
st.video("https://youtu.be/7RS9Ntnq9tA?si=qTB9n_o5_Vk-CjZz")  # Replace with your video ID

# Add a Lottie animation
st_lottie(lottie_animation, height=200, key="wine")

# Input fields for wine features
st.sidebar.header("Input Wine Features")
alcohol = st.sidebar.number_input("Alcohol", format="%.2f")
malic_acid = st.sidebar.number_input("Malic Acid", format="%.2f")
ash = st.sidebar.number_input("Ash", format="%.2f")
alcalinity_of_ash = st.sidebar.number_input("Alcalinity of Ash", format="%.2f")
magnesium = st.sidebar.number_input("Magnesium", format="%.2f")
total_phenols = st.sidebar.number_input("Total Phenols", format="%.2f")
flavanoids = st.sidebar.number_input("Flavanoids", format="%.2f")
nonflavanoid_phenols = st.sidebar.number_input("Nonflavanoid Phenols", format="%.2f")
proanthocyanins = st.sidebar.number_input("Proanthocyanins", format="%.2f")
color_intensity = st.sidebar.number_input("Color Intensity", format="%.2f")
hue = st.sidebar.number_input("Hue", format="%.2f")
od280_od315_of_diluted_wines = st.sidebar.number_input("OD280/OD315 of Diluted Wines", format="%.2f")
proline = st.sidebar.number_input("Proline", format="%.2f")

# Predict button with spinner
if st.sidebar.button("Predict"):
    with st.spinner('Predicting...'):
        features = {
            "alcohol": alcohol,
            "malic_acid": malic_acid,
            "ash": ash,
            "alcalinity_of_ash": alcalinity_of_ash,
            "magnesium": magnesium,
            "total_phenols": total_phenols,
            "flavanoids": flavanoids,
            "nonflavanoid_phenols": nonflavanoid_phenols,
            "proanthocyanins": proanthocyanins,
            "color_intensity": color_intensity,
            "hue": hue,
            "od280_od315_of_diluted_wines": od280_od315_of_diluted_wines,
            "proline": proline
        }
        result = predict_wine(features)
        st.success(f"Prediction: {result['prediction']}")
