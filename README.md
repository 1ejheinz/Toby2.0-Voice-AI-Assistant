# Toby2.0-Voice-AI-Assistant

Python-based ChatGPT voice assistant for laptop and Raspberry Pi with future GPIO/robotic expansion for Toby 2.0.

## 🔧 Features
- 🎤 Mic input using Whisper API
- 🧠 GPT-3.5-Turbo for responses
- 🔊 TTS via gTTS + Pygame
- 🐾 GPIO placeholders for LEDs, servos, and a push-button
- 📢 Wake-word detection: say "Toby" to activate
- 🧪 Optional test mode (no API key required)

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install openai gtts pygame SpeechRecognition python-dotenv
```
If on Raspberry Pi:
```bash
pip install RPi.GPIO
```

### 2. Create a `.env` file in the root of your project
```
OPENAI_API_KEY=sk-...
```
If left blank or set to `test-mode`, the app enters non-billed test mode.

### 3. Limit API Usage (Highly Recommended)
Go to:
[https://platform.openai.com/account/billing/limits](https://platform.openai.com/account/billing/limits)
- Set a **monthly hard limit** (e.g. $1–2 max) to prevent accidental charges

### 4. Run
```bash
python main.py
```

## 💬 Common Voice Commands
- "Toby, what's the weather today?"
- "Toby, tell me a joke."
- "Toby, summarize the news."
- "Toby, define artificial intelligence."
- "Toby, what's 25 times 14?"

## 🐶 Toby 2.0 Robotic Actions (Future)
- 🐾 "Toby, wag your tail" → trigger servo GPIO (GPIO 18)
- 💡 "Toby, show excitement" → blink LED or NeoPixel (GPIO 17)
- 🔘 Activate voice by pressing GPIO button (GPIO 27)
- 📸 Add camera vision with OpenCV or picamera2
- 🔌 Optional: integrate wake-word engine with Vosk for offline use

## 🔐 License
MIT License — see LICENSE file.
"""
