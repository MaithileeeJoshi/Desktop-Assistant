import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..!!")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, my speech service is currently unavailable.")
    return None


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('maithilij44@gmail.com', 'EmilyInParis@7825')
    server.sendmail('maithilij44@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if query:
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I couldn't find any relevant information.")
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple pages matching your query. Please be more specific.")

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("https://stackoverflow.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codepath = r"C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                webbrowser.open(codepath)

            elif 'open photos' in query:
                path = r"C:\Users\Lenovo"
                webbrowser.open(path)

            elif 'email to harry' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "maithilij44@gmail.com"  # Update with the recipient's email address
                    sendEmail(to, content)
                    speak("Email has been sent.")
                except Exception as e:
                    print(e)
                    speak("Sorry, I cannot send this email.")

            elif 'exit' in query:
                speak("Goodbye!")
                break
