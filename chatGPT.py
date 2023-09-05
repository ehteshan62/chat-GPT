import openai
import speech_recognition
import pyttsx3


 #  Set up the OpenAI API client
openai.api_key = //"enter you API key which you can copy from your chatgpt"

# this loop will let us ask questions continuously and behave like ChatGPT
while True:
    # Set up the model and prompt
    model_engine = "text-davinci-003"

    prompt = input('Enter new prompt: ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    # Generate a response
    completion = openai.Completion.create(engine=model_engine,prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5,)

    # extracting useful part of response
    response = completion.choices[0].text

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)


    def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()


     #  printing response
    speak(response)
