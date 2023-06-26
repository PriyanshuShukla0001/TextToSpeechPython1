import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Priyanshu")
    while True:
        x = input("Enter what you want me to speak: ")
        if x== "q":
            break

        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Set the text that needs to be spoken
        engine.say(x)

        # Wait for speech to complete
        engine.runAndWait()

