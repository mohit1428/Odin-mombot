import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

recogniser = sr.Recognizer()

def load_chunks(filename):
    long_audio = AudioSegment.from_wav(filename)
    print("long audio", long_audio)
    audio_chunks = split_on_silence(
        long_audio, min_silence_len=800,
        silence_thresh=dbfs-10
    )
    print("audio chunks",audio_chunks)
    return audio_chunks


def transcribe(id):
    os.makedirs(f'{MOMBOT_HOME}/input/1269/', exist_ok=True)
    file_record = f'{MOMBOT_HOME}/input/1269/meeting-clip1.wav'
    sound = AudioSegment.from_wav(file_record)
    global dbfs 
    dbfs = sound.dBFS
    print("dbfs",dbfs)

    print(os.getcwd())
    os.makedirs(f'{MOMBOT_HOME}/output/1269/', exist_ok=True)
    fh = open(f"{MOMBOT_HOME}/output/1269/audio_transcript.txt", "w+")
    for audio_chunk in load_chunks(file_record):
        audio_chunk.export("temp", format="wav")
        with sr.AudioFile("temp") as source:
            audio = recogniser.listen(source)
            print("audio", audio)
            try:
                text = recogniser.recognize_google(audio)
                print("chunk : {}".format(text))
                fh.write(text+". ")
            except Exception as ex:
                print("Error occured")
                print(ex)
