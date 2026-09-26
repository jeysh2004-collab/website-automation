import os
import google.generativeai as genai

# 1. Setup Gemini API Key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = """
You are a daily content updater for my website.
Write a concise, engaging, 1-paragraph update for today's website post.
Connect the core topic to practical execution and real-world value.
Keep it authentic and professional.
"""

response = model.generate_content(prompt)
generated_text = response.text

print("Generated Content:\n", generated_text)

# 2. Save content to daily_update.txt in the repository
with open("daily_update.txt", "w", encoding="utf-8") as f:
    f.write(generated_text)

print("Saved update to daily_update.txt successfully!")
