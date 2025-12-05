import os
import json
import spacy
import requests
from keybert import KeyBERT
from dotenv import load_dotenv
from prompts.ner_prompt import NER_PROMPT

load_dotenv()

nlp_spacy = spacy.load("en_core_web_sm")
kw_model = KeyBERT(model='sentence-transformers/all-MiniLM-L6-v2')

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"

def extract_keywords(text, top_n=10):
    doc = nlp_spacy(text)
    cleaned_text = " ".join([sent.text for sent in doc.sents])
    keywords = kw_model.extract_keywords(cleaned_text, keyphrase_ngram_range=(1, 3), stop_words='english', top_n=top_n)
    keyword_list = [kw[0] for kw in keywords]
    return keyword_list

def extract_entities(text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = NER_PROMPT.format(text=text)

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
        return empty_ner_structure()

def normalize_array(field):
    if isinstance(field, list):
        return field
    if isinstance(field, dict):
        try:
            items = sorted(field.items(), key=lambda x: int(x[0]))
            return [v for k, v in items]
        except:
            pass
    return []

def normalize_ner_structure(raw):
    return {
        "Patient_Name": raw.get("Patient_Name", ""),
        "Symptoms": normalize_array(raw.get("Symptoms", [])),
        "Diagnosis": raw.get("Diagnosis", ""),
        "Treatment": normalize_array(raw.get("Treatment", [])),
        "Current_Status": raw.get("Current_Status", ""),
        "Prognosis": raw.get("Prognosis", "")
    }

def empty_ner_structure():
    return {
        "Patient_Name": "",
        "Symptoms": [],
        "Diagnosis": "",
        "Treatment": [],
        "Current_Status": "",
        "Prognosis": ""
    }