import speech_recognition as sr
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio).lower()
        print("You:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def chatbot_response(user_input):
    # Add your chatbot logic here
    return f"Chatbot: I heard you say {user_input}. I'm a simple chatbot and don't have specific answers yet."

def main():
    text_to_speech("Hello! I am your chatbot. Ask me anything.")
    
    while True:
        user_input = speech_to_text()

        if user_input == 'exit':
            text_to_speech("Goodbye!")
            break

        response = chatbot_response(user_input)
        text_to_speech(response)

if __name__ == "__main__":
    main()

