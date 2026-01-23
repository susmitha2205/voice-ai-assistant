# main.py

from assistant import voice_assistant

if __name__ == "__main__":
    print("Voice Assistant Started (Ctrl+C to stop)")
    while True:
        voice_assistant()
