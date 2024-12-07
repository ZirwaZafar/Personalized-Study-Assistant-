import time

def pomodoro_timer(work_duration, break_duration, cycles):
    """Pomodoro Timer for productivity."""
    for cycle in range(1, cycles + 1):
        print(f"\n🍅 Pomodoro Cycle {cycle} - Work for {work_duration} minutes!")
        countdown_timer(work_duration)
        if cycle < cycles:
            print(f"☕ Take a break for {break_duration} minutes.")
            countdown_timer(break_duration)
    print("\n🎉 All cycles complete! Great job staying productive!")

def countdown_timer(minutes):
    """Countdown timer in minutes."""
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"⏳ {timer}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("⏰ Time's up!")

def menu():
    """Menu for the Pomodoro Timer."""
    print("\n🍅 Welcome to the Pomodoro Timer!")
    try:
        work_duration = int(input("Enter work duration (minutes): "))
        break_duration = int(input("Enter break duration (minutes): "))
        cycles = int(input("Enter number of cycles: "))
        pomodoro_timer(work_duration, break_duration, cycles)
    except ValueError:
        print("⚠️ Please enter valid numbers for the durations and cycles.")

# Run the Pomodoro Timer
menu()
