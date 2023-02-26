import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import openai
openai.api_key = "your-api-code"


def send_message(message):
    response1 = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response1.choices[0].text.strip()


# Initialize speech recognizer
channels = 1

r = sr.Recognizer()
m = sr.Microphone()
value = ''
# Loop to listen for spoken input and respond
try:
    print("Initialising.....")
    print('Adjusting for ambient threshold, please wait...')
    with m as source: r.adjust_for_ambient_noise(source)
    print(f"Minimum energy threshold set to {r.energy_threshold}")
    while True:
        print("Speak something!")
        with m as source: audio = r.listen(source)
        print("Recognizing Audio...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print(f"You said {value}")
        except sr.UnknownValueError:
            print("Oops! couldn't catch that")
        except sr.RequestError as e:
            print(f"Uh oh! Couldn't request results from Google Speech Recognition service;{e}, Check your connection!")
        text_output = send_message(value)
        print("Chatbot replied: ", text_output)

        # Convert text output to spoken output
        tts = gTTS(text=text_output, lang="en-uk")
        tts.save("output.mp3")

        # Play spoken output
        playsound("output.mp3")

except KeyboardInterrupt:
    pass
