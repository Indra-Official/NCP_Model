from elevenlabs.client import ElevenLabs
import elevenlabs
import playsound

# Initialize ElevenLabs client
client = ElevenLabs(
    api_key="sk_4d10580da8584bb0c5fb72f232e55f41854101ff25c25b2b"
)

def gandhi_t2s(msg):
    voice_id = "ybsn8GUgoNB8oDLyFqwG" #Adam
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("gandhi.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("gandhi.mp3")

def ambed_t2s(msg):
    voice_id = "3gsg3cxXyFLcGIfNbM6C"
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("ambed.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("ambed.mp3")


def tej_t2s(msg):
    voice_id = "VR6AewLTigWG4xSOukaG" #Adam
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("tej.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("tej.mp3")


def mohommad_t2s(msg):
    voice_id = "TxGEqnHWrfWFTfGW9XjX" #Josh
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("mohommad.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("mohommad.mp3")


def ramsay_t2s(msg):
    voice_id = "nXIYu9FT5meibkBbZFT7" #Adam
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_monolingual_v1",
        text=msg
    )
    with open("ramsay.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("ramsay.mp3")


def voice(chra,msg):
    if chra == "Gandhi":
        gandhi_t2s(msg)
    elif chra == "Ambedkar":
        ambed_t2s(msg)
    elif chra == "Jinnah":
        mohommad_t2s(msg)
    elif chra == "Ramsay MacDonald":
        ramsay_t2s(msg)
    elif chra == "Tej bahadur Supru":
        tej_t2s(msg)