# app.pyhttp://127.0.0.1:8000/docs
from fastapi import FastAPI, Header, HTTPException
from config import API_KEY
from intelligence import extract_intelligence
from callback import send_final_result_to_guvi
from memory import mark_completed, is_completed
from memory import get_conversation, update_conversation
from agent_stage import get_agent_stage
from strategies import generate_response
from safety import sanitize_response
from self_correct import self_correct

app = FastAPI(title="Agentic HoneyPot API")
@app.post("/honeypot/message")
def honeypot(payload: dict, x_api_key: str = Header(...)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    session_id = payload.get("sessionId")
    message = payload.get("message", {}).get("text")

    # 🛑 If session already completed
    if is_completed(session_id):
        return {
            "status": "success",
            "reply": "Please start a new session for further assistance."
        }

    update_conversation(session_id, "scammer", message)
    conversation = get_conversation(session_id)

    stage = get_agent_stage(conversation)

    reply = generate_response(stage, message)
    reply = sanitize_response(reply)
    reply = self_correct(reply)

    update_conversation(session_id, "agent", reply)

    # 🚀 FINAL CALLBACK (only once)
    if stage == "stalling":
        intelligence = extract_intelligence(conversation)
        send_final_result_to_guvi(session_id, conversation, intelligence)
        mark_completed(session_id)

    return {
        "status": "success",
        "reply": reply
    }



# app = FastAPI(title="Agentic HoneyPot API")

# @app.post("/honeypot/message")
# def honeypot(payload: dict, x_api_key: str = Header(...)):

#     if x_api_key != API_KEY:
#         raise HTTPException(status_code=401, detail="Invalid API Key")

#     session_id = payload.get("sessionId")
#     message = payload.get("message", {}).get("text")

#     if not session_id or not message:
#         raise HTTPException(status_code=400, detail="Invalid payload")

#     # Store incoming scammer message
#     update_conversation(session_id, "scammer", message)

#     conversation = get_conversation(session_id)

#     # Internal agent reasoning (NOT returned)
#     stage = get_agent_stage(conversation)

#     raw_reply = generate_response(stage, message)
#     safe_reply = sanitize_response(raw_reply)
#     final_reply = self_correct(safe_reply)

#     update_conversation(session_id, "agent", final_reply)

#     # 🔒 STRICT GUVI OUTPUT FORMAT
#     return {
#         "status": "success",
#         "reply": final_reply
#     }


#How to run:
#uvicorn app:app --host 0.0.0.0 --port 8000
# uvicorn app:app --reload
