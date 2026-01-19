import streamlit as st
import requests
from PIL import Image
import io

# ---------------- CONFIG ----------------
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="ML + Gemini Assistant",
    page_icon="🤖",
    layout="centered"
)

# ---------------- UI ----------------
st.title("🤖 ML Prediction with Gemini Explanation")
st.markdown("Upload an image to get **ML prediction + AI advice**.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png" , "webp"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🚀 Predict"):
        with st.spinner("Running ML model..."):
            files = {
                "file": uploaded_file.getvalue()
            }

            response = requests.post(API_URL, files=files)
        if response.status_code == 200:
            data = response.json()

            st.success("Prediction Successful!")

            # ML Prediction
            st.subheader("🔍 ML Prediction")
            st.write(data.get("Prediction"))

            # Gemini Explanation
            st.subheader("🧠 Gemini Explanation")
            st.info(data.get("Expert advice"))

        else:
            st.error("Failed to get response from API")
