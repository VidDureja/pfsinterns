import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import os

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('800x600')
        self.root.configure(bg='#f0f0f0')
        
        # Database setup
        self.setup_database()
        
        # Create GUI
        self.create_widgets()
        self.load_reservations()
        
    def setup_database(self):
        """Initialize the database and create tables"""
        self.conn = sqlite3.connect('hotel.db')
        self.cursor = self.conn.cursor()
        
        # Create reservations table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guest_name TEXT NOT NULL,
                room_number TEXT NOT NULL,
                check_in DATE NOT NULL,
                check_out DATE NOT NULL,
                phone TEXT,
                email TEXT,
                total_amount REAL DEFAULT 0.0,
                status TEXT DEFAULT 'Active'
            )
        ''')
        
        # Create rooms table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                room_number TEXT PRIMARY KEY,
                room_type TEXT NOT NULL,
                price_per_night REAL NOT NULL,
                status TEXT DEFAULT 'Available'
            )
        ''')
        
        # Insert sample rooms if table is empty
        self.cursor.execute("SELECT COUNT(*) FROM rooms")
        if self.cursor.fetchone()[0] == 0:
            sample_rooms = [
                ('101', 'Standard', 100.0),
                ('102', 'Standard', 100.0),
                ('201', 'Deluxe', 150.0),
                ('202', 'Deluxe', 150.0),
                ('301', 'Suite', 250.0),
                ('302', 'Suite', 250.0)
            ]
            self.cursor.executemany(
                "INSERT INTO rooms (room_number, room_type, price_per_night) VALUES (?, ?, ?)",
                sample_rooms
            )
        
        self.conn.commit()
    
    def create_widgets(self):
        """Create the main GUI components"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text='🏨 Hotel Management System', 
                              font=('Arial', 20, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(pady=15)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Left frame for forms
        left_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        left_frame.pack(side='left', fill='y', padx=(0, 10))
        
        # Right frame for data display
        right_frame = tk.Frame(main_frame, bg='white', relief='raised', bd=2)
        right_frame.pack(side='right', fill='both', expand=True)
        
        self.create_form(left_frame)
        self.create_data_display(right_frame)
    
    def create_form(self, parent):
        """Create the reservation form"""
        # Form title
        form_title = tk.Label(parent, text='New Reservation', font=('Arial', 14, 'bold'), bg='white')
        form_title.pack(pady=10)
        
        # Form fields
        fields_frame = tk.Frame(parent, bg='white')
        fields_frame.pack(pady=10, padx=20)
        
        # Guest Name
        tk.Label(fields_frame, text='Guest Name:', bg='white').grid(row=0, column=0, sticky='w', pady=5)
        self.guest_name_var = tk.StringVar()
        tk.Entry(fields_frame, textvariable=self.guest_name_var, width=25).grid(row=0, column=1, pady=5, padx=5)
        
        # Room Number
        tk.Label(fields_frame, text='Room Number:', bg='white').grid(row=1, column=0, sticky='w', pady=5)
        self.room_number_var = tk.StringVar()
        room_combo = ttk.Combobox(fields_frame, textvariable=self.room_number_var, width=22)
        room_combo['values'] = self.get_available_rooms()
        room_combo.grid(row=1, column=1, pady=5, padx=5)
        
        # Check-in Date
        tk.Label(fields_frame, text='Check-in Date:', bg='white').grid(row=2, column=0, sticky='w', pady=5)
        self.check_in_var = tk.StringVar()
        tk.Entry(fields_frame, textvariable=self.check_in_var, width=25, placeholder='YYYY-MM-DD').grid(row=2, column=1, pady=5, padx=5)
        
        # Check-out Date
        tk.Label(fields_frame, text='Check-out Date:', bg='white').grid(row=3, column=0, sticky='w', pady=5)
        self.check_out_var = tk.StringVar()
        tk.Entry(fields_frame, textvariable=self.check_out_var, width=25, placeholder='YYYY-MM-DD').grid(row=3, column=1, pady=5, padx=5)
        
        # Phone
        tk.Label(fields_frame, text='Phone:', bg='white').grid(row=4, column=0, sticky='w', pady=5)
        self.phone_var = tk.StringVar()
        tk.Entry(fields_frame, textvariable=self.phone_var, width=25).grid(row=4, column=1, pady=5, padx=5)
        
        # Email
        tk.Label(fields_frame, text='Email:', bg='white').grid(row=5, column=0, sticky='w', pady=5)
        self.email_var = tk.StringVar()
        tk.Entry(fields_frame, textvariable=self.email_var, width=25).grid(row=5, column=1, pady=5, padx=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(parent, bg='white')
        buttons_frame.pack(pady=20)
        
        # Add button
        add_btn = tk.Button(buttons_frame, text='Add Reservation', command=self.add_reservation,
                           bg='#27ae60', fg='white', font=('Arial', 10, 'bold'), width=15)
        add_btn.pack(side='left', padx=5)
        
        # Clear button
        clear_btn = tk.Button(buttons_frame, text='Clear Form', command=self.clear_form,
                             bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'), width=15)
        clear_btn.pack(side='left', padx=5)
    
    def create_data_display(self, parent):
        """Create the data display area"""
        # Display title
        display_title = tk.Label(parent, text='Reservations', font=('Arial', 14, 'bold'), bg='white')
        display_title.pack(pady=10)
        
        # Search frame
        search_frame = tk.Frame(parent, bg='white')
        search_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(search_frame, text='Search:', bg='white').pack(side='left')
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side='left', padx=5)
        search_entry.bind('<KeyRelease>', self.search_reservations)
        
        # Treeview for displaying data
        columns = ('ID', 'Guest Name', 'Room', 'Check-in', 'Check-out', 'Phone', 'Status')
        self.tree = ttk.Treeview(parent, columns=columns, show='headings', height=15)
        
        # Configure columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(parent, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(pady=10, padx=20, fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Action buttons
        action_frame = tk.Frame(parent, bg='white')
        action_frame.pack(pady=10)
        
        update_btn = tk.Button(action_frame, text='Update', command=self.update_reservation,
                              bg='#3498db', fg='white', font=('Arial', 10, 'bold'), width=10)
        update_btn.pack(side='left', padx=5)
        
        delete_btn = tk.Button(action_frame, text='Delete', command=self.delete_reservation,
                              bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'), width=10)
        delete_btn.pack(side='left', padx=5)
        
        refresh_btn = tk.Button(action_frame, text='Refresh', command=self.load_reservations,
                               bg='#f39c12', fg='white', font=('Arial', 10, 'bold'), width=10)
        refresh_btn.pack(side='left', padx=5)
    
    def get_available_rooms(self):
        """Get list of available rooms"""
        self.cursor.execute("SELECT room_number FROM rooms WHERE status = 'Available'")
        return [row[0] for row in self.cursor.fetchall()]
    
    def add_reservation(self):
        """Add a new reservation"""
        try:
            # Validate required fields
            if not all([self.guest_name_var.get(), self.room_number_var.get(), 
                       self.check_in_var.get(), self.check_out_var.get()]):
                messagebox.showerror("Error", "Please fill all required fields!")
                return
            
            # Validate dates
            check_in = datetime.strptime(self.check_in_var.get(), '%Y-%m-%d')
            check_out = datetime.strptime(self.check_out_var.get(), '%Y-%m-%d')
            
            if check_in >= check_out:
                messagebox.showerror("Error", "Check-out date must be after check-in date!")
                return
            
            # Calculate total amount
            days = (check_out - check_in).days
            self.cursor.execute("SELECT price_per_night FROM rooms WHERE room_number = ?", 
                               (self.room_number_var.get(),))
            price = self.cursor.fetchone()[0]
            total_amount = days * price
            
            # Insert reservation
            self.cursor.execute('''
                INSERT INTO reservations (guest_name, room_number, check_in, check_out, 
                                        phone, email, total_amount)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.guest_name_var.get(), self.room_number_var.get(), 
                  self.check_in_var.get(), self.check_out_var.get(),
                  self.phone_var.get(), self.email_var.get(), total_amount))
            
            # Update room status
            self.cursor.execute("UPDATE rooms SET status = 'Occupied' WHERE room_number = ?",
                               (self.room_number_var.get(),))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Reservation added successfully!")
            self.clear_form()
            self.load_reservations()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid dates in YYYY-MM-DD format!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        self.guest_name_var.set('')
        self.room_number_var.set('')
        self.check_in_var.set('')
        self.check_out_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
    
    def load_reservations(self):
        """Load and display all reservations"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Fetch and display reservations
        self.cursor.execute('''
            SELECT id, guest_name, room_number, check_in, check_out, phone, status
            FROM reservations ORDER BY check_in DESC
        ''')
        
        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', values=row)
    
    def search_reservations(self, event=None):
        """Search reservations by guest name"""
        search_term = self.search_var.get().lower()
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Search and display results
        self.cursor.execute('''
            SELECT id, guest_name, room_number, check_in, check_out, phone, status
            FROM reservations WHERE LOWER(guest_name) LIKE ? ORDER BY check_in DESC
        ''', (f'%{search_term}%',))
        
        for row in self.cursor.fetchall():
            self.tree.insert('', 'end', values=row)
    
    def update_reservation(self):
        """Update selected reservation"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a reservation to update!")
            return
        
        # Get selected reservation data
        reservation_id = self.tree.item(selected_item[0])['values'][0]
        
        # Create update dialog
        self.create_update_dialog(reservation_id)
    
    def create_update_dialog(self, reservation_id):
        """Create dialog for updating reservation"""
        dialog = tk.Toplevel(self.root)
        dialog.title('Update Reservation')
        dialog.geometry('400x300')
        dialog.configure(bg='white')
        
        # Get current reservation data
        self.cursor.execute('''
            SELECT guest_name, room_number, check_in, check_out, phone, email, status
            FROM reservations WHERE id = ?
        ''', (reservation_id,))
        data = self.cursor.fetchone()
        
        # Create form fields
        tk.Label(dialog, text='Update Reservation', font=('Arial', 14, 'bold'), bg='white').pack(pady=10)
        
        # Status selection
        tk.Label(dialog, text='Status:', bg='white').pack()
        status_var = tk.StringVar(value=data[6])
        status_combo = ttk.Combobox(dialog, textvariable=status_var, values=['Active', 'Completed', 'Cancelled'])
        status_combo.pack(pady=5)
        
        # Update button
        def update():
            try:
                self.cursor.execute('''
                    UPDATE reservations SET status = ? WHERE id = ?
                ''', (status_var.get(), reservation_id))
                self.conn.commit()
                messagebox.showinfo("Success", "Reservation updated successfully!")
                dialog.destroy()
                self.load_reservations()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
        tk.Button(dialog, text='Update', command=update, bg='#27ae60', fg='white').pack(pady=20)
    
    def delete_reservation(self):
        """Delete selected reservation"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a reservation to delete!")
            return
        
        # Confirm deletion
        if not messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?"):
            return
        
        try:
            reservation_id = self.tree.item(selected_item[0])['values'][0]
            room_number = self.tree.item(selected_item[0])['values'][2]
            
            # Delete reservation
            self.cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
            
            # Update room status
            self.cursor.execute("UPDATE rooms SET status = 'Available' WHERE room_number = ?", (room_number,))
            
            self.conn.commit()
            messagebox.showinfo("Success", "Reservation deleted successfully!")
            self.load_reservations()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def __del__(self):
        """Cleanup database connection"""
        if hasattr(self, 'conn'):
            self.conn.close()

def main():
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main() 