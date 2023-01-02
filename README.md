# RANDOMLY TILING SHORT TRIVIAL SPEECH EVENTS IMPROVES SPEAKER RECOGNITION IN MASKED AUTOENCODERS
- [AudioMAE](https://github.com/facebookresearch/AudioMAE) is a relatively new pre-training method for audio classification tasks built on the ViT backbone.
- [CSLT-TRIVIAL-I](https://github.com/CSLT-THU/ICASSP2018-trivial/tree/master/CSLT-TRIVIAL-I) is a dataset composing of 75 speakers uttering short trivial speech events such as cough and laugh. It is mainly designed to perform speaker recognition tasks.
- This repo uses the same method as AudioMAE to finetune the model for speaker identification using cough and laugh data from CSLT-TRIVIAL-I. Several data augmentation methods are used, among which random tiling is the best.

## Steps to reproduce the experiments
1. Download the finetuned model checkpoint from [AudioMAE](https://github.com/facebookresearch/AudioMAE#5-inference) repo, place it under `./ckpt/`.
2. Download the [CSLT-TRIVIAL-I](https://github.com/CSLT-THU/ICASSP2018-trivial/tree/master/CSLT-TRIVIAL-I) dataset (specifically, the `cough` and `laugh` folder), place them under `./data/ICASSP2018-trivial/`.
3. Run data preparation and augmentation scripts:
```
python ./data/ICASSP2018-trivial/gen_class_labels.py
python ./data/ICASSP2018-trivial/tile_wavs.py
python ./data/ICASSP2018-trivial/gen_train_eval.py
```
4. Finetune and evaluate the model following the settings in `./.vscode/launch.json` (need to install VSCode or copy out the args).

## Results
Speaker recognition (laugh):
Model | Acc.(%)
------ | ------
Padded | 72.6
Tiled | 72.6
Rand-Tiled | **75.5**

Speaker recognition (cough):
Model | Acc.(%)
------ | ------
Padded | 85.8
Tiled | 86.8
Rand-Tiled | **89.2**
