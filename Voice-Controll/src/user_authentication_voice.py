import speech_recognition as sr
#provide funtion that interact with the os like restarting the program
import os
import sys

# Define user credentials - dictionary
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}

def check_access(user, password):
    if user in users and users[user]["password"] == password:
        return users[user]["role"]
    return None

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from the service; {0}".format(e))
    return None

def restart_program():
    """Restarts the current program."""
    print("Restarting the program...")
    # os.execv(): Replaces the current running program with a new instance of the same script.
    # sys.executable: Gets the path of the Python interpreter.
    # start new instance with same arg
    os.execv(sys.executable, ['python'] + sys.argv)

def main():
    print("Welcome! Please enter your username:")
    username = input()
    print("Please enter your password:")
    password = input()
    
    role = check_access(username, password)
    
    if role:
        print(f"Access granted for {role}. You can now execute commands.")
        
        while True:
            command = recognize_speech()
            if command:
                if role == "admin":
                    # Admin commands
                    if command == "shut down":
                        print("Shutting down...")
                        break  # Placeholder for shutdown logic
                    elif command == "restart":
                        restart_program()  # Call the restart function
                    else:
                        print("Command not recognized.")
                elif role == "user":
                    # User commands
                    if command == "status":
                        print("System status: All systems operational.")
                    else:
                        print("Command not recognized for user.")
    else:
        print("Access denied. Invalid username or password.")

# This line checks if the script is being run directly 
# entry point to the program - call function go start program
# construct to controll the execution of the code
if __name__ == "__main__":
    main()
