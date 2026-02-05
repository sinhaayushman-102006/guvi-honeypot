from llm_client import call_llm

def llm_agent_reply(history, stage):
    convo = "\n".join([f"{m['sender']}: {m['text']}" for m in history])

    prompt = f"""
You are an AI honeypot posing as a scam victim.
Stage: {stage}
Rules:
- Act human
- Ask only ONE question
- Never accuse

Conversation:
{convo}

Respond as the user.
"""
    return call_llm(prompt)
