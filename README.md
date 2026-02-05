Perfect — here is a **GUVI-submission-aligned README**, written **exactly in the language GUVI evaluators expect**.
You can **paste this directly** into `README.md` with zero changes.


# 🕵️ Agentic Honey-Pot for Scam Detection & Intelligence Extraction

**Hackathon:** GUVI Agentic AI Hackathon
**Team Name:** guvi-honeypot-team-alpha-2026



## 🧠 Problem Statement

Online scams such as bank fraud, UPI fraud, phishing, and fake offers are increasingly adaptive. Scammers modify their behavior based on user responses, making traditional rule-based detection systems ineffective.

This project implements an **Agentic Honey-Pot system** that detects scam intent and autonomously engages scammers using an AI Agent to extract actionable intelligence—without revealing detection.



## 🎯 Objective

Design and deploy a **public REST API** that:

* Detects scam or fraudulent intent in incoming messages
* Activates an autonomous AI Agent upon detection
* Maintains a believable human-like persona
* Handles multi-turn conversations
* Dynamically adapts responses
* Extracts scam-related intelligence
* Returns structured responses
* Sends a **mandatory final callback** to GUVI evaluation endpoint



## 🏗️ System Overview

**Evaluation Flow (As per GUVI spec):**

1. Platform sends a suspected scam message
2. System analyzes the message
3. Scam intent is detected
4. AI Agent is activated
5. Agent engages scammer autonomously
6. Intelligence is extracted
7. Final results are sent to GUVI callback endpoint



## 📡 Honeypot API Endpoint

### Endpoint

POST /honeypot/message


### Authentication

x-api-key: YOUR_SECRET_API_KEY
Content-Type: application/json


### Request Format (Input)

Each request represents **one incoming message** in a conversation.

json
{
  "sessionId": "wertyu-dfghj-ertyui",
  "message": {
    "sender": "scammer",
    "text": "Your bank account will be blocked today. Verify immediately.",
    "timestamp": "2026-01-21T10:15:30Z"
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}




## 📤 API Response Format (As Required by GUVI)

json
{
  "status": "success",
  "reply": "Why is my account being suspended?"
}


✔ Response strictly follows GUVI output contract
✔ No detection disclosure
✔ Human-like reply



## 🤖 AI Agent Behavior

The AI Agent is designed to:

* Handle **multi-turn conversations**
* Adapt responses dynamically
* Avoid revealing scam detection
* Behave like a real human
* Perform self-correction when needed

### Agent Stages

python
def get_agent_stage(messages):
    count = len(messages)
    if count <= 2:
        return "confused"
    elif count <= 5:
        return "cooperative"
    else:
        return "stalling"


The agent adjusts tone and engagement strategy based on conversation depth.


## 🔍 Intelligence Extraction

The agent extracts the following intelligence during engagement:

* Bank account numbers
* UPI IDs
* Phishing URLs
* Phone numbers
* Suspicious keywords



## 🔔 Mandatory Final Result Callback (GUVI Evaluation)

Once scam intent is confirmed and engagement is completed, the system **automatically sends** the final extracted intelligence to:

POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult


### Callback Payload
json
{
  "sessionId": "abc123-session-id",
  "scamDetected": true,
  "totalMessagesExchanged": 18,
  "extractedIntelligence": {
    "bankAccounts": ["XXXX-XXXX-XXXX"],
    "upiIds": ["scammer@upi"],
    "phishingLinks": ["http://malicious-link.example"],
    "phoneNumbers": ["+91XXXXXXXXXX"],
    "suspiciousKeywords": ["urgent", "verify now", "account blocked"]
  },
  "agentNotes": "Scammer used urgency tactics and payment redirection"
}


⚠️ **This callback is mandatory for evaluation and scoring.**



## 🛠️ Technology Stack

* Python
* FastAPI
* Uvicorn
* Regex-based intelligence extraction
* Optional LLM (OpenAI / Gemini)

---

## ⚙️ Local Setup

bash
pip install -r requirements.txt
uvicorn app:app --reload

Swagger UI:

http://127.0.0.1:8000/docs




## 🌐 Deployment

The application is deployed as a **public REST API** (Render).
The deployed URL is submitted as the **Honeypot API Endpoint URL** to GUVI.



## ⚖️ Ethics & Constraints

* ❌ No impersonation of real individuals
* ❌ No illegal instructions
* ❌ No harassment
* ✅ Responsible data handling
* ✅ Safe AI behavior



## 🏁 One-Line Summary

An AI-powered **agentic honeypot API** that detects scam messages, autonomously engages scammers, extracts actionable intelligence, and sends mandatory evaluation callbacks to GUVI.



