# agent_stage.py
def get_agent_stage(messages):
    # Only count scammer messages (IMPORTANT)
    scammer_msgs = [m for m in messages if m["role"] == "scammer"]
    count = len(scammer_msgs)

    if count == 1:
        return "confused"
    elif count == 2:
        return "cooperative"
    elif count == 4:
        return "stalling"
    else:
        return "completed"
