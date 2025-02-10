import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
import sqlite3

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Calendar")
        self.current_view = "week"
        
        # Create main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10, expand=True, fill='both')
        
        # Create view selection buttons
        self.view_frame = tk.Frame(self.main_frame)
        self.view_frame.pack(fill='x', pady=(0, 10))
        
        self.month_btn = tk.Button(self.view_frame, text="Month View", 
                                 command=lambda: self.change_view("month"))
        self.month_btn.pack(side='left', padx=5)
        
        self.week_btn = tk.Button(self.view_frame, text="Week View", 
                                command=lambda: self.change_view("week"))
        self.week_btn.pack(side='left')
        
        # Create calendar widget
        self.calendar = Calendar(self.main_frame, 
                               selectmode='day',
                               date_pattern='y-mm-dd',
                               showweeknumbers=True)
        self.calendar.pack(expand=True, fill='both')
        
        # Create event frame
        self.event_frame = tk.Frame(self.main_frame)
        self.event_frame.pack(fill='x', pady=10)
        
        # Event entry
        self.event_label = tk.Label(self.event_frame, text="Event:")
        self.event_label.pack(side='left')
        
        self.event_entry = tk.Entry(self.event_frame)
        self.event_entry.pack(side='left', padx=5, expand=True, fill='x')
        
        self.add_button = tk.Button(self.event_frame, text="Add Event", 
                                  command=self.add_event)
        self.add_button.pack(side='left')
        
        # Initialize database
        self.init_db()
        
        # Bind selection
        self.calendar.bind('<<CalendarSelected>>', self.show_events)
        
    def init_db(self):
        self.conn = sqlite3.connect('calendar_events.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events
            (date TEXT, event TEXT)
        ''')
        self.conn.commit()
        
    def add_event(self):
        date = self.calendar.get_date()
        event = self.event_entry.text.get()
        if event:
            self.cursor.execute('INSERT INTO events VALUES (?, ?)', (date, event))
            self.conn.commit()
            self.event_entry.delete(0, 'end')
            self.show_events(None)
            
    def show_events(self, event):
        date = self.calendar.get_date()
        self.cursor.execute('SELECT event FROM events WHERE date = ?', (date,))
        events = self.cursor.fetchall()
        # Update UI to show events for selected date
        # (Implementation left as exercise)
        
    def change_view(self, view):
        self.current_view = view
        if view == "week":
            self.calendar.configure(showweeknumbers=True)
        else:
            self.calendar.configure(showweeknumbers=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()