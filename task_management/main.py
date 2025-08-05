from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.String(20), default='Medium')
    status = db.Column(db.String(20), default='Pending')
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        status = request.form['status']
        due_date_str = request.form['due_date']
        
        if not title:
            flash('Title is required!', 'error')
            return redirect(url_for('add_task'))
        
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
            except ValueError:
                flash('Invalid date format!', 'error')
                return redirect(url_for('add_task'))
        
        task = Task(
            title=title,
            description=description,
            priority=priority,
            status=status,
            due_date=due_date
        )
        
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_task.html')

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.priority = request.form['priority']
        task.status = request.form['status']
        
        due_date_str = request.form['due_date']
        if due_date_str:
            try:
                task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
            except ValueError:
                flash('Invalid date format!', 'error')
                return redirect(url_for('edit_task', task_id=task_id))
        else:
            task.due_date = None
        
        # Update completed_at if status is completed
        if task.status == 'Completed' and not task.completed_at:
            task.completed_at = datetime.utcnow()
        elif task.status != 'Completed':
            task.completed_at = None
        
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', task=task)

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/toggle_status/<int:task_id>')
def toggle_status(task_id):
    task = Task.query.get_or_404(task_id)
    
    if task.status == 'Completed':
        task.status = 'Pending'
        task.completed_at = None
    else:
        task.status = 'Completed'
        task.completed_at = datetime.utcnow()
    
    db.session.commit()
    return jsonify({'status': task.status})

@app.route('/filter_tasks')
def filter_tasks():
    status_filter = request.args.get('status', 'all')
    priority_filter = request.args.get('priority', 'all')
    
    query = Task.query
    
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    if priority_filter != 'all':
        query = query.filter_by(priority=priority_filter)
    
    tasks = query.order_by(Task.created_at.desc()).all()
    return render_template('task_list.html', tasks=tasks)

@app.route('/search_tasks')
def search_tasks():
    search_term = request.args.get('q', '')
    
    if search_term:
        tasks = Task.query.filter(
            Task.title.contains(search_term) | 
            Task.description.contains(search_term)
        ).order_by(Task.created_at.desc()).all()
    else:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
    
    return render_template('task_list.html', tasks=tasks)

@app.route('/dashboard')
def dashboard():
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(status='Completed').count()
    pending_tasks = Task.query.filter_by(status='Pending').count()
    high_priority_tasks = Task.query.filter_by(priority='High').count()
    
    # Recent tasks
    recent_tasks = Task.query.order_by(Task.created_at.desc()).limit(5).all()
    
    # Tasks due soon (within 3 days)
    from datetime import timedelta
    soon = datetime.utcnow() + timedelta(days=3)
    due_soon = Task.query.filter(
        Task.due_date <= soon,
        Task.status != 'Completed'
    ).order_by(Task.due_date).all()
    
    return render_template('dashboard.html', 
                         total_tasks=total_tasks,
                         completed_tasks=completed_tasks,
                         pending_tasks=pending_tasks,
                         high_priority_tasks=high_priority_tasks,
                         recent_tasks=recent_tasks,
                         due_soon=due_soon)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001) 