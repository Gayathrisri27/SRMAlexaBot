import speech

def authenticate_user():
    pin = speech.listen("Please enter your PIN: ")
    if pin.isdigit() and len(pin) == 4:  # assuming 4-digit PIN
        # Verify PIN with stored PIN (e.g., from a database or file)
        stored_pin = "1234"  # replace with actual stored PIN
        if pin == stored_pin:
            speech.speak("Authentication successful. Welcome!")
            return True
        else:
            speech.speak("Invalid PIN. Please try again.")
            return False
    else:
        speech.speak("Invalid PIN format. Please try again.")
        return False