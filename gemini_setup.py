import google.generativeai as genai
import os
import re
genai.configure(api_key = os.getenv("Gemini_api_key"))
def Gemini_ke_updesh():
    fallback_text = "Store fruits in a cool, dry place. \nAvoid consuming fruits with visible mold \nWash fruits thoroughly before eating"
    try:
        model=genai.generativemodel("gemini-3-flash-preview"),
        prompt= "You are an fruit quality expert. Tell me tips for preventing fresh fruits from rotten. And effect of eating rotten fruits. Answer it in few lines only."
        response = model.generate_content(prompt)
        Text = response.text
    except:
        return fallback_text
    if Text == "":
        return fallback_text
    Text = re.sub(r"\*\*"  , "", Text)
    Text = re.sub(r"\n+" , " " , Text)
    return Text.replace("\\" , "")


