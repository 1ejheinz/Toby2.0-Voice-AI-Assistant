# Toby2.0-Voice-AI-Assistant

Python-based ChatGPT voice assistant for laptop and Raspberry Pi with future GPIO/robotic expansion for Toby 2.0.

## 🔧 Features
- 🎤 Mic input using Whisper API
- 🧠 GPT-3.5-Turbo for responses
- 🔊 TTS via gTTS + Pygame
- 🐾 GPIO placeholders for LEDs, servos (Toby 2.0)
- 📢 Wake-word detection: say "Toby" to activate

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install openai gtts pygame SpeechRecognition
```
If on Raspberry Pi:
```bash
pip install RPi.GPIO
```

### 2. Set your OpenAI API key
Create an account and key at:
[https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

Add this to your terminal or .env file:
```bash
export OPENAI_API_KEY="sk-..."
```

### 3. Limit API Usage (Highly Recommended)
Go to:
[https://platform.openai.com/account/billing/limits](https://platform.openai.com/account/billing/limits)
- Set a **monthly hard limit** (e.g. $1–2 max)
- This protects you from accidental overuse while testing

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
- 👂 "Toby, listen only when I press your button" → GPIO input with state
- 📸 Add camera vision with OpenCV or picamera2
- 🔌 Optional: integrate wake-word with Vosk

## 🔐 License
MIT License — see LICENSE file.
"""
