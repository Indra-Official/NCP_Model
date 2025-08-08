from elevenlabs.client import ElevenLabs
import elevenlabs
import playsound
import simpleaudio

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
    with open("gandhi.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("gandhi.mp3")

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
    with open("ambed.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("ambed.mp3")


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
    with open("tej.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("tej.mp3")


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
    with open("mohommad.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("mohommad.mp3")


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
    with open("ramsay.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)
    playsound.playsound("ramsay.mp3")


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
