from RealtimeSTT import AudioToTextRecorder
from SpeechApparatus import SpeechApparatus

def process_text(text):
    print(text)

if __name__ == "__main__":
    recorder = AudioToTextRecorder()
    while True:
        recorder.text(process_text)