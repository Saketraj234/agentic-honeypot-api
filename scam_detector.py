# scam_detector.py

def is_scam(text: str) -> bool:
    keywords = [
        "blocked",
        "account",
        "send money",
        "upi",
        "click",
        "link",
        "urgent",
        "verify"
    ]

    text = text.lower()
    return any(word in text for word in keywords)
