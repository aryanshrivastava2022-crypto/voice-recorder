import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
duration = int(input("Enter recording duration (seconds): "))

print("🎙️ Recording...")

recording = sd.rec(
    int(duration * fs),
    samplerate=fs,
    channels=2
)

sd.wait()

filename = "recorded_audio.wav"
write(filename, fs, recording)

print(f"✅ Recording saved as {filename}")
