from llm_client import call_llm

def llm_confirm_scam(text):
    prompt = f"""
Classify the following message as SCAM or NOT SCAM.
Reply only with one word.

Message:
{text}
"""
    result = call_llm(prompt)
    return result and "SCAM" in result.upper()
