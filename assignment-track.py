import datetime

# Assignment Tracker
assignments = []

def add_assignment(subject, due_date):
    """Add a new assignment."""
    assignments.append({"subject": subject, "due_date": due_date, "completed": False})
    print(f"✅ Assignment for {subject} added, due on {due_date}.")

def view_assignments():
    """View all assignments."""
    if not assignments:
        print("📂 No assignments found!")
    else:
        print("\n📋 Your Assignments:")
        for i, assignment in enumerate(assignments, start=1):
            status = "✅ Completed" if assignment["completed"] else "❌ Pending"
            print(f"{i}. {assignment['subject']} (Due: {assignment['due_date']}) - {status}")

def mark_completed(index):
    """Mark an assignment as completed."""
    if 0 < index <= len(assignments):
        assignments[index - 1]["completed"] = True
        print(f"🎉 Assignment {index} marked as completed!")
    else:
        print("⚠️ Invalid assignment number!")

def menu():
    """Display the menu."""
    while True:
        print("\n📚 Assignment Tracker Menu:")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark Assignment as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            subject = input("Enter subject: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")  # Validate date
                add_assignment(subject, due_date)
            except ValueError:
                print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            try:
                index = int(input("Enter assignment number to mark as completed: "))
                mark_completed(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please try again!")

# Run the Assignment Tracker
menu()
