# Task Management System

My first web application! This was the most challenging project because I had to learn web development from scratch.

## What I Learned

- **Flask**: My first web framework - learned about routes and templates
- **HTML/CSS/JavaScript**: How to make web pages look good and interactive
- **SQLAlchemy**: A more advanced way to work with databases
- **Web Development**: How websites actually work behind the scenes
- **Bootstrap**: Making things look professional without being a designer

## What It Does

It's like a digital to-do list but much better! You can:
- Create tasks with titles and descriptions
- Set priorities (High, Medium, Low)
- Track status (Pending, In Progress, Completed)
- Set due dates
- Search and filter your tasks
- See statistics and progress

## How to Run It

1. Go to the task_management folder:
   ```bash
   cd task_management
   ```

2. Create a virtual environment (this keeps your project isolated):
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the web application:
   ```bash
   python main.py
   ```

6. Open your web browser and go to: `http://localhost:5001`

## How It Works

The app creates a database to store all your tasks. When you add a task, it saves it to the database so your tasks don't disappear when you close the browser.

The web interface has:
- A form to add new tasks
- A list showing all your tasks
- Buttons to edit, delete, and mark tasks complete
- A search bar to find specific tasks
- A dashboard with statistics

## Challenges I Faced

- **Web development was overwhelming** at first - so many new concepts!
- **Understanding how Flask works** took me a while
- **CSS and styling** was harder than I expected
- **Database relationships** were confusing
- **Getting the virtual environment to work** was tricky

## What I'm Proud Of

- I built a real web application that actually works!
- The interface looks pretty good (thanks Bootstrap!)
- The search and filter functions work well
- I learned how to handle web forms and user input
- The dashboard shows useful statistics

## Cool Features

- **Real-time updates**: You can mark tasks complete without refreshing the page
- **Responsive design**: Works on both desktop and mobile
- **Search functionality**: Find tasks quickly
- **Statistics dashboard**: See your progress at a glance
- **Clean interface**: Looks professional and is easy to use

This project taught me that web development is a whole different world from desktop apps. You have to think about user experience, data persistence, and making things look good in a browser.

---
#pinnaclefullstackinterns #pfsinterns 