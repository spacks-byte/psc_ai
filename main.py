import speech_recognition as sr
from rich import print


def transcribe_chinese_audio(audio_file_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = r.record(source) # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # For Mandarin Chinese (Mainland China)
        text = r.recognize_google(audio, language="zh-CN")
        return text
        #print(f"Transcription: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# The audio file must be in a compatible format (PCM WAV, AIFF/AIFF-C, or Native FLAC)
proper = "我今天去健身房"
transcription = transcribe_chinese_audio('correctpronounced.wav')

print(f"Proper: \t{proper}")
print(f"Your Input: \t{transcription}")

length = len(proper) if proper > transcription else len(transcription)
for charIndex in range(length):
    if proper[charIndex] == transcription[charIndex]:
        print(f"[bold green]{transcription[charIndex]}[/bold green]", end="")
    else:
        print(f"[bold red]{transcription[charIndex]}[/bold red]", end="")
