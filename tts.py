# tts.py

import time
import pyttsx3
from logger import setup_logger
from metrics import metrics


logger = setup_logger("TTS")

engine = pyttsx3.init()
engine.setProperty("rate", 170)


def text_to_speech(text: str):
    start = time.perf_counter()

    try:
        logger.info("Speaking response")
        engine.say(text)
        engine.runAndWait()
        metrics.increment("tts_success")

    except Exception as e:
        metrics.increment("tts_error")
        logger.error(f"TTS failed: {e}")

    finally:
        metrics.record_latency("tts", time.perf_counter() - start)
