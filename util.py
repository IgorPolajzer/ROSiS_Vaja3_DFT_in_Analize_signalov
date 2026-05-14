from pydub import AudioSegment
import numpy as np
from matplotlib import pyplot as plt


def read_signal_from_m4a(input_file):
    sound = AudioSegment.from_file(input_file, format="m4a")
    samples = np.frombuffer(sound.raw_data, dtype=np.int16).astype(np.float32) / 32767
    return samples, sound.frame_rate


def dft(signal, Fs, max_sample_count, max_freqs_hz):
    signal = signal[:max_sample_count]
    T = len(signal) / Fs # Signal length.

    length = np.arange(len(signal))

    freqs = np.arange(0, Fs, 1/T)
    freqs = freqs[freqs <= max_freqs_hz]
    result = []

    for f in freqs:
        result.append(np.dot(signal, np.exp(-1j * 2 * np.pi * f * length / Fs)))

    return np.array(result), freqs


def plot_analasys(y, x, label):
    plt.plot(x, abs(y), label=label)
    plt.title('Frekvenčna vsebina')
    plt.xlabel('Frekvenca [Hz]')
    plt.ylabel('Amplituda')
    plt.legend()
    plt.grid(True)
    plt.show()


def calculate_rpm(f_bmp, blade_count):
    rpm = (f_bmp * 60) / blade_count
    print(f"Rpm: {rpm}")
    return rpm


def get_peak_freq(y_dft, freqs):
    peak_idx = np.argmax(np.abs(y_dft))
    f_blade = freqs[peak_idx]
    print(f"Peak frequency: {f_blade:.2f} Hz")
    return f_blade