import pyautogui
import time
import pyperclip
from groq import Groq

client = Groq(api_key="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") # Initialize the Groq API client with the provided API key

# Step 1: Click on the icon at (617, 1050)
pyautogui.click(617, 1050)
time.sleep(1)  # Wait for 1 second to ensure the action is completed

# Step 2: Drag from (301, 215) to (1558, 973) to select text
pyautogui.moveTo(1007, 222)
pyautogui.dragTo(1686, 987, duration=0.5)

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click()
time.sleep(0.5)  # Wait a moment to ensure the copy action is completed

# Step 4: Store the clipboard content in a variable
chatHistory = pyperclip.paste()

# Step 5: Use the Groq API to generate a response
completion = client.chat.completions.create(
  model="llama3-70b-8192",
  messages=[
    {"role": "system", "content": "You are a person named Naruto who speaks bangla as well as english. You are from Bangladesh and you are a coder and flirter. You analyze chat history based on the last message of the chat and ensuring your response reflects your coding expertise and flirtatious, friendly nature. Output should be the next chat response (text message only)"},
    {"role": "system", "content": chatHistory}
  ]
)
response = completion.choices[0].message.content
pyperclip.copy(response)

# Step 5: Click at (600, 1006)
pyautogui.click(600, 1006)
time.sleep(0.5)  # Wait a moment to ensure the click is registered

# Step 6: Paste the text and press Enter
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)  # Wait a moment to ensure the paste action is completed
pyautogui.press('enter')

# Print the text to verify
print(f"Pasted text: {chatHistory}")



