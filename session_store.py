from collections import defaultdict

sessions = defaultdict(lambda: {
    "messages": [],
    "scamDetected": False,
    "intelligence": {
        "bankAccounts": [],
        "upiIds": [],
        "phishingLinks": [],
        "phoneNumbers": [],
        "suspiciousKeywords": []
    }
})
