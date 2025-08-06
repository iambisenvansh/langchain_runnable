import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini 1.5 Flash model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Step 1: Generate a joke about the topic
topic = "cricket"
joke_prompt = f"Write a joke about {topic}."
joke_response = model.generate_content(joke_prompt)
joke = joke_response.text.strip()

# Step 2: In parallel:
# - passthrough the joke (like RunnablePassthrough)
# - ask Gemini to explain the joke
explanation_prompt = f"Explain the following joke:\n\n{joke}"
explanation_response = model.generate_content(explanation_prompt)
explanation = explanation_response.text.strip()

# Final output
result = {
    "joke": joke,
    "explanation": explanation
}

# Print result
print("😂 Joke:\n", result["joke"])
print("\n🧠 Explanation:\n", result["explanation"])
