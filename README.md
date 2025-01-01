# Chat Automation Bot

![Chat-Automation-Bot](https://scontent.fdac138-2.fna.fbcdn.net/v/t39.30808-6/472029725_122132275670552158_7324699147322623844_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=Rra3NHGro-AQ7kNvgETyEui&_nc_zt=23&_nc_ht=scontent.fdac138-2.fna&_nc_gid=AcXOzl_J_wbHQSnFAlrUqme&oh=00_AYDeDJfTcHoO6Q-X1AfBm2XByapH_DiZz2Hbk4U33i6XZg&oe=6778ED8E)

This repository contains a Python script that automates chat interactions by leveraging PyAutoGUI for UI automation, Pyperclip for clipboard management, and the Groq API for intelligent chat responses. Designed for coders who enjoy a fun, flirty twist while automating mundane chat tasks.

---

## Features

- **Automated UI Interaction:** Uses PyAutoGUI to simulate mouse clicks, drags, and keyboard inputs.
- **Clipboard Management:** Captures and pastes text seamlessly with Pyperclip.
- **AI-Powered Responses:** Integrates with the Groq API to generate intelligent, personalized chat responses.
- **Custom Persona:** Configured to respond as a friendly, flirty coder with a mix of English and Bangla languages.

---

## Requirements

- Python 3.7+
- Libraries:
  - `pyautogui`
  - `pyperclip`
  - `groq`

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chat-automation-bot.git](https://github.com/SagarBiswas-MultiHAT/Chat-Automation-Bot.git
   cd chat-automation-bot
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install pyautogui pyperclip groq
   ```

4. Add your Groq API key:
   Replace `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` in the script with your actual API key.

---

## Usage

1. Run the script:
   ```bash
   python 03_bot.py
   ```

2. The script will:
   - Simulate a click on a specific screen position.
   - Select and copy text from a designated area.
   - Use the Groq API to analyze chat history and generate a response.
   - Paste the response into a chat application and press Enter to send it.

---

## How It Works

- **Step 1:** Simulates a mouse click on the chat icon.
- **Step 2:** Selects the text area by dragging the cursor.
- **Step 3:** Copies the selected text to the clipboard.
- **Step 4:** Sends the text to the Groq API, which generates a chat response.
- **Step 5:** Pastes the response back into the chat application and sends it.

---

## Example Scenario

You’re managing a busy chat platform and need quick, intelligent responses without typing manually. This bot:
- Reads the last message.
- Crafts a thoughtful response based on your configured persona.
- Sends the message, saving you time and effort.

---

## Notes

- **Accuracy:** Ensure your screen resolution matches the coordinates used in the script.
- **Custom Persona:** Modify the system message in the Groq API section to tailor the bot’s personality.
- **Safety:** Use responsibly and in compliance with chat platform rules.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as you like.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## Contact

For questions or suggestions, feel free to reach out at [eng.sagar.aiub@gmail.com].

