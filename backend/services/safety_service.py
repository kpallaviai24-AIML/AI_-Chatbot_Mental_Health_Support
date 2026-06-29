
danger_keywords = [
    "suicide",
    "kill",
    "overdose",
    "self harm",
    "poison"
]

def is_dangerous(text):

    text = text.lower()

    for word in danger_keywords:
        if word in text:
            return True

    return False
