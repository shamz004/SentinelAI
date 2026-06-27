def detect_sms_scam(text):
    text = text.lower()

    keywords = [
        "otp", "kyc", "account blocked",
        "urgent transfer", "verify bank"
    ]

    return any(word in text for word in keywords)