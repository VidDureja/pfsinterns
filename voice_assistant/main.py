import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        speak("Could not request results; check your network connection.")
    return None

def main():
    print("Hello! I am your personal voice assistant.")
    speak("Hello! I am your personal voice assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            # Placeholder for command processing
            if "exit" in command.lower():
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main() 