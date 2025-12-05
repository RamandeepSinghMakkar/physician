import os
import requests
import json
from prompts.soap_prompt import SOAP_PROMPT

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"

def generate_soap_note(text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = SOAP_PROMPT.format(text=text)

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
        return empty_soap_structure()

def empty_soap_structure():
    return {
        "Subjective": {"Chief_Complaint": "", "History_of_Present_Illness": ""},
        "Objective": {"Physical_Exam": "", "Observations": ""},
        "Assessment": {"Diagnosis": "", "Severity": ""},
        "Plan": {"Treatment": "", "Follow-Up": ""}
    }