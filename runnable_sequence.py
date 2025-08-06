import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the API key from your .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model (you can change to gemini-1.5-pro if needed)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Step 1: Generate a joke about a topic
topic = "AI"

joke_prompt = f"Write a joke about {topic}."
joke_response = model.generate_content(joke_prompt)
joke = joke_response.text.strip()

# Step 2: Ask Gemini to explain the joke
explain_prompt = f"Explain the following joke:\n\n{joke}"
explanation_response = model.generate_content(explain_prompt)
explanation = explanation_response.text.strip()

# Final output
print("😂 Joke:")
print(joke)
print("\n🧠 Explanation:")
print(explanation)
