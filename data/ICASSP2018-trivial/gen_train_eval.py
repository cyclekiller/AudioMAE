import glob

def gen(data_split, dataset_folder, rand_tile=False):
    if rand_tile:
        dataset_folder += '_rand_*'
    with open(f"./data/ICASSP2018-trivial/{data_split}_{dataset_folder}.json", "w") as outfile:
        outfile.write("{" + '\n')
        outfile.write('"data": [' + '\n')

        first = True
        nums_segments = {i: 0 for i in range(1, 1000)}
        for wav_path in glob.glob(f"./data/ICASSP2018-trivial/{dataset_folder}/*.wav"):
            pure_path = wav_path.rsplit('/', 1)[1]
            speaker = pure_path.split('_')[1]
            segment = pure_path.rsplit('.', 1)[0].split('_')[2]
            if int(speaker) not in speaker_set:
                continue
            nums_segments[int(speaker)] += 1
            if data_split == "eval":
                if int(segment) % 3 != 0:
                    continue
            else:
                if int(segment) % 3 == 0:
                    continue
            if not first:
                outfile.write('},' + '\n')
            first = False

            outfile.write('{' + '\n')
            outfile.write('"wav": "{}",'.format(wav_path) + '\n')
            outfile.write('"labels": "{}"'.format(speaker) + '\n')
        outfile.write('}' + '\n')    
        
        outfile.write(']' + '\n')
        outfile.write('}' + '\n')

        total_speakers = 0
        for speaker in nums_segments:
            if nums_segments[speaker] > 0:
                print(f'speaker {speaker} has {nums_segments[speaker]} segments')
                total_speakers += 1
        print(f'total speakers: {total_speakers}')

speaker_set = set()
with open(f"./data/ICASSP2018-trivial/class_labels_indices.csv", 'r') as f:
    lines = f.readlines()[1:]
    for line in lines:
        speaker_set.add(int(line.split(',')[1]))

# for data_split in ['train', 'eval']:
#     for dataset_folder in ['laugh', 'cough']:
#         gen(data_split, dataset_folder)
#         gen(data_split, f'tiled_{dataset_folder}')

gen('train', 'tiled_laugh', True)
gen('eval', 'tiled_laugh', True)