# callback.py
import requests

def send_final_result_to_guvi(session_id, intelligence, total_messages):
    payload = {
        "sessionId": session_id,
        "scamDetected": True,
        "totalMessagesExchanged": total_messages,
        "extractedIntelligence": intelligence,
        "agentNotes": "Scammer used urgency and payment redirection tactics"
    }

    try:
        response = requests.post(
            "https://hackathon.guvi.in/api/updateHoneyPotFinalResult",
            json=payload,
            timeout=5
        )
        print("✅ GUVI CALLBACK SENT", response.status_code)
    except Exception as e:
        print("❌ GUVI CALLBACK FAILED", e)


# GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

# def send_final_callback(session_id, messages, intelligence):

#     payload = {
#         "sessionId": session_id,
#         "scamDetected": True,
#         "totalMessagesExchanged": len(messages),
#         "extractedIntelligence": intelligence,
#         "agentNotes": "Scammer used urgency tactics and requested sensitive payment details"
#     }

#     try:
#         requests.post(
#             GUVI_CALLBACK_URL,
#             json=payload,
#             timeout=5
#         )
#     except Exception as e:
#         print("Callback failed:", e)
