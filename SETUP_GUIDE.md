# How to Set Up My Projects

Hey! This guide will help you get my three Python projects running on your computer. I'll walk you through the setup step by step.

## What You Need

- Python 3.7 or higher
- A computer with internet
- Some patience (I ran into a few issues when setting these up!)

## Getting Started

### Step 1: Download the Projects
First, you need to get the code on your computer:
```bash
git clone <your-repository-url>
cd pfsinterns
```

## Setting Up Each Project

### Project 1: Hotel Management System

This one is the easiest to set up!

**What you need:**
- Python (should already be installed)
- Tkinter (for the GUI)

**Setup:**
```bash
cd hotel_management
python3 main.py
```

**If you get a Tkinter error on Mac:**
```bash
brew install python-tk
```

**What happens:**
- A window will open with the hotel management interface
- You can add reservations, view them, edit them, etc.
- Data is saved in a file called `hotel.db`

### Project 2: Voice Assistant

This one is fun but needs some setup!

**What you need:**
- Microphone
- Internet connection
- Some Python packages

**Setup:**
```bash
cd voice_assistant
pip install -r requirements.txt
python main.py
```

**If pip gives you an error about "externally-managed-environment":**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**What happens:**
- The assistant will say hello and start listening
- Try saying "What time is it?" or "Help"
- Say "Exit" to quit

**For weather features:**
- Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
- Replace `YOUR_API_KEY_HERE` in the code with your actual key

### Project 3: Task Management System

This is my web application - it's the most complex but also the coolest!

**What you need:**
- Python
- Flask and other web packages

**Setup:**
```bash
cd task_management
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**What happens:**
- A web server starts running
- Open your browser and go to `http://localhost:5001`
- You'll see a nice web interface for managing tasks

## Common Problems I Ran Into

### "Command not found: python"
**Solution:** Try `python3` instead of `python`

### "No module named 'tkinter'"
**Solution:** On Mac, run `brew install python-tk`

### "externally-managed-environment"
**Solution:** Use a virtual environment (see the task management setup above)

### "Port 5000 is in use"
**Solution:** The app will automatically use port 5001 instead

### "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure you activated the virtual environment and ran `pip install -r requirements.txt`

## Testing the Projects

### Hotel Management System
1. Run the app
2. Try adding a reservation
3. Search for the reservation you just added
4. Try editing and deleting it

### Voice Assistant
1. Run the app
2. Say "Hello" to test basic functionality
3. Try "What time is it?"
4. Say "Help" to see all commands
5. Try "Search for Python tutorials"

### Task Management System
1. Run the app and open in browser
2. Add a new task
3. Try filtering by priority
4. Search for your task
5. Check out the dashboard

## What Each Project Teaches

- **Hotel Management**: Desktop apps, databases, GUI development
- **Voice Assistant**: Speech recognition, APIs, background processing
- **Task Management**: Web development, Flask, modern UI design

## If You Get Stuck

1. **Check the error message** - it usually tells you what's wrong
2. **Make sure you're in the right folder** - use `pwd` to check
3. **Try the troubleshooting steps** above
4. **Google the error message** - someone else probably had the same problem

## My Experience

When I first set these up, I ran into several issues:
- Tkinter wasn't installed on my Mac
- I didn't understand virtual environments
- The Flask app wouldn't start because of port conflicts
- I had trouble with the voice assistant's microphone setup

But I figured it out, and now all three projects work perfectly! Don't get discouraged if you run into issues - that's normal when learning new technologies.

Good luck! 🚀

---
#pinnaclefullstackinterns #pfsinterns #python #setup 