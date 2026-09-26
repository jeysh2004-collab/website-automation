import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import google.generativeai as genai

# 1. Setup Gemini API
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

# 2. Save content to local file for Claude Desktop sync
with open("daily_update.txt", "w", encoding="utf-8") as f:
    f.write(generated_text)

# 3. Send Approval Email via Outlook/SMTP
sender_email = os.environ["EMAIL_USER"]
sender_password = os.environ["EMAIL_PASS"]
receiver_email = os.environ["RECEIVER_EMAIL"]

subject = "Daily Website Content Approval Required"
body = f"""
Hi Jeyshu,

Here is today's generated website content update:

--------------------------------------------------
{generated_text}
--------------------------------------------------

If this looks good, it has been saved to 'daily_update.txt' in your repository.
You can ask Claude Desktop to pull and update your HTML file directly!

Reply to this email if you need any manual tweaks or prompt adjustments.
"""

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # SMTP server for Outlook/Office365 (Use smtp.gmail.com if using Gmail)
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    print("Approval email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
