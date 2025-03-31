import argparse
from todo import TodoList

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo")
    add_parser.add_argument("task", help="The task to add")
    add_parser.add_argument("-p", "--priority", choices=["low", "medium", "high"], 
                          default="medium", help="Priority of the task")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List todos")
    list_parser.add_argument("-a", "--all", action="store_true", 
                           help="Show all todos including completed")
    
    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a todo as complete")
    complete_parser.add_argument("id", type=int, help="ID of the todo to complete")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_parser.add_argument("id", type=int, help="ID of the todo to delete")
    
    # Clear command
    clear_parser = subparsers.add_parser("clear", help="Clear completed todos")
    
    args = parser.parse_args()
    todo_list = TodoList()
    
    if args.command == "add":
        todo_list.add_todo(args.task, args.priority)
    elif args.command == "list":
        todo_list.list_todos(show_all=args.all)
    elif args.command == "complete":
        todo_list.complete_todo(args.id)
    elif args.command == "delete":
        todo_list.delete_todo(args.id)
    elif args.command == "clear":
        todo_list.clear_completed()

if __name__ == "__main__":
    main()