import glob

with open("./data/ICASSP2018-trivial/class_labels_indices.csv", "w") as outfile:
    outfile.write("index,mid,display_name" + '\n')
    speakers = set()
    for wav_path in glob.glob("./data/ICASSP2018-trivial/laugh/*.wav"):
        pure_path = wav_path.rsplit('/', 1)[1]
        speakers.add(int(pure_path.split('_')[1]))
    for i, speaker_id in enumerate(sorted(speakers)):
        # 0,/m/09x0r,"Speech"
        spk_str = "spk_{}".format(i)
        outfile.write("{},{},{}".format(str(i), str(speaker_id), spk_str) + '\n')