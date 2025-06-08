# Toby2.0-Voice-AI-Assistant

Python-based ChatGPT voice assistant for laptop and Raspberry Pi with future GPIO/robotic expansion for Toby 2.0.

## 🔧 Features
- 🎤 Mic input using Whisper API
- 🧠 GPT-3.5-Turbo for responses
- 🔊 TTS via gTTS + Pygame
- 🐾 GPIO placeholders for LEDs, servos (Toby 2.0)

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install openai gtts pygame SpeechRecognition
 on Pi: pip install RPi.GPIO
 API: export OPENAI_API_KEY="sk-..."
 RUN: python main.py

