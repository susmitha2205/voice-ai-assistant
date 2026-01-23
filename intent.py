# intent.py

def detect_intent(text: str):
    text = text.lower()

    if "date" in text or "day" in text:
        return "DATE"

    if "time" in text:
        return "TIME"

    if "weather" in text:
        return "WEATHER"

    if "bye" in text or "exit" in text:
        return "EXIT"

    return "LLM"
