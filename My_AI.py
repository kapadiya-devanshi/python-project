import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipediaapi
import os
import pyjokes
from PIL import Image
import subprocess
import mtranslate

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello ", "wake up user", "you there user", "time to work sir",
             "ok", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

# =======================================================================================================================================================

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def speak(audio) -> None:
    # audio = mtranslate.translate(audio, to_language='hi', from_language='en-in')
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def time() -> None:
    """Tells the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(current_time)
    print("The current time is", current_time)


def date() -> None:
    """Tells the current date."""
    now = datetime.datetime.now()
    speak("The current date is")
    speak(f"{now.day} {now.strftime('%B')} {now.year}")
    print(f"The current date is {now.day}/{now.month}/{now.year}")

def shutdown_system():
    speak("Shutting down the system.")
    subprocess.call(["shutdown", "/s", "/t", "1"])  

def get_answer(question):
    # Define a dictionary of questions and answers
    responses = {
        "about the college": "Noble University in Junagadh, Gujarat, is a multi-disciplinary institution offering over 80 courses across various fields, including engineering, arts, and sciences. It aims to be a center of excellence in education and has a strong focus on placements and student development.",
        "what is computer application": "A computer application is a software program designed to perform specific tasks or functions for the user. Applications can range from simple programs that perform a single function to complex systems that integrate multiple functionalities.",
        "bye": "Goodbye! Have a great day!",
    }

    # Return the answer if the question is in the dictionary
    return responses.get(question.lower(), "I'm sorry, I don't understand that question.")

    

def search_wikipedia(query):
    user_agent = "MyWikipediaSearchApp/1.0 (https://example.com; myemail@example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',  
        user_agent=user_agent
    )

    # Search for the page
    page = wiki_wiki.page(query)

    # Check if the page exists
    if page.exists():
        print(f"Title: {page.title}\n")
        print(f"Summary:\n{page.summary}\n")
        # speak(page.summary)
    else:
        print("Sorry, no page found for that query.")


def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Welcome to the Wikipedia Search Program!")
    while True:
        print("Please say a search term (or type 'exit' to quit): ")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            if query.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            search_wikipedia(query)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def wishme():
    speak("Initializing System ")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 16:
        speak("Good afternoon!")
    elif 16 <= hour < 24:
        speak("Good evening!")
    else:
        speak("Good night, see you tomorrow.")


def screenshot() -> None:
    """Takes a screenshot and saves it."""
    speak("Alright sir, taking the screenshot")
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("D:\\Project\\screenshot\\screenshot.png")
    img.save(img_path)
    speak(f"Screenshot saved as {img_path}.")
    print(f"Screenshot saved as {img_path}.")


def takecommand() -> str:
    """Takes microphone input from the user and returns it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        try:
            audio = r.listen(source, timeout=5) 
        except sr.WaitTimeoutError:
            speak("Timeout occurred. Please try again.")
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        query = mtranslate.translate(query,to_language='en-in')
        # print(query)
        speak(query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None
    except Exception as e:
        speak(f"An error occurred: {e}")
        print(f"Error: {e}")
        return None



if __name__ == "__main__":
    wishme()

    while True:
        command = takecommand()
        if not command:
            continue

        if command in GREETINGS:
            speak(random.choice(GREETINGS_RES))

        elif "time" in command:
            time()

        elif "date" in command:
            date()

        elif "play music" in command:
            speak("play music for you ")
            os.startfile("C:\\Users\\Admin\\AppData\\Local\\Microsoft\\WindowsApps\\spotify.exe") 

        elif "add task" in command:
            task =  command.replace("add task","")
            task = task.strip()
            if task != "":
                speak("Adding task: "+ task)
                with open("todo.txt","a") as file:
                    file.write(task + "\n")

        elif "read task" in command:
            with open("todo.txt","r") as file:
                speak("task we have to do today is:" + file.read())

        elif "show me work" in command:
            with open("todo.txt","r") as file:
                tasks = file.read()
                notification.notify(
                title = "Todays work",
                message = tasks
            )

        elif "open website" in command:
            request = command. replace("open website", "")
            speak("hear, Noble University website")
            webbrowser.open("https://nobleuniversity.ac.in/")
            speak("The Noble University is a one-of-its-kind, multi-disciplinary academic establishment in the region, determined to become a ‘Centre for Excellence’ in Engineering, Technology, Management, Commerce, Pharmacy, Homeopathy, Ayurveda, Science, Education, and Nursing.")
            
        elif "open youtube" in command:
            request = command. replace("open youtube", "")
            webbrowser.open("www.youtube.com")

        elif "open" in command:
            command = command.replace("opem", "")
            pyautogui.press("super")
            pyautogui.typewrite(command)
            pyautogui.sleep(1)
            pyautogui.press("enter")
        
        elif "search google" in command:
            command = command. replace("search google", "")
            webbrowser.open("https://www.google.com/search?q="+command)


        elif "screenshot" in command:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "show me the picture" in command:
            try:
                img = Image.open("D:\\Project\\screenshot\\screenshot.png")
                img.show(img)
                speak("Here it is sir")
                # time.sleep(2)

            except IOError:
                speak("Sorry sir, I am unable to display the screenshot")

        elif "wikipedia" in command:
            main()

        elif "tell me a joke" in command:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            
        elif "switch the window" in command or "switch window" in command:
            speak("Okay sir, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            # time.sleep(1)
            pyautogui.keyUp("alt")

        elif "goodbye" in command or "offline" in command or "exit" in command:
            speak("Alright sir, going offline. It was nice working with you")
            exit()

        elif "lock" in command:
            subprocess.run("rundll32.exe user32.dll,LockWorkStation")

        elif "restart" in command:
            speak("Restarting the system now.")
            subprocess.run(["shutdown", "/r", "/t", "1"])
            
        elif "shutdown" in command:
            shutdown_system()

        elif " " in command:
            if "bye" in command:
                answer = get_answer("bye")
                print(answer)
                break
            answer = get_answer(command)
            speak(answer)
