from google import genai
from gemini_api_key import Gemini_api_key
import re
client = genai.Client(api_key = Gemini_api_key)
def Gemini_ke_updesh():
    try:
        response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= "You are an fruit quality expert. Tell me tips for preventing fresh fruits from rotten. And effect of eating rotten fruits. Answer it in few lines only."
        )
        Text = response.text
    except:
        return "Not any advice is currently available....."
    if Text == "":
        return "No advice available at this moment of time......"
    Text = re.sub(r"\*\*"  , "", Text)
    Text = re.sub(r"\n+" , " " , Text)
    return Text.replace("\\" , "")