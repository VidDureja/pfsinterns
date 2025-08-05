# Task Management System

A modern web-based task management application built with Flask and SQLAlchemy. This project provides a comprehensive solution for managing tasks with features like priority levels, due dates, status tracking, and a beautiful responsive interface.

## Features

- **Task Management**: Create, read, update, and delete tasks
- **Priority Levels**: Set tasks as High, Medium, or Low priority
- **Status Tracking**: Track task status (Pending, In Progress, Completed)
- **Due Dates**: Set and track due dates for tasks
- **Search & Filter**: Search tasks by title/description and filter by status/priority
- **Dashboard**: View task statistics and overview
- **Responsive Design**: Modern UI that works on desktop and mobile
- **Real-time Updates**: Toggle task status without page refresh

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Icons**: Font Awesome

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd task_management
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access the application**:
   Open your browser and go to `http://localhost:5000`

## Usage

### Adding Tasks
1. Click "Add New Task" button
2. Fill in the task details:
   - Title (required)
   - Description (optional)
   - Priority (Low/Medium/High)
   - Status (Pending/In Progress/Completed)
   - Due Date (optional)
3. Click "Create Task"

### Managing Tasks
- **Edit**: Click the dropdown menu on any task card and select "Edit"
- **Toggle Status**: Use the dropdown menu to quickly toggle between statuses
- **Delete**: Use the dropdown menu to delete tasks (with confirmation)

### Filtering & Searching
- Use the filter options on the home page to filter by status and priority
- Use the search bar in the navigation to search tasks by title or description

### Dashboard
- View task statistics and overview
- See recent tasks and tasks due soon
- Access quick actions for common tasks

## Database Schema

The application uses SQLite with the following main table:

```sql
CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    priority VARCHAR(20) DEFAULT 'Medium',
    status VARCHAR(20) DEFAULT 'Pending',
    due_date DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at DATETIME
);
```

## API Endpoints

- `GET /` - Home page with all tasks
- `GET /dashboard` - Dashboard with statistics
- `GET /add_task` - Add task form
- `POST /add_task` - Create new task
- `GET /edit_task/<id>` - Edit task form
- `POST /edit_task/<id>` - Update task
- `GET /delete_task/<id>` - Delete task
- `GET /toggle_status/<id>` - Toggle task status (AJAX)
- `GET /filter_tasks` - Filter tasks by status/priority
- `GET /search_tasks` - Search tasks by query

## Project Structure

```
task_management/
├── main.py              # Main Flask application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── templates/          # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── index.html      # Home page with task list
│   ├── add_task.html   # Add task form
│   ├── edit_task.html  # Edit task form
│   ├── dashboard.html  # Dashboard page
│   └── task_list.html  # Filtered task list
└── tasks.db            # SQLite database (created automatically)
```

## Features in Detail

### Task Management
- Full CRUD operations for tasks
- Validation for required fields
- Automatic timestamp tracking
- Soft deletion with confirmation

### User Interface
- Responsive Bootstrap 5 design
- Card-based task display
- Color-coded priority and status indicators
- Dropdown menus for actions
- Search and filter functionality

### Dashboard
- Task statistics cards
- Recent tasks list
- Tasks due soon
- Quick action buttons
- Progress indicators

## Future Enhancements

- User authentication and authorization
- Task categories/tags
- File attachments
- Email notifications
- Task sharing and collaboration
- Mobile app
- API for external integrations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the Pinnacle Full-Stack Interns Python Developer Internship Program.

---
#pinnaclefullstackinterns #pfsinterns 