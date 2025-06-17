import google.generativeai as genai

# Set up the Gemini API
genai.configure(api_key="AIzaSyDhJE5nxCZlkqNzjQzUz4ibpkRb6SbfE0g")

# Load the model (Gemini 1.5 Flash is free and fast)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get Gemini response
def get_gemini_reply(prompt):
    response = model.generate_content(prompt)
    return response.text
