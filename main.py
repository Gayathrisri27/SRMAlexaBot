import threading
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipediaapi
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class API:
    @staticmethod
    def search_wikipedia(query):
        user_agent = "SRM-Alexa (https://en.wikipedia.org/wiki/SRM_Institute_of_Science_and_Technology)"
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            user_agent=user_agent
        )
        page = wiki_wiki.page(query)
        if page.exists():
            return page.summary[:500]  # Returning the first 500 characters of the summary
        return "Apologies, I couldn't find any information on Wikipedia."

class Speech:
    @staticmethod
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        print(f"SRM-Alexa: {text}")

    @staticmethod
    def process_command(command):
        if "portal" in command:
            webbrowser.open("https://sp.srmist.edu.in/srmiststudentportal/students/loginManager/youLogin.jsp")
        elif "website" in command:
            webbrowser.open("https://www.srmist.edu.in/")
        elif "youtube" in command:
            webbrowser.open("https://www.youtube.com/channel/UCm1shC2LXjkKmgjz8LyJkFw")
        elif "hospital" in command:
            webbrowser.open("https://www.srmhospital.co.in/")
        elif "map" in command:
            webbrowser.open("https://www.google.com/maps/dir//R2FV%2B6Q7+SRM+Institute+of+Science+and+Technology,+Potheri,+SRM+Nagar,+Kattankulathur,+Tamil+Nadu+603203/@12.823033,79.8919807,12z/data=!4m18!1m8!3m7!1s0x3a52f712b82a78d9:0xfdb944a3aee53831!2sSRM+Institute+of+Science+and+Technology!8m2!3d12.823033!4d80.044416!15sCgNzcm0iA4gBAZIBCnVuaXZlcnNpdHngAQA!16zL20vMGJwNzl6!4m8!1m0!1m5!1m1!1s0x3a52f712b82a78d9:0xfdb944a3aee53831!2m2!1d80.044416!2d12.823033!3e3?entry=ttu")
        elif "contact" in command:
            webbrowser.open("https://www.srmist.edu.in/contact-us/")
        elif "attendance" in command:  # Added attendance command
            webbrowser.open("https://academia.srmist.edu.in/#Page:My_Attendance")
        elif "wikipedia" in command:
            query = command.replace("wikipedia", "").strip()
            if query:
                Speech.speak(f"Searching Wikipedia for {query}")
                summary = API.search_wikipedia(query)
                if summary:
                    Speech.speak(summary)
                    SRMAlexaApp.display_text(summary)
                    print(f"SRM-Alexa:\n{summary}\n")
                else:
                    Speech.speak("Apologies, I couldn't find any information on Wikipedia.")
            else:
                Speech.speak("Please specify what you want to search on Wikipedia.")
        else:
            Speech.speak("Apologies, I didn't understand that command.")

class SRMAlexaApp(App):
    @staticmethod
    def display_text(text):
        popup = Popup(title='Information', content=Label(text=text), size_hint=(None, None), size=(400, 400))
        close_button = Button(text='Close', size_hint_y=None, height=40)
        close_button.bind(on_press=popup.dismiss)
        popup.content.add_widget(close_button)
        popup.open()

    def build(self):
        sm = ScreenManager()
        main_screen = Screen(name='main')
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Adding logo
        logo = Image(source='./Capture.png', size_hint=(1, 0.3))
        main_layout.add_widget(logo)

        # Welcome label
        welcome_label = Label(text='Welcome to SRM Alexa Bot!', font_size=24, size_hint=(1, 0.1))
        main_layout.add_widget(welcome_label)

        # Adding a GridLayout for buttons
        button_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.3))

        talk_button = Button(text='Interact with me', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        talk_button.bind(on_press=self.talk_with_me)
        button_layout.add_widget(talk_button)

        portal_button = Button(text='Open Student Portal', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        portal_button.bind(on_press=lambda x: self.open_url("https://sp.srmist.edu.in/srmiststudentportal/students/loginManager/youLogin.jsp"))
        button_layout.add_widget(portal_button)

        website_button = Button(text='Visit SRMIST Website', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        website_button.bind(on_press=lambda x: self.open_url("https://www.srmist.edu.in/"))
        button_layout.add_widget(website_button)

        youtube_button = Button(text='Explore SRMIST on YouTube', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        youtube_button.bind(on_press=lambda x: self.open_url("https://www.youtube.com/channel/UCm1shC2LXjkKmgjz8LyJkFw"))
        button_layout.add_widget(youtube_button)

        hospital_button = Button(text='Discover SRM Hospital', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        hospital_button.bind(on_press=lambda x: self.open_url("https://www.srmhospital.co.in/"))
        button_layout.add_widget(hospital_button)

        map_button = Button(text='View Campus Map', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        map_button.bind(on_press=lambda x: self.open_url("https://www.google.com/maps/dir//R2FV%2B6Q7+SRM+Institute+of+Science+and+Technology,+Potheri,+SRM+Nagar,+Kattankulathur,+Tamil+Nadu+603203/@12.823033,79.8919807,12z/data=!4m18!1m8!3m7!1s0x3a52f712b82a78d9:0xfdb944a3aee53831!2sSRM+Institute+of+Science+and+Technology!8m2!3d12.823033!4d80.044416!15sCgNzcm0iA4gBAZIBCnVuaXZlcnNpdHngAQA!16zL20vMGJwNzl6!4m8!1m0!1m5!1m1!1s0x3a52f712b82a78d9:0xfdb944a3aee53831!2m2!1d80.044416!2d12.823033!3e3?entry=ttu"))
        button_layout.add_widget(map_button)

        contact_button = Button(text='Contact SRMIST', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        contact_button.bind(on_press=lambda x: self.open_url("https://www.srmist.edu.in/contact-us/"))
        button_layout.add_widget(contact_button)

        # Adding Attendance Button
        attendance_button = Button(text='Check Attendance', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        attendance_button.bind(on_press=lambda x: self.open_url("https://academia.srmist.edu.in/#Page:My_Attendance"))
        button_layout.add_widget(attendance_button)

        main_layout.add_widget(button_layout)

        # Adding a text input and button for Wikipedia search
        wiki_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.wiki_input = TextInput(hint_text='Search Wikipedia...', font_size=24)
        wiki_button = Button(text='Search', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        wiki_button.bind(on_press=self.search_wikipedia)
        wiki_layout.add_widget(self.wiki_input)
        wiki_layout.add_widget(wiki_button)
        main_layout.add_widget(wiki_layout)

        main_screen.add_widget(main_layout)
        sm.add_widget(main_screen)
        return sm

    def talk_with_me(self, instance):
        threading.Thread(target=listen_for_commands).start()

    def open_url(self, url):
        webbrowser.open(url)

    def search_wikipedia(self, instance):
        query = self.wiki_input.text
        if query:
            Speech.speak(f"Searching Wikipedia for {query}")
            summary = API.search_wikipedia(query)
            if summary:
                Speech.speak(summary)
                SRMAlexaApp.display_text(summary)
                print(f"SRM-Alexa:\n{summary}\n")
            else:
                Speech.speak("Apologies, I couldn't find any information on Wikipedia.")
        else:
            Speech.speak("Please specify what you want to search on Wikipedia.")

def listen_for_commands():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            try:
                print("Listening for commands...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                if command:
                    Speech.process_command(command)
            except sr.UnknownValueError:
                Speech.speak("Apologies, I didn't understand that.")
            except sr.RequestError:
                Speech.speak("Could not request results; please check your network connection.")

if __name__ == "__main__":
    SRMAlexaApp().run()
