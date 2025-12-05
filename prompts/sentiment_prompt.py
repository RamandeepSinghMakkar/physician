SENTIMENT_PROMPT = """
You are a medical assistant. Analyze the doctor-patient conversation and classify the patient's sentiment and intent.

RESPONSE FORMAT (Strict JSON):
{{
  "Sentiment": "Anxious, Neutral, or Reassured",
  "Intent": "Patient's Intent (e.g., Seeking reassurance, Reporting symptoms)"
}}

Conversation:
{text}
"""
