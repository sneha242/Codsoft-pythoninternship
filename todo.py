tasks = []           # List to hold tasks
categories = {}      # Dictionary to hold categories as keys and their corresponding tasks as values

# functions for adding, deleting, and submitting tasks
def add_task(task):
    tasks.append(task)

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' deleted successfully.")
    else:
        print("Task not found.")

def submit_task(task, category):
    if category not in categories:
        categories[category] = []
    categories[category].append(task)
    print(f"Task '{task}' submitted to category '{category}' successfully.")

# functions for creating and managing categories
def create_category(category):
    if category not in categories:
        categories[category] = []
        print(f"Category '{category}' created successfully.")
    else:
        print("Category already exists.")

def delete_category(category):
    if category in categories:
        del categories[category]
        print(f"Category '{category}' deleted successfully.")
    else:
        print("Category not found.")

def print_categories():
    print("Categories:")
    for category in categories:
        print(f"- {category}")

def print_tasks():
    print("Tasks:")
    for task in tasks:
        print(f"- {task}")

def main():
    while True:
        print("\n To-Do List App")
        print_categories()
        print_tasks()

        print("\nOptions:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Submit task to category")
        print("4. Create category")
        print("5. Delete category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to delete: ")
            delete_task(task)
        elif choice == "3":
            task = input("Enter the task: ")
            category = input("Enter the category: ")
            submit_task(task, category)
        elif choice == "4":
            category = input("Enter the category name: ")
            create_category(category)
        elif choice == "5":
            category = input("Enter the category to delete: ")
            delete_category(category)
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
