from scipy.io.wavfile import read, write
import glob
import numpy as np
from tqdm import tqdm
import random
import os

def tile(dataset_folder, rand=False, rand_time=1):
    tiled_dir = f"./data/ICASSP2018-trivial/tiled_{dataset_folder}"
    if rand:
        tiled_dir += f'_rand_{rand_time}'
    os.makedirs(tiled_dir)
    for wav_path in tqdm(glob.glob(f"./data/ICASSP2018-trivial/{dataset_folder}/*.wav")):
        rate, data = read(wav_path)
        if rand:
            data = np.array(list(data) + [0] * random.randint(200, 2000), dtype=data.dtype)

        shape = (10 * rate,)

        tiled_wav = np.tile(data, np.array(shape) // np.array(np.shape(data)) + 1)[tuple(map(slice, shape))]

        pure_path = wav_path.rsplit('/', 1)[1]
        write(tiled_dir  + '/' + pure_path, rate, tiled_wav)

# tile('laugh')
# tile('cough')
for rand_time in range(3):
    tile('laugh', rand=True, rand_time=rand_time)

for rand_time in range(3):
    tile('cough', rand=True, rand_time=rand_time)