import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sampleRate, data = wavfile.read('250+500+750+noise.wav')
timestamps = np.arange(0.0, 0.012, 1 / sampleRate)

# plt.tight_layout()
# plt.plot(timestamps, data[:len(timestamps)])
# plt.grid(True)
# plt.xlabel('Time (s)', fontsize=9)
# plt.ylabel('Amplitude', fontsize=9)
# plt.ylim((-35000, 35000))

# plt.show()
# plt.clf()

def sign(x): return 0 if x < 0 else 1

previous = sign(data[0])
data[0] = previous
for index in range(1, len(data) - 1):
    if sign(data[index]) != previous:
        data[index] = (1 if previous == 0 else 0)
    else:
        data[index] = previous

    previous = sign(data[index])

# plt.plot(timestamps, data[:len(timestamps)])
# plt.grid(True)
# plt.xlabel('Time (s)', fontsize=9)
# plt.ylabel('Zero Crossing', fontsize=9)
# plt.ylim((-0.1, 1.1))

# plt.show()
# plt.clf()

# Take first second of audio
data = data[:sampleRate]
maxLag = int(0.05 * sampleRate)
lags = np.arange(0, maxLag, 1)
bsac = []
for lag in lags:
    corr = 0
    for index in range(0, len(data) - maxLag - 1):
        corr += data[index] ^ data[index + lag]
    
    bsac.append(corr)

# plt.plot(lags, bsac)
# plt.grid(True)
# plt.xlabel('Lag (sampleRate)', fontsize=9)
# plt.ylabel('Correlation (XOR)', fontsize=9)

# plt.show()

print(np.argmin(bsac[int((1 / 10000) * sampleRate):]))