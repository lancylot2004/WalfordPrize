from scipy.fftpack import fft
from matplotlib import pyplot as plt
from scipy.io import wavfile
import numpy as np
import scipy

fs_rate, signal = wavfile.read("250+500+750+noise.wav")

# print (f"Sampling: {fs_rate}Hz")
# print (f"Channels: {len(signal.shape)}")
# print (f"Samples: {samples}")
# print (f"Seconds: {seconds}")
# print (f"Step between Samples: {1.0 / fs_rate}")

if len(signal.shape) == 2: signal = signal.sum(axis = 1) / 2
samples = signal.shape[0]
seconds = samples / float(fs_rate)
step = 1.0 / fs_rate
timeVector = scipy.arange(0, seconds, step)

FFT = abs(fft(signal))
FFTPositive = FFT[range(int(samples / 2))]

freqs = scipy.fftpack.fftfreq(signal.size, timeVector[1] - timeVector[0])
FFTFreqsPositive = freqs[range(int(samples / 2))]  # one side frequency range

plt.plot(FFTFreqsPositive[:50000], abs(FFTPositive[:50000]), "b")  # plotting the positive fft spectrum
plt.xlabel('Frequency (Hz)')
plt.ylabel('Positive Count')
plt.show()


