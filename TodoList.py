import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task, priority="medium"):
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority.lower(),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"Added todo: {task}")
    
    def list_todos(self, show_all=False):
        if not self.todos:
            print("No todos found!")
            return
        
        for todo in self.todos:
            if show_all or not todo['completed']:
                status = "✓" if todo['completed'] else " "
                print(f"{todo['id']}. [{status}] {todo['task']} (Priority: {todo['priority']})")
    
    def complete_todo(self, todo_id):
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                todo['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_todos()
                print(f"Completed todo: {todo['task']}")
                return
        print(f"Todo with ID {todo_id} not found!")
    
    def delete_todo(self, todo_id):
        self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
        self.save_todos()
        print(f"Deleted todo with ID {todo_id}")
    
    def clear_completed(self):
        initial_count = len(self.todos)
        self.todos = [todo for todo in self.todos if not todo['completed']]
        removed_count = initial_count - len(self.todos)
        self.save_todos()
        print(f"Removed {removed_count} completed todos")