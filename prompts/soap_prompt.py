SOAP_PROMPT = """
You are a medical assistant. Generate a SOAP note based on the conversation.

CRITICAL INSTRUCTION: You MUST populate ALL sections. If information is missing, infer it or use "Not mentioned".

RESPONSE FORMAT (Strict JSON):
{{
  "Subjective": {{
    "Chief_Complaint": "Patient's complaints",
    "History_of_Present_Illness": "History"
  }},
  "Objective": {{
    "Physical_Exam": "Physical exam findings",
    "Observations": "Doctor's observations"
  }},
  "Assessment": {{
    "Diagnosis": "Diagnosis",
    "Severity": "Severity of condition"
  }},
  "Plan": {{
    "Treatment": "Treatment plan",
    "Follow_Up": "Follow-up instructions"
  }}
}}

Conversation:
{text}
"""
