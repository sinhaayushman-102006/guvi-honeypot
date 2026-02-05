# safety.py
FORBIDDEN_TERMS = [
    "scam", "fraud", "honeypot",
    "detected", "AI", "model"
]

def sanitize_response(text):
    for word in FORBIDDEN_TERMS:
        if word.lower() in text.lower():
            return "Sorry, I may have misunderstood. Can you explain again?"
    return text
