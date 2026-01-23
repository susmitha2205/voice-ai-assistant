# Voice AI Assistant

A simple voice-enabled AI assistant built using Python.  
You can speak to it, and it will listen, understand, and speak back.

This project was created as part of an AI Intern technical assessment, with a focus on clean architecture and real-world engineering practices.

## Features
- Speech-to-Text using Whisper
- Low-latency LLM responses using Groq + LLaMA-3
- Text-to-Speech output
- Intent detection for date and time
- Summarized responses for better voice output
- Graceful handling of silence and errors
- Logging and basic latency metrics

## How It Works
Voice Input → Speech to Text → Intent Detection → LLM or Local Tools → Summarized Response → Text to Speech

## Setup

### Install dependencies
pip install -r requirements.txt

**Windows users:**  
If `pyaudio` fails:
pip install pipwin
pipwin install pyaudio

### Add environment variables
Create a `.env` file:
GROQ_API_KEY=your_api_key_here

### Run the assistant
python main.py


