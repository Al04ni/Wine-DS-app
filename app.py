import streamlit as st
import requests
import streamlit_lottie as st_lottie
from streamlit_lottie import st_lottie

# Define the URL of your FastAPI backend
API_URL = "http://localhost:8000/predict"

#Page properties
st.set_page_config(
    page_title="Wine Quality App",
    page_icon="🍷",
    layout="centered",
    initial_sidebar_state="auto",
)

# Create a function to make a prediction request to the FastAPI backend
def predict_wine(features):
    response = requests.post(API_URL, json=features)
    return response.js
    on()

# Load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animation URL
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_animation = load_lottieurl(lottie_url)

###################################################################################################################
######################################SideBar######################################################################
################################################################################################################
with st.sidebar:
    st.markdown('''
                <p style="text-align: center; font-size:30px">
                <span> About</span>''',
                unsafe_allow_html=True)
    
    st_lottie(lottie_animation, height=200, key="wine")
    with st.expander("In Nutshell 💀"):
        st.caption(f'''We leveraged the machine learning technique(LogisticRegression) to predict the quality of the wine based on its different ingredients.
        Please note that it may hallucinate based on the data we used during training.''')
    
    st.markdown("")
    st.markdown('''
                <p style="text-align: center; font-size: 16px"> 
                <span>Feel free to modify any part of this project 
                to  fit your next project's specifics.</span>
                <br>
                <br>
                <span>Happy Coding!</span>
                </P>''',
                unsafe_allow_html=True
    )
    st.markdown(
        """
        <hr style="border: none; border-top: 1px solid #ccc; margin: 20px 0;">
        """,
        unsafe_allow_html=True,
        )
    st.markdown("[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Al04ni/Wine-DS-app?quickstart=1)")
#######################################################################################################################
######################################################################################################################
# ########################################Streamlit app##############################################################
#####################################################################################################################
st.title("Wine Quality Prediction")

#Adding markdown
st.markdown('''Wine has a rich history dating back over 8,000 years, originating in the
Caucasus region of Georgia—ancient civilizations, including the Egyptians and Greeks, 
revered wine for its cultural and religious significance. 
The Romans expanded viticulture across Europe, establishing vineyards that laid the groundwork for modern wine production.''')

# Add a YouTube video
st.video("https://youtu.be/7RS9Ntnq9tA?si=qTB9n_o5_Vk-CjZz")  # Replace with your video ID

#The rest of the page
with st.expander("Wine storing Tips!"):
        st.caption(f'''To store wine at home, keep bottles upright in a cool, 
            dark place with stable temperatures (50-55°F), moderate humidity (around 70%), and minimal vibration to preserve quality.''')

st.markdown('''During the Middle Ages, monasteries preserved winemaking techniques. 
The New World saw the introduction of wine in the 16th century with Spanish and Portuguese colonization. Today, wine is produced globally, 
with diverse styles reflecting regional climates and traditions, making it an integral part of culinary and social experiences worldwide.''')

#Defining the container for measurements
with st.container(border=True):
    st.subheader("Exploring Wine Features o_o")
    st.markdown('''Various chemical features are analyzed to measure wine quality, including alcohol content, acidity levels, and phenolic compounds.
                By evaluating these attributes, experts can assess the wine's balance, complexity, and overall quality profile, making informed 
                recommendations for food pairings or aging potential.''')
    with st.expander("How it works?"):
            st.caption('''For instance, consider a wine sample with an alcohol content of 13.5%, which indicates a balanced strength. The malic acid level of 
            0.5 g/L suggests a fresh acidity that enhances the wine's crispness. High total phenols at 2.5 g/L and flavonoids at 1.2 g/L contribute to a rich 
            flavor profile and potential aging ability. A color intensity 5.0 indicates a deep hue, often associated with quality red wines, while a proline 
            level of 1.8 g/L can suggest the wine's body and mouthfeel.''')
            
            
    # Input fields for wine features
    alcohol = st.number_input("Alcohol", format="%.2f")
    malic_acid = st.number_input("Malic Acid", format="%.2f")
    ash = st.number_input("Ash", format="%.2f")
    alcalinity_of_ash = st.number_input("Alcalinity of Ash", format="%.2f")
    magnesium = st.number_input("Magnesium", format="%.2f")
    total_phenols = st.number_input("Total Phenols", format="%.2f")
    flavanoids = st.number_input("Flavanoids", format="%.2f")
    nonflavanoid_phenols = st.number_input("Nonflavanoid Phenols", format="%.2f")
    proanthocyanins = st.number_input("Proanthocyanins", format="%.2f")
    color_intensity = st.number_input("Color Intensity", format="%.2f")
    hue = st.number_input("Hue", format="%.2f")
    od280_od315_of_diluted_wines = st.number_input("OD280/OD315 of Diluted Wines", format="%.2f")
    proline = st.number_input("Proline", format="%.2f")

# Predict button with spinner
    if st.button("Predict"):
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

#Footer 
st.markdown("# Note:")
st.markdown('''Moderate wine consumption can offer health benefits, 
            particularly for cardiovascular health. Research indicates 
            that light to moderate drinking, defined as one glass daily 
            for women and two for men, is linked to a 30-50% reduction in heart disease risk (Herszage & Ebeler, 2011).
''')

st.markdown(
        """
        <p style="text-align: center; font-size: 16px; margin: 50px 0px">
        <span>Enjoy responsibly 😉!</span>
        </p>
        """,
        unsafe_allow_html=True,
        )
st.markdown(
        """
        <hr style="border: none; border-top: 1px solid #ccc; margin: 50px 0px 0px 15px;">
        <p style="text-align: center; font-size: 14px;">
        <span>Developed with ❤️ from Kigali, Rwanda.</span>
        </p>
        """,
        unsafe_allow_html=True,
        )
