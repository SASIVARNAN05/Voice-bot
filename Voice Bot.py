import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def respond(text):
    print(f"Bot: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

def answer_question(question):
    try:
        summary = wikipedia.summary(question, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "There are multiple options for this query. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            if "exit" in command.lower():
                respond("Goodbye!")
                break
            else:
                answer = answer_question(command)
                respond(answer)
