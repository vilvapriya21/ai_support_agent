GENERATION_PROMPT_TEMPLATE = """
Conversation history (only if relevant):
{history}

User message:
{message}

Return ONLY raw JSON. Do NOT wrap in markdown. Do NOT add explanations.:

{{
  "type": "answer" | "clarification" | "out_of_scope",
  "message": "<short precise response>"
}}

Rules:
- Maximum 3 sentences.
- No greetings.
- No filler text.
- No extra keys.
- If information is missing, use type="clarification".
"""
