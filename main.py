import os
import requests
import google.generativeai as genai

# 1. Setup Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

prompt = """
You are a daily content updater for my website.
Write a concise, engaging, 1-paragraph update for today's website post.
Connect the core topic to real-life application, focusing on practical execution and real-world value.
Keep it authentic and professional.
"""

response = model.generate_content(prompt)
generated_text = response.text

print("Generated Content:\n", generated_text)

# 2. Trigger Outlook Email or Direct Webhook Approval
# (Note: Webhook URL will be called after approval)
webhook_url = os.environ["WEBSITE_WEBHOOK_URL"]

# For testing direct push or sending for approval:
payload = {"content": generated_text}
res = requests.post(webhook_url, json=payload)

if res.status_code == 200:
    print("Successfully pushed update to website!")
else:
    print("Failed to push:", res.status_code, res.text)
