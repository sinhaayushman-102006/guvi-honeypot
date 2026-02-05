INTENT_SIGNALS = {
    "urgency": ["urgent", "immediately", "today", "now"],
    "threat": ["blocked", "suspended", "frozen"],
    "financial": ["upi", "bank", "account", "kyc", "verify"]
}

def detect_scam(text: str):
    text = text.lower()
    score = 0
    found = []

    for category, words in INTENT_SIGNALS.items():
        for w in words:
            if w in text:
                score += 1
                found.append(w)

    return score >= 3, list(set(found))
