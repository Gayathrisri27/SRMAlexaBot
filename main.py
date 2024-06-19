import tkinter as tk
import threading
import webbrowser
import speech_recognition as sr
from PIL import Image, ImageTk, ImageSequence
import pyttsx3


class speech:
    @staticmethod
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        print(f"SRM-Alexa: {text}")

    @staticmethod
    def process_command(command):
        if "portal " in command:
            webbrowser.open("https://sp.srmist.edu.in/srmiststudentportal/students/loginManager/youLogin.jsp")
        elif "website" in command:
            webbrowser.open("https://www.srmist.edu.in/")
        elif "youtube " in command:
            webbrowser.open("https://www.youtube.com/channel/UCm1shC2LXjkKmgjz8LyJkFw")
        elif "hospital" in command:
            webbrowser.open("https://www.srmhospital.co.in/")
        elif "map" in command:
            webbrowser.open("https://www.google.com/maps/dir//R2FV%2B6Q7+SRM+Institute+of+Science+and+Technology,+Potheri,+SRM+Nagar,+Kattankulathur,+Tamil+Nadu+603203/@12.823033,79.8919807,12z/data=!4m18!1m8!3m7!1s0x3a52f712b82a78d9:0xfdb944a3aee53831!2sSRM+Institute+of+Science+and+Technology!8m2!3d12.823033!4d80.044416!15sCgNzcm0iA4gBAZIBCnVuaXZlcnNpdHngAQA!16zL20vMGJwNzl6!4m8!1m0!1m5!1m1!1s0x3a52f712b82a78d9:0xfdb944a3aee53831!2m2!1d80.044416!2d12.823033!3e3?entry=ttu")
        elif "contact" in command:
            webbrowser.open("https://www.srmist.edu.in/contact-us/")
        else:
            speech.speak("Sorry, I did not understand that command.")


def speak(text):
    speech.speak(text)
    gui.text_box.insert(tk.END, "SRM-Alexa:\n", "header")
    options_text = (
        "Say portal for student portal/fee details\n"
        "Say website to access official website\n"
        "Say youtube to view the SRM Education YouTube channel\n"
        "Say hospital if you want to access SRM GLOBAL HOSPITALS\n"
        "Say map if you want directions to visit us\n"
        "Say contact if you want to contact us\n"
    )
    gui.text_box.insert(tk.END, options_text, "options")
    gui.text_box.see(tk.END)


def listen_for_commands():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            try:
                print("Listening for commands...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                if command:
                    speech.process_command(command)
                    gui.text_box.insert(tk.END, "You: " + command + "\n", "user")
                    gui.text_box.see(tk.END)
            except sr.UnknownValueError:
                gui.text_box.insert(tk.END, "SRM-Alexa: Sorry, I did not understand that.\n", "error")
            except sr.RequestError:
                gui.text_box.insert(tk.END, "SRM-Alexa: Could not request results; check your network connection.\n",
                                    "error")
            gui.update()


def update_gif(frame_index):
    frame = gif_frames[frame_index]
    gif_label.config(image=frame)
    frame_index = (frame_index + 1) % len(gif_frames)
    gui.after(100, update_gif, frame_index)  # Adjust the delay as needed


def main():
    global gui, gif_frames, gif_label
    gui = tk.Tk()
    gui.title("SRM-Alexa")

    gui.text_box = tk.Text(gui, width=60, height=20)
    gui.text_box.pack()

    gui.text_box.tag_config("header", foreground="blue", font=("Helvetica", 12, "bold"))
    gui.text_box.tag_config("options", foreground="green", font=("Helvetica", 10))
    gui.text_box.tag_config("user", foreground="red", font=("Helvetica", 10, "italic"))
    gui.text_box.tag_config("error", foreground="yellow", font=("Helvetica", 10, "italic"))

    gif_image = Image.open("C:/Users/Hp/Downloads/7kmF.gif")  # Update with your GIF path
    gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif_image)]

    gif_label = tk.Label(gui)
    gif_label.pack()

    update_gif(0)

    speak("Hello! I'm SRM-Alexa your assistant. How can I help you today?")
    thread = threading.Thread(target=listen_for_commands)
    thread.daemon = True
    thread.start()
    gui.mainloop()


if __name__ == "__main__":
    main()
