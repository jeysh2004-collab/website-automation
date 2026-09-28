import os
import urllib.parse
import xml.etree.ElementTree as ET
import requests
import google.generativeai as genai

# 1. Configure Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 2. Fetch Latest Real-World News via Google News RSS
topic = "E-commerce AI support sales automation"
encoded_topic = urllib.parse.quote(topic)
rss_url = f"https://news.google.com/rss/search?q={encoded_topic}&hl=en-US&gl=US&ceid=US:en"

response = requests.get(rss_url)
root = ET.fromstring(response.content)

news_items = []
for item in root.findall('.//item')[:5]:  # Top 5 news headlines
    title = item.find('title').text
    news_items.append(f"- {title}")

news_context = "\n".join(news_items)

# 3. Prompt Gemini with Real-World Context
prompt = f"""
You are a senior tech blogger for MindX AI.
Based on these real-world news headlines from this past week:
{news_context}

Write a high-converting, SEO-optimized weekly blog update (2-3 short paragraphs).
Explain how these real-world trends impact e-commerce store owners and how AI support automation helps them adapt.
Keep it crisp, professional, and actionable.
"""

response = model.generate_content(prompt)
generated_text = response.text

print("Generated Blog Post:\n", generated_text)

# 4. Save locally to daily_update.txt
with open("daily_update.txt", "w", encoding="utf-8") as f:
    f.write(generated_text)

print("Saved update to daily_update.txt successfully!")
