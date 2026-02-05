# self_correct.py
def self_correct(response):

    if len(response) < 15:
        return response + " Can you explain a bit more?"

    if not response.endswith("?") and "busy" not in response:
        return response + " Does that make sense?"

    return response

