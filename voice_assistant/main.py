import speech_recognition as sr
import pyttsx3
import requests
import json
import webbrowser
import datetime
import os
import time
from threading import Thread

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.reminders = []
        self.is_listening = True
        
        # Configure speech engine
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Index 0 for male voice
        self.engine.setProperty('rate', 150)  # Speed of speech
        
        # Weather API key (you'll need to get a free API key from openweathermap.org)
        self.weather_api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice input and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.WaitTimeoutError:
                print("No speech detected within timeout")
                return None
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return None
    
    def get_weather(self, city):
        """Get weather information for a city"""
        if self.weather_api_key == "YOUR_API_KEY_HERE":
            return "Please set up your weather API key first. Get a free key from openweathermap.org"
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description']
                return f"The weather in {city} is {description}. Temperature is {temp}°C with {humidity}% humidity."
            else:
                return f"Sorry, I couldn't get weather information for {city}."
        except Exception as e:
            return f"Error getting weather: {str(e)}"
    
    def search_web(self, query):
        """Search the web using Google"""
        try:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            return f"Searching the web for {query}"
        except Exception as e:
            return f"Error searching the web: {str(e)}"
    
    def set_reminder(self, text, time_str):
        """Set a reminder"""
        try:
            # Parse time (simple format: "5 PM", "3:30 PM", etc.)
            current_time = datetime.datetime.now()
            
            # Simple time parsing (you can enhance this)
            if "pm" in time_str.lower():
                hour = int(time_str.split()[0])
                if hour != 12:
                    hour += 12
            elif "am" in time_str.lower():
                hour = int(time_str.split()[0])
                if hour == 12:
                    hour = 0
            else:
                hour = int(time_str.split()[0])
            
            # Set reminder for today at specified time
            reminder_time = current_time.replace(hour=hour, minute=0, second=0, microsecond=0)
            
            # If the time has already passed today, set it for tomorrow
            if reminder_time <= current_time:
                reminder_time += datetime.timedelta(days=1)
            
            reminder = {
                'text': text,
                'time': reminder_time
            }
            self.reminders.append(reminder)
            
            return f"Reminder set for {reminder_time.strftime('%I:%M %p')} tomorrow: {text}"
        except Exception as e:
            return f"Error setting reminder: {str(e)}"
    
    def check_reminders(self):
        """Check if any reminders are due"""
        current_time = datetime.datetime.now()
        due_reminders = []
        
        for reminder in self.reminders[:]:
            if current_time >= reminder['time']:
                due_reminders.append(reminder)
                self.reminders.remove(reminder)
        
        for reminder in due_reminders:
            self.speak(f"Reminder: {reminder['text']}")
    
    def get_time(self):
        """Get current time"""
        current_time = datetime.datetime.now()
        return f"The current time is {current_time.strftime('%I:%M %p')}"
    
    def get_date(self):
        """Get current date"""
        current_date = datetime.datetime.now()
        return f"Today is {current_date.strftime('%A, %B %d, %Y')}"
    
    def open_application(self, app_name):
        """Open system applications"""
        try:
            if "notepad" in app_name.lower():
                os.system("notepad")
                return "Opening Notepad"
            elif "calculator" in app_name.lower():
                os.system("calc")
                return "Opening Calculator"
            elif "browser" in app_name.lower() or "chrome" in app_name.lower():
                webbrowser.open("https://www.google.com")
                return "Opening web browser"
            else:
                return f"Sorry, I don't know how to open {app_name}"
        except Exception as e:
            return f"Error opening application: {str(e)}"
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return
        
        # Exit commands
        if any(word in command for word in ['exit', 'quit', 'stop', 'goodbye']):
            self.speak("Goodbye! Have a great day!")
            self.is_listening = False
            return
        
        # Weather commands
        elif 'weather' in command:
            # Extract city name (simple extraction)
            words = command.split()
            try:
                city_index = words.index('in') + 1
                city = words[city_index]
                response = self.get_weather(city)
                self.speak(response)
            except:
                self.speak("Please specify a city. For example: 'What's the weather in London?'")
        
        # Web search commands
        elif any(word in command for word in ['search', 'google', 'find']):
            # Extract search query
            if 'search for' in command:
                query = command.split('search for', 1)[1].strip()
            elif 'google' in command:
                query = command.split('google', 1)[1].strip()
            else:
                query = command.split('search', 1)[1].strip()
            
            response = self.search_web(query)
            self.speak(response)
        
        # Reminder commands
        elif 'reminder' in command or 'remind' in command:
            # Simple reminder parsing
            if 'set a reminder' in command:
                # Extract reminder text and time
                parts = command.split('set a reminder for')
                if len(parts) > 1:
                    reminder_part = parts[1].strip()
                    # Simple parsing - you can enhance this
                    words = reminder_part.split()
                    if len(words) >= 3:
                        time_str = f"{words[-2]} {words[-1]}"
                        reminder_text = ' '.join(words[:-2])
                        response = self.set_reminder(reminder_text, time_str)
                        self.speak(response)
                    else:
                        self.speak("Please specify what to remind and when. For example: 'Set a reminder for buy groceries at 5 PM'")
                else:
                    self.speak("Please specify what to remind and when.")
        
        # Time commands
        elif 'time' in command:
            response = self.get_time()
            self.speak(response)
        
        # Date commands
        elif 'date' in command:
            response = self.get_date()
            self.speak(response)
        
        # Application commands
        elif any(word in command for word in ['open', 'launch', 'start']):
            for app in ['notepad', 'calculator', 'browser', 'chrome']:
                if app in command:
                    response = self.open_application(app)
                    self.speak(response)
                    return
            self.speak("Sorry, I don't know how to open that application.")
        
        # Help command
        elif 'help' in command:
            help_text = """
            I can help you with the following commands:
            - "What's the weather in [city]?"
            - "Search for [query]" or "Google [query]"
            - "Set a reminder for [task] at [time]"
            - "What time is it?"
            - "What's the date today?"
            - "Open [application]" (notepad, calculator, browser)
            - "Exit" or "Goodbye" to quit
            """
            self.speak(help_text)
        
        # Greeting commands
        elif any(word in command for word in ['hello', 'hi', 'hey']):
            self.speak("Hello! How can I help you today?")
        
        # Default response
        else:
            self.speak("I'm sorry, I didn't understand that command. Say 'help' for available commands.")
    
    def run_reminder_checker(self):
        """Run reminder checker in background"""
        while self.is_listening:
            self.check_reminders()
            time.sleep(30)  # Check every 30 seconds
    
    def main_loop(self):
        """Main assistant loop"""
        self.speak("Hello! I am your personal voice assistant. How can I help you today? Say 'help' for available commands.")
        
        # Start reminder checker in background
        reminder_thread = Thread(target=self.run_reminder_checker, daemon=True)
        reminder_thread.start()
        
        while self.is_listening:
            command = self.listen()
            if command:
                self.process_command(command)
            time.sleep(0.1)

def main():
    assistant = VoiceAssistant()
    try:
        assistant.main_loop()
    except KeyboardInterrupt:
        print("\nAssistant stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 