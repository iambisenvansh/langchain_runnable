import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Input topic
topic = "AI"

# Prompts
tweet_prompt = f"Generate a tweet about {topic}."
linkedin_prompt = f"Generate a LinkedIn post about {topic}."

# Parallel generation using two separate prompts
tweet_response = model.generate_content(tweet_prompt)
linkedin_response = model.generate_content(linkedin_prompt)

# Extract and strip outputs
tweet = tweet_response.text.strip()
linkedin_post = linkedin_response.text.strip()

# Print results
print("🐦 Tweet:\n", tweet)
print("\n💼 LinkedIn Post:\n", linkedin_post)
