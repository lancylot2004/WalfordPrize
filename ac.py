import librosa
import numpy as np
import scipy
import matplotlib.pyplot as plt

data, sampleRate = librosa.load('250+500+750+noise.wav')
r = librosa.autocorrelate(data, max_size=10000)

# Plot the autocorrelation function
plt.plot(r[:200])
plt.show()

# Eliminate unlikely ranges of pitches
r[:int(sampleRate/librosa.midi_to_hz(120))] = 0
r[int(sampleRate/librosa.midi_to_hz(12)):] = 0

lagMax = r.argmax()
print(float(sampleRate) / lagMax)