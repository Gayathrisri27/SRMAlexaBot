# SRMAlexaBot
### Project Overview: SRM-Alexa

**SRM-Alexa** is a Python-based virtual assistant designed to provide users with voice-activated access to various SRM Institute of Science and Technology resources. The assistant uses speech recognition and text-to-speech technologies to interact with users, opening web pages based on specific voice commands. It also features a graphical user interface (GUI) with animated elements to enhance user engagement.

#### Key Components:

1. **Speech Recognition and Processing**:
    - **Speech Recognition**: The assistant utilizes the `speech_recognition` library to capture and process voice commands. It listens for specific keywords to trigger actions, such as opening web pages.
    - **Text-to-Speech**: The `pyttsx3` library is employed to provide audio feedback to the user, enhancing interactivity.

2. **Graphical User Interface (GUI)**:
    - **Tkinter**: The GUI is built using the `tkinter` library, offering a simple and intuitive interface for users to interact with SRM-Alexa.
    - **Text Box**: A text box is included to display the interactions between the user and the assistant, with different text styles to distinguish user commands, assistant responses, and errors.
    - **GIF Animation**: An animated GIF is displayed within the GUI using the `PIL` library's `ImageSequence` module, adding a dynamic visual element.

3. **Web Browser Integration**:
    - The assistant opens various SRM-related web pages in response to voice commands, providing quick access to the student portal, official website, YouTube channel, hospital information, campus map, and contact details.

#### Detailed Description:

1. **Speech Recognition and Text-to-Speech**:
    - **Class `speech`**: Contains static methods for text-to-speech (`speak`) and processing commands (`process_command`). The `process_command` method matches the recognized voice command with predefined keywords to perform specific actions, such as opening URLs.
    - **Function `listen_for_commands`**: Continuously listens for voice commands using a background thread. It handles exceptions for unknown or unrecognized speech and updates the GUI accordingly.

2. **GUI Setup and Management**:
    - **Function `main`**: Initializes the main application window, sets up the text box with specific styling, and loads the animated GIF. It also starts the speech recognition thread and welcomes the user with a spoken message.
    - **Function `update_gif`**: Handles the animation of the GIF by updating the displayed frame at a regular interval.

#### Features:

- **Voice Commands**: Users can issue voice commands like "portal," "website," "youtube," "hospital," "map," and "contact" to quickly access corresponding web resources.
- **Text Feedback**: The assistant provides text feedback in the GUI for both user commands and its responses.
- **Error Handling**: The system informs users about any recognition errors or network issues through both text and speech.
- **Animated GUI**: An animated GIF enhances the visual appeal of the assistant, making it more engaging.

#### Usage:

- **Starting the Assistant**: Run the script to launch the GUI. SRM-Alexa will greet the user and start listening for voice commands.
- **Interacting with SRM-Alexa**: Speak the predefined commands to navigate to various SRM-related online resources. The assistant will confirm actions and handle errors gracefully.

This project demonstrates the integration of multiple technologies to create a responsive and interactive virtual assistant, providing a useful tool for students and staff at the SRM Institute of Science and Technology.
