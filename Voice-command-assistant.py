import pyttsx3  # Text-to-speech
import speech_recognition as sr  # Speech recognition
import datetime  # For date and time
import webbrowser  # For opening websites

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user input via microphone and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("Network error. Please try again.")
        return ""

def respond_to_command(command):
    """Process and respond to user commands."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            speak(f"Searching for {query}.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("I can’t help with that yet, but I’m learning more every day!")

# Main function
def main():
    speak("Hello! I am your Personalized Study Assistant. How can I help you today?")
    while True:
        user_command = listen()
        if user_command:
            if "exit" in user_command or "quit" in user_command:
                speak("Goodbye! Have a great day.")
                break
            respond_to_command(user_command)

if __name__ == "__main__":
    main()
