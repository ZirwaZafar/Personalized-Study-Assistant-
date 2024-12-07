study_progress = []

def add_topic(topic):
    """Add a new topic to the study progress tracker."""
    study_progress.append({"topic": topic, "completed": False})
    print(f"✅ Topic '{topic}' added to your study list!")

def view_progress():
    """View all study topics and their status."""
    if not study_progress:
        print("📂 No topics added yet!")
    else:
        print("\n📋 Your Study Progress:")
        for i, item in enumerate(study_progress, start=1):
            status = "✅ Completed" if item["completed"] else "❌ Not Completed"
            print(f"{i}. {item['topic']} - {status}")

def mark_topic_completed(index):
    """Mark a topic as completed."""
    if 0 < index <= len(study_progress):
        study_progress[index - 1]["completed"] = True
        print(f"🎉 Topic {index} marked as completed!")
    else:
        print("⚠️ Invalid topic number!")

def view_summary():
    """View summary of study progress."""
    total = len(study_progress)
    completed = sum(1 for topic in study_progress if topic["completed"])
    print("\n📊 Study Progress Summary:")
    print(f"Total Topics: {total}")
    print(f"Completed: {completed}")
    print(f"Remaining: {total - completed}")

def menu():
    """Display the menu."""
    while True:
        print("\n📚 Study Progress Tracker Menu:")
        print("1. Add a Study Topic")
        print("2. View Study Progress")
        print("3. Mark a Topic as Completed")
        print("4. View Progress Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            topic = input("Enter the study topic: ")
            add_topic(topic)
        elif choice == "2":
            view_progress()
        elif choice == "3":
            try:
                index = int(input("Enter topic number to mark as completed: "))
                mark_topic_completed(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            view_summary()
        elif choice == "5":
            print("Goodbye! 👋 Keep studying hard!")
            break
        else:
            print("⚠️ Invalid choice. Please try again!")

# Run the Study Progress Tracker
menu()
