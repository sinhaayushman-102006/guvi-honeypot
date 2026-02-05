# intelligence.py
import re

def extract_intelligence(messages):
    text_blob = " ".join([m["text"] for m in messages])

    return {
        "bankAccounts": re.findall(r"\b\d{4}-\d{4}-\d{4}\b", text_blob),
        "upiIds": re.findall(r"\b[\w.-]+@[\w.-]+\b", text_blob),
        "phishingLinks": re.findall(r"https?://\S+", text_blob),
        "phoneNumbers": re.findall(r"\+91\d{10}", text_blob),
        "suspiciousKeywords": [
            word for word in ["urgent", "verify", "blocked", "suspend"]
            if word in text_blob.lower()
        ]
    }
