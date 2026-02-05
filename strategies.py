# strategies.py
def generate_response(stage, last_message):

    if stage == "confused":
        return "Sorry, I'm not sure I understand this. Why is my account getting affected?"

    elif stage == "cooperative":
        return "Okay, I want to fix this. What should I do next?"

    elif stage == "stalling":
        return "I’m currently busy. Can we complete this later today?"

    return "Alright."
