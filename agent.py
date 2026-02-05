def get_agent_stage(messages):
    count = len(messages)
    if count <= 2:
        return "confused"
    elif count <= 5:
        return "cooperative"
    else:
        return "stalling"


def rule_based_reply(history):
    stage = get_agent_stage(history)
    last = history[-1]["text"].lower()

    if stage == "confused":
        return "Sorry, I didn’t understand. Which bank is this about?"

    if stage == "cooperative":
        if "upi" in last:
            return "I have two UPI apps. Which one should I use?"
        return "Okay, please guide me step by step."

    if stage == "stalling":
        return "The app seems to be crashing. Can you resend the details?"

    return "Can you explain again?"


def agent_reply(history):
    return rule_based_reply(history)
