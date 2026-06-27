def analyze_transcript(text):
    text = text.lower()

    scam_keywords = [
        "transfer money",
        "otp",
        "account blocked",
        "verify bank",
        "urgent",
        "police case"
    ]

    if any(word in text for word in scam_keywords):
        return "scam"

    return "safe"