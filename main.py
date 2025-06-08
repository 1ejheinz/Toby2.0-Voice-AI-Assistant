# Toby 2.0 - ChatGPT Voice Assistant (Starter for Laptop & Raspberry Pi)
# Author: EJ Heinz

import os
import openai
import time
import speech_recognition as sr
import pygame
from dotenv import load_dotenv

try:
    import RPi.GPIO as GPIO  # For future Toby 2.0 servo/LED integration
except ImportError:
    GPIO = None

# ============================
# LOAD ENV VARIABLES
# ============================
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
SKIP_API_CALL = not openai.api_key or openai.api_key == "test-mode"

VOICE_LANGUAGE = 'en'
OUTPUT_FILENAME = "response.mp3"
USE_RPI = False  # Set to True on Raspberry Pi with GPIO/servo code enabled
WAKE_WORD = "toby"
BUTTON_PIN = 27  # Optional push-button input

# GPIO setup placeholder (Toby 2.0)
if USE_RPI and GPIO:
    GPIO.setmode(GPIO.BCM)
    SERVO_PIN = 18
    LED_PIN = 17
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    servo = GPIO.PWM(SERVO_PIN, 50)
    servo.start(0)
    GPIO.output(LED_PIN, GPIO.LOW)

# ============================
# FUNCTION: Speak with gTTS and play via pygame
# ============================
def speak_text(text):
    from gtts import gTTS
    tts = gTTS(text=text, lang=VOICE_LANGUAGE)
    tts.save(OUTPUT_FILENAME)
    pygame.mixer.init()
    pygame.mixer.music.load(OUTPUT_FILENAME)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

# ============================
# FUNCTION: Record from mic and transcribe with Whisper
# ============================
def get_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if USE_RPI and GPIO:
            print("Waiting for button press...")
            while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                time.sleep(0.1)
        print("Listening for wake word...")
        audio = r.listen(source)
        try:
            print("Transcribing...")
            text = r.recognize_whisper_api(audio, api_key=openai.api_key or "")
            print(f"You said: {text}")
            if WAKE_WORD.lower() in text.lower():
                print("Wake word detected. Listening for command...")
                speak_text("Yes?")
                audio = r.listen(source)
                command = r.recognize_whisper_api(audio, api_key=openai.api_key or "")
                print(f"Command: {command}")
                return command
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

# ============================
# FUNCTION: Send to OpenAI and return response
# ============================
def get_chatgpt_response(prompt):
    if SKIP_API_CALL:
        print("Test mode: skipping API call.")
        return "This is a test response."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

# ============================
# MAIN LOOP
# ============================
if __name__ == "__main__":
    try:
        while True:
            query = get_user_input()
            if not query:
                continue
            reply = get_chatgpt_response(query)
            print(f"Assistant: {reply}")
            speak_text(reply)

            # Future Toby 2.0 GPIO hooks
            if USE_RPI and GPIO:
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LED_PIN, GPIO.LOW)
                servo.ChangeDutyCycle(7.5)
                time.sleep(0.5)
                servo.ChangeDutyCycle(5)
                time.sleep(0.3)
                servo.ChangeDutyCycle(10)
                time.sleep(0.3)
                servo.ChangeDutyCycle(0)

    except KeyboardInterrupt:
        print("Exiting...")
        if USE_RPI and GPIO:
            servo.stop()
            GPIO.cleanup()

