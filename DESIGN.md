# System Design – Voice AI Assistant

## Overview
This project implements a voice-enabled AI assistant that converts user speech into text, generates a response using an LLM, and converts the response back into speech.

The goal is to demonstrate clean architecture, modular design, and awareness of real-world voice AI constraints such as latency and response length.

---

## Architecture Components

1. **Speech-to-Text (STT)**
   - Converts microphone input into text
   - Implemented using Whisper for better accuracy
   - Silence is handled as a valid state, not an error

2. **Intent Detection**
   - Simple rule-based intent detection
   - Routes date and time queries to local tools
   - Prevents LLM hallucination for factual data

3. **LLM Response Generator**
   - Uses Groq-hosted LLaMA-3 for low-latency inference
   - Token limits applied to control latency and cost

4. **Response Summarization**
   - Long responses are summarized before speech output
   - Improves user experience for voice-based interaction

5. **Text-to-Speech (TTS)**
   - Converts final text response into audio output
   - Keeps responses short and natural

---

## Data Flow

User Voice
    ↓
Speech-to-Text
    ↓
Intent Detection
    ↓
LLM or Local Tool
    ↓
Summarization
    ↓
Text-to-Speech


---

## Latency Considerations

- Whisper model size is kept small for faster local execution
- LLM responses are limited in length
- Silence detection avoids unnecessary processing loops

---

## Failure Handling

- Microphone silence is treated as normal behavior
- STT and LLM failures return safe fallback responses
- Errors are logged without crashing the system

---

## Design Trade-offs

- Used local TTS for simplicity instead of cloud TTS
- Used rule-based intent detection instead of NLU models
- Focused on clarity and modularity over advanced optimizations

---

## Conclusion

This design prioritizes clarity, robustness, and real-world voice AI behavior while keeping the implementation simple and extensible.
