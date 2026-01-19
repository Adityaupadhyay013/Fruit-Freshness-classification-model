import google.generativeai as genai
import os
import re
genai.configure(api_key = os.getenv("Gemini_api_key"))
def Gemini_ke_updesh():
    try:
        model=genai.generativemodel("gemini-3-flash-preview"),
        prompt= "You are an fruit quality expert. Tell me tips for preventing fresh fruits from rotten. And effect of eating rotten fruits. Answer it in few lines only."
        response = model.generate_content(prompt)
        Text = response.text
    except:
        return "Not any advice is currently available....."
    if Text == "":
        return "No advice available at this moment of time......"
    Text = re.sub(r"\*\*"  , "", Text)
    Text = re.sub(r"\n+" , " " , Text)
    return Text.replace("\\" , "")
