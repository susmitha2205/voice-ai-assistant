# assistant.py

import time
from stt import speech_to_text
from llm import generate_llm_response
from tts import text_to_speech
from summarizer import summarize_text
from intent import detect_intent
from tools import get_current_date_day, get_current_time


def voice_assistant():
    text = speech_to_text()

    # ✅ Silence handling (VERY IMPORTANT)
    if not text:
        time.sleep(0.8)  # prevents tight retry loop
        return

    intent = detect_intent(text)

    if intent == "DATE":
        response = get_current_date_day()

    elif intent == "TIME":
        response = get_current_time()

    elif intent == "EXIT":
        text_to_speech("Goodbye. Have a great day!")
        exit()

    else:
        llm_response = generate_llm_response(text)
        response = summarize_text(llm_response)

    print(f"[FINAL] {response}")
    text_to_speech(response)
