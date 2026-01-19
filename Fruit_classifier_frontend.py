import streamlit as st
import requests
from PIL import Image
import io
from FruitClassifier import Predictor
import numpy as np 
import cv2
from gemini_setup import Gemini_ke_updesh
# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="ML + Gemini Assistant",
    page_icon="🤖",
    layout="centered"
)

# ---------------- UI ----------------
st.title("🤖 Fruit quality(Fresh/Rotten) prediction with gemini tips")
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
            img = np.array(image)
            img = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
            result = Predictor(img)
            advice = Gemini_ke_updesh()
            st.success("Prediction Successful!")
            # ML Prediction
            st.subheader("🔍 ML Prediction")
            st.write(result)

            # Gemini Explanation
            st.subheader("🧠 Gemini advice ")
            st.info(advice)




