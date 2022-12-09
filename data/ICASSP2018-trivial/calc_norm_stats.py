import torch
import torchaudio
import glob
import numpy as np
from tqdm import tqdm

def wav2fbank(filename):
    waveform, sr = torchaudio.load(filename)
    waveform = waveform - waveform.mean()

    fbank = torchaudio.compliance.kaldi.fbank(waveform, htk_compat=True, sample_frequency=sr, use_energy=False,
                            window_type='hanning', num_mel_bins=128, dither=0.0, frame_shift=10) # modified: num_mel_bins

    target_length = 1024 # modified
    n_frames = fbank.shape[0]

    p = target_length - n_frames

    # cut and pad
    if p > 0:
        m = torch.nn.ZeroPad2d((0, 0, 0, p))
        fbank = m(fbank)
    elif p < 0:
        fbank = fbank[0:target_length, :]

    return fbank

X = [wav2fbank(wav_path) for wav_path in tqdm(glob.glob("./data/ICASSP2018-trivial/tiled_laugh/*.wav"))]
X = np.hstack(X)
norm_stats = np.array([X.mean(), X.std()])
print(norm_stats) # [-6.243623   3.9804757]