NER_PROMPT = """
You are a medical assistant. Extract relevant medical information from the conversation.

CRITICAL INSTRUCTION: You MUST populate ALL fields. If a field is not explicitly mentioned, try to INFER it from context. If it cannot be inferred, use "Not mentioned".

RESPONSE FORMAT (Strict JSON):
{{
  "Patient_Name": "Patient's Name",
  "Symptoms": ["Symptom 1", "Symptom 2"],
  "Diagnosis": "Patient's Diagnosis",
  "Treatment": ["Suggested treatment"],
  "Current_Status": "Current Status of the patient",
  "Prognosis": "Expected time to recover"
}}

Conversation:
{text}
"""
