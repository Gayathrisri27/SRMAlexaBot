

### SRM-Alexa Project Overview

**Project Description:**
SRM-Alexa is a voice-controlled assistant application developed using Python and the Kivy framework. It integrates several functionalities to provide information and access to various services related to SRM Institute of Science and Technology (SRMIST).

### Key Features:

1. **Voice Interaction:**
   - Utilizes the `speech_recognition` library to enable voice commands.
   - Commands trigger actions such as opening specific URLs related to SRMIST services.

2. **Web Integration:**
   - Direct access to SRMIST services like the Student Portal, official website, YouTube channel, hospital information, campus map, and contact details using `webbrowser`.

3. **Wikipedia Search:**
   - Allows users to search Wikipedia for information.
   - Displays summaries of queried topics using the `wikipediaapi` library.

4. **GUI with Kivy:**
   - Implements a graphical user interface (GUI) using Kivy.
   - Features include buttons for different functionalities, a text input for Wikipedia searches, and a pop-up window to display Wikipedia search results.

5. **Multithreading:**
   - Utilizes Python's `threading` module to handle continuous listening for voice commands without blocking the main application thread.

6. **Text-to-Speech:**
   - Uses `pyttsx3` for text-to-speech functionality to provide auditory feedback for commands and search results.

### Project Components:

- **API Class (`API`):**
  - Static methods to interface with Wikipedia using `wikipediaapi` for fetching summaries based on user queries.

- **Speech Class (`Speech`):**
  - Static methods for text-to-speech functionality (`speak` method).
  - Processes voice commands (`process_command` method) to trigger actions like opening URLs and searching Wikipedia.

- **SRMAlexaApp Class (`SRMAlexaApp`):**
  - Inherits from `App` in Kivy to manage the application lifecycle and GUI.
  - Builds the GUI layout using Kivy widgets (`BoxLayout`, `GridLayout`, `Button`, `Label`, `TextInput`, `Image`, `Popup`).
  - Methods include handling button events (`open_url`, `search_wikipedia`), displaying information in pop-up windows (`display_text`), and starting voice interaction (`talk_with_me`).

- **Voice Command Listener (`listen_for_commands`):**
  - Continuous loop using `speech_recognition` to listen for voice commands via microphone.
  - Recognizes spoken commands, processes them using `Speech.process_command`, and handles exceptions for unknown commands or network errors.
  - API Class in SRM-Alexa Project
-**Purpose:**
The API class serves as an abstraction layer that encapsulates the functionality to interact with external services, specifically Wikipedia in this case. Its role is to facilitate the retrieval of information from Wikipedia based on user queries.

Components and Usage:
Static Method search_wikipedia(query):
Purpose: This method is responsible for querying Wikipedia using the wikipediaapi library.
-Implementation:
It sets a user-agent string to identify the source of the request (SRM-Alexa).
Utilizes wikipediaapi.Wikipedia to create a Wikipedia object for English language.
Retrieves the Wikipedia page corresponding to the user-provided query.
Checks if the page exists (page.exists()) and if so, returns the first 500 characters of the summary (page.summary[:500]).
If the page does not exist or there's an issue, it returns a default message indicating no information was found.

### Conclusion:

SRM-Alexa showcases integration of voice control, web browsing capabilities, and Wikipedia search functionality in a user-friendly interface built with Kivy. It provides a practical example of how Python can be used to develop interactive and informative applications tailored to specific institutional needs, in this case, SRM Institute of Science and Technology. The project highlights the synergy between GUI development, web integration, and natural language processing capabilities in Python.
