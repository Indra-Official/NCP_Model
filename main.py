from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from elevenlabs.client import ElevenLabs
import playsound
import os

def gandhi_t2s(msg):
    client = ElevenLabs(
    api_key="sk_4d10580da8584bb0c5fb72f232e55f41854101ff25c25b2b" #JK
)
    voice_id = "ybsn8GUgoNB8oDLyFqwG" #Adam
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("Gandhi.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("Gandhi.mp3")

def ambed_t2s(msg):
    client = ElevenLabs(
    api_key="sk_4d10580da8584bb0c5fb72f232e55f41854101ff25c25b2b" #JK
)
    voice_id = "3gsg3cxXyFLcGIfNbM6C"
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("Ambedkar.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("Ambedkar.mp3")


def tej_t2s(msg):
    client = ElevenLabs(
    api_key="sk_df485e7c09d306e38e26f72cb7737db61ac0dbfefbca5410" #Lalith
)
    voice_id = "VR6AewLTigWG4xSOukaG"
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("Tej bahadur Supru.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("Tej bahadur Supru.mp3")


def mohommad_t2s(msg):
    client = ElevenLabs(
    api_key="sk_df485e7c09d306e38e26f72cb7737db61ac0dbfefbca5410" #Lalith
)
    voice_id = "TxGEqnHWrfWFTfGW9XjX"
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("Jinnah.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("Jinnah.mp3")


def ramsay_t2s(msg):
    client = ElevenLabs(
    api_key="sk_df485e7c09d306e38e26f72cb7737db61ac0dbfefbca5410" #Lalith
)
    voice_id = "nXIYu9FT5meibkBbZFT7"
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("Ramsay MacDonald.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("Ramsay MacDonald.mp3")


def voice(chra,response):
    if chra == "Gandhi":
        gandhi_t2s(response)
    elif chra == "Ambedkar":
        ambed_t2s(response)
    elif chra == "Jinnah":
        mohommad_t2s(response)
    elif chra == "Ramsay MacDonald":
        ramsay_t2s(response)
    elif chra == "Tej bahadur Supru":
        tej_t2s(response)


def startai(api):
    genai.configure(api_key=api)
    global model
    model = genai.GenerativeModel('gemini-1.5-flash')

def chatbot(usr):
    response = model.generate_content(usr)
    return response.text


app = Flask(__name__)

startai("AIzaSyCFcPoiSYZF9JBQSHHp0_W33ikaOjPYVu8")
me = True

print("This is a debate betwwen AIs (Gandhi , Ambedkar, Jhinna, etc) and you themed around the 1930 round table conference held in london.")
print("\n")

a = open("Data.txt", "w")
a.write('''"content": "You are simulating a fictional debate based on the 1930 London Round Table Conference. Participants include "Gandhi", "Ambedkar', "Jinnah", "Ramsay MacDonald", "Tej bahadur Supru", and "Lalith" (the user input). Lalith is an equal speaker, not a moderator it will be user input.

    Characters can:
    - Speak openly to any other speaker
    - React to user's arguments
    - Interrupt or team up with each other
    - Form alliances or criticize each other
    - Defer or double down based on context
    - ghandhi , ambedkar and lalith should have equal presence.

    The debate evolves naturally. Topics may shift (e.g., from independence to caste to identity). All responses must be in strict dictionary format:

    {
    'speaker': 'Who is speaking',
    'statement': 'Their argument or response',
    'next_speaker': 'self or someone else, the dialouge must mention Lalith if reply from lalith is needed',
    'audience_reaction': 'audience_clap' | 'officials_clap' | 'none',
    'debate_state': 'Optional summary of current focus or tension',
    'alliance': 'Optional — who is teaming up and why'
    }

    very important never write dialouges for Lalith.

    make there line short if its anything other than facts ot points.
    make lines more natural and feel free to make small intercation from all characters like starting with a greet from everyones sider.
    when asked to generate start as the nest speaker in the last dialouge, or can find who the question is directed towards.
    Do not include any extra explanation or narrative outside the Dictionary and send as plain text . Wait for user’s next input before continuing the debate unless instructed otherwise."

    lines spoke till now:'''
    )


while True:
    if True:
        a = open("Data.txt", "r")
        data = a.read()
        if me:
            usr = input("Lalith : ")
            data1 = "Lalith : " + usr
        else:
            usr= ""

        out = chatbot(str(data +"\n"+ usr)).replace("```","").replace("json","").replace("\n","")
        res = eval(out)

        response = res["speaker"]+ " : "+ res["statement"]
        
        print(response,"\n")

        voice(res["speaker"],res["statement"])

        data2 = str(res)

        if res['next_speaker'] == "Lalith":
            me = True
        else:
            me = False

        a = open("Data.txt", "a")
        a.write(str(data1+"\n"))
        a.write(str(data2+"\n"))
        a.close()