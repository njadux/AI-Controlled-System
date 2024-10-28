import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source)  # Adjusts noise level

    print("You can speak now:")
    # Capture audio
    audio_data = recognizer.listen(source)
    
    print("Recognizing speech...")
    try:
        # Recognize audio using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print(f"You said: {text}")


        # make a conversation
        if text.lower() == "hello" or text.lower() == "hi":
            print("Hi Jadu, Happy to hear from you!")
        elif text.lower() == "hey":
            print("Hey Jadu, How are you")
        elif "i am fine" in text.lower() or "good" in text.lower():
            print("that was good to have a nice day")
        elif text.lower() == "what's your name":
            print("My name is Valiere")
        elif text.lower() == "i'm so stressed out":
            print("Jadu, It's tough when you're feeling overwhelmed. Would you like to talk about what's making you feel this way?")
        else:
            print("I didn't understand that.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
