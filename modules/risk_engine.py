def analyze_risk(text):
    text = text.lower()

    # DIGITAL ARREST SCAM
    if "cbi" in text or "digital arrest" in text or "police case" in text:
        return {
            "risk": "HIGH",
            "category": "Digital Arrest Scam",
            "action": "Do NOT share OTP or personal details"
        }

    # OTP / BANKING FRAUD
    if "otp" in text or "bank" in text or "account blocked" in text:
        return {
            "risk": "HIGH",
            "category": "Banking / OTP Fraud",
            "action": "Do not share OTP or login credentials"
        }

    # KYC SCAM
    if "kyc" in text or "update account" in text:
        return {
            "risk": "MEDIUM",
            "category": "KYC Verification Scam",
            "action": "Verify only from official website"
        }

    # GENERAL SCAM
    if "urgent" in text or "reward" in text or "lottery" in text:
        return {
            "risk": "MEDIUM",
            "category": "General Scam",
            "action": "Be cautious before responding"
        }

    # SAFE MESSAGE
    return {
        "risk": "LOW",
        "category": "Safe Message",
        "action": "No action required"
    }