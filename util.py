from pydub import AudioSegment
import numpy as np
from matplotlib import pyplot as plt


def read_signal_from_m4a(input_file):
    sound = AudioSegment.from_file(input_file, format="m4a")
    samples = np.frombuffer(sound.raw_data, dtype=np.int16).astype(np.float32) / 32767
    return samples, sound.frame_rate


def plot_frequency(A, y, p, t, Fs, freq):
    plt.plot(t, y)
    plt.title(f'Vzor: {Fs} Hz, Frek: {freq} Hz, Ampl: {A}, Faza: {p} rad')
    plt.xlabel('Čas [s]')
    plt.ylabel('Amplituda')
    plt.grid(True)
    plt.show()


def dft(signal, Fs, T, max_freqs_hz):
    length = np.arange(len(signal)) # Frequency length.

    # All frequencies from 0 to Fs stepped by 1/T
    # Freqency resolution 1/T
    freqs = np.arange(0, Fs, 1/T)
    freqs = freqs[freqs <= max_freqs_hz]
    result = []

    # Dot product over all frequencies [0, Fs].
    for f in freqs:
        result.append(np.dot(signal, np.exp(-1j * 2 * np.pi * f * length / Fs)))

    return np.array(result)


def plot_analasys(y, Fs, T, label):
    N_total = int(T * Fs)
    max_freq = (len(y) / N_total) * Fs
    x = np.linspace(0, max_freq, len(y))

    plt.plot(x, abs(y), label=label)
    plt.title('Frekvenčna vsebina')
    plt.xlabel('Frekvenca [Hz]')
    plt.ylabel('Amplituda')
    plt.legend()
    plt.grid(True)
    plt.show()

    return max_freq


def calculate_rpm(f_bmp, blade_count):
    rpm = (f_bmp * 60) / blade_count
    print(f"Rpm: {rpm}")
    return rpm