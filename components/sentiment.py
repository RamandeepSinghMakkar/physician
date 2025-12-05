
import os
import json
import requests
from dotenv import load_dotenv
from prompts.sentiment_prompt import SENTIMENT_PROMPT

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"

def analyze_sentiment_intent(text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = SENTIMENT_PROMPT.format(text=text)

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.0
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        
        result_text = response.json()["choices"][0]["message"]["content"]
        return json.loads(result_text)
    except Exception as e:
        print(f"Groq API Error: {e}")
        if 'response' in locals():
            print(f"Response: {response.text}")
        return empty_sentiment_structure()

def empty_sentiment_structure():
    return {
        "Sentiment": "",
        "Intent": ""
    }