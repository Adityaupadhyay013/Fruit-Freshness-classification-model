import cv2 
import numpy as np
from skimage.feature import graycomatrix , graycoprops , local_binary_pattern
import pandas as pd 
import joblib
def load_image(img , size = (128 , 128)):
  img = cv2.resize(img , size)
  return img
def extract_HSV(img):
  hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
  h , s , v = cv2.split(hsv)
  features = [
      np.mean(h) , np.std(h) ,
      np.mean(s) , np.std(s) ,
      np.mean(v) , np.std(v)
  ]
  return features
def extract_GLCM(img):
  gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
  glcm = graycomatrix(
      gray , distances = [1] , angles = [0]  , levels = 256 , symmetric = True , normed = True
  )
  contrast = graycoprops(glcm , 'contrast')[0 , 0]
  energy = graycoprops(glcm , 'energy')[0 , 0]
  homogeneity = graycoprops(glcm , 'homogeneity')[0 , 0]
  correlation = graycoprops(glcm , 'correlation')[0 , 0]
  return [contrast , energy , homogeneity , correlation]
def lbp_feature(img):
  gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
  lbp = local_binary_pattern(gray , P = 8 , R = 1 ,method = 'uniform')
  hist , _ = np.histogram(lbp , bins = 10 , range = (0 , 10))
  hist = hist.astype("float")
  hist /= (hist.sum()+1e-6)
  return hist.tolist()
def feature_extraction(img):
  img = load_image(img)
  color = extract_HSV(img)
  glcm = extract_GLCM(img)
  lbp = lbp_feature(img)
  return color+glcm+lbp
def Img_to_dframe(img):
    cols = [f"HSV_{i}" for i in range(6)] + [f"GLCM_{i}" for i in range(4)] + [f"LBP_{i}" for i in range(10)]
    df = pd.DataFrame([feature_extraction(img)] , columns = cols)
    return df
def Predictor(img):
    df = Img_to_dframe(img)
    model = joblib.load("Fruit Freshness Classification model.pkl")
    prediction = model.predict(df)
    if prediction[0] == 0:
        return "Rotten"
    else:
        return "Fresh"


