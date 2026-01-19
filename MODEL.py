from fastapi import FastAPI , File , UploadFile
import io
from FruitClassifier import Predictor
from PIL import Image
import numpy as np 
import cv2
from gemini_setup import Gemini_ke_updesh
app = FastAPI()
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = np.array(image)
    img = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
    result = Predictor(img)
    advice = Gemini_ke_updesh()
    return {"Prediction": result ,"Expert advice": advice}