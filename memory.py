# memory.py
conversation_store = {}
completed_sessions = set()

def get_conversation(session_id):
    return conversation_store.get(session_id, [])

def update_conversation(session_id, role, text):
    if session_id not in conversation_store:
        conversation_store[session_id] = []
    conversation_store[session_id].append({
        "role": role,
        "text": text
    })

def mark_completed(session_id):
    completed_sessions.add(session_id)

def is_completed(session_id):
    return session_id in completed_sessions
