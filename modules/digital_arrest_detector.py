def detect_digital_arrest(text):
    text = text.lower()

    keywords = [
        "cbi", "digital arrest", "police case",
        "income tax", "customs", "arrest warrant",
        "jail", "case filed", "verify identity"
    ]

    return any(word in text for word in keywords)
