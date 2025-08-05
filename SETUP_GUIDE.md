# Setup Guide - Pinnacle Full Stack Internship Projects

This guide will help you set up and run all three Python projects in this repository.

## 🛠️ Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 📦 Installation Steps

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd pfsinterns
```

### 2. System Dependencies

#### macOS
```bash
# Install Python Tkinter (required for Hotel Management System)
brew install python-tk

# Install additional system dependencies
brew install portaudio  # Required for voice assistant
```

#### Ubuntu/Debian
```bash
# Install Python Tkinter
sudo apt-get update
sudo apt-get install python3-tk

# Install audio dependencies for voice assistant
sudo apt-get install portaudio19-dev python3-pyaudio
```

#### Windows
- Tkinter usually comes with Python installation
- For voice assistant, you may need to install PyAudio manually

## 🏨 Project 1: Hotel Management System

### Setup
```bash
cd hotel_management

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies (if any additional ones are needed)
pip install -r requirements.txt

# Run the application
python main.py
```

### Troubleshooting
- If you get a Tkinter error, install it using the system dependencies above
- The application will create a `hotel.db` file automatically

## 🎤 Project 2: Voice Assistant

### Setup
```bash
cd voice_assistant

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Troubleshooting
- If PyAudio installation fails, try: `pip install pyaudio --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib'`
- For weather functionality, get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `YOUR_API_KEY_HERE` in `main.py`

## 📋 Project 3: Task Management System

### Setup
```bash
cd task_management

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Access the Application
- Open your web browser
- Go to: `http://localhost:5000`
- The application will create a `tasks.db` file automatically

## 🚀 Quick Start (All Projects)

### Option 1: Individual Setup (Recommended)
Follow the setup instructions for each project individually. This gives you more control and isolation.

### Option 2: Global Setup
```bash
# Install all dependencies globally (not recommended for production)
pip install flask flask-sqlalchemy speechrecognition pyttsx3 requests pyaudio

# Then run each project from its directory
cd hotel_management && python main.py
cd ../voice_assistant && python main.py
cd ../task_management && python main.py
```

## 🔧 Common Issues and Solutions

### Tkinter Issues
**Error**: `ModuleNotFoundError: No module named '_tkinter'`

**Solution**:
- macOS: `brew install python-tk`
- Ubuntu/Debian: `sudo apt-get install python3-tk`
- Windows: Reinstall Python with Tkinter option checked

### PyAudio Issues
**Error**: `pip install pyaudio` fails

**Solution**:
- macOS: `brew install portaudio` then `pip install pyaudio`
- Ubuntu/Debian: `sudo apt-get install portaudio19-dev python3-pyaudio`
- Windows: Download and install PyAudio wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

### Flask Issues
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install flask flask-sqlalchemy
```

### Port Issues
**Error**: `Address already in use`

**Solution**:
- Change the port in the Flask app or kill the process using the port
- For Flask: `app.run(debug=True, host='0.0.0.0', port=5001)`

## 📱 Testing the Applications

### Hotel Management System
1. Run the application
2. Add a new reservation with guest details
3. Test search functionality
4. Try updating and deleting reservations

### Voice Assistant
1. Run the application
2. Say "Hello" to test basic functionality
3. Try "What time is it?" for time information
4. Say "Help" for available commands
5. Test "Search for Python tutorials" for web search

### Task Management System
1. Open `http://localhost:5000` in your browser
2. Add a new task
3. Test filtering and search functionality
4. Try updating task status
5. Check the dashboard for statistics

## 📊 Project Features Summary

| Feature | Hotel Management | Voice Assistant | Task Management |
|---------|------------------|-----------------|-----------------|
| GUI Interface | ✅ Tkinter | ❌ CLI | ✅ Web (Bootstrap) |
| Database | ✅ SQLite | ❌ In-memory | ✅ SQLite + SQLAlchemy |
| CRUD Operations | ✅ Full | ❌ N/A | ✅ Full |
| Search/Filter | ✅ Basic | ❌ N/A | ✅ Advanced |
| API Integration | ❌ | ✅ Weather API | ❌ |
| Speech Recognition | ❌ | ✅ Google Speech API | ❌ |
| Real-time Updates | ❌ | ✅ Background threads | ✅ AJAX |

## 🎯 Next Steps

1. **Complete the Setup**: Follow the installation guide for each project
2. **Test Functionality**: Run each application and test its features
3. **Customize**: Modify the code to add your own features
4. **Documentation**: Read the individual README files for detailed information
5. **Deploy**: Consider deploying the web application to a cloud platform

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Verify your Python version: `python3 --version`
3. Ensure all dependencies are installed correctly
4. Check the individual project README files for specific instructions

---

**Happy Coding! 🚀**

Tags: #pinnaclefullstackinterns #pfsinterns #python #setup #installation 