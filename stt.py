# stt.py

import speech_recognition as sr
from faster_whisper import WhisperModel
import tempfile
import os
import time


# Load lightweight Whisper model (fast & stable locally)
try:
    whisper_model = WhisperModel("tiny", compute_type="int8")
except Exception as e:
    print(f"[STT ERROR] Failed to load Whisper model: {e}")
    whisper_model = None


def speech_to_text() -> str:
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening... Speak now")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=10,            # wait longer for speech to start
                phrase_time_limit=8    # max length of speech
            )

    # ✅ Silence is NORMAL — not an error
    except sr.WaitTimeoutError:
        print("[STT INFO] No speech detected (silence)")
        time.sleep(0.5)  # prevent tight retry loop
        return ""

    except OSError:
        print("[STT ERROR] Microphone not found or not accessible")
        time.sleep(1)
        return ""

    except Exception as e:
        print(f"[STT ERROR] Microphone failure: {e}")
        time.sleep(1)
        return ""

    audio_path = None

    try:
        # Save audio properly as WAV
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio.get_wav_data())
            audio_path = temp_audio.name

        if whisper_model is None:
            print("[STT ERROR] Whisper model not available")
            return ""

        segments, _ = whisper_model.transcribe(audio_path)
        text = " ".join(segment.text for segment in segments).strip()

        if not text:
            print("[STT INFO] Speech detected but no text recognized")
            return ""

        print(f"[STT] Transcribed: {text}")
        return text

    except Exception as e:
        print(f"[STT ERROR] Transcription failed: {e}")
        return ""

    finally:
        if audio_path and os.path.exists(audio_path):
            os.remove(audio_path)
