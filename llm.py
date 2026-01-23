# llm.py

import os
import time
from groq import Groq
from dotenv import load_dotenv
from logger import setup_logger
from metrics import metrics


load_dotenv()
logger = setup_logger("LLM")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_llm_response(text: str) -> str:
    start = time.perf_counter()

    if not text.strip():
        return "I didn't catch that. Please repeat."

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a voice assistant. Keep responses short."},
                {"role": "user", "content": text}
            ],
            max_tokens=120,
            temperature=0.3
        )

        reply = response.choices[0].message.content.strip()
        metrics.increment("llm_success")
        logger.info("LLM response generated")

        return reply

    except Exception as e:
        metrics.increment("llm_error")
        logger.error(f"LLM failure: {e}")
        return "I'm having trouble responding right now."

    finally:
        metrics.record_latency("llm", time.perf_counter() - start)
