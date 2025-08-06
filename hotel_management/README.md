# Hotel Management System

This was my first attempt at building a desktop application with a database! I learned a lot about GUI development and SQL.

## What I Learned

- **Tkinter**: My first time creating a graphical interface (it was harder than I expected!)
- **SQLite**: Learned how databases work and how to store data permanently
- **Classes**: Finally understood how object-oriented programming works
- **User Input**: How to handle forms and validate data

## What It Does

Basically, it's like a digital hotel reception desk where you can:
- Add new guest reservations
- See all current reservations
- Edit reservation details
- Delete reservations
- Search for specific guests

## How to Run It

1. Make sure you're in the hotel_management folder:
   ```bash
   cd hotel_management
   ```

2. Run the application:
   ```bash
   python3 main.py
   ```

**Note**: If you're on Mac and get a Tkinter error, you need to install it first:
```bash
brew install python-tk
```

## How It Works

The app creates a database file called `hotel.db` that stores all the reservation data. When you add a reservation, it saves it to the database so it doesn't disappear when you close the app.

The interface has:
- A form on the left to add new reservations
- A table on the right showing all reservations
- Buttons to edit, delete, and search

## Challenges I Faced

- **Tkinter was confusing** at first - so many widgets and options!
- **Understanding classes** took me a while, but now I get it
- **Database concepts** were new to me - had to learn SQL basics
- **Making the GUI look good** was harder than I thought

## What I'm Proud Of

- The app actually works and saves data!
- I figured out how to organize code using classes
- The search function works pretty well
- I learned how to handle errors gracefully

This project taught me that building desktop apps is totally different from writing scripts. You have to think about user experience and data persistence.

---
#pinnaclefullstackinterns #pfsinterns 