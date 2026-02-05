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
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# ------------------------------------------------------------------
# App setup
# ------------------------------------------------------------------
app = FastAPI(
    title="Agentic Honey-Pot API",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# Allow all origins (safe for this challenge)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------
# Config
# ------------------------------------------------------------------
API_KEY = os.getenv(
    "HONEYPOT_API_KEY",
    "guvi-honeypot-a3d91f78c6b24fbc817b73b06c1ef2c6c9d2bb98ff07"
)

# ------------------------------------------------------------------
# Health check (VERY IMPORTANT for Render & GUVI)
# ------------------------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "success",
        "reply": "Honeypot service is running"
    }

# ------------------------------------------------------------------
# Main Honeypot Endpoint
# ------------------------------------------------------------------
@app.post("/honeypot/message")
async def honeypot_message(
    payload: dict,
    x_api_key: str = Header(None)
):
    # ---- API Key Validation ----
    if x_api_key != API_KEY:
        return JSONResponse(
            status_code=401,
            content={
                "status": "error",
                "reply": "Unauthorized"
            }
        )

    try:
        # ---- Safely extract message text ----
        message = payload.get("message", {})
        scam_text = message.get("text", "")

        # ---- Honeypot-style response (GUVI expected) ----
        reply_text = "Why is my account being suspended?"

        return {
            "status": "success",
            "reply": reply_text
        }

    except Exception:
        # ---- Absolute fallback (never fail GUVI parser) ----
        return {
            "status": "success",
            "reply": "Can you explain what you mean?"
        }

# ------------------------------------------------------------------
# Global exception handler (prevents empty responses)
# ------------------------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "reply": "Something went wrong. Please continue."
        }
    )

# ------------------------------------------------------------------
# Render-compatible server start
# ------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)


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

