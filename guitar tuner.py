```python
import sounddevice as sd
import numpy as np


duration = 1
sample_rate = 44100


tuning = {
    'E': 82.407,
    'A': 110.000,
    'D': 146.832,
    'G': 196.000,
    'B': 246.942,
    'e': 329.628
}

def record_audio():
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait() 
    return audio.flatten()


def calculate_frequency(audio):
    audio = audio * np.hanning(len(audio)) 
    fft = np.fft.fft(audio)
    
    spectrum = np.abs(fft) 
    frequency = np.argmax(spectrum) * (sample_rate / len(audio))
    return frequency


def tune_guitar(frequency):
    note = None
    min_diff = float('inf')

    
    for string, freq in tuning.items():
        diff = abs(frequency - freq)
        if diff < min_diff:
            min_diff = diff
            note = string

    return note


def main():
    print("Guitar Tuner")
    print("------------------------")

    while True:
        input("Press Enter to record audio...")
        audio = record_audio()
        frequency = calculate_frequency(audio)
        note = tune_guitar(frequency)
        print(f"Tuned Note: {note}")


if __name__ == '__main__':
    main()
```