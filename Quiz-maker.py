import random

quizzes = {}

def create_quiz():
    """Create a new quiz."""
    quiz_name = input("Enter quiz name: ")
    if quiz_name in quizzes:
        print("⚠️ A quiz with this name already exists. Try another name.")
        return
    
    questions = []
    print("Enter your questions (type 'done' when finished):")
    while True:
        question = input("Enter question: ")
        if question.lower() == "done":
            break
        options = []
        for i in range(4):
            option = input(f"Enter option {i + 1}: ")
            options.append(option)
        correct = input("Enter the number of the correct option (1-4): ")
        questions.append({"question": question, "options": options, "answer": int(correct)})
    
    quizzes[quiz_name] = questions
    print(f"✅ Quiz '{quiz_name}' created successfully!")

def attempt_quiz():
    """Attempt a quiz."""
    if not quizzes:
        print("📂 No quizzes available to attempt.")
        return
    
    print("\nAvailable Quizzes:")
    for name in quizzes.keys():
        print(f"- {name}")
    
    quiz_name = input("Enter the name of the quiz you want to attempt: ")
    if quiz_name not in quizzes:
        print("⚠️ Quiz not found!")
        return
    
    questions = quizzes[quiz_name]
    score = 0
    random.shuffle(questions)
    
    print(f"\n🎯 Starting Quiz: {quiz_name}")
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q["options"], start=1):
            print(f"{j}. {option}")
        try:
            answer = int(input("Your answer (1-4): "))
            if answer == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer was {q['answer']}.")
        except ValueError:
            print("⚠️ Invalid input. Moving to the next question.")
    
    print(f"\n🎉 Quiz Completed! Your Score: {score}/{len(questions)}")

def menu():
    """Quiz Maker Menu."""
    while True:
        print("\n📚 Quiz Maker Menu:")
        print("1. Create a Quiz")
        print("2. Attempt a Quiz")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            create_quiz()
        elif choice == "2":
            attempt_quiz()
        elif choice == "3":
            print("Goodbye! 👋 Keep learning!")
            break
        else:
            print("⚠️ Invalid choice. Please try again!")

# Run the Quiz Maker
menu()
