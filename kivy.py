from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class SRMAlexaApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = Screen(name='main')
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(Image(source='./Capture.png'))  # Add SRM Alexa logo
        welcome_label = Label(text='Welcome to SRM Alexa Bot!', font_size=24)
        main_layout.add_widget(welcome_label)
        talk_button = Button(text='Talk with me', font_size=24, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
        talk_button.bind(on_press=self.talk_with_me)
        main_layout.add_widget(talk_button)
        main_screen.add_widget(main_layout)
        sm.add_widget(main_screen)
        return sm

    def talk_with_me(self, instance):
        print("Let's talk!")

    def show_updates_popup(self, instance):
        popup = Popup(title='New Updates', content=Label(text='New updates available!'), size_hint=(None, None), size=(400, 400))
        close_button = Button(text='Close')
        close_button.bind(on_press=popup.dismiss)
        popup.content.add_widget(close_button)
        popup.open()

if __name__ == '__main__':
    SRMAlexaApp().run()
