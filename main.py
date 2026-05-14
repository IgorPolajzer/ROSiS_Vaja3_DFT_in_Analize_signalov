from importlib import reload
import util
from util import *

reload(util)

MAX_SAMPLE_COUNT = 5000
MAX_FREQS_HZ = 1000

y, Fs = util.read_signal_from_m4a("/home/igor/Desktop/MAG/1_LETNIK/2_SEMESTER/RACUNALNISKA_OBDELAVA_SIGNALOV_IN_SLIK/Vaja_3/naloga_1_rpm/sig_a_1.m4a")

T = len(y) / Fs
y_dft, freqs = dft(y, Fs, MAX_SAMPLE_COUNT, MAX_FREQS_HZ)

plot_analasys(y_dft, freqs, "DFT sig_a_1.m4a")

f_bmp = get_peak_freq(y_dft, freqs)

calculate_rpm(f_bmp, 3)