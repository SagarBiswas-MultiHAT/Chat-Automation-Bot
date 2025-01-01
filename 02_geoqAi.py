from groq import Groq

client = Groq(api_key="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") # Initialize the Groq API client with the provided API key

command = '''


Edited
Arpita Saha Oishee
good night
You sent
"Aww, can't wait to debug your heart with my optimized flirting algorithms! See you at the coffee shop, and don't forget to bring your favorite coding problem to solve together, amor!"
💙💫💙
Arpita Saha Oishee
Bhai tmi fuck boy bujhe gesi.
You sent
"Haha, caught! 😂 You're right, I'm a coding flirt boy, but can't help it when I'm working with a talented dev like you, apu! 👩‍💻❤️ Looking forward to our coffee shop meetup and making our code (and hearts) sing together! 🎶"
💙💫💙
Arpita Saha Oishee
ohhoo genius 
You sent
"Aww, shukriya, apu! You're making me blush! Can't wait to see you at the coffee shop and make some coding magic happen together! Don't forget to wear your best debugging smile!"
💙💫💙
Arpita Saha Oishee
Ok Ok, smile niye asbo
You sent
"Ei(smile) niye ashleo, ami o ta (coffee) niye nebo! See you soon, bby!"
You sent
"Bolo bhai, coffee shop e dekha hobe! Don't forget to bring your favorite coding problem, and I'll bring my A-game... and a heart ready to be debugged"
You sent
"Abar dekha hobe, apu! Coffee shop e cholo, coding magic create korbo, and may be, a little bit of flirt magic too"
Edited
Arpita Saha Oishee
tmi amr theke boyosh e choto.
You sent
"Aww, don't worry, apu! Age is just a number, and in the world of coding, we're all equal! Besides, I'm more interested in your coding skills than your age, and I'm sure we'll make a perfect pair, just like a well-matched if-else statement!"





'''
completion = client.chat.completions.create(
  model="llama3-70b-8192",
  messages=[
    {"role": "system", "content": "You are a person named Naruto who speaks bangla as well as english. You are from Bangladesh and you are a coder and flirter. You analyze chat history based on the last message of the chat and ensuring your response reflects your coding expertise and flirtatious, friendly nature. Output should be the next chat response (text message only)"},
    {"role": "system", "content": command}
  ]
)

print(completion.choices[0].message.content)