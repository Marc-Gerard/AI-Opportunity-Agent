import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_website(website_text, url):
    prompt = f"""
You are an expert business analyst. Analyze this website content and generate a structured report.

URL: {url}
Content: {website_text}

Generate a report with these sections:
1. What the site sells and who it targets
2. Potential friction points
3. Missed opportunities
4. 3 concrete recommendations

Be precise and actionable.
"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    
    return response.choices[0].message.content